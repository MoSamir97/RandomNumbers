import math
import matplotlib.pyplot as plt


def search(numbers_list, e):
    # Search if the item e is in numbers_list

    for i in range(0, len(numbers_list)):
        if numbers_list[i] == e:
            return True
    return False


def full_digits(n, number_of_digits_of_seed):
    # Check if the number n = seed^2, has full number of digits or not?

    if len(n) < 2 * number_of_digits_of_seed:
        number_of_zeros = 2 * number_of_digits_of_seed - len(n)
        for _ in range(1, number_of_zeros + 1):
            n = '0' + n
    return n


def compute(seed, number_of_digits):
    # For n digits number, number_of_digits_of_seed = n

    number_of_digits_of_seed = number_of_digits  # Working with 2 digits numbers
    mid_index = number_of_digits_of_seed
    start_index = mid_index - math.ceil((number_of_digits_of_seed - 1) / 2)
    end_index = mid_index + math.ceil((number_of_digits_of_seed - 1) / 2)

    numbers_list = []
    while not search(numbers_list, seed):
        # as long as seed isn't in number_list, keep working ...
        numbers_list.append(seed)
        squared = full_digits(str(seed ** 2), number_of_digits_of_seed)
        mid = ((int)(squared[start_index:end_index]))
        print(f'Number: {seed} Squared: {squared} Mid: {mid}')
        seed = mid

    return numbers_list, len(numbers_list)


def compute_max_cycle(number_of_digits_seed, required_digits):
    max_cycle = []
    max_period = 0
    max_seed = 0

    # If number_of_digits_of_seed = n, then check the integer seeds with range: [10 ** (n-1), ..., 10 ** n[

    for i in range(10 ** (number_of_digits_seed - 1), 10 ** (number_of_digits_seed)):
        print(f'For seed {i}:')
        numbers_list, period = compute(i, required_digits)
        print(f'Has period {period}\n')

        if period > max_period:
            max_period = period
            max_cycle = numbers_list
            max_seed = i

    return max_seed, max_period, max_cycle


def draw_plots():
    # Draw Histogram, Scatter

    # number_of_digits_seed = 4, required_digits = 4

    max_cycle, max_period = compute(6239, 4)
    plt.subplot(1, 2, 1)
    plt.scatter([i for i in range(1, max_period + 1)], max_cycle)

    plt.subplot(1, 2, 2)
    plt.hist(max_cycle)
    plt.show()


# Start Program
draw_plots()

# max_seed, max_period, max_cycle = compute_max_cycle(4, 4) # max period = 111, at seed = 6239. Time: < 3 minutes
# max_seed, max_period, max_cycle = compute_max_cycle(2, 2)

# print(
#     f'Max period = {max_period}, at seed = {max_seed}.\n\nMax Cycle:\n{max_cycle}')
