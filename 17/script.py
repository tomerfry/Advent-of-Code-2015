import itertools

TOTAL_LITERS = 150


def main():
    print('Advent of Code 2015')

    with open('input.txt', 'r') as f:
        content = f.read()

    containers_capacities = [int(capacity) for capacity in content.split('\n')]

    counts = {}

    for perm_len in range(1, len(containers_capacities) + 1):
        count = 0
        for perm in itertools.combinations(containers_capacities, perm_len):
            if sum(perm) == TOTAL_LITERS:
                count += 1
        if count > 0:
            counts[perm_len] = count

    print(counts[sorted(counts.keys())[0]])


if __name__ == '__main__':
    main()