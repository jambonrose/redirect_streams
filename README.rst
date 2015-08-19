====================
 Redirect Streams
====================

Description
-----------

This project provides Python context managers to help redirect multiple
forms of output into a buffer (capturing the output).

The `Basic Usage`_ section below provides a brief overview of the
problem these context managers solve. The full `documentation`_ describes
the problem in more detail, and descibes how the context managers
provided in the package solve the problem.

Installation
------------

The project may be installed via pip:

.. code:: console

    $ pip install redirect-streams

To install the development version:

.. code:: console

    $ pip install git+git://github.com/jambonrose/redirect_streams

Basic Usage
-----------

The most common use of this project is to redirect ``stdout``.

.. code:: python

    from io import BytesIO, SEEK_SET, TextIOWrapper
    from sys import stdout

    from redirect_streams import redirect_stdout

    with TextIOWrapper(BytesIO(), stdout.encoding) as buffer:
        with redirect_stdout(buffer):
            print('this will be saved in the buffer')
        buffer.seek(SEEK_SET)
        saved = buffer.read()
    print(saved)

This behavior is identical to the ``redirect_stdout`` context manager
provided by the ``contextlib`` module in the Python standard library
starting in version 3.4. The key difference is that the context managers
provided here will handle output from forked processes and at the C
level.

.. code:: python

    from io import BytesIO, SEEK_SET, TextIOWrapper
    from os import system
    from sys import stdout

    from redirect_streams import redirect_stdout

    with TextIOWrapper(BytesIO(), stdout.encoding) as buffer:
        with redirect_stdout(buffer):
            # this will not work with the code from stdlib
            system('this will be saved in the buffer')
        buffer.seek(SEEK_SET)
        saved = buffer.read()
    print(saved)

For more information please refer to the `documentation`_.

.. _`documentation`: https://redirect-streams.readthedocs.org/
