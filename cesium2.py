dict_example = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": None,  # Default value for color
    "price": 27000
}

brand = dict_example["brand"]
print("Brand:", brand)  # Output: Brand: Ford

price = dict_example["price"]
print("Price:", price)  # Output: Price: 27000

if "color" in dict_example:
    color = dict_example["color"]
    print("Color:", color)  # Output: Color: Red
else:
    print("Color key not found.")

dict_example["model"] = "Cougar"
print("Updated model:", dict_example["model"])  # Output: Updated model: Cougar

dict_example.update({"features": ["Leather seats", "Sunroof"]})
print("Updated features:", dict_example["features"])  # Output: Updated features: ['Leather seats', 'Sunroof']