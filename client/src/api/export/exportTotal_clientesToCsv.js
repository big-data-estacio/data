const { createObjectCsvWriter } = require('csv-writer');
const { PrismaClient } = require('@prisma/client');
const path = require('path');

const csvFilePath = path.join(__dirname, '..', '..', 'data', 'total_clientes.csv');
const prisma = new PrismaClient();

async function main() {
  const clientes = await prisma.cliente.findMany();

  if (clientes.length === 0) {
    console.log('Não há clientes cadastrados.');
    return;
  }

  const records = clientes.map(cliente => ({
    id: cliente.id.toString(),
    nome: cliente.nome,
    gasto: cliente.compra.reduce((total, compra) => total + compra.valor_total, 0).toFixed(2),
  }));

  const csvWriter = createObjectCsvWriter({
    path: csvFilePath,
    header: [
      { id: 'id', title: 'ID' },
      { id: 'nome', title: 'NOME' },
      { id: 'gasto', title: 'GASTO' },
    ],
  });

  try {
    await csvWriter.writeRecords(records);
    console.log(`Dados exportados com sucesso para o arquivo ${csvFilePath}`);
  } catch (err) {
    console.error(`Erro ao exportar dados: ${err}`);
  } finally {
    await prisma.$disconnect();
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
