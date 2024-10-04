def main():
    slow = input("Input ")
    replace(slow)

def replace(text):
    new_str = text.replace(" ", "...")
    print(new_str)

main()
