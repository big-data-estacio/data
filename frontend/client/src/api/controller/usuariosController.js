const { PrismaClient } = require('@prisma/client');
const csv = require('csv-parser');
const fs = require('fs');
const path = require('path');

const prisma = new PrismaClient();


async function importarUsuarios(req, res) {
  const results = [];

  fs.createReadStream(path.join(__dirname, '..', '..', 'data', 'cadastro.csv'))
    .pipe(csv())
    .on('data', async (data) => {
      results.push(data);
      await prisma.usuario.create({
        data: {
          nome: data.Nome,
          email: data.E - mail,
          login: data.Login,
          senha: data.Senha
        },
      });
    })
    .on('end', () => {
      console.log('CSV file successfully processed');
      res.send('CSV file successfully processed');
    });
}

async function consultarUsuario(req, res) {
  try {
    const usuario = await prisma.usuario.findUnique({
      where: {
        id: parseInt(req.params.id),
      },
    });
    res.json(usuario);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao consultar usuário');
  }
}

async function consultarUsuarios(req, res) {
  const usuarios = await prisma.usuario.findMany();
  res.json(usuarios);
}

async function criarUsuario(req, res) {
  try {
    const usuario = await prisma.usuario.create({
      data: {
        nome: req.body.nome,
        email: req.body.email,
        login: req.body.login,
        senha: req.body.senha
      },
    });
    res.json(usuario);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao criar usuário');
  }
}

async function atualizarUsuario(req, res) {
  try {
    const usuario = await prisma.usuario.update({
      where: {
        id: parseInt(req.params.id),
      },
      data: {
        nome: req.body.nome,
        email: req.body.email,
        login: req.body.login,
        senha: req.body.senha
      },
    });
    res.json(usuario);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao atualizar usuário');
  }
}

async function deletarUsuario(req, res) {
  try {
    const usuario = await prisma.usuario.delete({
      where: {
        id: parseInt(req.params.id),
      },
    });
    res.json(usuario);
  } catch (e) {
    console.error(e);
    res.status(500).send('Erro ao deletar usuário');
  }
}


module.exports = {
  importarUsuarios,
  consultarUsuario,
  consultarUsuarios,
  criarUsuario,
  atualizarUsuario,
  deletarUsuario
};

