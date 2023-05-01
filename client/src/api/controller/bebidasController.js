const { PrismaClient } = require('@prisma/client');
const csv = require('csv-parser');
const fs = require('fs');
const path = require('path');

const prisma = new PrismaClient();

async function importarBebidas(req, res) {
  const results = [];

  fs.createReadStream(path.join(__dirname, '..', '..', 'data', 'bebidas.csv'))
    .pipe(csv())
    .on('data', async (data) => {
      results.push(data);
      await prisma.bebida.create({
        data: {
          nome: data.NOME,
          preco: parseFloat(data.PRECO),
          quantidade: parseInt(data.QUANTIDADE),
          descricao: data.DESCRICAO || null,
          total_vendas: parseFloat(data.TOTAL_VENDAS) || null,
          quantidade_vendas: parseInt(data.QUANTIDADE_VENDAS) || null,
        },
      });
    })
    .on('end', () => {
      console.log('CSV file successfully processed');
      res.send('CSV file successfully processed');
    });
}

async function consultarBebida(req, res) {
  try {
    const bebida = await prisma.bebida.findUnique({
      where: {
        id: parseInt(req.params.id),
      },
    });
    res.json(bebida);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao consultar bebida');
  }
}

async function consultarBebidas(req, res) {
  const bebidas = await prisma.bebida.findMany();
  res.json(bebidas);
}

async function criarBebida(req, res) {
  try {
    const bebida = await prisma.bebida.create({
      data: {
        nome: req.body.nome,
        preco: req.body.preco,
        quantidade: req.body.quantidade,
        descricao: req.body.descricao || null,
        total_vendas: req.body.total_vendas || null,
        quantidade_vendas: req.body.quantidade_vendas || null,
      },
    });
    res.json(bebida);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao criar bebida');
  }
}

async function atualizarBebida(req, res) {
  try {
    const bebida = await prisma.bebida.update({
      where: {
        id: parseInt(req.params.id),
      },
      data: {
        nome: req.body.nome,
        preco: req.body.preco,
        quantidade: req.body.quantidade,
        descricao: req.body.descricao || null,
        total_vendas: req.body.total_vendas || null,
        quantidade_vendas: req.body.quantidade_vendas || null,
      },
    });
    res.json(bebida);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao atualizar bebida');
  }
}

async function deletarBebida(req, res) {
  try {
    const bebida = await prisma.bebida.delete({
      where: {
        id: parseInt(req.params.id),
      },
    });
    res.json(bebida);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao deletar bebida');
  }
}

module.exports = {
  importarBebidas,
  consultarBebida,
  consultarBebidas,
  criarBebida,
  atualizarBebida,
  deletarBebida,
};

