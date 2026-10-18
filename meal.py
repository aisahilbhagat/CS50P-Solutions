
# input and output
def main():
    time = convert(input("What time is it? "))
    if 8 >= time >= 7:
        print("breakfast time")
    elif 13 >= time >= 12:
        print("lunch time")
    elif 19 >= time >= 18:
        print("dinner time")
    else:
        ...

# convert time in hrs
def convert(a):
    x , y = a.split(":")
    hrs = round(int(y)/60 + int(x), 2)
    return hrs

if __name__ == "__main__":
    main()