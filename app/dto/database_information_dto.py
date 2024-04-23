"""
Module: database_information_dto

This module defines a data class representing database information.
"""

from dataclasses import dataclass

from app.constants.application_constant import APPLICATION_STATUS_DOWN


@dataclass(kw_only=True)
class DatabaseInformationDTO:
    """
    Data class representing database information.

    Attributes:
        database_name (str): The name of the database.
        database_version (str): The version of the database.
        database_connectivity (str): The connectivity status of the database.
    """
    database_name: str = 'database name'
    database_version: str = 'database version'
    database_connectivity: str = APPLICATION_STATUS_DOWN
