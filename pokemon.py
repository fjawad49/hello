
def read_pokemon_data():
    """
    Reads pokemon data from a file and returns a dictionary.
    Returns:
        A dictionary where keys are pokemon types
        and values are dictionaries of properties.
    """
    # Reading the filename from the user input
    pokemon_data_file = input()
    with open(pokemon_data_file, 'r') as read_file:
        initial_lines = read_file.readlines()

    data_lines = []
    properties = []

    # Separate the lines into header and data
    for line in initial_lines:
        if not line.startswith('#'):
            data_lines.append(line.strip().split(","))
        else:
            properties = line.lower().strip().split(",")

    # Renaming specific properties to match the query input
    properties[8] = "specialattack"
    properties[9] = "specialdefense"

    pokemon_data = {}

    # Populating the pokemon_data dictionary
    for line in data_lines:
        pokemon_type = line[2]
        inner_dict = {}

        if pokemon_type not in pokemon_data:
            for i in range(4, 11):
                inner_dict[properties[i]] = int(line[i])
            inner_dict["count"] = 1
            pokemon_data[pokemon_type] = inner_dict
        else:
            for i in range(4, 11):
                pokemon_data[pokemon_type][properties[i]] += int(line[i])
            pokemon_data[pokemon_type]["count"] += 1

    return pokemon_data


def compute_averages(pokemon_data):
    """
    Computes averages of various properties for each type of pokemon.

    Parameters:
        pokemon_data: Dictionary containing summed up properties and counts.

    Returns:
        A dictionary containing the average properties.
    """
    # Initialize an empty dictionary to store the average data
    average_data = {}

    # Compute the average for each attribute of each type
    for pokemon_type, properties in pokemon_data.items():
        count = properties.pop("count")
        average_values = {}
        for prop, value in properties.items():
            average_value = value / count
            average_values[prop] = average_value
        # Store the average values for this type
        average_data[pokemon_type] = average_values

    return average_data


def process_queries(averages):
    """
    Processes user queries to find the pokemon type with the maximum average for a given property.

    Parameters:
        averages: Dictionary containing average properties for each pokemon type.
    """
    while True:
        query = input().strip().lower()
        if query == "":
            break
        # Continue to the next iteration if the query is invalid
        if query not in ["total", "hp", "attack", "defense", "specialattack", "specialdefense", "speed"]:
            continue

        max_avg = 0
        max_types = []
        # Finding the type with the maximum average for the queried attribute
        for pokemon_type, values in averages.items():
            if values[query] > max_avg:
                max_avg = values[query]
                max_types = [pokemon_type]
            elif values[query] == max_avg:
                max_types.append(pokemon_type)

        max_types.sort()
        for pokemon_type in max_types:
            print(f"{pokemon_type}: {max_avg}")


def main():
    """
    Main function to execute the program.
    """
    pokemon_data = read_pokemon_data()
    averages = compute_averages(pokemon_data)
    process_queries(averages)


if __name__ == "__main__":
    main()

