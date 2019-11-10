import yaml, json
from socket import socket
from argparse import ArgumentParser
from .protocol import validate_request, make_response

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
try:
    sock = socket()
    sock.bind((host, port))
    sock.listen(5)

    print(f'Server was started with {host}:{port}')

    while True:
        client, addres = sock.accept()
        print(f'client was connected with {addres[0]}:{addres[1]}')
        b_request = client.recv(defaul_config.get('buffersize'))
        request = json.loads(b_request.decode())

        if validate_request(request):
            action = request.get('action')

            if action == 'echo':
                try:
                    print(f'Client send message: {b_request.decode()}')
                    # client.send(b_request)
                    response = make_response(request, 200, request.get('data'))
                except Exception as err:
                    response = make_response(request, 500, 'Internal server error')
            else:
                response = make_response(request, 404, f'Action with name {action} not supported')
        else:
            response = make_response(request, 400, 'wrong requst format')

        client.send(
            json.dumps(response).encode()
        )

        client.close()
except KeyboardInterrupt:
    print('server shutdown')
