#!/usr/bin/env python3


# Simple API server that listen on a port and print the data received on the console
# The response returned contains a message with informations on the server and the
# name : traitement-A

import socket
import json
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=10000)
    return parser.parse_args()


def run(args):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_address = ('localhost', args.port)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            data = connection.recv(1024)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                response = {
                    "message": "Hello, I am traitement-A",
                    "server": "localhost",
                    "port": args.port
                }
                connection.sendall(json.dumps(response).encode())
            else:
                print('no data from', client_address)
                break

        finally:
            # Clean up the connection
            connection.close()


def main():
    args = parse_args()
    run(args)


if __name__ == "__main__":
    main()
