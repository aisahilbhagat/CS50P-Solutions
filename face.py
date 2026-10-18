# ask the user for sentence and display it
def main():
    sen = convert(input("Enter your sentence: "))
    print(sen)

#convert into emojies
def convert(sen="fk yu for entering :)"):
    sen = sen.replace(":)","🙂").replace(":(","😞")
    return sen

main()