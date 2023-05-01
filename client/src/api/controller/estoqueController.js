const { PrismaClient } = require('@prisma/client');
const csv = require('csv-parser');
const fs = require('fs');
const path = require('path');

const prisma = new PrismaClient();

async function importarEstoque(req, res) {
  const results = [];

  fs.createReadStream(path.join(__dirname, '..', '..', 'data', 'estoque_mercadorias.csv'))
    .pipe(csv())
    .on('data', async (data) => {
      results.push(data);
      await prisma.mercadoria.create({
        data: {
          nome: data.NOME,
          quantidade: parseInt(data.QUANTIDADE),
        },
      });
    })
    .on('end', () => {
      console.log('CSV file successfully processed');
      res.send('CSV file successfully processed');
    });
}

async function consultarMercadoria(req, res) {
  try {
    const mercadoria = await prisma.mercadoria.findUnique({
      where: {
        id: parseInt(req.params.id),
      },
    });
    res.json(mercadoria);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao consultar mercadoria');
  }
}

async function consultarMercadorias(req, res) {
  const mercadorias = await prisma.mercadoria.findMany();
  res.json(mercadorias);
}

async function criarMercadoria(req, res) {
  try {
    const mercadoria = await prisma.mercadoria.create({
      data: {
        nome: req.body.nome,
        quantidade: req.body.quantidade,
      },
    });
    res.json(mercadoria);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao criar mercadoria');
  }
}

async function atualizarMercadoria(req, res) {
  try {
    const mercadoria = await prisma.mercadoria.update({
      where: {
        id: parseInt(req.params.id),
      },
      data: {
        nome: req.body.nome,
        quantidade: req.body.quantidade,
      },
    });
    res.json(mercadoria);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao atualizar mercadoria');
  }
}

async function deletarMercadoria(req, res) {
  try {
    const mercadoria = await prisma.mercadoria.delete({
      where: {
        id: parseInt(req.params.id),
      },
    });
    res.json(mercadoria);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao deletar mercadoria');
  }
}


module.exports = {
  importarEstoque,
  consultarMercadoria,
  consultarMercadorias,
  atualizarMercadoria,
  deletarMercadoria
};

