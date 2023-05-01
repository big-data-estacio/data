-- CreateTable
CREATE TABLE "Bebida" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "nome" TEXT NOT NULL,
    "preco" REAL NOT NULL,
    "quantidade" INTEGER NOT NULL,
    "descricao" TEXT,
    "total_vendas" REAL,
    "quantidade_vendas" INTEGER
);

-- CreateTable
CREATE TABLE "Cadastro" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "nome" TEXT,
    "email" TEXT NOT NULL,
    "login" TEXT NOT NULL,
    "senha" TEXT NOT NULL
);

-- CreateTable
CREATE TABLE "EstoqueMercadorias" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "nome" TEXT NOT NULL,
    "quantidade" INTEGER NOT NULL
);

-- CreateTable
CREATE TABLE "Funcionarios" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "nome" TEXT NOT NULL,
    "cargo" TEXT NOT NULL,
    "especialidade" TEXT NOT NULL,
    "salario" REAL NOT NULL,
    "diasTrabalhados" INTEGER NOT NULL,
    "salarioDia" REAL NOT NULL
);

-- CreateTable
CREATE TABLE "PrevisaoVendas" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "data" DATETIME NOT NULL,
    "totalVendas" REAL NOT NULL
);

-- CreateTable
CREATE TABLE "Pratos" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "nome" TEXT NOT NULL,
    "preco" REAL NOT NULL,
    "acompanhamento" TEXT
);

-- CreateTable
CREATE TABLE "Reservas" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "nome" TEXT NOT NULL,
    "data" DATETIME NOT NULL,
    "reservasData" INTEGER NOT NULL
);

-- CreateTable
CREATE TABLE "TotalClientes" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "nome" TEXT NOT NULL,
    "gasto" REAL NOT NULL
);

-- CreateTable
CREATE TABLE "VendasCategorias" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "categoria" TEXT NOT NULL,
    "vendas" INTEGER NOT NULL,
    "precoMedio" REAL NOT NULL
);

-- CreateIndex
CREATE UNIQUE INDEX "Cadastro_email_key" ON "Cadastro"("email");

-- CreateIndex
CREATE UNIQUE INDEX "Cadastro_login_key" ON "Cadastro"("login");
