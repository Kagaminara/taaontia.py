from .registry import CommandsRegistry, commands
from .command import Command


@commands.register
class TravelCommand(Command):
    helper = "Try to move a bit ."
    trigger = "travel"

    def run(self, taaontia_instance, message):
        return "You travel a bit to try to change your peevish, poor life. You failed."

