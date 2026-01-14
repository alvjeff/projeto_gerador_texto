import tkinter as tk
from tkinter import messagebox
# Importamos do core que está na mesma pasta
from .core import gerar_declaracao 

def gerar():
    # 1. Captura os dados
    dados = {
        "nome": nome_entry.get(),
        "funcao": funcao_entry.get(),
        "periodo": periodo_entry.get(),
        "unidade": unidade_entry.get()
    }

    # 2. Validação simples: não deixa gerar se o nome estiver vazio
    if not dados["nome"]:
        messagebox.showwarning("Atenção", "O campo 'Nome' é obrigatório!")
        return

    try:
        # 3. Chama o motor (core.py) que agora usa docxtpl
        # Usamos o nome do arquivo dinâmico baseado no nome da pessoa
        caminho = gerar_declaracao(dados, f"Declaracao_{dados['nome']}")
        
        # 4. Feedback visual para o usuário (essencial em automação)
        messagebox.showinfo("Sucesso", f"Documento gerado com sucesso!\nSalvo em: {caminho}")
        
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao gerar documento: {e}")