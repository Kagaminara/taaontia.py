class TaaontiaException(Exception):
    pass


class NoEngineException(TaaontiaException):
    pass


class TaaontiaNotInitializedException(TaaontiaException):
    pass


class CommandException(TaaontiaException):
    pass


class CommandNotImplementedException(CommandException):
    pass
