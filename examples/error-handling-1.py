import time

print("error handling")

denominators = [3,2,0,6,4]
k = 0
while True:
    try:
        k = k + 1
        for denominator in denominators:
            print(k, denominator)
            try:
                print(k, 6/denominator)
            except ZeroDivisionError as e:
                print(str(e))
                print("well, you tried to divide by zero")
        time.sleep(5)
    except KeyboardInterrupt:
        print("Well, you want out, right?")
        exit(0)

print("we are done")