# process the input
def process(extension):
    if extension in ("jpg","jpeg"):
        print("image/jpeg")
    elif extension in ("gif", "png"):
        print(f"image/{extension}")
    elif extension in ("pdf", "zip"):
        print(f"application/{extension}")
    elif extension == "txt":
        print(f"text/plain")
    else:
        print("application/octet-stream")



# ask the questions
def main():
    file_name = input("File name: ").strip()
    name , extension = file_name.rsplit(".")
    process(extension)

main()

# a = "hello.py"
# a , b = a.rsplit(".")
# print(b)