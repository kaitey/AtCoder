def calc_score(cards):
    nums = list(map(int, list(cards)))
    score = 0
    for i in range(1, 10):
        score += (i * 10 ** nums.count(i))
    return score


def main():
    k = int(input())
    s = input()[:-1]
    t = input()[:-1]
    st = s + t
    used = [st.count(str(i)) for i in range(1, 10)]
    count = 0
    for i in range(1, 10):
        s_score = calc_score(s + str(i))
        for j in range(1, 10):
            t_score = calc_score(t + str(j))
            if s_score > t_score:
                if i == j:
                    count += ((k - used[i - 1]) * (k - used[i - 1] - 1))
                else:
                    count += ((k - used[i - 1]) * (k - used[j - 1]))
    print(count / ((9 * k - 8) * (9 * k - 9)))


if __name__ == '__main__':
    main()
