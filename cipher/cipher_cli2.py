import sys, getopt, binascii

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
alphabetLength = alphabet.__len__()


def usage(message=""):
    if (message != ""):
        print(message)
    print("usage: {} -e|d|[h] --encrypt|--decrypt--key=<-{} to {}> --file=<filename> [-h|--help]".format(sys.argv[0], alphabetLength-1, alphabetLength-1))
    sys.exit(1)
      
def parse_commandline(argv):
    myArgs = {"write":False, "decode":False, "encode":False}
#     print('Number of arguments:', len(argv), 'arguments.')
#     print('Argument List:', str(argv))
    try:
        opts, args = getopt.getopt(argv[1:], "edhwf:", ["key=", "file=", "encode", "decode", "write", "help"])
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
            elif option in ("-e", "--encode"):
                if myArgs["decode"]:
                    usage("Can't encode and decode at the same time")
                myArgs["encode"] = True
                print("encoding")
            elif option in ("-d", "--decode"):
                if myArgs["encode"]:
                    usage("Can't encode and decode at the same time")
                myArgs["decode"] = True
                print("decoding")
            elif option == "--key":
                if value == "":
                    usage("Please provide an integer key to designate the shift amount with -k option")
                myArgs["key"] = int(value)
#                 print("using {} for key".format(myArgs["key"]))
            elif option in("-f", "--file"):
                if value == "":
                    usage("Please provide a filename to read")
                myArgs["file"] = value
            elif option in ("-w", "--write"):
                myArgs["write"] = True
            else:
                assert False, "Unhandled option {}".format(option)
    except ValueError as err:
        usage(err)
    return myArgs

def binaryEncode(ascii_string):
    binary = bin(int.from_bytes(ascii_string.encode(), 'big'))
    # print("binary: " + binary)
    return binary

def binaryDecode(binary):
    n = int(binary, 2)
    decoded = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    # print("decoded: " + decoded)
    return decoded

def encryptFile(arguments):
    print("filename = {}".format(arguments["file"]))
    print("key = {}".format(arguments["key"]))
    newfilename = "{}.enc".format(arguments["file"])
    if arguments["write"]:
        print("writing new file {}".format(newfilename))
    with open(arguments["file"]) as f:
        for line in f:
            # print(line.rstrip())
            fields = line.split()
            #print("fields[0] {}, fields[1] {}".format(fields[0], fields[1]))
            if(arguments["decode"] == True):
                encrypted = binaryDecode(fields[1])
            else:
                encrypted = fields[1]
            encrypted = caesar_cipher(encrypted, arguments["key"])
            if(arguments["encode"]):
                encrypted = binaryEncode(encrypted)
            print("{} {}".format(fields[0], encrypted))
            if arguments["write"]:
                newfile = open(newfilename, "a")
                newfile.write("{} {}\n".format(fields[0], encrypted))
                newfile.close()


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
    #clearText = clearText
    encryptedString = ""

    for currentCharacter in clearText:
        position = alphabet.find(currentCharacter)
        newPosition = (position + shiftAmount) % alphabetLength
        if currentCharacter in alphabet:
            encryptedString = encryptedString + alphabet[newPosition]
        else:
            encryptedString = encryptedString + currentCharacter
    return encryptedString


argsMap = parse_commandline(sys.argv)

encryptFile(argsMap)

