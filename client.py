from taaontia.commands.registry import commands
from taaontia.core import Taaontia


def test():

    taaontia = Taaontia()
    taaontia.init(db_path=None)

    try:
        while True:
            rawcommand = input("> Type in a command:\n> ")
            if rawcommand == "exit":
                break
            parsed_message = rawcommand.split(" ", 2)
            print(
                commands.get(parsed_message[0])(
                    taaontia, parsed_message[1] if len(parsed_message) > 1 else None
                )
            )
            print("\n")
    except (EOFError, KeyboardInterrupt):
        quit_gracefully(taaontia)


def quit_gracefully(taaontia):
    taaontia.close()
    print("Taking a break from your adventure? Fine...")
    exit()


if __name__ == "__main__":
    test()

