nested_dict = {
    "person1": {"name": "Juan", "age": 22, "city": "Bogotá"},
    "person2": {"name": "Pepe", "age": 15, "city": "Medallo"},
    "person3": {"name": "Laura", "age": 25, "city": "Veneca"},
}

print(nested_dict)

for person, info in nested_dict.items():
    print(f"\n {person}:")
    for item, value in info.items():
        print(f"  {item}: {value}")
    print()
