# Caesar's cipher is a simple letter-shift
from sys import argv

def main():
    caesar()

""" chr(65) -> 'A' ord('A') -> 65
chr(90) -> 'Z' """

def shift(num=0):
    ascii = {}
    num = (num%26)

    for i in range(65, 91):
        shifted = ((i + num)%91)
        if shifted < 65:
            shifted += 65
        ascii[chr(i)] = chr(shifted)
    # print(ascii)
    return ascii

def caesar():
    if len(argv) == 2:
        argv[1] = int(argv[1])
        if argv[1] < 1:
            print("Please enter a number greater than or equal to 1.")
        else:
            shift_num = argv[1]
            cipher_hash = shift(shift_num)
            val = ""
            while True:
                plain_text = str(input("plaintext: ")).upper().rstrip()
                if len(plain_text) > 0:
                    break
            for c in plain_text:
                val += cipher_hash[c]
            print(f"ciphertext: {val}")
    else:
        print("No fewer or greater than 1 extra argument allowed")


""" plaintext: HELLO
ciphertext: URYYB """


if __name__ == "__main__":
    main()
