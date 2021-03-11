#Duke A.
#Problem 3
#02/10/2021


for n in range(0,50):
    if n%3 == 0 and n%5 == 0:
        print("ZipZap")
    elif n%3 == 0:
        print("Zip")
    elif n%5 == 0:
        print("Zap")
    else:
        print(n)
