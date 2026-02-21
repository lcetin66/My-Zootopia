import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

output = ''
for info in animals_data:
    name = info.get("name")
    characteristics = info.get("characteristics", {})
    diet = characteristics.get("diet")
    locations = info.get("locations")
    location = locations[0]
    type_value = characteristics.get("type")

    output += f"Name: {name}\n"
    output += f"Diet: {diet}\n"
    output += f"Location: {location}\n"
    output += f"{f'Type: {type_value}\n' if type_value else ''}\n"

with open("animals_template.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as f:
    f.write(html)


