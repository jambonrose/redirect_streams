Usage
=====

Basic Usage
-----------

The most common use of this project is to redirect ``stdout``.

.. code:: python

    from io import BytesIO, SEEK_SET, TextIOWrapper
    from os import system
    from sys import stdout

    from redirect_streams import redirect_stdout

    with TextIOWrapper(BytesIO(), stdout.encoding) as buffer:
        with redirect_stdout(buffer):
            print('this will be saved in the buffer')
            # code below won't work with stdlib's redirect_stdout
            system('this will be saved in the buffer')
        buffer.seek(SEEK_SET)
        saved = buffer.read()
    print(saved)
