import math

class CipherUtils:

    '''
    CipherUtils is a utility containing functions to encrypt,
    decrypt encode and decode messages
    '''

    def __init__(self):
        ''' Constructor for CipherUtils '''
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def binaryEncode(self, ascii_string):
        ''' Dncode an ascii string into binary '''
        binary = bin(int.from_bytes(ascii_string.encode(), 'big'))
        return binary

    def binaryDecode(self, binary):
        ''' Decode a binary encoded message into an ascii string '''
        n = 0
        try:
            n = int(binary, 2)
        except:
            print("Error: input is not binary")
        decoded = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        return decoded

    def asciiEncode(self, message):
        ''' Encode an ascii message into a string of each character's integer value '''
        encoded = ""
        for char in message:
            value = ord(char)
            formatted = "{0:03}".format(value)
            encoded += formatted
        return encoded

    def asciiDecode(self, encoded):
        ''' Decode an ascii encoded message into ascii characters '''
        if len(encoded) % 3 != 0:
            raise Exception("Message not ascii encoded")
        message = ""
        for i in range(0, len(encoded), 3):
            value="{}{}{}".format(encoded[i], encoded[i+1], encoded[i+2])
            try:
                message += chr(int(value))
            except:
                raise Exception ("Value is not an integer: '{}'".format(value))
        return message

    def getCaesarAlphabetLength(self):
        ''' Return the length of the caesar alphabet '''
        return self.alphabet.__len__()

    def caesarCipher(self, clearText, shiftAmount):
        """ caesar_cipher: Use the caesar cipher to encrypt clearText
        using shiftAmount

        Parameters
        ----------
        clearText: the text string to encrypt
        shiftAmount: the integer shift amount

        Return:
        the encrypted string
        """
        encryptedString = ""

        for currentCharacter in clearText:
            position = self.alphabet.find(currentCharacter)
            newPosition = (position + shiftAmount) % self.getCaesarAlphabetLength()
            if currentCharacter in self.alphabet:
                encryptedString = encryptedString + self.alphabet[newPosition]
            else:
                encryptedString = encryptedString + currentCharacter
        return encryptedString

    def transposeEncrypt(self, key, message):
        '''  Use the transpose cipher to encrypt a message using a key for column length '''
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

    def transposeDecrypt(self, key, message):
        '''  Decrypt a transpose encrypted message given the column key '''
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

    def reverseCipher(self,message):
        ''' Reverse the message and return it '''
        i = len(message) - 1
        translated = ""
        while i >= 0:
            translated = translated + message[i]
            i = i - 1
        return translated