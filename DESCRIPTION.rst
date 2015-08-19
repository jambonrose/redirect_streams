`Package Documentation`_

Description
-----------

This project provides Python context managers to help redirect multiple
forms of output into a buffer (capturing the output).

Installation
------------

.. code:: console

    $ pip install redirect-streams

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

For other context managers and more detailed information, please refer
to the `documentation`_.

.. _`documentation`: https://redirect-streams.readthedocs.org/
.. _`Package Documentation`: `documentation`_
