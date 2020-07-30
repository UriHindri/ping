
import argparse
import TcpClient
import TcpServer
import UdpClient
import UdpServer


def handle_commandline_args():
    parser = argparse.ArgumentParser(description="Send or receive ping based on tcp/udp to a selected target")

    parser.add_argument("-c",
                        dest="client",
                        action="store_true",
                        help="run client")
    parser.add_argument("-s",
                        dest="server",
                        action="store_true",
                        help="run server")
    parser.add_argument("-tcp",
                        dest="tcp",
                        action="store_true",
                        help="Use TCP for ping check")
    parser.add_argument("-udp",
                        dest="udp", action="store_true",
                        help="Use UDP for ping check")
    parser.add_argument("-t",
                        type=int,
                        metavar="Timeout",
                        dest="timeout", action="store",
                        help="Timeout for connection")
    parser.add_argument("-n",
                        type=int,
                        metavar="data size",
                        dest="size", action="store",
                        help="size of buffer to send")
    parser.add_argument("-d",
                        dest="destination",
                        type=str,
                        metavar="IP",
                        action="store",
                        help="Destination IP address to check")
    parser.add_argument("-p",
                        dest="port",
                        type=int,
                        metavar="port",
                        action="store",
                        required=True,
                        help="Destination port address to check")
    return parser.parse_args()


def run_client(args):
    print "Starting as client"
    if args.tcp:
        client = TcpClient.TcpClient(args.destination, args.port, args.size, args.timeout)
    elif args.udp:
        client = UdpClient.UdpClient(args.destination, args.port, args.size, args.timeout)
    else:
        print "Error - please specify tcp or udp"
        return -1

    res = client.send_ping()
    if res:
        print "Received response from server"
    else:
        print "Server is not responding"


def run_server(args):
    print "Starting as server"
    if args.tcp:
        server = TcpServer.TcpServer(args.port)
    elif args.udp:
        server = UdpServer.UdpServer(args.port)
    else:
        print "Error - please specify tcp or udp"
        return -1

    return server.listen()


if __name__ == '__main__':
    arguments = handle_commandline_args()

    result = 0
    if arguments.client:
        result = run_client(arguments)
    elif arguments.server:
        result = run_server(arguments)
    else:
        print "please choose server or client"
        result = -1

    exit(result)
