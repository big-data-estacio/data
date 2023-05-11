# Running vscode in the browser

## Pre-Requirements

- You need to have docker installed and running

## How to add extensions

- Add Python dependencies to `requirements.txt`
- Add Ubuntu dependencies to `Dockerfile`
- Install more VSCode extensions at `Dockerfile`

## How to add own settings to the environment

- Customize VSCode settings at `.vscode/settings.json`

## How to add different compiler

- Add Ubuntu dependencies to `Dockerfile`

## How to start the environment

1. Put your code in the `code` folder
2. Run the container with `docker-compose up -d`

## References

- The code of the Visual Stuio Code Server is from <https://github.com/cdr/code-server>
- The structure and docker-adaptions is inspired by <https://github.com/ThorbenJensen/code-server-blueprint>
