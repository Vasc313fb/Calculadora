import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        # Obtém os valores inseridos nos campos de entrada
        num1 = entry_num1.get()
        num2 = entry_num2.get() 
        
                
            # Converte os valores para float
        num1 = float(num1)
        num2 = float(num2)
        
            # Obtém o operador inserido
        operador = entry_operador.get()

            # Verifica se o operador é válido
        if operador not in ['+', '-', '*', '/', '**']:
            raise TypeError('Operador inválido! \n Os unicos operadores validos são \n ( [ + ] [ - ] [ * ] [ / ] [ ** ] )')

            # Realiza o cálculo com base no operador
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            resultado = num1 / num2
        elif operador == '**':
            resultado = num1 ** num2
            
            # Atualiza o texto do rótulo com o resultado
        label_resultado.config(text=f'Resultado: {resultado}')
            # Define o foco de volta para o primeiro campo de entrada (entry_num1)
        entry_num1.focus_set()

    except TypeError as e:
        # Exibe uma mensagem de erro se ocorrer um TypeError
        messagebox.showerror('Erro', f'Erro: {e}')
    except ValueError:
        # Exibe uma mensagem de erro se ocorrer um ValueError (por exemplo, se o usuário inserir texto em vez de números)
        messagebox.showerror('Erro', 'Digite apenas numeros')
    except ZeroDivisionError:
        # Exibe uma mensagem de erro se ocorrer uma ZeroDivisionError (divisão por zero)
        messagebox.showerror('Erro', 'Erro: Divisão por zero não permitida.')

# Cria a janela principal
root = tk.Tk()
root.title('Calculadora')
# Define o ícone da janela
root.iconbitmap("imagem/matematicas.ico")

# Configurações da janela
window_width = 235
window_height = 160
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width/2) - (window_width/2))
y_coordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Criação dos elementos da interface gráfica
label_num1 = tk.Label(root, text='Número 1: ')
label_num1.grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

label_operador = tk.Label(root, text='Operador: ')
label_operador.grid(row=1, column=0, padx=5, pady=5)
entry_operador = tk.Entry(root)
entry_operador.grid(row=1, column=1, padx=5, pady=5)

label_num2 = tk.Label(root, text='Número 2: ')
label_num2.grid(row=2, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=2, column=1, padx=5, pady=5)

button_calcular = tk.Button(root, text='Calcular', command=calcular, bg='#F38282')
button_calcular.grid(row=5, column=0, columnspan=6, padx=5, pady=5)

label_resultado = tk.Label(root, text='Resultado:')
label_resultado.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")  

# Vincula a tecla "Enter" em cada campo de entrada (Entry) para chamar a função calcular
entry_num1.bind('<Return>', lambda event=None: entry_operador.focus_set())
entry_operador.bind('<Return>', lambda event=None: entry_num2.focus_set())
entry_num2.bind('<Return>', lambda event=None: calcular())

# Inicia o loop principal da interface gráfica
root.mainloop()