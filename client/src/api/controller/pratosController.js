const { PrismaClient } = require('@prisma/client');
const csv = require('csv-parser');
const fs = require('fs');
const path = require('path');

const prisma = new PrismaClient();


async function importarPratos(req, res) {
  const results = [];

  fs.createReadStream(path.join(__dirname, '..', '..', 'data', 'pratos.csv'))
    .pipe(csv())
    .on('data', async (data) => {
      results.push(data);
      await prisma.prato.create({
        data: {
          nome: data.NOME,
          preco: parseFloat(data.PRECO),
          acompanhamento: data.ACOMPANHAMENTO || null,
        },
      });
    })
    .on('end', () => {
      console.log('CSV file successfully processed');
      res.send('CSV file successfully processed');
    });
}

async function consultarPrato(req, res) {
  try {
    const prato = await prisma.prato.findUnique({
      where: {
        id: parseInt(req.params.id),
      },
    });
    res.json(prato);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao consultar prato');
  }
}

async function consultarPratos(req, res) {
  const pratos = await prisma.prato.findMany();
  res.json(pratos);
}

async function criarPrato(req, res) {
  try {
    const prato = await prisma.prato.create({
      data: {
        nome: req.body.nome,
        preco: req.body.preco,
        acompanhamento: req.body.acompanhamento || null,
      },
    });
    res.json(prato);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao criar prato');
  }
}

async function atualizarPrato(req, res) {
  try {
    const prato = await prisma.prato.update({
      where: {
        id: parseInt(req.params.id),
      },
      data: {
        nome: req.body.nome,
        preco: req.body.preco,
        acompanhamento: req.body.acompanhamento || null,
      },
    });
    res.json(prato);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao atualizar prato');
  }
}

async function deletarPrato(req, res) {
  try {
    const prato = await prisma.prato.delete({
      where: {
        id: parseInt(req.params.id),
      },
    });
    res.json(prato);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao deletar prato');
  }
}


module.exports = {
  importarPratos,
  consultarPrato,
  consultarPratos,
  criarPrato,
  atualizarPrato,
  deletarPrato
};

