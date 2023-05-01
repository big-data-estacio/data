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
