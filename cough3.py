# has no special name
def main():
    cough(3)

def cough(n):
    print(n*"cough")

""" 
    This basically makes sure main is executed first.
    - since it's at the bottom cough is already defined
    - only at run time does it look at the order of appearance
    - the order it's called in is when
"""

# a convention that keeps it tidy, as you make more complicated
if __name__ == "__main__":
    main()
# cough()