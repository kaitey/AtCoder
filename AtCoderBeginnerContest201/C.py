def main():
    S = input()
    os = []
    xs = []
    qs = []
    for i, s in enumerate(S):
        if s == 'o':
            os.append(str(i))
        elif s == 'x':
            xs.append(str(i))
        elif s == '?':
            qs.append(str(i))
    ans = 0
    for i in range(10000):
        s = ''.join(('00000', str(i)))[-4:]
        flag = False
        for o in os:
            if o not in s:
                flag = True
                break
        if flag:
            continue
        for x in xs:
            if x in s:
                flag = True
                break
        if flag:
            continue
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
