import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def output_animals(animals):
    output =''
    for animal in animals:
        # append information to each string
        output += '<li class="cards__item">'
        output += f"<div class='card__title'>{animal['name']}</div>\n"
        output += '<p class="card__text">'
        output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
        if "locations" in animal and len(animal["locations"]) > 0:
            output += f"Location: {animal['locations'][0]}<br/>\n"
        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}<br/>\n"
        output += '</p>'
        output += '</li>'
    return output


def main():
    animals_data = load_data('animals_data.json')
    # open and read file
    with open("animals_template.html", "r") as file:
        content = file.read()

    # replace __REPLACE_ANIMALS_INFO__
    content = content.replace("__REPLACE_ANIMALS_INFO__", output_animals(animals_data))

    # write back to file
    with open("animals_template.html", "w") as file:
        file.write(content)

if __name__ == '__main__':
    main()