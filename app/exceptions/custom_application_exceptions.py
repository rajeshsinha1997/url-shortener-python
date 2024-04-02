"""
Module: custom_application_exceptions

This module defines the custom exception classes
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


class DatabaseEngineNotInitializedException(Exception):
    """
    Exception raised when the database engine is not initialized.
    """

    def __init__(self, *args: object) -> None:
        """
        Initialize the DatabaseEngineNotInitializedException instance.

        Args:
            *args: Variable length argument list.

        Returns:
            None
        """

        self.exception_message = 'DATABASE ENGINE NOT INITIALIZED'
        super().__init__(*args)



class QueryFileNotFoundException(Exception):
    """
    Exception raised when a SQL query file is not found.
    """

    def __init__(self, exception_message: str) -> None:
        """
        Initialize the QueryFileNotFoundException instance.

        Args:
            exception_message (str): The error message describing the exception.

        Returns:
            None
        """

        self.exception_message: str = exception_message
        super().__init__(exception_message)
