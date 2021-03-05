def main():
    nums = [int(s) for s in input()]
    print(count_one(nums))


def count_one(nums):
    one_num = 0
    for num in nums:
        if num == 1:
            one_num += 1
    return one_num


if __name__ == '__main__':
    main()
