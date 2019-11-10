import yaml, json
from socket import socket
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-c', '--config', type=str,
    required=False, help = 'Sets config file path'
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
try:
    sock = socket()
    sock.bind((host, port))
    sock.listen(5)

    print(f'Server was started with {host}:{port}')

    while True:
        client, addres = sock.accept()
        print(f'client was connected with {addres[0]}:{addres[1]}')
        b_request= client.recv(defaul_config.get('buffersize'))
        request = json.loads(b_request.decode())

        action = request.get('action')

        if action == 'echo':
            print(f'Client send message: {b_request.decode()}')
            client.send(b_request)

        client.close()
except KeyboardInterrupt:
    print('server shutdown')
