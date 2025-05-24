##########################
#
# Hash Radish
# Version: 1.0.0
#
# By: Jake Murray
#
##########################
import hasher
import menus

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

    # List of available hash algorithms
    # User can either type out algorithm, or enter the relevant number selection.
    ALGORITHMS = [
            'sha224',
            'sha256',
            'sha384',
            'sha512',
            'sha3-224',
            'sha3-256',
            'sha3-384',
            'sha3-512'
    ]

    # Check for zero input
    if not userInput:
        print(" [ERROR] No input provided.")
        return None

    # Check for valid algorithm selection
    if algorithm not in ALGORITHMS:
        print(f"[ERROR] {algorithm} is not a valid selection.")

    try:
        # Convert unserInput into bytes
        encodedInput: bytes = userInput.encode('utf-8')

        # Create hasher object
        hasher: object = ALGORITHMS[algorithm]()

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
    return None

if __name__ == '__main__':
    main()
