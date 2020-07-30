
import socket
from Server import BaseServer


class UdpServer(BaseServer):
    def __init__(self, port):
        BaseServer.__init__(self, port)
        self.set_max_recv_size(1472)    # 1514 - 14 - 20 - 8
        print "UDP server initialized"

    def listen(self):
        try:
            # create tcp socket for listening
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            server_socket.bind(('0.0.0.0', self.port))

            print "Waiting for a packet"
            # wait for a single data packet and echo back
            recv_buf, address = server_socket.recvfrom(self.max_recv_size)

            # echo back
            print "Packet received, echo back"
            server_socket.sendto(recv_buf, address)
            return True

        except Exception as e:
            print "Closing server socket: " % e.message

        return False
