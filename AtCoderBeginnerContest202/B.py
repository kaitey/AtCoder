def main():
    S = input()
    Sr = list(reversed(S))
    for i, s in enumerate(Sr):
        if s == '6':
            Sr[i] = '9'
        elif s == '9':
            Sr[i] = '6'
    print(''.join(Sr))


if __name__ == '__main__':
    main()
