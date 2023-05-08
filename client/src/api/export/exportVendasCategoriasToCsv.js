const { createObjectCsvWriter } = require('csv-writer');
const { PrismaClient } = require('@prisma/client');
const path = require('path');

const csvFilePath = path.join(__dirname, '..', '..', 'data', 'vendasCategorias.csv');
const prisma = new PrismaClient();

async function main() {
  const vendasCategorias = await prisma.$queryRaw(`
    SELECT categoria.nome AS categoria, SUM(venda.quantidade) AS vendas, AVG(venda.preco) AS precoMedio
    FROM main.Venda venda
    INNER JOIN main.Produto produto ON produto.id = venda.produto_id
    INNER JOIN main.Categoria categoria ON categoria.id = produto.categoria_id
    GROUP BY categoria
  `);

  if (vendasCategorias.length === 0) {
    console.log('Não há vendas cadastradas.');
    return;
  }

  const csvWriter = createObjectCsvWriter({
    path: csvFilePath,
    header: [
      { id: 'id', title: 'ID' },
      { id: 'categoria', title: 'CATEGORIA' },
      { id: 'vendas', title: 'VENDAS' },
      { id: 'precoMedio', title: 'PRECOMEDIO' },
    ],
  });

  try {
    await csvWriter.writeRecords(vendasCategorias);
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
