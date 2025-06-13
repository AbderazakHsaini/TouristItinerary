import requests

def get_coordinates(place_name):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": place_name,
        "format": "json",
        "limit": 1
    }
    
    headers = {
        "User-Agent": "location-coord-finder/1.0"
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    if data:
        lat = data[0]["lat"]
        lon = data[0]["lon"]
        display_name = data[0]["display_name"]
        print(f"Location: {display_name}")
        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}")
    else:
        print("Location not found.")

# Example use
place = input("Enter a location name: ")
get_coordinates(place)

