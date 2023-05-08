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
        ".py": ("python file modified", "🐍"),
        ".pyc": ("python file modified", "🐍"),
        ".pyo": ("python file modified", "🐍"),
        ".pyd": ("python file modified", "🐍"),
        ".pyw": ("python file modified", "🐍"),
        ".pyz": ("python file modified", "🐍"),
        ".pywz": ("python file modified", "🐍"),
        ".pyx": ("python file modified", "🐍"),
        ".js": ("javascript file modified", "✨"),
        ".jsx": ("javascript react file modified", "✨"),
        ".ts": ("typescript file modified", "📄"),
        ".tsx": ("typescript react file modified", "📄"),
        ".html": ("html file modified", "📄"),
        ".ts": ("typescript file modified", "📄"),
        ".tsx": ("typescript react file modified", "📄"),
        ".jsx": ("javascript react file modified", "📄"),
        ".json": ("json file modified", "📄"),
        ".md": ("markdown file modified", "📄"),
        ".sh": ("shell script modified", "📄"),
        ".yml": ("yaml file modified", "📄"),
        ".yaml": ("yaml file modified", "📄"),
        ".gitignore": ("gitignore file modified", "📄"),
        ".gitattributes": ("gitattributes file modified", "📄"),
        ".gitmodules": ("gitmodules file modified", "📄"),
        ".gitconfig": ("gitconfig file modified", "📄"),
        ".gitkeep": ("gitkeep file modified", "📄"),
        ".gitmessage": ("gitmessage file modified", "📄"),
        ".git": ("git file modified", "📄"),
        ".gitlab-ci.yml": ("gitlab ci file modified", "📄"),
        ".gitlab-ci.yaml": ("gitlab ci file modified", "📄"),
        ".gitlab-ci": ("gitlab ci file modified", "📄"),
        ".gitlab": ("gitlab file modified", "📄"),
        ".gitlab-ci.yml": ("gitlab ci file modified", "📄"),
        ".gitlab-ci.yaml": ("gitlab ci file modified", "📄"),
        ".gitlab-ci": ("gitlab ci file modified", "📄"),
        ".css": ("css file modified", "🎨"),
    }

    return phrases.get(file_extension, ("file modified", "🔧"))

def main():
    commit_msg_filepath = sys.argv[1]
    with open(commit_msg_filepath, "r") as file:
        commit_msg = file.read()

    changed_files = get_changed_files()
    file_extensions = {file.split('.')[-1] for file in changed_files if '.' in file}
    
    custom_phrases = [get_custom_phrase(f".{ext}") for ext in file_extensions]

    # Gere a mensagem de commit personalizada
    new_commit_msg = commit_msg + "\n\n" + "\n".join([f"{emoji} {phrase}" for phrase, emoji in custom_phrases])

    # Limita a mensagem de commit a 300 caracteres
    new_commit_msg = new_commit_msg[:300]

    with open(commit_msg_filepath, "w") as file:
        file.write(new_commit_msg)

if __name__ == "__main__":
    main()
