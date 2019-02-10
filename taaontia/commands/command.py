from .registry import CommandsRegistry
from taaontia.core import Session


class Command:
    __slots__ = ("helper", "trigger")
    subcommands = CommandsRegistry()

    def run(self, message):
        pass

    def __call__(self, message):
        # Things I want to do before actual command goes here
        if Session:
            session = Session()
            session.

        try:
            return self.run(message)
        except NotImplementedError:
            return self.subcommands.get(message[0])(message[1:])
