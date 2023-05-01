const { PrismaClient } = require('@prisma/client');
const csv = require('csv-parser');
const fs = require('fs');
const path = require('path');

const prisma = new PrismaClient();


async function importarPrevisaoVendas(req, res) {
  const results = [];

  fs.createReadStream(path.join(__dirname, '..', '..', 'data', 'previsaoVendas.csv'))
    .pipe(csv())
    .on('data', async (data) => {
      results.push(data);
      await prisma.previsaoVenda.create({
        data: {
          data: new Date(data.Data),
          total_vendas: parseFloat(data['Total Vendas'])
        },
      });
    })
    .on('end', () => {
      console.log('CSV file successfully processed');
      res.send('CSV file successfully processed');
    });
}

async function consultarPrevisaoVenda(req, res) {
  try {
    const previsaoVenda = await prisma.previsaoVenda.findUnique({
      where: {
        id: parseInt(req.params.id),
      },
    });
    res.json(previsaoVenda);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao consultar previsão de venda');
  }
}

async function consultarPrevisoesVenda(req, res) {
  const previsoesVenda = await prisma.previsaoVenda.findMany();
  res.json(previsoesVenda);
}

async function criarPrevisaoVenda(req, res) {
  try {
    const previsaoVenda = await prisma.previsaoVenda.create({
      data: {
        data: new Date(req.body.data),
        total_vendas: req.body.total_vendas
      },
    });
    res.json(previsaoVenda);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao criar previsão de venda');
  }
}

async function atualizarPrevisaoVenda(req, res) {
  try {
    const previsaoVenda = await prisma.previsaoVenda.update({
      where: {
        id: parseInt(req.params.id),
      },
      data: {
        data: new Date(req.body.data),
        total_vendas: req.body.total_vendas
      },
    });
    res.json(previsaoVenda);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao atualizar previsão de venda');
  }
}

async function deletarPrevisaoVenda(req, res) {
  try {
    const previsaoVenda = await prisma.previsaoVenda.delete({
      where: {
        id: parseInt(req.params.id),
      },
    });
    res.json(previsaoVenda);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao deletar previsão de venda');
  }
}


module.exports = {
  importarPrevisaoVendas,
  consultarPrevisaoVenda,
  consultarPrevisoesVenda,
  criarPrevisaoVenda,
  atualizarPrevisaoVenda,
  deletarPrevisaoVenda
};

