def list1():
    print("I'm in list1")
    mylist = []
    for value in range(1,21):
        mylist.append(value)
    print(mylist)


def million():
    print("I'm in million")
    mymillion = list(range(1,1000001))
    for value in mymillion:
        print(value)

    #print(mymillion)


def main():
    print("I'm in Main")
    list1()
    million()

if __name__ == '__main__':
    main()
