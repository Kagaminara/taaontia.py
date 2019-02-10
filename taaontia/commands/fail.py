from .registry import CommandsRegistry, commands
from .command import Command


@commands.register
class FailCommand(Command):
    helper = "Try something."
    trigger = "fail"

    def run(self, taaontia_instance, message):
        return "You tried something. You failed"

