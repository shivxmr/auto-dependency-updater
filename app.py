import pandas as pd
import requests

def get_user_data():
    """Fetches user data from a public API and returns it as a pandas DataFrame."""
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        df = pd.DataFrame(data)
        print("Successfully fetched and processed user data.")
        return df
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None

def main():
    """Main function to demonstrate the script's functionality."""
    print("Starting the application...")
    user_df = get_user_data()
    if user_df is not None:
        print("First 5 users:")
        print(user_df.head())

if __name__ == "__main__":
    main()
