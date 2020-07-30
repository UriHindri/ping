
import socket
from Client import BaseClient


class UdpClient(BaseClient):
    def __init__(self, destination, port, size, timeout):
        BaseClient.__init__(self, destination, port, size, timeout)
        self.set_max_send_size(1472)
        print "UDP client initialized"

    def send_ping(self):
        try:
            # create tcp socket for sending data
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            client_socket.settimeout(self.timeout)

            # send and receive buffer on the udp socket
            send_buf = "a" * self.size
            print "Sending ping via UDP"
            client_socket.sendto(send_buf, (self.destination, self.port))

            # expect to receive the same amount of data sent
            print "Waiting for response"
            recv_buf, address = client_socket.recvfrom(self.max_send_size)
            if len(recv_buf) == self.size:
                return True

        except socket.timeout:
            print "Connection timeout"
        except socket.error:
            print "Connection error"
        except Exception as e:
            print e.message

        return False
