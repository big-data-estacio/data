const { createObjectCsvWriter } = require('csv-writer');
const { PrismaClient } = require('@prisma/client');
const path = require('path');

const csvFilePath = path.join(__dirname, '..', '..', 'data', 'pratos.csv');
const prisma = new PrismaClient();

async function main() {
  const pratos = await prisma.prato.findMany();
  
  if (pratos.length === 0) {
    console.log('Não há pratos cadastrados.');
    return;
  }

  const csvWriter = createObjectCsvWriter({
    path: csvFilePath,
    header: [
      { id: 'id', title: 'ID' },
      { id: 'nome', title: 'Nome' },
      { id: 'preco', title: 'Preço' },
      { id: 'acompanhamento', title: 'Acompanhamento' },
    ],
  });

  try {
    await csvWriter.writeRecords(pratos);
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
