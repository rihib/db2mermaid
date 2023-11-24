from db2mermaid.db2mermaid import DB2Mermaid
from dotenv import load_dotenv

import os

load_dotenv()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
NAME = os.getenv('NAME')

if __name__ == '__main__':
    dm = DB2Mermaid()
    dm.init_db(USERNAME, PASSWORD, HOST, PORT, NAME)
    dm.generate()
