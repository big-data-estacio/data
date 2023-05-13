# API References

Este documento descreve as referências da API RESTful do projeto "Restaurante Pedacinho do Céu".


## Endpoints

A API possui os seguintes endpoints:

### Clientes

- `GET /clientes`: Lista todos os clientes.
- `GET /clientes/<int:cliente_id>`: Retorna os detalhes de um cliente específico.
- `POST /clientes`: Cria um novo cliente.
- `PUT /clientes/<int:cliente_id>`: Atualiza os detalhes de um cliente específico.
- `DELETE /clientes/<int:cliente_id>`: Exclui um cliente específico.

### Estoque

- `GET /estoque`: Lista todos os itens em estoque.
- `GET /estoque/<int:estoque_id>`: Retorna os detalhes de um item de estoque específico.
- `POST /estoque`: Cria um novo item de estoque.
- `PUT /estoque/<int:estoque_id>`: Atualiza os detalhes de um item de estoque específico.
- `DELETE /estoque/<int:estoque_id>`: Exclui um item de estoque específico.

### Produtos

- `GET /produtos`: Lista todos os produtos.
- `GET /produtos/<int:produto_id>`: Retorna os detalhes de um produto específico.
- `POST /produtos`: Cria um novo produto.
- `PUT /produtos/<int:produto_id>`: Atualiza os detalhes de um produto específico.
- `DELETE /produtos/<int:produto_id>`: Exclui um produto específico.

### Pedidos

- `GET /pedidos`: Lista todos os pedidos.
- `GET /pedidos/<int:pedido_id>`: Retorna os detalhes de um pedido específico.
- `POST /pedidos`: Cria um novo pedido.
- `PUT /pedidos/<int:pedido_id>`: Atualiza os detalhes de um pedido específico.
- `DELETE /pedidos/<int:pedido_id>`: Exclui um pedido específico.

### Fornecedores

- `GET /fornecedores`: Lista todos os fornecedores.
- `GET /fornecedores/<int:fornecedor_id>`: Retorna os detalhes de um fornecedor específico.
- `POST /fornecedores`: Cria um novo fornecedor.
- `PUT /fornecedores/<int:fornecedor_id>`: Atualiza os detalhes de um fornecedor específico.
- `DELETE /fornecedores/<int:fornecedor_id>`: Exclui um fornecedor específico.

### Transações

- `GET /transacoes`: Lista todas as transações.
- `GET /transacoes/<int:transacao_id>`: Retorna os detalhes de uma transação específica.
- `POST /transacoes`: Cria uma nova transação.
- `PUT /transacoes/<int:transacao_id>`: Atualiza os detalhes de uma transação específica.
- `DELETE /transacoes/<int:transacao_id>`: Exclui uma transação específica.


## Autenticação e Autorização

A API utiliza um sistema de autenticação e autorização baseado em tokens JWT. Para acessar os endpoints protegidos, os clientes devem fornecer um token JWT válido no cabeçalho `Authorization` das requisições.

Os tokens JWT podem ser obtidos através do endpoint `POST /auth/login`, fornecendo um nome de usuário e senha válidos. Os tokens têm uma duração limitada e devem ser renovados periodicamente.


## Erros e Mensagens

A API retorna códigos de status HTTP apropriados para indicar o sucesso ou a falha das requisições. Além disso, mensagens de erro específicas podem ser retornadas no corpo da resposta em formato JSON.

### Exemplo de resposta de erro:

```json
{
  "error": "Invalid credentials",
  "message": "The provided username or password is incorrect."
}
```


## Paginação e Filtragem

A API suporta paginação e filtragem para endpoints que retornam listas de recursos. Os parâmetros de consulta page, per_page e filter podem ser usados para controlar a paginação e a filtragem.

Exemplo de uso de paginação e filtragem:

* **`GET /clientes?page=2&per_page=10&filter=nome:João`**

Neste exemplo, a API retornará a segunda página de clientes, com 10 clientes por página, e filtrará os clientes cujo nome contenha "João".


## Versionamento

A API utiliza versionamento semântico. A versão atual da API é `v1.0.0`. A versão da API pode ser fornecida como um prefixo no caminho dos endpoints, por exemplo, `GET /v1.0.0/clientes`. Se a versão não for fornecida, a API usará a versão mais recente por padrão.


## Futuras Atualizações e Implementações

* Implementação de cache para melhorar o desempenho da API.
* Adição de suporte para múltiplos idiomas nas mensagens de erro e na documentação.
* Expansão da funcionalidade de filtragem para permitir filtragem avançada com operadores lógicos.
* Implementação de mecanismos de segurança adicionais, como limitação de taxa de requisições e prevenção de ataques de força bruta.


## Deploy do Projeto no Heroku

O projeto pode ser facilmente implantado no Heroku seguindo os passos abaixo:

1. Crie uma conta no Heroku, caso ainda não tenha uma.
2. Instale o Heroku CLI no seu computador.
3. Faça login no Heroku CLI executando heroku login.
4. Clone o repositório do projeto do GitHub para o seu computador.
5. Navegue até a pasta do projeto e execute heroku create para criar um novo aplicativo no Heroku.
6. Execute git push heroku main para implantar o projeto no Heroku.
7. Execute heroku open para abrir o aplicativo no seu navegador.


## Utilização do Travis

O projeto utiliza o Travis CI para integração contínua e implantação automática. O arquivo de configuração do Travis CI, .travis.yml, está localizado na raiz do projeto. Ele define as etapas de construção, teste e implantação do projeto. Para utilizar o Travis CI com este projeto, siga os passos abaixo:

1. Crie uma conta no Travis CI caso ainda não tenha uma.
2. Vincule sua conta do Travis CI à sua conta do GitHub.
3. Ative o repositório do projeto nas configurações do Travis CI.
4. Faça um push das alterações para o repositório do GitHub. O Travis CI iniciará automaticamente a construção e os testes do projeto.


## Nível do Projeto

Este projeto é um sistema profissional e bem estruturado, seguindo boas práticas de programação e padrões de projeto. Ele utiliza uma arquitetura baseada em API RESTful e suporta integração com Big Data e Power BI. A aplicação foi desenvolvida com foco em escalabilidade, modularidade e manutenibilidade.


## Princípios SOLID

Este projeto segue os princípios SOLID, que são um conjunto de diretrizes de design de software para desenvolver sistemas flexíveis, robustos e escaláveis:

* **S**ingle Responsibility Principle (Princípio da Responsabilidade Única): Cada classe tem uma única responsabilidade.
* **O**pen/Closed Principle (Princípio Aberto/Fechado): As classes e módulos devem ser abertos para extensão, mas fechados para modificação.
* **L**iskov Substitution Principle (Princípio da Substituição de Liskov): As classes derivadas devem ser substituíveis por suas classes base.
* **I**nterface Segregation Principle (Princípio da Segregação de Interface): As interfaces devem ser pequenas e específicas, em vez de grandes e genéricas.
* **D**ependency Inversion Principle (Princípio da Inversão de Dependência): As dependências devem ser abstraídas e invertidas, ou seja, os módulos de alto nível não devem depender diretamente de módulos de baixo nível.

Ao aderir a esses princípios, o projeto mantém um alto grau de qualidade, facilitando futuras atualizações e expansões.


## Suporte ao Insomnia

Para facilitar o teste e a documentação da API, este projeto inclui um arquivo de exportação do Insomnia com todos os endpoints e exemplos de requisições. Para utilizar o arquivo de exportação do Insomnia, siga os passos abaixo:

1. Instale o Insomnia no seu computador, caso ainda não tenha feito.
2. Abra o Insomnia e clique em "Import/Export" no menu superior direito.
3. Clique em "Import Data" e selecione "From File".
4. Navegue até a pasta do projeto e selecione o arquivo de exportação do Insomnia.
5. Clique em "Import" e o Insomnia importará todos os endpoints e exemplos de requisições.

Agora você pode utilizar o Insomnia para testar facilmente todos os endpoints da API e visualizar as respostas em tempo real.