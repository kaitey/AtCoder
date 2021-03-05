def main():
    s = input()[::-1]
    ts = [["ab"] for _ in range(4)]
    ts[0] = "dream"[::-1]
    ts[1] = "dreamer"[::-1]
    ts[2] = "erase"[::-1]
    ts[3] = "eraser"[::-1]
    if find_from_start(s, ts):
        print("YES")
    else:
        print("NO")


def find_from_start(s, ts):
    while True:
        for t in ts:
            if s.startswith(t):
                s = s[len(t):]
                break
        else:
            return False
        if not s:
            return True


if __name__ == '__main__':
    main()
