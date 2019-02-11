from marshmallow import Schema, fields, post_load
import json
from uuid import uuid4
from socket import gethostname
from os import path
from datetime import datetime
from taaontia.commands.registry import commands
from taaontia.core import Taaontia
from getpass import getpass

from sys import argv

auth_path = argv[1] if len(argv) > 1 else "./auth.data"


class Authentication(object):
    def __init__(self, auth_key, machine_name=None, creation_date=None):
        self.auth_key = auth_key
        self.machine_name = machine_name or gethostname()
        self.creation_date = creation_date or datetime.now()

    def __repr__(self):
        return f"<Authentication(auth_key={self.auth_key}, machine_name={self.machine_name}, creation_date={self.creation_date})>"


class AuthenticationSchema(Schema):
    auth_key = fields.UUID()
    machine_name = fields.Str()
    creation_date = fields.DateTime()

    @post_load
    def make_authentication(self, data):
        return Authentication(**data)


class TaaontiaClient(object):
    """Client to use with taaontia.py"""

    taaontia: Taaontia
    auth_key = None

    def create_auth_file(self):
        auth = Authentication(auth_key=self.auth_key)
        schema = AuthenticationSchema(strict=True)
        dump = schema.dump(auth)
        if dump:
            with open(auth_path, "w+") as file:
                file.write(json.dumps(dump.data))
            return True
        return False

    def get_authentication_info(self):
        try:
            with open(auth_path) as f:
                dumps = f.read()
            dump = json.loads(dumps)
            schema = AuthenticationSchema(strict=True)
            result = schema.load(dump)
            auth = result.data or None
        except FileNotFoundError:
            return None
        return auth

    def prompt_credentials(self):
        username = input("Username: ")
        password = getpass("Password: ")
        return username, password

    def init(self):
        self.taaontia = Taaontia()
        # self.taaontia.init(db_path=None)
        self.taaontia.init()
        credentials = self.get_authentication_info()
        connected = None
        if credentials:
            connected = self.taaontia.connect(auth_key=credentials.auth_key)
        if not connected:
            username, password = self.prompt_credentials()
            self.auth_key = self.taaontia.connect(
                auth_key=credentials.auth_key if credentials else None,
                username=username,
                password=password,
            )
            if not self.auth_key or not self.create_auth_file():
                print("Couldn't log to Taaontia")
                self.quit_gracefully()
        self.play()

    def play(self):
        try:
            while True:
                rawcommand = input("> Type in a command:\n> ")
                if rawcommand == "quit":
                    self.quit_gracefully()
                parsed_message = rawcommand.split(" ", 2)
                print(
                    commands.get(parsed_message[0])(
                        self.taaontia, parsed_message[1] if len(parsed_message) > 1 else None
                    )
                )
                print("\n")
        except (EOFError, KeyboardInterrupt):
            self.quit_gracefully()

    def quit_gracefully(self):
        self.taaontia.close()
        print("Taking a break from your adventure? Fine...")
        exit()


def main():
    taaontia_client = TaaontiaClient()
    taaontia_client.init()


if __name__ == "__main__":
    main()

