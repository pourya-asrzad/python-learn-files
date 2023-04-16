class InvalidOperationError(Exception):
    pass

class Stream:
    def __init__(self):
        self.opened =True

    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already open')
        self.opened=True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('Stream is already close')
        self.opened=False




class FileStreem(Stream):
    def read(self):
        print('Reading data from a file')

class NetworkStreem(Stream):
    def read(self):
        print('Reading data from a network')

test = Stream()
test.open()