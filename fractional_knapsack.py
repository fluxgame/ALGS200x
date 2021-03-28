# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    if capacity == 0 or len(weights) == 0:
        return 0

    assert(len(weights) == len(values))

    max_density = 0.
    best_item_found = -1
    for i in range(0, len(weights)):
        item_density = values[i] / weights[i]
        if item_density > max_density:
            max_density = item_density
            best_item_found = i

    best_item_weight = weights.pop(best_item_found)
    best_item_value = values.pop(best_item_found)

    if best_item_weight < capacity:
        return best_item_value + get_optimal_value(capacity - best_item_weight, weights, values)

    return best_item_value * capacity / best_item_weight


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
