import os

def main():
    print("== BOT RUNNER ==")
    print("1. Normie Bot (boy1)")
    print("2. Shadow Bot (shadowmurmur)")
    choice = input("Pick your bot: ")

    if choice == "1":
        os.system("python3 ../normies/boy1.py")
    elif choice == "2":
        os.system("python3 ../shadow-bots/shadowmurmur.py")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()