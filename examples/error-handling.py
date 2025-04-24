import time

print("error handling")

class OutOfStockError(Exception):
    pass

denominators = [3,2,5,1,0,6,4]
k = 0
while True:
    try:
        k = k + 1
        for denominator in denominators:
            print(k, denominator)
            try:
                print(k, 6/denominator)
                # if denominator > 4:
                #     raise OutOfStockError("Out of stock, perhaps")
                #if denominator == 2:
                #    raise ArithmeticError("Can't divide by two")
            except Exception as e:
                error = str(e)
                print(error)
                if "division" in error:
                    print("well, you tried to divide by zero")
                    continue
                print("don't know what that error is...")
                # raise e
        time.sleep(5)
    except ZeroDivisionError:
        print("Well, you divided by zero. What did you expect?")
        time.sleep(5)
    except KeyboardInterrupt:
        print("Well, you want out, right?")
        exit(0)
    except ArithmeticError as e:
        print(f"Arithmetic Error: {str(e)}!")
        exit(0)
    except OutOfStockError as e:
        print(f"OutOfStockError: {str(e)}!")
        exit(0)
    except Exception as e:
        print(f"Something happened: {str(e)}!")
        exit(0)
    else: 
        print("thank goodness, that worked!")
    finally:
        print("Goodbye!")

print("we are done")