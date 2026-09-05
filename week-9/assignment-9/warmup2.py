#Access and print just name and age from the response.
#Try accessing a key that doesnt exist in the response and handle the exception gracefully.

import requests

def fetch_nameage():
    url = "https://api.agify.io/?name=michael"
    params = {"fields": "name,age"}

    try: 
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        print("Name:", data.get("name"))
        print("Age:", data.get("age"))

        #access a key that doesn't exist
        birthday = data.get("birthday", "Not available")
        print("Birthday:", birthday)


    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

fetch_nameage()



