import os
from pathlib import Path
from docxtpl import DocxTemplate

def gerar_declaracao(dados, nome_arquivo):
    # 1. Localiza o modelo (Pasta templates na raiz do projeto)
    # Usamos Path().resolve() para garantir que o Python ache o arquivo
    template_path = Path.cwd() / "templates" / "template_modelo.docx"
    
    if not template_path.exists():
        raise FileNotFoundError(f"Modelo não encontrado em: {template_path}")

    # 2. Carrega o modelo Word
    doc = DocxTemplate(str(template_path))

    # 3. Preenche as variáveis (O render faz tudo de uma vez!)
    # Os 'dados' devem ser um dicionário: {'nome': 'Arnold', 'data': '14/01'}
    doc.render(dados)

    # 4. Define e cria a pasta de saída
    output_dir = Path.cwd() / "output"
    output_dir.mkdir(exist_ok=True)

    # 5. Salva o arquivo final
    caminho_final = output_dir / f"{nome_arquivo}.docx"
    doc.save(str(caminho_final))

    return caminho_final