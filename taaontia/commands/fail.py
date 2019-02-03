from registry import CommandsRegistry, commands
from command import Command


@commands.register
class FailCommand(Command):
    helper = "Try something."
    trigger = "fail"

    def __call__(self, message):
        return "You tried something. You failed"

