def to_list():
    res = []

    with open('./1.txt', 'r') as f:
        for line in f:
            new_str = line.rstrip("\n")
            print(new_str)
            res.append(new_str)

    print(res)
    print(len(res))


if __name__ == '__main__':
    to_list()
