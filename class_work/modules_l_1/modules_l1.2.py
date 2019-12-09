import os
import shutil

ROOT_DIR = 'example'
BASE_DIR = 'data'
BASE_PATH = os.path.join(ROOT_DIR, BASE_DIR)

FILE_NAME = 'example.txt'
FILE_PATH = os.path.join(ROOT_DIR, BASE_DIR, FILE_NAME)

# if not os.path.exists(ROOT_DIR):
#     os.mkdir('example')
#
# if not os.path.exists(BASE_PATH):
#     os.mkdir(BASE_PATH)

# with open(FILE_NAME, 'w') as file:
#     file.close()
# os.remove(FILE_NAME)
shutil.rmtree(ROOT_DIR)