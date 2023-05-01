# Variáveis
PORT := 3000

# Instalar as dependências
install:
  yarn install

# Executar a aplicação
start:
    PORT=$(PORT) node index.js
# Criar um novo migration
migrate-new:
  npx prisma migrate dev --name $(name)

# Aplicar as migrações pendentes
migrate-up:
  npx prisma migrate deploy

# Desfazer a última migração aplicada
migrate-down:
  npx prisma migrate reset

# Rodar os testes
test:
  yarn test

# Verificar a cobertura dos testes
test-coverage:
  yarn test:coverage

# Lint nos arquivos
lint:
  yarn lint

# Limpar arquivos temporários
clean:
  rm -rf node_modules
  rm -rf coverage
  rm -rf dist

# Empacotar a aplicação
package:
  yarn build
  mkdir -p dist
  cp -r node_modules dist
  cp -r build dist
  cp package.json dist
  cp yarn.lock dist

# Instalar a aplicação em um ambiente de produção
install-prod:
  cd dist && yarn install --production

# Executar a aplicação em um ambiente de produção
start-prod:
  cd dist && PORT=$(PORT) node index.js
