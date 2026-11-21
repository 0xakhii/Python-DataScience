def ft_filter(func, iterable):
    """Return an iterator yielding those items
        of iterable for which function(item)
        is true. If function is None,
        return the items that are true."""
    ret = list()
    for it in iterable:
        if func(it):
            ret.append(it)
        else:
            pass
    return (ret)


# def main():
#     """Main function, act as the program starting point"""
#     ages = [15, 18, 52, 64, 10, 19, -1, 20]
#     even_numbers = list(filter(lambda x: x % 2 == 0, ages))
#     print("og fitler:", even_numbers)
#     even_numbers = list(ft_filter(lambda x: x % 2 == 0, ages))
#     print("ft filter:", even_numbers)


# if __name__ == "__main__":
#     main()
