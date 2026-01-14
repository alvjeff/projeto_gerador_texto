import tkinter as tk
from tkinter import messagebox
from app.core import gerar_documento


def iniciar_ui():
    # janela principal
    root = tk.Tk()
    root.title("Gerador de Documentos")
    root.geometry("400x350")
    root.resizable(False, False)

    # ---------- FUNÇÃO DO BOTÃO ----------
    def gerar():
        dados = {
            "nome": entry_nome.get(),
            "funcao": entry_funcao.get(),
            "periodo": entry_periodo.get(),
            "unidade": entry_unidade.get()
        }

        nome_arquivo = entry_arquivo.get().strip()
        if not nome_arquivo:
            nome_arquivo = "declaracao"

        try:
            caminho = gerar_documento(dados, nome_arquivo)
            messagebox.showinfo(
                "Sucesso",
                f"Documento gerado com sucesso!\n\n{caminho}"
            )
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # ---------- CAMPOS ----------
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(fill="both", expand=True)

    def criar_campo(texto, linha):
        tk.Label(frame, text=texto).grid(row=linha, column=0, sticky="w", pady=5)
        entry = tk.Entry(frame, width=30)
        entry.grid(row=linha, column=1, pady=5)
        return entry

    entry_nome = criar_campo("Nome:", 0)
    entry_funcao = criar_campo("Função:", 1)
    entry_periodo = criar_campo("Período:", 2)
    entry_unidade = criar_campo("Unidade:", 3)
    entry_arquivo = criar_campo("Nome do arquivo:", 4)

    # ---------- BOTÃO ----------
    botao = tk.Button(
        frame,
        text="Gerar Documento",
        command=gerar,
        width=20
    )
    botao.grid(row=5, column=0, columnspan=2, pady=20)

    root.mainloop()
