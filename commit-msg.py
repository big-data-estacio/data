#!/usr/bin/env python3
import sys
import random
import subprocess

def get_changed_files():
    output = subprocess.check_output(["git", "diff", "--cached", "--name-only"])
    changed_files = output.decode("utf-8").splitlines()
    return changed_files

def get_custom_phrase(file_extension):
    phrases = {
        ".py": "Python file modified",
        ".js": "JavaScript file modified",
        ".html": "HTML file modified",
        ".css": "CSS file modified",
    }

    return phrases.get(file_extension, "File modified")

def main():
    commit_msg_filepath = sys.argv[1]
    with open(commit_msg_filepath, "r") as file:
        commit_msg = file.read()

    changed_files = get_changed_files()
    file_extensions = {file.split('.')[-1] for file in changed_files if '.' in file}
    
    custom_phrases = [get_custom_phrase(f".{ext}") for ext in file_extensions]

    # Escolha um membro da equipe
    team_member = "@fulano"

    # Gere a mensagem de commit personalizada
    new_commit_msg = f"🔒📝 {team_member} atualizando o projeto. 👥📝 #feature #config #analise-dados"

    with open(commit_msg_filepath, "w") as file:
        file.write(new_commit_msg)

if __name__ == "__main__":
    main()
