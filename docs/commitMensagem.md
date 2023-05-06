# Mensagens de Commit Personalizadas com Emojis

Este roteiro descreve como configurar e usar um script Python para gerar mensagens de commit personalizadas com emojis e frases específicas para cada tipo de arquivo alterado.

## 1. Criando o script

Crie um arquivo chamado `commit_msg_generator.py` com o seguinte conteúdo:

```python
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
        ".js": ("javascript file modified", "✨"),
        ".html": ("html file modified", "📄"),
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

    new_commit_msg = commit_msg + "\n\n" + "\n".join([f"{emoji} {phrase}" for phrase, emoji in custom_phrases])

    new_commit_msg = new_commit_msg[:300]

    with open(commit_msg_filepath, "w") as file:
        file.write(new_commit_msg)

if __name__ == "__main__":
    main()
```


## 2. Configurando o hook prepare-commit-msg

Vá para a pasta ```.git/hooks``` no diretório do seu projeto e crie um novo arquivo chamado ```prepare-commit-msg``` (sem extensão de arquivo) nesta pasta. Copie o conteúdo do script que você criou no passo 1 (```commit_msg_generator.py```) para o arquivo ```prepare-commit-msg```.

Torne o arquivo ```prepare-commit-msg``` executável com o seguinte comando:

```bash
chmod +x prepare-commit-msg
```


## 3. Fazendo commit das alterações

Agora, quando você executar o comando ```git commit```, o hook ```prepare-commit-msg``` será executado automaticamente antes do commit, gerando a mensagem de commit com base no script.

Use o seguinte comando para fazer commit e push das alterações:

```bash
git add . && git commit -m "" && git push https://github.com/big-data-estacio/data.git && git push heroku main
```

Desta forma, você não precisa fornecer uma mensagem de commit manualmente usando a opção ```-m```. O script gerará a mensagem de commit automaticamente com base nos arquivos modificados e nos emojis e frases personalizadas.


Copie o conteúdo acima e crie um arquivo README.md no seu projeto com essas informações. Isso fornecerá um guia passo a passo para configurar e usar o script de mensagens de commit personalizadas.


## 4. Solução de problemas

Se você encontrar problemas ao usar o script ou o hook ```prepare-commit-msg```, siga estas etapas para solucionar problemas:

1. Verifique se o arquivo ```prepare-commit-msg``` está localizado no diretório ```.git/hooks``` do seu projeto.
2. Certifique-se de que o arquivo ```prepare-commit-msg``` seja executável, executando o comando chmod +x prepare-commit-msg.
3. Verifique se a linha ```#!/usr/bin/env python3``` está presente no início do arquivo ```prepare-commit-msg```.
4. Verifique se você está usando a versão correta do Python e se todos os módulos necessários estão instalados no seu sistema.
5. Reveja o conteúdo do script e certifique-se de que não há erros no código.


## 5. Personalizando o script

Se você deseja personalizar o script para incluir outros tipos de arquivos, emojis ou frases, siga estas etapas:

1. Abra o arquivo ```commit_msg_generator.py```.
2. No dicionário ```phrases```, adicione novas entradas para cada tipo de arquivo que deseja incluir. As chaves do dicionário devem ser as extensões de arquivo (por exemplo, ```".php"```), e os valores devem ser tuplas contendo a frase personalizada e o emoji (por exemplo, ```("php file modified", "🐘")```).
3. Salve o arquivo e copie seu conteúdo para o arquivo ```prepare-commit-msg``` no diretório ```.git/hooks```.

Agora, o script incluirá automaticamente as novas frases e emojis personalizados nas mensagens de commit sempre que os tipos de arquivo correspondentes forem modificados.

Seguindo este roteiro, você pode configurar e usar um script Python para gerar mensagens de commit personalizadas com emojis e frases específicas para cada tipo de arquivo alterado no seu projeto Git.