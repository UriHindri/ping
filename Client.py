
class BaseClient(object):
    def __init__(self, destination, port, size, timeout):
        self.destination = destination
        self.port = port
        self.size = size
        self.timeout = timeout
        self.max_send_size = 10000

    def set_max_send_size(self, size):
        self.max_send_size = size

    def send_ping(self):
        print "Error - unimplemented"
        return False
