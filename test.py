def load_habitat(file_name):
    """
    Load a habitat file and return a list of entries
    """
    try:
        with open(file_name, 'r') as f:
            entries = [line.strip().split(', ') for line in f.readlines()]
        return entries
    except FileNotFoundError:
        print(f"Habitat file '{file_name}' not found.")
        return []

def save_habitat(file_name, entries):
    """
    Save a list of entries to a habitat file
    """
    with open(file_name, 'w') as f:
        for entry in entries:
            f.write(', '.join(entry) + '\n')

def add_entry(file_name, entry):
    """
    Add an entry to a habitat file
    """
    entries = load_habitat(file_name)
    entries.append(entry)
    save_habitat(file_name, entries)

def find_entry_by_image_id(file_name, image_id):
    """
    Find an entry by image ID
    """
    entries = load_habitat(file_name)
    for entry in entries:
        if entry[3] == image_id:
            return entry
    return None

def find_entry_by_common_name(file_name, common_name):
    """
    Find an entry by common name
    """
    entries = load_habitat(file_name)
    for entry in entries:
        if entry[0] == common_name:
            return entry
    return None

def find_entry_by_scientific_name(file_name, scientific_name):
    """
    Find an entry by scientific name
    """
    entries = load_habitat(file_name)
    for entry in entries:
        if entry[1] == scientific_name:
            return entry
    return None

def main():
    file_name = input("Enter the habitat file name: ")
    
    while True:
        print("\nOptions:")
        print("1. Add an entry")
        print("2. Find entry by image ID")
        print("3. Find entry by common name")
        print("4. Find entry by scientific name")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            entry = input("Enter the entry (common name, scientific name, gender, image ID): ").split(', ')
            add_entry(file_name, entry)
        elif choice == "2":
            image_id = input("Enter the image ID: ")
            entry = find_entry_by_image_id(file_name, image_id)
            if entry:
                print(entry)
            else:
                print("Entry not found.")
        elif choice == "3":
            common_name = input("Enter the common name: ")
            entry = find_entry_by_common_name(file_name, common_name)
            if entry:
                print(entry)
            else:
                print("Entry not found.")
        elif choice == "4":
            scientific_name = input("Enter the scientific name: ")
            entry = find_entry_by_scientific_name(file_name, scientific_name)
            if entry:
                print(entry)
            else:
                print("Entry not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()