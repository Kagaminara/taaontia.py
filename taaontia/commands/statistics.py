from .registry import CommandsRegistry, commands
from .command import Command
from taaontia.exception import TaaontiaNotInitializedException


@commands.register
class StatisticsCommand(Command):
    helper = "Check user's statisctics"
    trigger = "statistics"

    def run(self, taaontia_instance, message):
        if not taaontia_instance:
            raise TaaontiaNotInitializedException
        session = taaontia_instance.get_new_session()
        if not session:
            raise TaaontiaNotInitializedException

        from taaontia.models.user import User

        user = session.query(User).first()
        message = f"Here are your statistics, {message}\n - command count: {user.statistics.command_count}"
        session.close()

        return message
