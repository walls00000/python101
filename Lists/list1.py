
def million():
    print("in million")
    mymillion = list(range(1, 1000001))
    print("min: ", min(mymillion))
    print("max: ", max(mymillion))
    print("sum: ", sum(mymillion))

def main():
    print("in main")
    million()

if __name__ == '__main__':
    main()