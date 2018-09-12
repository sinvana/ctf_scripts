import time
d={
    "1":"2",
    "3":"4",
    "5":"6"

    }
print(d.items())
for i,j in d.items():
    print(i,j)
    time.sleep(2)
