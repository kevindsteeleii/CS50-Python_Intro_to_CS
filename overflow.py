# sleep is like setInterval in js
from time import sleep
i = 1
# do not trigger! infinite loop
while True:
    print(i)
    i *= 2