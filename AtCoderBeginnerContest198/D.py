from itertools import permutations


def calc(nums, letters, lens):
    number = ["0"] * lens[2]
    for n, let in zip(nums, letters.values()):
        for i in let:
            number[int(i)] = str(n)
    if int(number[0]) * int(number[lens[0]]) * int(number[lens[1]]) == 0:
        return False
    if int(''.join(number[0:lens[0]])) + int(''.join(number[lens[0]:lens[1]])) != int(''.join(number[lens[1]:lens[2]])):
        return False
    print(int(''.join(number[0:lens[0]])))
    print(int(''.join(number[lens[0]:lens[1]])))
    print(int(''.join(number[lens[1]:lens[2]])))
    return True


def main():
    s1 = input()
    s2 = input()
    s3 = input()
    let = set(s1 + s2 + s3)
    if len(let) > 10:
        print("UNSOLVABLE")
        exit()
    lens = [len(s1), len(s1 + s2), len(s1 + s2 + s3)]
    letters = {}
    for l in let:
        letters[l] = []
    S = s1 + s2 + s3
    for i, s in enumerate(S):
        letters[s].append(i)
    for nums in permutations(range(10), len(let)):
        if calc(nums, letters, lens):
            exit()
    print("UNSOLVABLE")
    exit()


if __name__ == '__main__':
    main()
