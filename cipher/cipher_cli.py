import sys, getopt

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
alphabetLength = alphabet.__len__()
myArgs = {};

def usage(message=""):
    if (message != ""):
        print(message)
    print("usage: {} --key=<-{} to {}> [-h|--help]".format(sys.argv[0], alphabetLength-1, alphabetLength-1))
    sys.exit(1)
      
def parse_commandline(argv):
#     print('Number of arguments:', len(argv), 'arguments.')
#     print('Argument List:', str(argv))
    try:
        opts, args = getopt.getopt(argv[1:], "h", ["key=","help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        usage(err)
        sys.exit(2)
    if len(argv) == 0:
        usage("Please provide an argument")
    try:
        for option, value in opts:
            if option in ("-h", "--help"):
                usage()
            elif option == "--key":
                if (value == ""):
                    usage("Please provide an integer key to designate the shift amount with -k option")
                myArgs["key"] = int(value)
#                 print("using {} for key".format(myArgs["key"]))
            else:
                assert False, "Unhandled option {}".format(option)
    except ValueError as err:
         usage(err)       

def run_caesar(intKey):
    stringToEncrypt = input("Please enter a message to encrypt: ")   
    encrypted = caesar_cipher(stringToEncrypt, intKey)    
    print(encrypted)

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
 
parse_commandline(sys.argv)
run_caesar(myArgs["key"])
