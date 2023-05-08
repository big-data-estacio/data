const { createObjectCsvWriter } = require('csv-writer');
const { PrismaClient } = require('@prisma/client');
const path = require('path');

const csvFilePath = path.join(__dirname, '..', '..', 'data', 'estoque_mercadorias.csv');
const prisma = new PrismaClient();

async function main() {
  const mercadorias = await prisma.mercadoria.findMany();
  
  if (mercadorias.length === 0) {
    console.log('Não há mercadorias cadastradas.');
    return;
  }

  const csvWriter = createObjectCsvWriter({
    path: csvFilePath,
    header: [
      { id: 'id', title: 'ID' },
      { id: 'nome', title: 'NOME' },
      { id: 'quantidade', title: 'QUANTIDADE' },
    ],
  });

  try {
    await csvWriter.writeRecords(mercadorias);
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
