def main():
    cash()

def get_change():
    change = 0
    while True:
        change = round(float(input('How much change?: ')), 2)
        if change < 0:
            break
    return change
# _NOTE: had to round every transaction/operation what a pain in the @$$
def cash():
    coins = [.25, .10, .05, .01]
    amt_coins = 0
    change = round(get_change(), 2)
    while True:
        for i in range(len(coins)):
            c = coins[i]
            while change  <= (c*-1):
                change = round((change + c), 2)
                amt_coins += 1
        break
    print(amt_coins)

if __name__ == "__main__":
    main()