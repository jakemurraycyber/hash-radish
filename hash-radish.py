##########################
#
# Hash Radish
# Version: 1.0.0
#
# By: Jake Murray
#
##########################
import hashlib


def hasher(userInput: str, algorithm: str) -> str | None:
    '''
    Generate a hash value using the proveded input
    and algorithm.

    Arguments:
        User Input
        Hashing Algorithm

    This function takes user input and a user selected algorithm.
    It then returns the hash value. No side-effects.

    (Eventually file input will be implemented, along
    with relevant exception handlers.)

    Return:
        Generated hash string.
    '''

    # Check for zero input
    if not userInput:
        print(" [ERROR] No input provided.")
        return None

    # Dictionary of available hash algorithms
    algorithms = {
            'sha1': hashlib.sha1,
            'sha256': hashlib.sha256,
            'sha512': hashlib.sha512,
            'md5': hashlib.md5
    }

    # Check for valid algorithm selection
    if algorithm not in algorithms:
        print(f"[ERROR] {algorithm} is not a valid selection.")

    try:
        # Convert unserInput into bytes
        encodedInput: bytes = userInput.encode('utf-8')

        # Create hasher object
        hasher = algorithms[algorithm]()

        # Hash the encoded input
        hasher.update(encodedInput)

        return hasher.hexdigest()

    except UnicodeEncodeError:
        print("[ERROR] Your input could not be encoded.")
        return None
    except Exception as error:
        print(f"[ERROR] {error}")
        return None


def main():
    # Test call
    hash = hasher('hello', 'sha512')
    print(hash)


if __name__ == '__main__':
    main()
