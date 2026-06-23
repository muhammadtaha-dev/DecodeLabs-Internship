def check_password(pwd):
    has_upper=False
    has_digit=False
    has_symbol=False

    if any(c.isupper() for c in pwd):
        has_upper=True
    if any(c.isdigit() for c in pwd):
        has_digit=True
    if any(c in "!@#$%^&*" for c in pwd):
        has_symbol=True

    if (len(pwd)<8):
        print("Weak")
        return
    if(has_upper==True and has_digit==True and has_symbol==True):
        print("Strong")
    elif(has_upper==True and has_digit==True):
        print("Medium")
    else:
        print("Weak")


def main():
    while True:
        print("\n 1.Check Password \n 2.Quit")
        choice:int=int(input("Enter the choice (1-2):"))
        if(choice==1):
            pwd=str(input("Enter the password:"))
            check_password(pwd)
        elif(choice==2):
            print("Thankyou!")
            break
        else:
            print("Invalid choice!")
            return

if __name__=="__main__":
    main() 