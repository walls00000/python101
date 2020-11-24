# Transposition Cipher Encryption
# https://www.nostarch.com/crackingcodes/
import math
#import pyperclip

def main():
    # myMessage = "Common sense is not so common."
    file = input("Enter a filename: ")
    handle = open(file, "r")
    myMessage = handle.read()
    print("ClearText: \n{}".format(myMessage))
    print("Length: {}".format(len(myMessage)))
    print("======================================")
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string ciphertext to the screen
    print(ciphertext)
    print("Length: {}".format(len(ciphertext)))
    print("======================================")

    cleartext = decryptMessage(myKey, ciphertext)
    print(cleartext)
    print("Length: {}".format(len(cleartext)))
    print("======================================")

def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key
    #Loop through each column in ciphertext
    for column in range(key):
        currentIndex = column

        #Keep looping until currentIndex goes past the message length.
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the ciphertext list:
            ciphertext[column] += message[currentIndex]

            #Move currentIndex over.
            currentIndex += key

    # Convert the ciphertext list into a single string value and return it
    return ''.join(ciphertext)

def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First we need to calculate a few values.

    # The number of "cplumns" in our transposition grid.
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = key

    # The number of "shaded boxes" in the last "column" of the grid.
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid
    plaintext = [''] * numOfColumns

    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go.
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # Point to the next column.

        # If there are no more columns OR we're at a shaded box, go back
        # to the first column and the next row.
        if(column == numOfColumns) or (column == numOfColumns-1 and
        row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1
    return ''.join(plaintext)


# If transpostion.py is run (instead of imported as a module) call
# the main() function:
if __name__ == '__main__':
    main()