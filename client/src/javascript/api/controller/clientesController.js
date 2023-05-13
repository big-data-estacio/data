const { PrismaClient } = require('@prisma/client');
const csv = require('csv-parser');
const fs = require('fs');
const path = require('path');

const prisma = new PrismaClient();


async function importarClientes(req, res) {
  const results = [];

  fs.createReadStream(path.join(__dirname, '..', '..', 'data', 'total_clientes.csv'))
    .pipe(csv())
    .on('data', async (data) => {
      results.push(data);
      await prisma.cliente.create({
        data: {
          nome: data.NOME,
          gasto: parseFloat(data.GASTO),
        },
      });
    })
    .on('end', () => {
      console.log('CSV file successfully processed');
      res.send('CSV file successfully processed');
    });
}

async function consultarCliente(req, res) {
  try {
    const cliente = await prisma.cliente.findUnique({
      where: {
        id: parseInt(req.params.id),
      },
    });
    res.json(cliente);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao consultar cliente');
  }
}

async function criarCliente(req, res) {
  try {
    const cliente = await prisma.cliente.create({
      data: {
        nome: req.body.nome,
        gasto: req.body.gasto,
      },
    });
    res.json(cliente);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao criar cliente');
  }
}

async function atualizarCliente(req, res) {
  try {
    const cliente = await prisma.cliente.update({
      where: {
        id: parseInt(req.params.id),
      },
      data: {
        nome: req.body.nome,
        gasto: req.body.gasto,
      },
    });
    res.json(cliente);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao atualizar cliente');
  }
}

async function deletarCliente(req, res) {
  try {
    const cliente = await prisma.cliente.delete({
      where: {
        id: parseInt(req.params.id),
      },
    });
    res.json(cliente);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao deletar cliente');
  }
}


module.exports = {
  importarClientes,
  consultarCliente,
  criarCliente,
  atualizarCliente,
  deletarCliente
};

