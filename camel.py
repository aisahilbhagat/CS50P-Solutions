
def snake_case(name):
    size = len(name)
    for char in name:
            if char.isupper():
                lchar = char.lower()
                name = name.replace(char , f"_{lchar}")
    return name

def main():
    name = input("camelCase: ").strip()
    print("snake_case:", snake_case(name))

main()