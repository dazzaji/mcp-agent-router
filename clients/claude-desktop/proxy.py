import socket
import sys
import threading
import argparse
import os

def log(message):
    with open(r'C:\Users\amanda\mcp\proxy.log', 'a') as f:
        f.write(f'{message}\n')

def create_parser():
    parser = argparse.ArgumentParser(description='Proxy stdin/stdout over TCP')
    parser.add_argument('host', help='Remote host to connect to')
    parser.add_argument('port', type=int, help='Remote port to connect to')
    return parser

def forward_stdin(sock):
    """Forward stdin to socket"""
    try:
        while True:
            data = sys.stdin.buffer.read1(4096)
            if not data:
                break
            sock.sendall(data)
    except (socket.error, IOError) as e:
        log(f"Error forwarding stdin: {e}")
    finally:
        try:
            sock.shutdown(socket.SHUT_WR)
        except socket.error:
            pass

def forward_socket(sock):
    """Forward socket data to stdout"""
    try:
        while True:
            data = sock.recv(4096)
            log(f'Received data: {data}')
            if not data:
                break
            sys.stdout.buffer.write(data)
            sys.stdout.buffer.flush()
    except (socket.error, IOError) as e:
        log(f"Error forwarding socket: {e}")

def main():
    log(f'Running proxy.py with arguments: {sys.argv}')
    parser = create_parser()
    args = parser.parse_args()

    try:
        # Create TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((args.host, args.port))
        log(f'Connected to {args.host}:{args.port}')
        
        # Set up threads for bidirectional forwarding
        stdin_thread = threading.Thread(target=forward_stdin, args=(sock,))
        socket_thread = threading.Thread(target=forward_socket, args=(sock,))

        # Start forwarding threads
        stdin_thread.start()
        socket_thread.start()

        # Wait for threads to complete
        stdin_thread.join()
        socket_thread.join()

    except socket.error as e:
        log(f"Socket error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        log("\nExiting due to user interrupt")
    finally:
        try:
            sock.close()
        except NameError:
            pass

if __name__ == "__main__":
    main()
