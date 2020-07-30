
class BaseServer(object):
    def __init__(self, port):
        self.port = port
        self.max_recv_size = 10000

    def set_max_recv_size(self, size):
        self.max_recv_size = size

    def listen(self):
        print "Error - unimplemented"
        return False
