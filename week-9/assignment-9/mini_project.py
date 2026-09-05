import requests

import json



headers = {"Authorization": "Bearer rc_live_5df66c893b684828835d44663d0d21e7"}
base_url = "https://api.restcountries.com/countries/v5"

def fetch_countries():
    # Fetch all countries with requested fields
    url = f"{base_url}?response_fields=names.official,capitals,region,population"
    
    try:
        response = requests.get(url, headers=headers)
        
        # Check if HTTP status code is anything other than 200
        if response.status_code != 200:
            print(f"Error: API returned status code {response.status_code}")
            return None

        result = response.json()
        
        # Extract objects list based on sample schema
        raw_objects = result.get("data", {}).get("objects", [])
        
        cleaned_countries = []
        for item in raw_objects:
            # 1. Official Name
            name = item.get("names", {}).get("official", "N/A")

            # 2. Capital (handles missing capitals cleanly)
            capitals_list = item.get("capitals", [])
            if isinstance(capitals_list, list) and len(capitals_list) > 0:
                capital = capitals_list[0].get("name", "N/A")
            else:
                capital = "N/A"

            # 3. Region and Population
            region = item.get("region", "N/A")
            population = item.get("population", 0)

            cleaned_countries.append({
                "name": name,
                "capital": capital,
                "region": region,
                "population": population
            })

        return cleaned_countries

    except requests.exceptions.RequestException as e:
        print(f"Error: Could not reach the server ({e}). Check your connection and try again.")
        return None

def search_by_name(countries):
    search_term = input("Search: ").strip().lower()
    matches = [c for c in countries if search_term in c["name"].lower()]

    if not matches:
        print("No matching countries found.\n")
        return

    for c in matches:
        print(f"{c['name']} — Capital: {c['capital']} | Region: {c['region']} | Population: {c['population']:,}")
    print()

def filter_by_region(countries):
    region_term = input("Enter region (e.g., Africa, Asia, Europe): ").strip().lower()
    matches = [c for c in countries if c["region"].lower() == region_term]

    if not matches:
        print(f"No countries found in region '{region_term}'.\n")
        return

    # Sort matches by population descending (largest first)
    sorted_matches = sorted(matches, key=lambda x: x["population"], reverse=True)

    for c in sorted_matches:
        print(f"{c['name']} — Capital: {c['capital']} | Region: {c['region']} | Population: {c['population']:,}")
    print()

def main():
    print("Fetching country data...")
    countries = fetch_countries()

    if countries is None:
        return  # Exit if the API request failed

    while True:
        print("=== Country Explorer ===")
        print("1. Search by name")
        print("2. Filter by region")
        print("3. Quit")
        
        choice = input("Choose an option (1-3): ").strip()
        print()

        if choice == "1":
            search_by_name(countries)
        elif choice == "2":
            filter_by_region(countries)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()