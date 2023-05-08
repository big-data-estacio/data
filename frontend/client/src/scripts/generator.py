import os

# Crie a pasta client/src/pages se ela não existir
os.makedirs("client/src/pages", exist_ok=True)

opcoes_emojis = [
    ("Home", "🏠"),
    ("Dados Brutos", "📊"),
    ("Consultar Dados", "🔍"),
    ("Inserir Dados", "➕"),
    ("Atualizar Dados", "♻️"),
    ("Deletar Dados", "🗑️"),
    ("Mapa", "🗺️"),
    ("Análise de rentabilidade", "💰"),
    ("Reservas", "📆"),
    ("Previsão de demanda", "📈"),
    ("Análise de lucro líquido", "💵"),
    ("Análise de Tendências de Vendas", "📉"),
    ("Sobre", "ℹ️"),
    ("Gráficos", "📊"),
    ("Contato", "📞"),
    ("Developers", "💻"),
    ("funcionarios", "👥"),
    ("Análise de desempenho dos funcionários", "📋"),
    ("Grafico de Vendas por Categoria", "📚"),
    ("Previsão de Vendas", "🔮"),
    ("Cardápio", "🍽️"),
    ("Previsão de clientes", "👩‍💼"),
]

for opcao, emoji in opcoes_emojis:
    # Substitua espaços por underscores e adicione o emoji e .py ao nome do arquivo
    arquivo = f"{emoji}_{opcao.replace(' ', '_')}.py"

    # Crie o caminho completo do arquivo na pasta client/src/pages
    caminho = os.path.join("client/src/pages", arquivo)

    with open(caminho, "w") as f:
        # Escreva o conteúdo básico do arquivo
        f.write(f"# {opcao}\n")
        f.write("\n")
        f.write("def main():\n")
        f.write(f"    print('Esta é a página {emoji} {opcao}')\n")
        f.write("\n")
        f.write("if __name__ == '__main__':\n")
        f.write("    main()\n")

print("Arquivos criados na pasta client/src/pages")
