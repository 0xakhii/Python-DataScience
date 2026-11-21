from os import get_terminal_size


def ft_tqdm(lst: range) -> None:
    size = int(get_terminal_size().columns - get_terminal_size().lines)
    for i, item in enumerate(lst, start=1):
        percentage = int(100 * float(i) / float(len(lst)))
        filled = int(size * percentage / 100)
        bar = '█' * filled + ' ' * (size - filled)
        print(f"\r{percentage:3}%|{bar}| {i}/{len(lst)}", end='', flush=True)
        yield item
