const { PrismaClient } = require('@prisma/client');
const csv = require('csv-parser');
const fs = require('fs');
const path = require('path');

const prisma = new PrismaClient();

async function importarFuncionarios(req, res) {
  const results = [];

  fs.createReadStream(path.join(__dirname, '..', '..', 'data', 'funcionarios.csv'))
    .pipe(csv())
    .on('data', async (data) => {
      results.push(data);
      await prisma.funcionario.create({
        data: {
          nome: data.NOME,
          cargo: data.CARGO,
          especialidade: data.ESPECIALIDADE,
          salario: parseFloat(data.SALÁRIO),
          dias_trabalhados: parseInt(data.DIASTRABALHADOS),
          salario_dia: parseFloat(data.SALÁRIODIA)
        },
      });
    })
    .on('end', () => {
      console.log('CSV file successfully processed');
      res.send('CSV file successfully processed');
    });
}

async function consultarFuncionario(req, res) {
  try {
    const funcionario = await prisma.funcionario.findUnique({
      where: {
        id: parseInt(req.params.id),
      },
    });
    res.json(funcionario);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao consultar funcionário');
  }
}

async function consultarFuncionarios(req, res) {
  const funcionarios = await prisma.funcionario.findMany();
  res.json(funcionarios);
}

async function criarFuncionario(req, res) {
  try {
    const funcionario = await prisma.funcionario.create({
      data: {
        nome: req.body.nome,
        cargo: req.body.cargo,
        especialidade: req.body.especialidade,
        salario: req.body.salario,
        dias_trabalhados: req.body.dias_trabalhados,
        salario_dia: req.body.salario_dia
      },
    });
    res.json(funcionario);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao criar funcionário');
  }
}

async function atualizarFuncionario(req, res) {
  try {
    const funcionario = await prisma.funcionario.update({
      where: {
        id: parseInt(req.params.id),
      },
      data: {
        nome: req.body.nome,
        cargo: req.body.cargo,
        especialidade: req.body.especialidade,
        salario: req.body.salario,
        dias_trabalhados: req.body.dias_trabalhados,
        salario_dia: req.body.salario_dia
      },
    });
    res.json(funcionario);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao atualizar funcionário');
  }
}

async function deletarFuncionario(req, res) {
  try {
    const funcionario = await prisma.funcionario.delete({
      where: {
        id: parseInt(req.params.id),
      },
    });
    res.json(funcionario);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao deletar funcionário');
  }
}


module.exports = {
  importarFuncionarios,
  consultarFuncionario,
  consultarFuncionarios,
  criarFuncionario,
  atualizarFuncionario,
  deletarFuncionario
};

