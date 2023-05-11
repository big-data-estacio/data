FROM codercom/code-server:latest


# extensions to code-server
USER coder
RUN code-server --install-extension njpwerner.autodocstring && \
    # code-server --install-extension adpyke.vscode-sql-formatter && \
    # code-server --install-extension axetroy.vscode-changelog-generator && \
    code-server --install-extension bmewburn.vscode-intelephense-client && \
    code-server --install-extension DavidAnson.vscode-markdownlint && \
    code-server --install-extension dbaeumer.vscode-eslint && \
    code-server --install-extension DotJoshJohnson.xml && \
    code-server --install-extension dunstontc.vscode-gitignore-syntax && \
    code-server --install-extension eamodio.gitlens && \
    code-server --install-extension esbenp.prettier-vscode && \
    code-server --install-extension felixfbecker.php-intellisense && \
    code-server --install-extension GrapeCity.gc-excelviewer && \
    code-server --install-extension Ikuyadeu.r && \
    code-server --install-extension ionutvmi.reg && \
    code-server --install-extension mikestead.dotenv && \
    code-server --install-extension ms-azuretools.vscode-docker && \
    code-server --install-extension ms-dotnettools.csharp && \
    code-server --install-extension ms-python.python && \
    # code-server --install-extension ms-vscode-remote.remote-containers && \
    # code-server --install-extension ms-vscode-remote.remote-ssh && \
    # code-server --install-extension ms-vscode-remote.remote-ssh-edit && \
    # code-server --install-extension ms-vscode-remote.remote-wsl && \
    # code-server --install-extension ms-vscode-remote.vscode-remote-extensionpack && \
    # code-server --install-extension ms-vsliveshare.vsliveshare && \
    code-server --install-extension mtxr.sqltools && \
    code-server --install-extension octref.vetur && \
    code-server --install-extension piotrpalarz.vscode-gitignore-generator && \
    code-server --install-extension redhat.java && \
    code-server --install-extension redhat.vscode-xml && \
    code-server --install-extension redhat.vscode-yaml && \
    code-server --install-extension rexshi.phpdoc-comment-vscode-plugin && \
    code-server --install-extension shd101wyy.markdown-preview-enhanced && \
    # code-server --install-extension vivaxy.vscode-conventional-commits && \
    # code-server --install-extension Yannick-Lagger.vscode-fhir-tools && \
    code-server --install-extension yzhang.markdown-all-in-one
    

# ubuntu installations (e.g. Python)
RUN sudo -E apt-get update && sudo -E apt-get install -y \
    python3 \
    python3-pip \
    && sudo rm -rf /var/lib/apt/lists/*


# Set the password for the IDE:
ENV PASSWORD=demo


# python requirements
COPY requirements.txt /home/coder/
RUN python3 -m pip install --no-cache-dir -r ~/requirements.txt
# Python dependencies will be installed to "/home/coder/.local/bin"

CMD ["code-server"]