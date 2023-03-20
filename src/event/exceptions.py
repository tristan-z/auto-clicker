class FindImageError(Exception):
    """Exception raised for errors with finding images.

    Attributes:
        message -- explanation of the error
    """

    default_message = "Could not find specified image."

    def __init__(self, message=default_message):
        self.message = message
        super().__init__(self.message)
