def main():
    b, c = list(map(int, input().split(" ")))
    bb_plus_min, bb_plus_max = b - (c // 2), max(b + ((c - 2) // 2), b + (c // 3))
    bb_minus_min, bb_minus_max = -b - ((c - 1) // 2), -b + ((c - 1) // 2)
    if bb_plus_min <= bb_minus_max:
        print(max(bb_plus_max, bb_minus_max) - min(bb_minus_min, bb_plus_min) + 1)
    else:
        print((bb_plus_max - bb_plus_min + 1) + (bb_minus_max - bb_minus_min + 1))


if __name__ == '__main__':
    main()
