
import socket
from Client import BaseClient


class TcpClient(BaseClient):
    def __init__(self, destination, port, size, timeout):
        BaseClient.__init__(self, destination, port, size, timeout)
        print "TCP client initialized"

    def send_ping(self):
        try:
            # create tcp socket for sending data
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(self.timeout)

            send_buf = "a" * self.size

            # connect tcp socket
            print "Connecting to server"
            client_socket.connect((self.destination, self.port))

            print "Sending ping via TCP"
            client_socket.send(send_buf)

            # expect to receive the same amount of data sent
            print "Waiting for response"
            recv_buf = client_socket.recv(self.size)
            if len(recv_buf) == self.size:
                return True

        except socket.timeout:
            print "Connection timeout"
        except socket.error:
            print "Connection error"
        except Exception as e:
            print e.message

        return False
