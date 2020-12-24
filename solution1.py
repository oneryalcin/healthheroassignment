
def my_func(lst: list) -> int:
    """Generator for cumulative sum of even integers

    Args:
        lst: (list) List of integers as input
    Returns:
        (int): Cumulative sum of even integers
    """
    cum_sum = 0
    for elem in lst:
        cum_sum += 0 if elem % 2 else elem
        yield cum_sum


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]

    for cumsum in my_func(my_list):
        print(cumsum)
