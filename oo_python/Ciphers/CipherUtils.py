class CipherUtils:

    '''
    CipherUtils is a utility containing functions to encrypt,
    decrypt encode and decode messages
    '''

    def __init__(self):
        ''' Constructor for CipherUtils '''
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def getAlphabetLength(self):
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
            newPosition = (position + shiftAmount) % self.getAlphabetLength()
            if currentCharacter in self.alphabet:
                encryptedString = encryptedString + self.alphabet[newPosition]
            else:
                encryptedString = encryptedString + currentCharacter
        return encryptedString