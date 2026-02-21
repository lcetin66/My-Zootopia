import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def serialize_animal(animal_obj):
    """Read JSON and convert it to HTML list items"""
    name = animal_obj.get("name", "Unknown")
    characteristics = animal_obj.get("characteristics", {})
    diet = characteristics.get("diet", "Unknown")
    skin_type = characteristics.get("skin_type", "Unknown")
    animal_type = characteristics.get("type")
    locations = animal_obj.get("locations", [])
    location = locations[0] if locations else "Unknown"

    html = "<li class='cards__item'>"
    html += f"<div class='card__title'>{name}</div>"
    html += "<div class='cards__text'>"
    html += f"<ul>"
    html += f"<li><strong>Diet:</strong> {diet}</li>"
    html += f"<li><strong>Skin type:</strong> {skin_type}</li>"
    html += f"<li><strong>Location:</strong> {location}</li>"
    if animal_type:
        html += f"<li><strong>Type:</strong> {animal_type}</li>"
    html += "</ul></div></li>"

    return html

def main():
    """ Main function """
    data = load_data("animals_data.json")

    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj)

    with open('animals_template.html', 'r', encoding='utf-8') as data_file:
        html_content = data_file.read()

    html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', output)

    with open('animals.html', 'w', encoding='utf-8') as data_file:
        data_file.write(html_content)


if __name__ == '__main__':
    main()