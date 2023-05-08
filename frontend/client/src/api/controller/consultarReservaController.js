const { PrismaClient } = require('@prisma/client');
const csv = require('csv-parser');
const fs = require('fs');
const path = require('path');

const prisma = new PrismaClient();


async function importarReservas(req, res) {
  const results = [];

  fs.createReadStream(path.join(__dirname, '..', '..', 'data', 'reservas.csv'))
    .pipe(csv())
    .on('data', async (data) => {
      results.push(data);
      await prisma.reserva.create({
        data: {
          nome: data.Nome || null,
          data: new Date(data.DATA),
          quantidade_pessoas: parseInt(data.RESERVASDATA),
          cliente: data.NOME || null,
        },
      });
    })
    .on('end', () => {
      console.log('CSV file successfully processed');
      res.send('CSV file successfully processed');
    });
}

async function consultarReserva(req, res) {
  try {
    const reserva = await prisma.reserva.findUnique({
      where: {
        id: parseInt(req.params.id),
      },
    });
    res.json(reserva);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao consultar reserva');
  }
}

async function consultarReservas(req, res) {
  const reservas = await prisma.reserva.findMany();
  res.json(reservas);
}

async function criarReserva(req, res) {
  try {
    const reserva = await prisma.reserva.create({
      data: {
        nome: req.body.nome || null,
        data: new Date(req.body.data),
        quantidade_pessoas: parseInt(req.body.quantidade_pessoas),
        cliente: req.body.cliente || null,
      },
    });
    res.json(reserva);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao criar reserva');
  }
}

async function atualizarReserva(req, res) {
  try {
    const reserva = await prisma.reserva.update({
      where: {
        id: parseInt(req.params.id),
      },
      data: {
        nome: req.body.nome || null,
        data: new Date(req.body.data),
        quantidade_pessoas: parseInt(req.body.quantidade_pessoas),
        cliente: req.body.cliente || null,
      },
    });
    res.json(reserva);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao atualizar reserva');
  }
}

async function deletarReserva(req, res) {
  try {
    const reserva = await prisma.reserva.delete({
      where: {
        id: parseInt(req.params.id),
      },
    });
    res.json(reserva);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao deletar reserva');
  }
}


module.exports = {
  importarReservas,
  consultarReserva,
  consultarReservas,
  criarReserva,
  atualizarReserva,
  deletarReserva
};

