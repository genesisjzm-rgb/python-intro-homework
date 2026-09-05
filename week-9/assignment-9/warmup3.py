#Fetch from endpoint to return a list of countries in Europe

#Then loop throught list and print common name of each country on its own line.
#Print only the first 10 results


import requests

def fetch_european_countries():


    base_url = "https://api.restcountries.com/countries/v5"
    headers = {
        "Authorization": "rc_live_5df66c893b684828835d44663d0d21e7"
    }

    try:
        response = requests.get(f"{base_url}/region/Europe?response_fields=names.official,population", headers=headers)
        response.raise_for_status()
        result = response.json()

        # Extract list from 'data' key returned by v5
        countries = result.get("data", result) if isinstance(result, dict) else result

        cleaned = []
        # Slice for the first 10 countries
        for item in countries[:10]:
            # Access singular "name" dictionary safely
            name_dict = item.get("name") or item.get("names") or {}
            common_name = name_dict.get("common", "Unknown")
            cleaned.append(common_name)

        # OUTSIDE the for loop so it returns all 10
        return cleaned

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def print_summary(countries):
    # Print each common name on its own line
    for country_name in countries:
        print(country_name)

if __name__ == "__main__":
    countries = fetch_european_countries()
    if countries:
        print_summary(countries)