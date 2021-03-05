from copy import deepcopy


def main():
    coins = [int(input()), int(input()), int(input())]
    target = int(input())
    cnd = make_first_candidate(target, coins)
    if not cnd:
        print("0")
        return
    candidates = make_candidates(cnd)

    count = 0
    for candidate in get_unique_list(candidates):
        if compare_two_lists(candidate, coins):
            count += 1

    print(count)


def make_first_candidate(target, coins):
    small_coin = target // 50
    if small_coin <= coins[2]:
        return [0, 0, small_coin]
    for i in range(2):
        small_coin = coins[2] - i
        if small_coin < 0:
            return []
        rest = target - 50 * small_coin
        if rest % 100 == 0:
            break
    mid_coin = rest // 100
    if mid_coin <= coins[1]:
        return [0, mid_coin, small_coin]
    for i in range(5):
        mid_coin = coins[1] - i
        if mid_coin < 0:
            return []
        rest = target - 100 * mid_coin - 50 * small_coin
        if rest % 500 == 0:
            break
    big_coin = rest // 500
    if big_coin <= coins[0]:
        return [big_coin, mid_coin, small_coin]
    return []


def make_candidates(candidate):
    new_candidates = []
    new_cnd = deepcopy(candidate)
    while True:
        new_candidates.append(new_cnd)
        nn = exchange_mid2big(new_cnd)
        new_candidates.extend(nn)
        new_cnd = exchange_small2mid(new_cnd)
        if new_cnd[2] < 0:
            break
    return new_candidates


def exchange_small2mid(candidate):
    new_cnd = deepcopy(candidate)
    new_cnd[2] -= 2
    new_cnd[1] += 1
    return new_cnd


def exchange_mid2big(candidate):
    new_candidates = []
    new_cnd = deepcopy(candidate)
    while True:
        new_cnd[1] -= 5
        new_cnd[0] += 1
        if new_cnd[1] < 0:
            break
        new_candidates.append(deepcopy(new_cnd))
    return new_candidates


def compare_two_lists(targets, criteria):
    for t, c in zip(targets, criteria):
        if t > c:
            return False
    return True


def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]


if __name__ == '__main__':
    main()
