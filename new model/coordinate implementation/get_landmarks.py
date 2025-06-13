import requests

def get_wikipedia_page_links(page_title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "links",
        "titles": page_title,
        "pllimit": "max"
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    pages = data.get("query", {}).get("pages", {})
    for page_id, page in pages.items():
        if "links" in page:
            return [link["title"] for link in page["links"]]
    return None

def search_wikipedia(title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": title,
        "format": "json"
    }
    response = requests.get(url, params=params)
    results = response.json()
    search_results = results.get("query", {}).get("search", [])
    if search_results:
        return search_results[0]["title"]
    return None

def get_landmarks(city_name):
    # Try common formats
    possible_titles = [
        f"List of tourist attractions in {city_name}",
        f"Tourist attractions in {city_name}",
        f"List of attractions in {city_name}"
    ]
    
    for title in possible_titles:
        landmarks = get_wikipedia_page_links(title)
        if landmarks:
            print(f"\nLandmarks in {city_name} (from: {title}):\n")
            for item in landmarks:
                print(f" - {item}")
            return

    # Fallback: Search Wikipedia
    print(f"\n Couldn't find direct list. Searching Wikipedia for '{city_name}'...")
    found_title = search_wikipedia(f"Tourist attractions in {city_name}")
    if found_title:
        landmarks = get_wikipedia_page_links(found_title)
        if landmarks:
            print(f"\nLandmarks in {city_name} (from: {found_title}):\n")
            for item in landmarks:
                print(f" - {item}")
            return

    print(f"\nNo landmark list found for {city_name} on Wikipedia.")

# Example usage
city = input("Enter a city name: ")
get_landmarks(city)
