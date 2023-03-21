from exceptions import BaseError


class ScriptFileError(BaseError):
    """Exception raised for errors encounterd when interacting with script files.

    Attributes:
        message -- explanation of the error
    """

    default_message = "Issue with script file."

    def __init__(self, message=default_message):
        self.message = message
        super().__init__(self.message)


class ScriptExecutionError(BaseError):
    """Exception raised for errors encounterd when executing script instructions.

    Attributes:
        message -- explanation of the error
    """

    default_message = "Issue executing script instruction."

    def __init__(self, message=default_message):
        self.message = message
        super().__init__(self.message)
