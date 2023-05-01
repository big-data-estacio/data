const { createObjectCsvWriter } = require('csv-writer');
const { PrismaClient } = require('@prisma/client');
const path = require('path');

const csvFilePath = path.join(__dirname, '..', 'data', 'bebidas.csv');
const prisma = new PrismaClient();

async function main() {
  const bebidas = await prisma.bebida.findMany();
  
  if (bebidas.length === 0) {
    console.log('Não há bebidas cadastradas.');
    return;
  }

  const csvWriter = createObjectCsvWriter({
    path: csvFilePath,
    header: [
      { id: 'nome', title: 'Nome' },
      { id: 'preco', title: 'Preço' },
      { id: 'quantidade', title: 'Quantidade' },
      { id: 'descricao', title: 'Descrição' },
      { id: 'total_vendas', title: 'Total de vendas' },
      { id: 'quantidade_vendas', title: 'Quantidade de vendas' },
    ],
  });

  try {
    await csvWriter.writeRecords(bebidas);
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
