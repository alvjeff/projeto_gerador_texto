import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from datetime import datetime
from docxtpl import DocxTemplate

# --- MOTOR (O que estava no core.py) ---
def gerar_documento(dados, nome_arquivo):
    try:
        template_path = Path.cwd() / "app"/"templates" / "template_modelo.docx"
        if not template_path.exists():
            return False, f"Modelo não encontrado em: {template_path}"

        doc = DocxTemplate(str(template_path))
        doc.render(dados)

        output_dir = Path.cwd() / "output"
        output_dir.mkdir(exist_ok=True)

        caminho_final = output_dir / f"{nome_arquivo}.docx"
        doc.save(str(caminho_final))
        return True, caminho_final
    except Exception as e:
        return False, str(e)

# --- LÓGICA DA INTERFACE (O que estava no ui.py) ---
def acao_botao():
    dados = {
        "nome": entry_nome.get(),
        "funcao": entry_funcao.get(),
        "periodo": entry_periodo.get(),
        "unidade": entry_unidade.get(),
        "data": datetime.now().strftime("%d/%m/%Y")
    }

    if not dados["nome"]:
        messagebox.showwarning("Atenção", "Preencha pelo menos o Nome!")
        return

    sucesso, resultado = gerar_documento(dados, f"Declaracao_{dados['nome']}")

    if sucesso:
        messagebox.showinfo("Sucesso", f"Documento gerado!\nSalvo em: {resultado}")
    else:
        messagebox.showerror("Erro", f"Falha: {resultado}")

# --- JANELA PRINCIPAL ---
root = tk.Tk()
root.title("Gerador Pro v1.0")
root.geometry("400x450")

tk.Label(root, text="DADOS DA DECLARAÇÃO", font=("Arial", 12, "bold")).pack(pady=15)

# Criando campos de forma organizada
tk.Label(root, text="Nome:").pack()
entry_nome = tk.Entry(root, width=40)
entry_nome.pack(pady=5)

tk.Label(root, text="Função:").pack()
entry_funcao = tk.Entry(root, width=40)
entry_funcao.pack(pady=5)

tk.Label(root, text="Período:").pack()
entry_periodo = tk.Entry(root, width=40)
entry_periodo.pack(pady=5)

tk.Label(root, text="Unidade:").pack()
entry_unidade = tk.Entry(root, width=40)
entry_unidade.pack(pady=5)

btn = tk.Button(root, text="GERAR WORD", command=acao_botao, bg="blue", fg="white", padx=20, pady=10)
btn.pack(pady=30)

root.mainloop()