from marshmallow import Schema, fields
from uuid import uuid4
from socket import gethostname
from os import path
from datetime import datetime
from taaontia.commands.registry import commands
from taaontia.core import Taaontia

auth_path = "./auth.data"


class Authentication(object):
    def __init__(self, auth_key):
        self.auth_key = auth_key
        self.machine_name = gethostname()
        self.creation_date = datetime.now()


class AuthenticationSchema(Schema):
    auth_key = fields.UUID()
    machine_name = fields.Str()
    creation_date = fields.DateTime()


class TaaontiaClient(object):
    """Client to use with taaontia.py"""

    taaontia: Taaontia

    def create_auth_file(self, auth_key):
        auth = Authentication(auth_key=auth_key)

    def init(self):
        self.taaontia = Taaontia()
        self.taaontia.init(db_path=None)
        if not path.isfile(auth_path):
            self.taaontia.connect()

    def test(self):
        try:
            while True:
                rawcommand = input("> Type in a command:\n> ")
                if rawcommand == "exit":
                    break
                parsed_message = rawcommand.split(" ", 2)
                print(
                    commands.get(parsed_message[0])(
                        self.taaontia, parsed_message[1] if len(parsed_message) > 1 else None
                    )
                )
                print("\n")
        except (EOFError, KeyboardInterrupt):
            self.quit_gracefully(self.taaontia)

    def quit_gracefully(self, taaontia):
        self.taaontia.close()
        print("Taking a break from your adventure? Fine...")
        exit()


def main():
    taaontia_client = TaaontiaClient()
    taaontia_client.test()


if __name__ == "__main__":
    main()

