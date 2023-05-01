const { createObjectCsvWriter } = require('csv-writer');
const { PrismaClient } = require('@prisma/client');
const path = require('path');

const csvFilePath = path.join(__dirname, '..', '..', 'data', 'reservas.csv');
const prisma = new PrismaClient();

async function main() {
  const reservas = [
    { id: '', nome: 'Estevam Souza', data: '2023-04-30', reservasData: 3, Nome: '' },
    { id: '', nome: 'Node.js', data: '2023-04-30', reservasData: 1, Nome: '' },
    { id: '', nome: '', data: '2023-04-30', reservasData: 1, Nome: '' },
    { id: '', nome: 'Estevam Souza Estevam', data: '2023-04-30', reservasData: 1, Nome: '' },
    { id: '', nome: '', data: '2023-05-01 00:00:00', reservasData: 5, Nome: 'Estevam Souza Estevam' },
    { id: '', nome: '', data: '2023-05-01 00:00:00', reservasData: 5, Nome: 'Estevam Souza Estevam' },
    { id: '', nome: '', data: '2023-05-01 00:00:00', reservasData: 5, Nome: 'Estevam Souza Estevam' },
  ];

  const csvWriter = createObjectCsvWriter({
    path: csvFilePath,
    header: [
      { id: 'id', title: 'ID' },
      { id: 'nome', title: 'NOME' },
      { id: 'data', title: 'DATA' },
      { id: 'reservasData', title: 'RESERVASDATA' },
      { id: 'Nome', title: 'Nome' },
    ],
  });

  try {
    await csvWriter.writeRecords(reservas);
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