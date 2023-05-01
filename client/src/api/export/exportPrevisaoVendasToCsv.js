const { createObjectCsvWriter } = require('csv-writer');
const { PrismaClient } = require('@prisma/client');
const path = require('path');

const csvFilePath = path.join(__dirname, '..', '..', 'data', 'previsaoVendas.csv');
const prisma = new PrismaClient();

async function main() {
  const vendas = await prisma.venda.findMany();
  
  if (vendas.length === 0) {
    console.log('Não há vendas cadastradas.');
    return;
  }

  const csvWriter = createObjectCsvWriter({
    path: csvFilePath,
    header: [
      { id: 'data', title: 'Data' },
      { id: 'total_vendas', title: 'Total Vendas' },
    ],
  });

  try {
    const records = vendas.map((venda) => ({
      data: venda.data_venda.toISOString().split('T')[0],
      total_vendas: venda.valor_total.toFixed(2),
    }));
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
