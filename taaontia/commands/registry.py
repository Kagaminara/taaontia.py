class CommandsRegistry:
    def __init__(self):
        self.commands = {}

    def register(self, command):
        self.commands[command.trigger] = command()
        return command

    def get(self, command):
        from .helper import HelpCommand

        return self.commands.get(command, HelpCommand())


commands = CommandsRegistry()
