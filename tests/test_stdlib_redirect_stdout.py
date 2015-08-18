#!/usr/bin/env python
from __future__ import print_function, unicode_literals

from sys import version_info as pythonversion
from unittest import TestCase, expectedFailure, skipIf

from base import BaseMixin

try:
    from contextlib import redirect_stdout
except:  # version < 3.4
    contextlib = None


@skipIf(pythonversion < (3, 4), "Python 3.4+ required.")
class RedirectTests(BaseMixin, TestCase):
    redirect_stdout_ctx = redirect_stdout

    test_system = expectedFailure(BaseMixin.test_system)
    test_libc = expectedFailure(BaseMixin.test_libc)
