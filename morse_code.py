
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
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


def letters_to_morse_code(sentence):
    cipher = ''
    for text in sentence:
        if text != ' ':
            cipher += MORSE_CODE_DICT[text] + ' '
        else:
            cipher += ' '  
    return cipher

def morse_code_to_letters(sentence):
    
    sentence += ' '
  
    decrypt = '' 
    encrypt = '' 
    for text in sentence:

        if (text != ' '): 
            space_counter = 0
  
            encrypt += text 
  
        else: 
            space_counter += 1
  
            if space_counter == 2 : 
  
                decrypt += ' '
            else:  
                decrypt += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT .values()).index(encrypt)] 
                encrypt = ''            
    return decrypt 
    
def main():
    
    sentence = "Hi There"
    result = letters_to_morse_code(sentence.upper())
    assert len(sentence) != 0, "You cannot not encrypt a empty message"
    print('Encryption Taking Place')
    print(f'Ciphered Message : {result}')
    print(f'Ciphered Message Length : {len(sentence)}')
    
    sentence = ".... ..  - .... . .-. ."
    sentence_len = list(sentence.split(' '))
    result = morse_code_to_letters(sentence)
    assert len(sentence) != 0, " You cannot decipher a empty message"
    print('Decryption Taking Place')
    print(f'Deciphered Message : {result}')
    print(f'Deciphered Message Length : {len(sentence_len)}')
    
if __name__ == "__main__":
    main()
