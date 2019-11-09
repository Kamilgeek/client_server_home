import timestamp
import yaml
from socket import socket
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-c', '--config', type=str,
    required=False, help='Sets config file path'
)

args = parser.parse_args()

defaul_config = {
    'host': 'localhost',
    'port': 8000,
    'buffersize': 1024
}

if args.config:
    with open(args.config) as file:
        file_config = yaml.load(file, Loader=yaml.Loader)
        defaul_config.update(file_config)

host, port = defaul_config.get('host'), defaul_config.get('port')

sock = socket()
sock.connect((host, port))

print(f'Client was started')

data = input('Enter data:')
msg_to_server = {
    'action': 'presence',
    'data': data,
    'time': timestamp()
}

sock.send(str(msg_to_server).encode())
print(f'Client send data: {data}')
b_response = sock.recv(defaul_config.get('buffersize'))
print(b_response.decode())
