import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura_cm = float(entry_altura.get())
        altura_m = altura_cm / 100

        imc = peso / (altura_m ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 24.9:
            classificacao = "Peso normal"
        elif imc < 29.9:
            classificacao = "Sobrepeso"
        elif imc < 34.9:
            classificacao = "Obesidade grau 1"
        elif imc < 39.9:
            classificacao = "Obesidade grau 2"
        else:
            classificacao = "Obesidade grau 3"

        label_resultado["text"] = f"IMC: {imc:.2f}\n{classificacao}"
    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos para peso e altura.")

def reiniciar():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    label_resultado["text"] = "Resultado"

def sair():
    root.destroy()

root = tk.Tk()
root.title("Cálculo do IMC – Índice de Massa Corporal")
root.configure(bg="#e6f0fa")
root.resizable(False, False)

frame = tk.LabelFrame(root, text="Cálculo do IMC - Índice de Massa Corporal",
                      bg="#f5fbff", fg="#154360", font=("Arial", 12, "bold"), bd=2)
frame.grid(row=0, column=0, padx=20, pady=20)

tk.Label(frame, text="Nome do Paciente:", bg="#f5fbff").grid(row=0, column=0, sticky="e", padx=7, pady=7)
entry_nome = tk.Entry(frame, width=33)
entry_nome.grid(row=0, column=1, padx=7, pady=7)

tk.Label(frame, text="Endereço Completo:", bg="#f5fbff").grid(row=1, column=0, sticky="e", padx=7, pady=7)
entry_endereco = tk.Entry(frame, width=33)
entry_endereco.grid(row=1, column=1, padx=7, pady=7)

tk.Label(frame, text="Altura (cm):", bg="#f5fbff").grid(row=2, column=0, sticky="e", padx=7, pady=7)
entry_altura = tk.Entry(frame, width=10)
entry_altura.grid(row=2, column=1, sticky="w", padx=7, pady=7)

tk.Label(frame, text="Peso (Kg):", bg="#f5fbff").grid(row=3, column=0, sticky="e", padx=7, pady=7)
entry_peso = tk.Entry(frame, width=10)
entry_peso.grid(row=3, column=1, sticky="w", padx=7, pady=7)

label_resultado = tk.Label(frame, text="Resultado", width=29, height=4,
                           bg="#d6eaf8", fg="#154360", relief="sunken", anchor="nw", justify="left", font=("Arial", 10))
label_resultado.grid(row=2, column=2, rowspan=2, padx=10, pady=7, sticky="n")

# Botões
botao_frame = tk.Frame(frame, bg="#f5fbff")
botao_frame.grid(row=4, column=0, columnspan=3, pady=(13, 0))

tk.Button(botao_frame, text="Calcular", width=13, command=calcular_imc, bg="#85c1e9").grid(row=0, column=0, padx=8)
tk.Button(botao_frame, text="Reiniciar", width=13, command=reiniciar, bg="#aed6f1").grid(row=0, column=1, padx=8)
tk.Button(botao_frame, text="Sair", width=13, command=sair, bg="#d5dbdb").grid(row=0, column=2, padx=8)

root.mainloop()
