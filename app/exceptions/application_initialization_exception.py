"""
Module: application_initialization_exception

This module defines the ApplicationInitializationException class, which is used to represent
errors related to application initialization.
"""

class ApplicationInitializationException(Exception):
    """
    Exception class for application initialization errors.
    """

    def __init__(self, exception_message: str) -> None:
        """
        Initialize the ApplicationInitializationException.

        Args:
            exception_message (str): The message describing the exception.

        Returns:
            None
        """

        self.exception_message: str = exception_message
        super().__init__(exception_message)
