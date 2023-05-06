#!/usr/bin/env python3
import sys
import random


def main():
    commit_msg_filepath = sys.argv[1]
    with open(commit_msg_filepath, "r") as file:
        commit_msg = file.read()

    # Lista de emojis
    emojis = ["😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "🥲", "😊", "😇"]

    # Escolhe um emoji aleatório da lista
    chosen_emoji = random.choice(emojis)

    # Adiciona o emoji à mensagem de commit
    new_commit_msg = f"{chosen_emoji} {commit_msg}"

    with open(commit_msg_filepath, "w") as file:
        file.write(new_commit_msg)


if __name__ == "__main__":
    main()
