import tkinter as tk
from tkinter import messagebox

def calcular_juros():
    try:
        capital = float(entrada_capital.get().replace(",", "."))
        taxa = float(entrada_juros.get().replace(",", ".")) / 100
        tempo = float(entrada_tempo.get().replace(",", "."))
        aporte = float(entrada_aporte.get().replace(",", "."))

        tipo_juros = opcao_juros.get()
        tipo_tempo = opcao_tempo.get()

        if tipo_juros == "Ano":
            taxa = (1 + taxa) ** (1 / 12) - 1

        if tipo_tempo == "Anos":
            tempo = tempo * 12

        tempo = int(tempo)

        if taxa == 0:
            montante = capital + (aporte * tempo)
        else:
            montante = capital * (1 + taxa) ** tempo + aporte * (((1 + taxa) ** tempo - 1) / taxa)

        total_investido = capital + (aporte * tempo)
        juros = montante - total_investido

        resultado_label.config(
            text=f"Montante final: R$ {montante:.2f}\n"
                 f"Total investido: R$ {total_investido:.2f}\n"
                 f"Juros ganhos: R$ {juros:.2f}",
            fg="#00ff7f"
        )

    except ValueError:
        messagebox.showerror("Algo deu errado!", "Digite valores válidos!")

def limpar_campos():
    entrada_capital.delete(0, tk.END)
    entrada_juros.delete(0, tk.END)
    entrada_tempo.delete(0, tk.END)
    entrada_aporte.delete(0, tk.END)
    opcao_juros.set("Mês")
    opcao_tempo.set("Meses")
    resultado_label.config(text="Resultado aparecerá aqui", fg="#FFD700")

janela = tk.Tk()
janela.title("Calculadora de Juros Compostos")
janela.geometry("400x550")
janela.configure(bg="#212138")
janela.resizable(False, False)

estilo_label = {"bg": "#212138", "fg": "#ffffff", "font": ("Arial", 10, "bold")}
estilo_entry = {"font": ("Arial", 12), "justify": "center", "width": 18}

tk.Label(
    janela,
    text="💰 Juros Compostos",
    font=("Arial", 16, "bold"),
    bg="#212138",
    fg="#00ff7f"
).pack(pady=20)

tk.Label(janela, text="Capital Inicial (R$):", **estilo_label).pack()
entrada_capital = tk.Entry(janela, **estilo_entry)
entrada_capital.pack(pady=5)

tk.Label(janela, text="Taxa de Juros (%):", **estilo_label).pack()

frame_juros = tk.Frame(janela, bg="#212138")
frame_juros.pack(pady=5)

entrada_juros = tk.Entry(frame_juros, font=("Arial", 12), justify="center", width=15)
entrada_juros.grid(row=0, column=0, padx=5)

opcao_juros = tk.StringVar(value="Mês")
menu_juros = tk.OptionMenu(frame_juros, opcao_juros, "Mês", "Ano")
menu_juros.config(
    font=("Arial", 9, "bold"),
    bg="#33334d",
    fg="white",
    activebackground="#444466",
    activeforeground="white",
    width=5,
    relief="flat"
)
menu_juros["menu"].config(
    font=("Arial", 9),
    bg="#33334d",
    fg="white"
)
menu_juros.grid(row=0, column=1, padx=5)

tk.Label(janela, text="Aporte Mensal (R$):", **estilo_label).pack()
entrada_aporte = tk.Entry(janela, **estilo_entry)
entrada_aporte.pack(pady=5)

tk.Label(janela, text="Tempo:", **estilo_label).pack()

frame_tempo = tk.Frame(janela, bg="#212138")
frame_tempo.pack(pady=5)

entrada_tempo = tk.Entry(frame_tempo, font=("Arial", 12), justify="center", width=15)
entrada_tempo.grid(row=0, column=0, padx=5)

opcao_tempo = tk.StringVar(value="Meses")
menu_tempo = tk.OptionMenu(frame_tempo, opcao_tempo, "Meses", "Anos")
menu_tempo.config(
    font=("Arial", 9, "bold"),
    bg="#33334d",
    fg="white",
    activebackground="#444466",
    activeforeground="white",
    width=6,
    relief="flat"
)
menu_tempo["menu"].config(
    font=("Arial", 9),
    bg="#33334d",
    fg="white"
)
menu_tempo.grid(row=0, column=1, padx=5)

frame_botoes = tk.Frame(janela, bg="#212138")
frame_botoes.pack(pady=25)

botao_calcular = tk.Button(
    frame_botoes,
    text="Calcular",
    font=("Arial", 12, "bold"),
    bg="#4caf50",
    fg="white",
    activebackground="#45a049",
    activeforeground="white",
    relief="flat",
    width=12,
    command=calcular_juros
)
botao_calcular.grid(row=0, column=0, padx=10)

botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    font=("Arial", 12, "bold"),
    bg="#f44336",
    fg="white",
    activebackground="#d32f2f",
    activeforeground="white",
    relief="flat",
    width=12,
    command=limpar_campos
)
botao_limpar.grid(row=0, column=1, padx=10)

resultado_label = tk.Label(
    janela,
    text="Resultado aparecerá aqui",
    font=("Arial", 13, "bold"),
    bg="#212138",
    fg="#FFD700",
    justify="center"
)
resultado_label.pack(pady=20)

janela.mainloop()
