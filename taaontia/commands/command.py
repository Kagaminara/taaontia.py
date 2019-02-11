from .registry import CommandsRegistry


def increment_command_count(taaontia_instance):
    from taaontia.models.user import User
    from taaontia.models.statistics import Statistics

    session = taaontia_instance.get_new_session()
    user = session.query(User).first()
    if user:
        if not user.statistics:
            user.statistics = Statistics(command_count=0)
        user.statistics.command_count += 1
        session.commit()
    session.close()
    pass


class Command:
    __slots__ = ("helper", "trigger")
    subcommands = CommandsRegistry()

    def run(self, taaontia_instance, message):
        pass

    def __call__(self, taaontia_instance, message):
        if taaontia_instance.is_initialized():
            increment_command_count(taaontia_instance)

        try:
            return self.run(taaontia_instance, message)
        except NotImplementedError:
            return self.subcommands.get(message[0])(message[1:])
