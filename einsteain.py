# take the user input as interger
def main():
    mass = int(input("Enter the Mass: "))
    print(f"M: {mass}")
    energy = engine(mass)
    print(f"E: {energy}")
    
# E = MC2
# convert it into energy
def engine(mass=0):
    light = 300000000
    energy = mass*pow(light,2)
    return energy

main()

    