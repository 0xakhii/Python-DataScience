from ft_package import ft_tqdm
from ft_package import morse_encode
from time import sleep


def main():
    for elem in ft_tqdm(range(222)):
        sleep(0.005)
    print()
    morse_encode("Don3")


if __name__ == "__main__":
    main()
