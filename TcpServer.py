
import socket
from Server import BaseServer


class TcpServer(BaseServer):
    def __init__(self, port):
        BaseServer.__init__(self, port)
        print "TCP server initialized"

    def listen(self):
        try:
            # create tcp socket for listening
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', self.port))
            sock.listen(1)

            print "Listening for a connection"
            connection, server_address = sock.accept()

            # connection received, echo back
            recv_buf = connection.recv(self.max_recv_size)
            print "Data received, echo back"
            connection.send(recv_buf)
            connection.close()
            return True
        except Exception as e:
            print "Closing server socket: %s" % e.message

        return False
