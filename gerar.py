from jinja2 import Template

#coleta dos dados
dados = {
    "nome": input("Nome: "),
    "funcao": input("Função: "),
    "periodo": input("Período: "),
    "unidade": input("Unidade: ")
}

# carrega o template
with open("template.txt", encoding="utf-8") as f:
    template_texto = f.read()


template = Template(template_texto)

# gera o texto final
texto_final = template.render(dados)

#salva o arquivo
with open("declaracao_gerada.txt", "w", encoding="utf-8") as f:
    f.write(texto_final)

print("\nDocumento gerado com sucesso!")