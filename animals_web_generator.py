import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

for info in animals_data:
    name = info.get("name")
    characteristics = info.get("characteristics", {})
    diet = characteristics.get("diet")
    locations = info.get("locations")
    location = locations[0]
    type_value = characteristics.get("type")

    print(
        f"Name: {name}\n"
        f"Diet: {diet}\n"
        f"Location: {location}\n"
        f"{f'Type: {type_value}\n' if type_value else ''}"
    )




