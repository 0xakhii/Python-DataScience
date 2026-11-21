from os import get_terminal_size


def ft_tqdm(lst: range) -> None:
    """ ft_tqdm is an implementation of
        tqdm function with the yeild operator """
    total = len(lst)
    if total == 0:
        return

    try:
        columns = get_terminal_size().columns
    except OSError:
        columns = 80
    for i, item in enumerate(lst, start=1):
        percentage = int(100 * i / total)
        prefix = f"{percentage:3}%|"
        suffix = f"| {i}/{total}"
        bar_size = max(10, columns - len(prefix) - len(suffix) - 1)
        filled = int(bar_size * i / total)
        bar = '█' * filled + ' ' * (bar_size - filled)
        print(f"\r{prefix}{bar}{suffix}", end='', flush=True)
        yield item
