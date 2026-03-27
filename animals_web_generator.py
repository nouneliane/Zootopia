import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def output_animals(animals):
    output =''
    for animal in animals:
        output += f"Name: {animal['name']}"
        output += f"\nDiet: {animal['characteristics']['diet']}"
        output += f"\nLocation: {", ".join(animal['locations'])}"
        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output += f"\nType: {animal['characteristics']['type']}"
        output += "\n\n"
    return output


def main():
    animals_data = load_data('animals_data.json')
    output_data =output_animals(animals_data)
    print( output_data)


if __name__ == '__main__':
    main()