import sys

from walterize.algorithm import walterize_phrase, WalterizeException


def exit_error():
    print(
        "Oppese! You forgot to say what word to walterize...\n"
        "Usage: walterize <word>"
    )
    exit(1)


def walterize_cli():
    if len(sys.argv) == 1:
        exit_error()
    try:
        print(walterize_phrase(sys.argv[1:]))
    except WalterizeException:
        exit_error()
