def calc(x,y,z):
    if y == "+":
        print(round(x+z,1))
    elif y == "-":
        print(round(x-z,1))
    elif y == "*":
        print(round(x*z,1))
    else:
        print(round(x/z,1))

def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    calc(float(x),y,float(z)) 

main()