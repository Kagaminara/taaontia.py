from .registry import CommandsRegistry, commands
from .command import Command


@commands.register
class SuccessCommand(Command):
    helper = "Try something."
    trigger = "succeed"

    def run(self, message):
        return "You successfully failed"
