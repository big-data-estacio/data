CREATE TABLE bebida (
  id                SERIAL PRIMARY KEY,
  nome              TEXT NOT NULL,
  preco             DECIMAL NOT NULL,
  quantidade        INTEGER NOT NULL,
  descricao         TEXT,
  total_vendas      DECIMAL,
  quantidade_vendas INTEGER
);

INSERT INTO bebida (nome, preco, quantidade, descricao, total_vendas, quantidade_vendas) VALUES
  ('Coca-Cola', 4.5, 10, 'Refrigerante', 0.0, 0),
  ('Guaraná', 3.5, 10, 'Refrigerante', 0.0, 0),
  ('Suco de Laranja', 5.0, 10, 'Suco', 0.0, 0),
  ('Suco de Uva', 5.0, 10, 'Suco', 0.0, 0),
  ('Água', 2.0, 10, 'Água', 0.0, 0);
