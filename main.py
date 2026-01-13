from jinja2 import Environment, FileSystemLoader
from pathlib import Path

#coleta dos dados
dados = {
    "nome": input("Nome: "),
    "funcao": input("Função: "),
    "periodo": input("Período: "),
    "unidade": input("Unidade: ")
}

# nome do arquivo
nome_arquivo = input("Nome do arquivo (sem extensão): ").strip()
if not nome_arquivo:
    nome_arquivo = "declaracao"


# carrega o template
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("template.txt")


# gera o texto final
texto_final = template.render(dados)

#garante pasta de saída
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

#salva o arquivo (por enquanto txt)
caminho = output_dir / f"{nome_arquivo}.txt"
with open(caminho, "w", encoding="utf-8") as f:
    f.write(texto_final)

print("\nDocumento gerado com sucesso em: {caminho}")