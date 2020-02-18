# Python program to implement Morse Code  
# Dictionary representing the morse code
morse_code = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
  
# encrypt string to Morse Code 
def lettersToMorseCode(message): 
    encrypt = '' 
    for letter in message: 
        if letter != ' ': 
  
            # looks up characters in Dictionary 
            encrypt += morse_code[letter] + ' '
        else: 
            # 1 space indicates different characters 
            # and 2 indicates different words 
            encrypt += ' '
    return encrypt 
  
# decrypt Morse Code to English
def morseCodeToLetters(message): 
  
    # extra space added at the end to access the 
    # last morse code 
    message += ' '
  
    decrypt_text = '' 
    encrypt_text = '' 
    for letter in message: 
  
        # checks for space 
        if (letter != ' '): 
            # counter to keep track of space 
            word = 0
  
            # storing morse code of a single character 
            encrypt_text += letter 
  
        # in case of space 
        else: 
            # if i = 1 that indicates a new character 
            word += 1
  
            # start a new word 
            if word == 2 : 
  
                # space to separate words 
                decrypt_text += ' '
            else:  
                decrypt_text += list(morse_code.keys())[list(morse_code .values()).index(encrypt_text)] 
                encrypt_text = ''            
    return decrypt_text 
  
# driver function to run the program 
def main():

    message = "Hi There"
    result = lettersToMorseCode(message.upper())
    assert len(message) != 0, "You cannot encrypt a black space or character "
    print("Encrypted message has : " + str(len(message)) + " characters") 
    print(result) 
  
    message = ".... ..  - .... . .-. ."
    message_length = list(message.split(' '))
    result = morseCodeToLetters(message) 
    assert len(message) != 0, "You cannot decrypt a black space or character"
    
    print (result)
    print("Decrypted message has : " + str(len(message_length)) + " characters") 
  
# Run main function 
if __name__ == '__main__': 
    main() 
