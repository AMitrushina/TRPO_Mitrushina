import time
import random
from colorama import init, Fore


init(autoreset=True)


def random_color(msg: str = 'Hello!!!'):
    colors = (
        Fore.BLUE, Fore.GREEN,
        Fore.RED, Fore.YELLOW,
        Fore.CYAN, Fore.MAGENTA
    )
    return random.choice(colors)


def timer():
    for i in range(10, 0, -1):
        print(random_color() + f'Time: {i}' + Fore.RESET)
        time.sleep(1)
    print('Congratulations! You have waited for the timer to end. You are a very patient person.')


if __name__ == "__main__":
    timer()
