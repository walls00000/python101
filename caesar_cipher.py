alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
alphabetLength = alphabet.__len__()

def run_caesar():
    stringToEncrypt = input("Please enter a message to encrypt")   
    shiftMessage = "Please enter a whole number from -%d to %d to be your key" % (alphabetLength-1, alphabetLength-1)
    intKey = int(input(shiftMessage))
    encrypted = caesar_cipher(stringToEncrypt, intKey)    
    print("Your encrypted message is", encrypted)

def caesar_cipher(clearText, shiftAmount):
    """ caesar_cipher: Use the caesar cipher to encrypt clearText 
    using shiftAmount
    
    Parameters
    ----------
    clearText: the text string to encrypt
    shiftAmount: the integer shift amount
    
    Return: 
    the encrypted string
    """
    clearText = clearText.upper()
    encryptedString = ""

    for currentCharacter in clearText:
        position = alphabet.find(currentCharacter)
        newPosition = (position + shiftAmount) % alphabetLength
        if currentCharacter in alphabet:
            encryptedString = encryptedString + alphabet[newPosition]
        else:
            encryptedString = encryptedString + currentCharacter
    
    return encryptedString
 
run_caesar()
