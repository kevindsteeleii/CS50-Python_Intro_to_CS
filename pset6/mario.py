# comfortable

def main():
    get_input()

def get_input():
    height = 0
    while True:
        height = int(input("Give a height in units from 1 to 8."))
        if  height > 0 and height < 9:
            break
    for i in range(height+1):
        print(f"{(height - i)*' '}{i*'#'}  {i*'#'}{(height - i)*' '}")

if __name__ == "__main__":
    main()
