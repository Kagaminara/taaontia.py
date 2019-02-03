from .registry import CommandsRegistry


class Command:
    __slots__ = ("helper", "trigger")
    subcommands = CommandsRegistry()

    def __call__(self, message):
        try:
            return self.handler(message)
        except NotImplementedError:
            return self.subcommands.get(message[0])(message[1:])

    def handler(self, _):
        raise NotImplementedError()

