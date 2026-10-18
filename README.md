# CS50P-Solutions
So i am a young developer trying to learn python so here are the solutions i have come up with. 

# CS50P Lecture 2 : camelCase
**My Solution to it a little simple but it does the job**
python```def snake_case(name):
    size = len(name)
    for char in name:
            if char.isupper():
                lchar = char.lower()
                name = name.replace(char , f"_{lchar}")
    return name

def main():
    name = input("camelCase: ").strip()
    print("snake_case:", snake_case(name))

main()```
