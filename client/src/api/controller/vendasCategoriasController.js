const { PrismaClient } = require('@prisma/client');
const csv = require('csv-parser');
const fs = require('fs');
const path = require('path');

const prisma = new PrismaClient();


async function importarVendasCategorias(req, res) {
  const results = [];

  fs.createReadStream(path.join(__dirname, '..', '..', 'data', 'vendasCategorias.csv'))
    .pipe(csv())
    .on('data', async (data) => {
      results.push(data);
      await prisma.categoria.create({
        data: {
          id: data.ID,
          categoria: data.CATEGORIA,
          vendas: parseFloat(data.VENDAS),
          preco_medio: parseFloat(data.PRECOMEDIO),
        },
      });
    })
    .on('end', () => {
      console.log('CSV file successfully processed');
      res.send('CSV file successfully processed');
    });
}

async function consultarCategoria(req, res) {
  try {
    const categoria = await prisma.categoria.findUnique({
      where: {
        id: req.params.id,
      },
    });
    res.json(categoria);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao consultar categoria');
  }
}

async function consultarCategorias(req, res) {
  const categorias = await prisma.categoria.findMany();
  res.json(categorias);
}

async function criarCategoria(req, res) {
  try {
    const categoria = await prisma.categoria.create({
      data: {
        id: req.body.id,
        categoria: req.body.categoria,
        vendas: req.body.vendas,
        preco_medio: req.body.preco_medio,
      },
    });
    res.json(categoria);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao criar categoria');
  }
}

async function atualizarCategoria(req, res) {
  try {
    const categoria = await prisma.categoria.update({
      where: {
        id: req.params.id,
      },
      data: {
        id: req.body.id,
        categoria: req.body.categoria,
        vendas: req.body.vendas,
        preco_medio: req.body.preco_medio,
      },
    });
    res.json(categoria);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao atualizar categoria');
  }
}

async function deletarCategoria(req, res) {
  try {
    const categoria = await prisma.categoria.delete({
      where: {
        id: req.params.id,
      },
    });
    res.json(categoria);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao deletar categoria');
  }
}


module.exports = {
  importarVendasCategorias,
  consultarCategoria,
  consultarCategorias,
  criarCategoria,
  atualizarCategoria,
  deletarCategoria
};

