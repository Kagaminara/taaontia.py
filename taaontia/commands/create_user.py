from .registry import CommandsRegistry, commands
from .command import Command
from taaontia.exception import TaaontiaNotInitializedException


@commands.register
class CreateUserCommand(Command):
    helper = "Create a user"
    trigger = "create"

    def run(self, taaontia_instance, message):
        if not taaontia_instance:
            raise TaaontiaNotInitializedException
        session = taaontia_instance.get_new_session()
        if not session:
            raise TaaontiaNotInitializedException

        from taaontia.models.user import User

        user = User(name=message)
        session.add(user)
        session.commit()
        session.close()

        return f"Welcome, {message}"

