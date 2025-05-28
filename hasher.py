'''
This is a reusable hashing class that create a hashing object, encode the user
input, and return the hash value of the input.
Library:
    hashlib from std lib.
Inputs:
    User Input or File Input
    Hashing algorithm selection

Returns:
    Hash value in hexadecimal format
'''
import hashlib


class Hasher:
    def __init__(self, input_data: str, algorithm: str, is_file: bool) -> None:
        self.input_data = input_data
        self.algorithm = algorithm
        self.is_file = is_file  # flag to indicate if input is a file

    def encode_input(self) -> bytes:
        # Encode input to be hashed
        if self.is_file:
            raise ValueError("Cannot encode file path as string input.")
        return self.input_data.encode('utf-8')

    def hash_encoded_input(self, encoded_input: bytes) -> str:
        # Create a hash object of the requested algorithm and takes the
        # input of encodedInput and returns the hash value.
        h = hashlib.new(self.algorithm, usedforsecurity=True)
        h.update(encoded_input)
        return h.hexdigest()

    def hash_file(self, chunk_size: int = 8192) -> str:
        # Hash file content in chunks
        if not self.is_file:
            raise ValueError("Input is not a filepath.")
        h = hashlib.new(self.algorithm, usedforsecurity=True)
        try:
            with open(self.input_data, 'rb') as file:
                while True:
                    chunk = file.read(chunk_size)
                    if not chunk:
                        break
                    h.update(chunk)
            return h.hexdigest()
        except FileNotFoundError:
            raise FileNotFoundError("File not found.")
        except PermissionError:
            raise PermissionError("Permission denied.")
        except Exception as e:
            raise Exception(f"Failed to hash file: {e}")

    def compute_hash(self) -> str:
        # This method is just for convenience, combining
        # encoding and hashing methods
        if self.is_file:
            return self.hash_file()
        else:
            encoded = self.encode_input()
        return self.hash_encoded_input(encoded)


__all__ = ['Hasher']
