import pytest
from app import get_user_data

def test_get_user_data():
    """
    Tests the get_user_data function to ensure it returns a non-empty DataFrame.
    This serves as a basic integration test to catch breaking changes in dependencies.
    """
    user_df = get_user_data()
    assert user_df is not None, "The function should return a DataFrame, not None."
    assert not user_df.empty, "The DataFrame should not be empty."
    # Check for expected columns to ensure data integrity
    expected_columns = ["id", "name", "username", "email"]
    for col in expected_columns:
        assert col in user_df.columns, f"Column '{col}' is missing from the DataFrame."
