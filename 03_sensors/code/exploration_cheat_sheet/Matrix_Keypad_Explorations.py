from keypad import KeyPad
import time

keyPad=KeyPad(14,13,12,11,10,9,8,18)

secret_code = 1235 # This can be changed to anything!
last_numbers = [] # Holds the numbers that you type with the keypad!

def key():
    keyvalue=keyPad.scan()
    if keyvalue!= None:
        print(keyvalue)
        time.sleep_ms(300)
        return keyvalue

print("There's a secret 4 digit code! Type in the correct numbers and hit # to confirm!")

while True:
    last_key = key() # Saves the last key pressed
    if type(last_key) == str and last_key not in ("a", "b", "c", "d", "*", "#"):
        last_numbers.append(last_key)
    
    
        if len(last_numbers) > len(str(secret_code)): # Deletes the oldest element in the list once the list is longer than the code.
            del last_numbers[0]
    
        print("Current Code: " + str(last_numbers))

    if last_key == "#": # If the last key pressed was # then the code will be checked to see if it's correct or not.
        if int("".join(last_numbers)) == secret_code:
            print("Congrats! You got it! The code was " + str(secret_code) + "!")
        elif int("".join(last_numbers)) != secret_code:
            print("Hmmm, try again.")

    
    
    
    
    
    
    
    
    
