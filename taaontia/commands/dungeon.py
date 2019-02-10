from .registry import CommandsRegistry, commands
from .command import Command


@commands.register
class DungeonCommand(Command):
    helper = "Try to explore a dungeon."
    trigger = "dungeon"

    def run(self, taaontia_instance, message):
        return "A latex-covered dominatrix comes to you with a leather whip. You undestand that's not the kind of dungeon you want to explore."

