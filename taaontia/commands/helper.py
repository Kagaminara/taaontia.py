from registry import CommandsRegistry, commands
from command import Command


@commands.register
class HelpCommand(Command):
    helper = "Show this help."
    trigger = "help"

    def __call__(self, message):
        if message:
            return commands.get(message).helper
        ret = "```"
        for _, command in commands.commands.items():
            ret += "{} - {}\n".format(command.trigger, command.helper)
            for _, subCommand in command.subcommands.commands.items():
                ret += "\t{} - {}\n".format(subCommand.trigger, subCommand.helper)
        return ret + "```"
