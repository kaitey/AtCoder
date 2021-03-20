def main():
    s = input()
    t = input()
    if t in s:
        print("0")
        return
    t_len = len(t)
    t_bin = int("0b" + t, 0)
    score = t_len
    for i in range(len(s) - t_len + 1):
        diff = bin(int("0b" + s[i:i+t_len], 0) ^ t_bin)[2:].count('1')
        print(diff)
        if diff < score:
            score = diff
            if score == 1:
                break
    print(score)


if __name__ == '__main__':
    main()
