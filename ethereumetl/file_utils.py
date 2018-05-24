import os
import sys


# https://stackoverflow.com/questions/17602878/how-to-handle-both-with-open-and-sys-stdout-nicely
def get_file_handle(filename, mode='w', binary=False):
    full_mode = mode + ('b' if binary else '')
    is_file = filename and filename != '-'
    if is_file:
        fh = open(filename, full_mode)
    elif filename == '-':
        fd = sys.stdout.fileno() if mode == 'w' else sys.stdin.fileno()
        fh = os.fdopen(fd, full_mode)
    else:
        fh = NoopFile()
    return fh


def close_silently(file_handle):
    if file_handle is None:
        pass
    try:
        file_handle.close()
    except OSError:
        pass


class NoopFile:
    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def readable(self):
        pass

    def writable(self):
        pass

    def seekable(self):
        pass

    def close(self):
        pass

    def write(self):
        pass
