##########################
#
# Hash Radish
# Version: 1.0.0
#
# By: Jake Murray
#
########################## 
import hashlib

def hasher(userInput, algorithm) -> string:
    '''
    Generate a hash value using the proveded input
    and algorithm.

    Return:
        Generated hash string.
    '''

    # Check for zero input
    if not userInput:
        print(" [ERROR] No input proveded.")
        return none

    # Dictionary of available hash algorithms
    algorithms = {
            'sha1':hashlib.sha1,
            'sha256':hashlib.sha256,
            'sha512':hashlib.sha512,
            'md5':hashlib.md5
    }

    # Check for valid algorithm selection
    if algorithm not in algorithms:
        print(f"[ERROR] {algorithm} is not a valid selection.")

if __name__ == '__main__':
    main()
