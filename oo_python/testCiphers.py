#####################################
# Test program for ciphers
# Run with py.test ./testCiphers.py
#####################################

import pytest
from Ciphers.CipherUtils import CipherUtils

message = "I love to encrypt things"
cipherUtils = CipherUtils()

def testAlphabetLength():
    actual = cipherUtils.getAlphabetLength()
    expected = 62
    assert actual == expected, "failed: expected {} but got {}".format(expected, actual)

def testCaesarCipher():
    encrypted = cipherUtils.caesarCipher(message, 7)
    expected = "P svCl Av lujyFwA Aopunz"
    assert encrypted == expected, "failed: expected '{}' but got '{}'".format(expected, encrypted)

    decrypted = cipherUtils.caesarCipher(encrypted, -7)
    assert decrypted == message, "failed: expected '{}' but got '{}'".format(message, decrypted)

def testAllCaesarKeys():
    for i in range(1,cipherUtils.getAlphabetLength()):
        decryptKey=0-i
        encrypted = cipherUtils.caesarCipher(message,i)
        decrypted = cipherUtils.caesarCipher(encrypted,decryptKey)
        assert decrypted == message, "failed: Iteration with key {} and decryption key {}"\
            .format(i, decryptKey)
