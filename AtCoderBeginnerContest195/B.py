import math


def main():
    a, b, w = list(map(int, input().split()))
    mini = math.ceil(w * 1000 / b)
    maxi = math.floor(w * 1000 / a)
    if mini > maxi:
        print("UNSATISFIABLE")
    else:
        print("{} {}".format(mini, maxi))


if __name__ == '__main__':
    main()
