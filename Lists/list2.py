

def odds():
    print("That's odd")
    myodds = list(range(1,21,2))
    print("odds: ", myodds)

def threes():
    # List of multiples of 3 from 3-30
    print("threes")
    mythreesLC = [value*3 for value in range(1,11)]
    for i in mythreesLC:
        print(i)



def main():
    print("main")
    odds()
    threes()



if __name__ == '__main__':
    main()