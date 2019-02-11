from .registry import CommandsRegistry, commands
from .command import Command
from taaontia.exception import TaaontiaNotInitializedException


@commands.register
class StatisticsCommand(Command):
    helper = "Check user's statisctics"
    trigger = "statistics"

    def run(self, taaontia_instance, message):
        if not taaontia_instance.is_initialized():
            raise TaaontiaNotInitializedException
        session = taaontia_instance.get_new_session()

        from taaontia.models.user import User

        user = session.query(User).first()
        message = f"Here are your statistics, {user.username}\n - command count: {user.statistics.command_count}"
        session.close()

        return message
