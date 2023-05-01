const { createObjectCsvWriter } = require('csv-writer');
const { PrismaClient } = require('@prisma/client');
const path = require('path');

const csvFilePath = path.join(__dirname, '..', '..', 'data', 'funcionarios.csv');
const prisma = new PrismaClient();

async function main() {
  const funcionarios = await prisma.funcionario.findMany();

  if (funcionarios.length === 0) {
    console.log('Não há funcionários cadastrados.');
    return;
  }

  const csvWriter = createObjectCsvWriter({
    path: csvFilePath,
    header: [
      { id: 'id', title: 'ID' },
      { id: 'nome', title: 'NOME' },
      { id: 'cargo', title: 'CARGO' },
      { id: 'especialidade', title: 'ESPECIALIDADE' },
      { id: 'salario', title: 'SALÁRIO' },
      { id: 'dias_trabalhados', title: 'DIAS TRABALHADOS' },
      { id: 'salario_dia', title: 'SALÁRIO/DIA' },
    ],
  });

  try {
    await csvWriter.writeRecords(funcionarios);
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
