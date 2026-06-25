def encrypt_text(text,shift):
    encrypted_text=""
    
    for i in text:
        if (i.isupper()):
            encrypted_text+=chr((ord(i)-ord('A')+shift)%26+ord('A'))         
        
        elif (i.islower()):
            encrypted_text+=chr((ord(i)-ord('a')+shift)%26+ord('a'))
        else:
            encrypted_text+=i
    print(f"Text: {text}")
    print(f"Encrypted Text: {encrypted_text}")

def decrypt_text(text,shift):
    decrypted_text=""
    for i in text:
        if i.isupper():
            decrypted_text+=chr((ord(i)-ord('A')-shift)%26+ord('A'))
        elif i.islower():
            decrypted_text+=chr((ord(i)-ord('a')-shift)%26+ord('a'))
        else:
            decrypted_text+=i
    print(f"Text: {text}")
    print(f"Decrypted Text: {decrypted_text}")
        
def main():
    while True:

        print("\n 1.Encrypt Text \n 2.Decrypt Text \n 3.Exit")
        choice:int=int(input("Enter your choice(1-3): "))

        if(choice==1):
            text:str=str(input("Enter the text: "))
            shift:int=int(input("Enter the shift number:"))
            encrypt_text(text,shift)

        elif(choice==2):
            text:str=str(input("Enter the text: "))
            shift:int=int(input("Enter the shift number:"))
            decrypt_text(text,shift)    

        elif(choice==3):
            print("Good Bye!")
            break

        else:
            print("Invalid Choice!")
            continue

if __name__=="__main__":
    main()