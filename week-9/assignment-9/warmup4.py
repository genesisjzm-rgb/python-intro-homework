import requests


def fetch_data():
    # URL designed to fail as specified in the assignment
    url = "https://thisurldoesnotexist.example.com"

    try:
        response = requests.get(url)
        
        # Check if the HTTP status code is anything other than 200
        if response.status_code != 200:
            print(f"Error: Server returned status code {response.status_code}.")
            return

        # Parse JSON only if status_code == 200
        data = response.json()
        print("Data successfully fetched:", data)

    except requests.exceptions.RequestException:
        # Catch connection failures, DNS errors, timeouts, etc.
        print("Error: Could not reach the server. Check your connection and try again.")

if __name__ == "__main__":
    fetch_data()