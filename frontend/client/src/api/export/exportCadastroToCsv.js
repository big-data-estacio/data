const { createObjectCsvWriter } = require('csv-writer');
const { PrismaClient } = require('@prisma/client');
const path = require('path');

const csvFilePath = path.join(__dirname, '..', '..', 'data', 'cadastro.csv');
const prisma = new PrismaClient();

async function main() {
  const usuarios = [
    {
      nome: 'Estevam Souza Estevam',
      email: '',
      login: 'user',
      senha: 'user',
    }
  ];

  const csvWriter = createObjectCsvWriter({
    path: csvFilePath,
    header: [
      { id: 'nome', title: 'Nome' },
      { id: 'email', title: 'E-mail' },
      { id: 'login', title: 'Login' },
      { id: 'senha', title: 'Senha' },
    ],
  });

  try {
    await csvWriter.writeRecords(usuarios);
    console.log(`Dados exportados com sucesso para o arquivo ${ csvFilePath }`);
  } catch (err) {
    console.error(`Erro ao exportar dados: ${ err }`);
  } finally {
    await prisma.$disconnect();
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});