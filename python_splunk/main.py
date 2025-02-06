import socket

HOST = '192.168.204.132'
PORT = 8080

with open('LAPTOP-K0SAVLK6.err') as error_file:
    errors = error_file.readlines()

# need to close connection after every paket sent,
# so that we will have each event separately in splunk
for index, error in enumerate(errors):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        print('Connection has been made')
        sock.sendall(error.encode())
        print(f'Sending error number {index}')
    