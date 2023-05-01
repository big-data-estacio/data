const express = require('express');
const router = express.Router();
const bebidasController = require('../controller/bebidasController');

router.post('/bebidas/import', bebidasController.importarBebidas);

router.get('/bebidas/:id', bebidasController.consultarBebida);

router.get('/bebidas', bebidasController.consultarBebidas);

router.post('/bebidas', bebidasController.criarBebida);

router.put('/bebidas/:id', bebidasController.atualizarBebida);

router.delete('/bebidas/:id', bebidasController.deletarBebida);

module.exports = router;
