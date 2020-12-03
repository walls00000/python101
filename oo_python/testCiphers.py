#####################################
# Test program for ciphers
# Run with py.test ./testCiphers.py
#####################################

import pytest
from Ciphers.CipherUtils import CipherUtils

message = "I love to encrypt things"
cipherUtils = CipherUtils()

def testBinaryEncode():
    ''' Verify binaryEncode encodes ascii 'A' properly '''
    actual = cipherUtils.binaryEncode("A")
    expected = "0b1000001"
    assert actual == expected

def testBinaryDecode():
    ''' Verify binaryDecode can decode ascii 'A' '''
    actual = cipherUtils.binaryDecode("0b1000001")
    expected = "A"
    assert actual == expected

def testBinaryDecodeInvalidInput():
    ''' Verify binaryDecode throws an exception when input is not binary '''
    with pytest.raises(Exception):
        assert cipherUtils.binaryDecode("A")

def testBinaryEncodeDecode():
    ''' Verify encode/decode results in the original input '''
    encoded = cipherUtils.binaryEncode(message)
    decoded = cipherUtils.binaryDecode(encoded)
    assert decoded == message

def testAsciiEncode():
    ''' Verify asciiEncode can encode '''
    expected = "073032108111118101032116111032101110099114121112116032116104105110103115"
    encoded = cipherUtils.asciiEncode(message)
    assert encoded == expected

def testAsciiDecode():
    ''' Verify asciiDecode can decode '''
    encoded = "073032108111118101032116111032101110099114121112116032116104105110103115"
    decoded = cipherUtils.asciiDecode(encoded)
    assert decoded == message

def testAsciiDecodeInvalidNonMultiple3():
    ''' Verify asciiDecode throws on sting length which is not a multiple of 3 '''
    with pytest.raises(Exception):
        assert cipherUtils.asciiDecode("0044")

def testAsciiDecodeInvalidNonInteger():
    ''' Verify asciiDecode throws on non-integer input '''
    with pytest.raises(Exception):
        assert cipherUtils.asciiDecode("00300A")

def testAsciiEncodeDecode():
    '''  Verify asciiEncoded messages can be decoded'''
    encoded = cipherUtils.asciiEncode(message)
    decoded = cipherUtils.asciiDecode(encoded)
    assert decoded == message

def testCaesarAlphabetLength():
    ''' Verify caesar cipher alphabet length is 62 '''
    actual = cipherUtils.getCaesarAlphabetLength()
    expected = 62
    assert actual == expected, "failed: expected {} but got {}".format(expected, actual)

def testCaesarCipher():
    ''' Verify caesar cipher encryption of a message '''
    encrypted = cipherUtils.caesarCipher(message, 7)
    expected = "P svCl Av lujyFwA Aopunz"
    assert encrypted == expected, "failed: expected '{}' but got '{}'".format(expected, encrypted)

    decrypted = cipherUtils.caesarCipher(encrypted, -7)
    assert decrypted == message, "failed: expected '{}' but got '{}'".format(message, decrypted)

def testAllCaesarKeys():
    ''' Verify encryption and decryption of all keys'''
    n = 0 - cipherUtils.getCaesarAlphabetLength()
    for i in range(n, cipherUtils.getCaesarAlphabetLength() + 1):
        decryptKey=0-i
        encrypted = cipherUtils.caesarCipher(message,i)
        decrypted = cipherUtils.caesarCipher(encrypted,decryptKey)
        assert decrypted == message, "failed: Iteration with key {} and decryption key {}"\
            .format(i, decryptKey)

def testOutOfRangeCipherKey():
    ''' Verify that a key outside the range of the alphabet is converted to a predictable key'''
    key = 2348392354
    decryptKey = 0 - key
    encrypted = cipherUtils.caesarCipher(message, key)
    assert encrypted == "K nqxg vq gpetArv vjkpiu"
    decrypted = cipherUtils.caesarCipher(encrypted, decryptKey)
    assert decrypted == message, "failed: encryption/decryption with key {} and decryption key {}" \
        .format(key, decryptKey)

def testTransposeEncrypt():
    ''' Verify transposeEncrypt will encrypt a message '''
    encrypted = cipherUtils.transposeEncrypt(8,message)
    assert encrypted == "Iot   letonhvciern ygtps"

def testTransposeDecrypt():
    ''' Veryfy transposeDecrypt will decrypt a message '''
    decrypted = cipherUtils.transposeDecrypt(8, "Iot   letonhvciern ygtps")
    assert decrypted == message

def testTranspopseEncrypt1():
    "Verify using a column key of 1 will result in the original message"
    encrypted = cipherUtils.transposeEncrypt(1,message)
    assert encrypted == message
def testTransposeEncryptDecrypt():
    ''' Verify transposeEncrypted messagges can be decrypted by transposeDecrypt with various keys '''
    for key in range(2,17):
        encrypted = cipherUtils.transposeEncrypt(key, message)
        decrypted = cipherUtils.transposeDecrypt(key, encrypted)
        assert encrypted != message, "Failed for key: {}".format(key)
        assert decrypted == message

def testTransposeEncryptKeyMax():
    ''' Verify transposeEncrypt with a key value >= results in the original message '''
    key = len(message)
    encrypted = cipherUtils.transposeEncrypt(key, message)
    assert encrypted == message
    key2 = len(message)+1
    encrypted = cipherUtils.transposeEncrypt(key2, message)
    assert encrypted == message

def testTransposeDecryptPlainText():
    ''' Verify transposeDecrypt on plain text will not throw '''
    decrypted = cipherUtils.transposeDecrypt(8, message)
    assert decrypted == "Io  cptn vterthgleony is"

def testReverseCipher():
    ''' Verify the reverse cipher can encrypt and decrypt '''
    encrypted = cipherUtils.reverseCipher(message)
    decrypted = cipherUtils.reverseCipher(encrypted)
    assert encrypted == "sgniht tpyrcne ot evol I"
    assert decrypted == message