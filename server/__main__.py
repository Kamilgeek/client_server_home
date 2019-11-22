import yaml
import select
import json
import logging
from socket import socket
from argparse import ArgumentParser
from handlers import handle_default_request
from resolvers import resolve
from protocol import validate_request, make_response

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

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-10s %(asctime)s %(message)s',
    handlers=[
        logging.FileHandler('log/server.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

requests = []
connections = []

try:
    sock = socket()
    sock.bind((host, port))
    sock.settimeout(0)
    sock.listen(5)

    logging.info(f'Server was started with {host}:{port}')

    while True:
        try:
            client, addres = sock.accept()
            connections.append(client)
            logging.info(f'client was connected with {addres[0]}:{addres[1]} | Connections: {connections}')
        except:
            pass


        rlist, wlist, xlist = select.select(
            connections, connections, connections, 0
        )

        for r_client in rlist:
            b_request = r_client.recv(defaul_config.get('buffersize'))
            requests.append(b_request)

        if requests:
            b_request = requests.pop()
            b_response = handle_default_request(b_request)

            for w_client in wlist:
                w_client.send(b_response)



except KeyboardInterrupt:
    logging.info('server shutdown')
