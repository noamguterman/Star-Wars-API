import requests

def fetch_data(option):
  url = f"https://swapi.mimo.dev/api/{option}/"

  data = []

  try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data
  except requests.HTTPError as e:
    print(f"Error: {e} ")
    return None

option = input("What StarWars data would you like to explore? ").strip().lower()

data = fetch_data(option)
  
if data:
  for entity in data:
    print(entity["name"])
else:
  print("Unable to download data")