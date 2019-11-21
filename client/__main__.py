import yaml
import zlib
import json
import logging
import hashlib
from socket import socket
from argparse import ArgumentParser
from datetime import datetime

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



logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-10s %(asctime)s %(message)s',
    handlers = [
        logging.FileHandler('log/client.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)



host, port = defaul_config.get('host'), defaul_config.get('port')

sock = socket()
sock.connect((host, port))

logging.info(f'Client was started')

hash_obj = hashlib.sha256()
hash_obj.update(
    str(datetime.now().timestamp()).encode()
)

action = input('Enter action:')
data = input('Enter data:')

request = {
    'action': action,
    'time': datetime.now().timestamp(),
    'data': data,
    'token': hash_obj.hexdigest()
}

s_request = json.dumps(request)
b_request = zlib.compress(s_request.encode())

sock.send(b_request)

logging.info(f'Client send data: {data}')
compressed_response = sock.recv(defaul_config.get('buffersize'))
b_response = zlib.decompress(compressed_response)

logging.info(b_response.decode())

