import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def read_and_convert_data(data):
    """Read JSON and convert it to HTML list items"""
    output = ""

    for animal_data in data:
        name = animal_data.get("name", "Unknown")

        characteristics = animal_data.get("characteristics", {})
        diet = characteristics.get("diet", "Unknown")
        animal_type = characteristics.get("type")

        locations = animal_data.get("locations", [])
        location = locations[0] if locations else "Unknown"

        output += "<li class='cards__item'>"
        output += f"<div class='card__title'>{name}</div>"
        output += "<p class='cards__text'>"
        output += f"<strong>Diet:</strong> {diet}<br>"
        output += f"<strong>Location:</strong> {location}<br>"

        if animal_type:
            output += f"<strong>Type:</strong> {animal_type}"

        output += "</p>"
        output += "</li>"

    return output

def write_data(output, file_path):
    """ Writes HTML content to file """
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', output)

    with open('animals.html', "w", encoding="utf-8") as file:
        file.write(html_content)

def main():
    """ Main function """
    data = load_data('animals_data.json')
    output = read_and_convert_data(data)
    write_data(output, 'animals_template.html')


if __name__ == '__main__':
    main()


