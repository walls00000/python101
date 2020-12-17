from Ciphers.CipherUtils import CipherUtils
import os
import argparse

config = {}
cipherUtils = CipherUtils()

def encrypt(cleartext):
    twidth = config["transposeWidth"]
    caesarKey = config["caesarKey"]

    caesar_encrypted = cipherUtils.caesarCipher(cleartext, caesarKey)
    reversed = cipherUtils.reverseCipher(caesar_encrypted)
    transposed = cipherUtils.transposeEncrypt(twidth, reversed)
    ascii_encoded = cipherUtils.asciiEncode(transposed)
    binary_encoded = cipherUtils.binaryEncode(ascii_encoded)
    return binary_encoded;

def decrypt(encrypted):
    twidth = config["transposeWidth"]
    caesarKey = 0-config["caesarKey"]

    binary_decoded = cipherUtils.binaryDecode(encrypted)
    ascii_decoded = cipherUtils.asciiDecode(binary_decoded)
    untransposed = cipherUtils.transposeDecrypt(twidth, ascii_decoded)
    unreversed = cipherUtils.reverseCipher(untransposed)
    decrypted = cipherUtils.caesarCipher(unreversed, caesarKey)
    return decrypted;

def readFile(inputfile):
    contents = ""
    f = open(inputfile, "r")
    return f.read().strip()


def readConfig():
    configfile = "{}/.cipher.conf".format(os.environ['HOME'])
    # print(configfile)
    with open(configfile, "r") as reader:
        for line in reader:
            line = line.strip()
            if (line):
                array = line.split("=")
                # print("config: {} = {}".format(array[0], int(array[1])))
                config[array[0]] = int(array[1])

def main():
    parser = argparse.ArgumentParser("Encrypt or Decrypt a file")
    parser.add_argument('-e', '--encrypt', action='store_true', help="encrypt mode")
    parser.add_argument('-d', '--decrypt', action='store_true', help="decrypt mode")
    parser.add_argument('-f', '--file', metavar='path_to_file', help="Input file for which to encrypt or decrypt")
    args = parser.parse_args()
    # print("encrypt: {}".format(args.encrypt))
    # print("decrypt: {}".format(args.decrypt))
    # print("file: {}".format(args.file))

    readConfig()
    # print("caesarKey: {}".format(config.get("caesarKey")))
    # print("transposeWidth: {}".format(config.get("transposeWidth")))

    file = args.file
    # print("using file {}".format(file))
    contents = readFile(file)
    if (args.encrypt):
        encrypted = encrypt(contents)
        print(encrypted)
    elif (args.decrypt):
        decrypted = decrypt(contents)
        print(decrypted)
    else:
        print("Please provide -e or -d")



if __name__ == '__main__':
    main()