'''
This is a reusable hashing class that create a hashing object, encode the user
input, and return the hash value of the input.
Library:
    hashlib from std lib.
Inputs:
    User Input
    Hashing algorithm selection

Returns:
    Hash value in hexidecimal format
'''

import hashlib

class Hasher:
    def __init__(self, input: str, algorithm: str) -> None:
        self.input = input
        self.algorithm = algorithm


    def encodeInput(self) -> bytes:
        # Encode input to be hashed
        return self.input.encode('utf-8')
    

    def hashEncodedInput(self, endodedInput: bytes) -> str:
        # Create a hash object of the requested algorithm and takes the
        # input of encodedInput and returns the hash value.
        h = hashlib.new(self.algorithm, usedforsecurity=True)
        h.update(endodedInput)
        return h.hexdigest()
    

# TESTING
name = 'jake'
algorithm = 'sha3_256'
newHasher = Hasher(name, algorithm)
encoded = newHasher.encodeInput()
newHash = newHasher.hashEncodedInput(encoded)
print(newHash)
