import random
import string

def generate_password():
    print("Random Password Generator")

    try:
        length = int(input("Enter Desired Password length (minimum 6 ): "))
    except ValueError:
        print("❌💀 Invalid Input Plz Enter A Numeber")
        return
    
    if length < 6:
        print("❌💀 Password Too Short! Must Be Atleast 6 Characters")
        return
    12
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation


    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)



    random.shuffle(password)


    final_password = ''.join(password)    
    print(f"\n🔐🔒Secure Password Is: \n{final_password}")

generate_password()

