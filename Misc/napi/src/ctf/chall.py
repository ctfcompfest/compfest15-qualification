password = open("creds.txt", "r")

del __builtins__.__import__

def main():
    banned = ['eval', 'exec', 'import', 'open', 'system', 'globals', 'os', 'password', 'admin']

    print("--- Prisoner Limited Access System ---")

    user = input("Enter your username: ")

    if user == "john":
        inp = input(f"{user} > ")

        while inp != "exit":
            for keyword in banned:
                if keyword in inp.lower() or not inp.isascii():
                    print(f"Cannot execute unauthorized input {inp}")
                    print("I told you our system is hack-proof.")
                    exit()
            try:
                eval(inp)
            except:
                print(f"Cannot execute {inp}")
            
            inp = input(f"{user} > ")

    elif user == "admin":
        print("LOGGING IN TO ADMIN FROM PRISONER SHELL IS NOT ALLOWED")
        print("SHUTTING DOWN...")
        exit()
    
    else:
        print("User not found.")

def admin(password_io=None):
    if password_io == globals()['password']:
        print(f"Welcome admin!")
        print("Here's the flag: ")
        with open("notice.txt", "r") as f:
            print(f.read())
    else:
        print("Wrong password!")
    

if __name__ == "__main__":
    try:
        main()
    except:
        print("Something horribly wrong happened")
