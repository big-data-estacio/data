const express = require('express');
const router = express.Router();
const bebidasController = require('../controller/bebidasController');
const usuariosController = require('../controller/usuariosController');
const estoqueController = require('../controller/estoqueController');
const funcionariosController = require('../controller/funcionariosController');
const pratosController = require('../controller/pratosController');
const previsaoVendasController = require('../controller/previsaoVendasController');
const consultarReservaController = require('../controller/consultarReservaController');
const clientesController = require('../controller/clientesController');
const vendasCategoriasController = require('../controller/vendasCategoriasController');

// Bebidas
router.post('/bebidas/import', bebidasController.importarBebidas);
router.get('/bebidas/:id', bebidasController.consultarBebida);
router.get('/bebidas', bebidasController.consultarBebidas);
router.post('/bebidas', bebidasController.criarBebida);
router.put('/bebidas/:id', bebidasController.atualizarBebida);
router.delete('/bebidas/:id', bebidasController.deletarBebida);

// Clientes
router.post('/usuarios/import', usuariosController.importarUsuarios);
router.get('/usuarios/:id', usuariosController.consultarUsuario);
router.get('/usuarios', usuariosController.consultarUsuarios);
router.post('/usuarios', usuariosController.criarUsuario);
router.put('/usuarios/:id', usuariosController.atualizarUsuario);
router.delete('/usuarios/:id', usuariosController.deletarUsuario);

// Mercadorias
router.post('/estoque/import', estoqueController.importarEstoque);
router.get('/estoque/:id', estoqueController.consultarMercadoria);
router.get('/estoque', estoqueController.consultarMercadorias);
router.put('/estoque/:id', estoqueController.atualizarMercadoria);
router.delete('/estoque/:id', estoqueController.deletarMercadoria);

// // Funcionarios
router.post('/funcionarios/import', funcionariosController.importarFuncionarios);
router.get('/funcionarios/:id', funcionariosController.consultarFuncionario);
router.get('/funcionarios', funcionariosController.consultarFuncionarios);
router.post('/funcionarios', funcionariosController.criarFuncionario);
router.put('/funcionarios/:id', funcionariosController.atualizarFuncionario);
router.delete('/funcionarios/:id', funcionariosController.deletarFuncionario);

// // Pratos
router.post('/pratos/import', pratosController.importarPratos);
router.get('/pratos/:id', pratosController.consultarPrato);
router.get('/pratos', pratosController.consultarPratos);
router.post('/pratos', pratosController.criarPrato);
router.put('/pratos/:id', pratosController.atualizarPrato);
router.delete('/pratos/:id', pratosController.deletarPrato);

// // Previsao de Vendas
router.post('/previsao-vendas/import', previsaoVendasController.importarPrevisaoVendas);
router.get('/previsao-vendas/:id', previsaoVendasController.consultarPrevisaoVenda);
router.get('/previsao-vendas', previsaoVendasController.consultarPrevisoesVenda);
router.post('/previsao-vendas', previsaoVendasController.criarPrevisaoVenda); 
router.put('/previsao-vendas/:id', previsaoVendasController.atualizarPrevisaoVenda);
router.delete('/previsao-vendas/:id', previsaoVendasController.deletarPrevisaoVenda);

// // Reservas
router.post('/reservas/import', consultarReservaController.importarReservas);
router.get('/reservas/:id', consultarReservaController.consultarReserva);
router.get('/reservas', consultarReservaController.consultarReservas);
router.post('/reservas', consultarReservaController.criarReserva);
router.put('/reservas/:id', consultarReservaController.atualizarReserva);
router.delete('/reservas/:id', consultarReservaController.deletarReserva);

// // Clientes
router.post('/clientes/import', clientesController.importarClientes);
router.get('/clientes/:id', clientesController.consultarCliente);
router.post('/clientes', clientesController.criarCliente);
router.put('/clientes/:id', clientesController.atualizarCliente);
router.delete('/clientes/:id', clientesController.deletarCliente);

// // Vendas Categoria
router.post('/categorias/import', vendasCategoriasController.importarVendasCategorias);
router.get('/categorias/:id', vendasCategoriasController.consultarCategoria);
router.get('/categorias', vendasCategoriasController.consultarCategorias);
router.post('/categorias', vendasCategoriasController.criarCategoria);
router.put('/categorias/:id', vendasCategoriasController.atualizarCategoria);
router.delete('/categorias/:id', vendasCategoriasController.deletarCategoria);

module.exports = router;
