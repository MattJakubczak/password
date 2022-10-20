###     Combination password generator and complexity checker!      ###
import secrets
import string
import re

def generate():
    letters = string.ascii_letters      #All upper and lowercase ASCII letters to choose from
    digits = string.digits              #All digits to choose from
    special_chars = ('[@_!#$%^&*()<>?/\|}{~:]')  #All special characters to choose from
    alphabet = letters + digits + special_chars #JOIN FORCES!
    pwd_length = 15 #Minimum password length set to 15 for EXTRA SECURITY!
    while True:
        pwd = '' #Initialize the password variable
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        if (any(char in special_chars for char in pwd) and #Force a minimum of one special character
                sum(char in digits for char in pwd) >= 2):  #Force a minimum of two digits
            break
    print('Your new password is: ', pwd) #HERE'S YOUR NEW PASSWORD!

def complexity(): #This function is not perfect, however, it does... Function...
    v = input("Enter the password:") #Enter the password to test for complexity
    if (len(v) >= 12):
        #Let us test the complexity using regular expressions! The STRONG test:
        if (bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[string.punctuation]).{8,30})', v)) == True):
            print("You have entered a STRONG password.")
        #Let us test the complexity using regular expressions! The WEAK test:
        elif (bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})', v)) == True):
            print("You have entered a WEAK password.")
    else: #For any entries that do not fit the STRONG or WEAK tests:
        print("You have entered a WEAK password.")

def main(): #Asking the user to make a selection between checking complexity and generating a new password.
    print("Welcome to Matt's Password Program!")   # Yes, multiple print statements. Easier for ME personally.
    print('Press 1 to generate a password')
    print('Press 2 to test password complexity')
    selection = input('I choose option: ')
    choices = str(selection)
    if choices == '1': # Time to verify the choices!
        generate()
    elif choices == '2':
        complexity()
    else: # Uh-Oh, wrong input!
        print('You have made an invalid selection, please try again.')


if __name__ == '__main__':
    main()

