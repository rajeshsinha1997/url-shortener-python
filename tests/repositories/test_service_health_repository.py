"""
This module provides test functions to test methods available in the
module: app.repositories.service_health_repository
"""
from unittest.mock import MagicMock, patch

from pytest import raises

from app.repositories.url_shortener_repository_postgresql import get_database_info


def test_get_database_info_without_engine() -> None:
    """
    Test for the method 'get_database_info' when an invalid instance of the database engine has
    been provided.
    """

    # call function under test and hold the error raised
    with raises(expected_exception=ReferenceError) as __error:
        get_database_info(engine=None, sql_query_string='')

    # asserts
    assert str(
        object=__error.value) == 'invalid instance of the database engine provided: None'


def test_get_database_info_without_result() -> None:
    """
    Test for the method 'get_database_info' when no result value has been retrieved.
    """

    # create mock database engine object
    __mock_database_engine = MagicMock()

    # create mock query string
    __mock_query_string = 'mock query string'

    # create mock query execution result
    __mock_result_value: None = None

    # mock retrieving the result by executing the query
    __mock_database_engine.connect.return_value.__enter__\
        .return_value.execute.return_value.first.return_value = __mock_result_value

    # mock the text method of SQLAlchemy
    with patch(target='app.repositories.service_health_repository.text',
               return_value=MagicMock()) as __mock_patched_text:
        # call the function under test
        __result: str | None = get_database_info(
            engine=__mock_database_engine, sql_query_string=__mock_query_string)

        # asserts
        assert __result == __mock_result_value
        __mock_patched_text.assert_called_once_with(text=__mock_query_string)


def test_get_database_info_with_result() -> None:
    """
    Test for the method 'get_database_info' when a result value has been retrieved successfully.
    """

    # create mock database engine object
    __mock_database_engine = MagicMock()

    # create mock query string
    __mock_query_string = 'mock query string'

    # create mock query execution result
    __mock_result_value: str = 'mock result'

    # mock retrieving the result by executing the query
    __mock_database_engine.connect.return_value.__enter__\
        .return_value.execute.return_value.first.return_value = (__mock_result_value,)

    # mock the text method of SQLAlchemy
    with patch(target='app.repositories.service_health_repository.text',
               return_value=MagicMock()) as __mock_patched_text:
        # call the function under test
        __result: str | None = get_database_info(
            engine=__mock_database_engine, sql_query_string=__mock_query_string)

        # asserts
        assert __result == __mock_result_value
        __mock_patched_text.assert_called_once_with(text=__mock_query_string)
