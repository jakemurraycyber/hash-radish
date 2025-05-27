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
    def __init__(self, input: str, algorithm: str, isFile: bool) -> None:
        self.input = input
        self.algorithm = algorithm
        self.isFile = isFile # flag to indicate if input is a file

    def encodeInput(self) -> bytes:
        # Encode input to be hashed
        return self.input.encode('utf-8')
    

    def hashEncodedInput(self, encodedInput: bytes) -> str:
        # Create a hash object of the requested algorithm and takes the
        # input of encodedInput and returns the hash value.
        h = hashlib.new(self.algorithm, usedforsecurity=True)
        h.update(encodedInput)
        return h.hexdigest()
    
    def hashFile(self, chunkSize: int = 4096) -> str:
        # Hash file in chunks
        if not self.isFile:
            raise ValueError("Input is not a filepath.")
        h = hashlib.new(self.algorithm, usedforsecurity=True)
        with open(self.input, 'rb') as file:
            while True:
                chunk = file.read(chunkSize)
                if not chunk:
                    break
                h.update(chunk)
        return h.hexdigest()

    def hash(self) -> str:
        # This method is just for convenience, combining 
        # encoding and hashing methods
        encoded = self.encodeInput()
        return self.hashEncodedInput(encoded)

__all__ = ['Hasher']  
