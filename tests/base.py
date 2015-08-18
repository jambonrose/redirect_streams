#!/usr/bin/env python
from __future__ import print_function, unicode_literals

import ctypes
from ctypes.util import find_library
from multiprocessing import Process
from os import system
from os.path import abspath, dirname, join
from tempfile import TemporaryFile
from unittest.mock import patch

import pytest
from flake8.engine import get_style_guide

from six.moves import cStringIO as StringIO

LIBC = ctypes.CDLL(find_library('c'))
TEST_DIR = dirname(abspath(__file__))


class BaseMixin(object):
    redirect_stdout_ctx = None
    expected = 'redirected'

    @pytest.mark.tryfirst
    @patch('sys.stdout', new_callable=StringIO)
    def test_test_assumption(self, mock_stdout):
        print(self.expected)
        self.assertEqual(self.expected+'\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def _general_structure(self, mock_stdout, func):
        with TemporaryFile(mode='w+', encoding='utf8') as buf:
            with self.redirect_stdout_ctx(buf):
                func(self.expected)
            buf.seek(0)
            buf_out = buf.read()
        self.assertEqual(self.expected+'\n', buf_out)
        self.assertEqual(mock_stdout.getvalue(), '')

    def test_basic(self):
        self._general_structure(func=print)

    def test_system(self):
        self._general_structure(func=system)

    def test_libc(self):
        self._general_structure(func=LIBC.puts)

    @patch('sys.stdout', new_callable=StringIO)
    def test_multiprocessing(self, mock_stdout):
        def worker():
            print(self.expected)
        with TemporaryFile(mode='w+', encoding='utf8') as buf:
            with self.redirect_stdout_ctx(buf):
                p = Process(target=worker)
                p.daemon = True
                p.start()
                p.join()  # wait for subprocess to terminate
            buf.seek(0)
            buf_out = buf.read()
        self.assertEqual(self.expected+'\n', buf_out)
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_flake8(self, mock_stdout):
        """Tests whether flake8 output is redirected.

        This test should be equivalent to the multiprocessing test,
        but is here in case my knowledge of flake8 is misplaced.
        """
        with TemporaryFile(mode='w+', encoding='utf8') as buf:
            with self.redirect_stdout_ctx(buf):
                flake8_file = join(TEST_DIR, 'flake8_file.py')
                flake8_style = get_style_guide()
                flake8_style.check_files([flake8_file])
            buf.seek(0)
            buf_out = buf.read()
        self.assertIn("F821 undefined name 'boo'", buf_out)
        self.assertEqual(mock_stdout.getvalue(), '')
