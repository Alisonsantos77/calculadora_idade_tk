from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import datetime, date

janela = Tk()
janela.title('Calculadora de idade')
janela.geometry('310x400')

# Paleta de cores
color_1 = '#000000'
color_2 = '#291528'
color_3 = '#3A3E3B'
color_4 = '#F0EFF4'
color_5 = '#E2C044'


# Criando frames
frame_cima = Frame(
    janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=color_1
)
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(
    janela, width=310, height=300, pady=0, padx=0, relief=FLAT, bg=color_2
)
frame_baixo.grid(row=1, column=0)

# Criando label para o frame de cima
l_calculadora = Label(
    frame_cima,
    text='CALCULADORA',
    width=25,
    height=1,
    padx=3,
    relief='flat',
    anchor='center',
    font=('Ivy', 15, 'bold'),
    bg=color_1,
    fg=color_4,
)
l_calculadora.place(x=0, y=30)

l_idade = Label(
    frame_cima,
    text='DE IDADE',
    width=11,
    height=1,
    padx=0,
    relief='flat',
    anchor='center',
    font=('Arial', 35, 'bold'),
    bg=color_1,
    fg=color_5,
)
l_idade.place(x=0, y=70)

# Função calcular idade


def calcular():
    inicial = cal_1.get()
    termino = cal_2.get()

    # Separando os valores
    mes, dia, ano = [int(f) for f in inicial.split('/')]

    # Convertendo os valores em formato date
    data_inicial = date(ano, mes, dia)

    mes_fim, dia_fim, ano_fim = [int(f) for f in termino.split('/')]

    # Convertendo os valores em formato date
    data_nascimento = date(ano_fim, mes_fim, dia_fim)

    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days

    l_app_anos['text'] = anos
    l_app_meses['text'] = meses
    l_app_dias['text'] = dias


# Criando label para o frame baixo
l_data_inicial = Label(
    frame_baixo,
    text='Data inicial',
    height=1,
    padx=0,
    pady=0,
    relief='flat',
    anchor=NW,
    font=('Ivy', 12, 'bold'),
    bg=color_2,
    fg=color_4,
)
l_data_inicial.place(x=15, y=30)

cal_1 = DateEntry(
    frame_baixo,
    width=13,
    bg='darkblue',
    fg=color_5,
    borderwidth=2,
    date_pattern='mm/dd/y',
    y=2024,
    locale='pt',
)
cal_1.place(x=190, y=30)

l_data_nascimento = Label(
    frame_baixo,
    text='Data de nascimento',
    height=1,
    padx=0,
    pady=0,
    relief='flat',
    anchor=NW,
    font=('Ivy', 12, 'bold'),
    bg=color_2,
    fg=color_4,
)
l_data_nascimento.place(x=15, y=70)

cal_2 = DateEntry(
    frame_baixo,
    width=13,
    bg='darkblue',
    fg=color_5,
    borderwidth=2,
    date_pattern='mm/dd/y',
    y=2024,
    locale='pt',
)
cal_2.place(x=190, y=70)

# Idade em anos, meses e dias
l_app_anos = Label(
    frame_baixo,
    text='--',
    height=1,
    padx=0,
    pady=0,
    relief='flat',
    anchor=CENTER,
    font=('Ivy', 25, 'bold'),
    bg=color_2,
    fg=color_4,
)
l_app_anos.place(x=60, y=135)

l_app_anos_nome = Label(
    frame_baixo,
    text='Anos',
    height=1,
    padx=0,
    pady=0,
    relief='flat',
    anchor=CENTER,
    font=('Ivy', 11, 'bold'),
    bg=color_2,
    fg=color_4,
)
l_app_anos_nome.place(x=60, y=175)

# Mes
l_app_meses = Label(
    frame_baixo,
    text='--',
    height=1,
    padx=0,
    pady=0,
    relief='flat',
    anchor=CENTER,
    font=('Ivy', 25, 'bold'),
    bg=color_2,
    fg=color_4,
)
l_app_meses.place(x=140, y=135)

l_app_meses_nome = Label(
    frame_baixo,
    text='meses',
    height=1,
    padx=0,
    pady=0,
    relief='flat',
    anchor=CENTER,
    font=('Ivy', 11, 'bold'),
    bg=color_2,
    fg=color_4,
)
l_app_meses_nome.place(x=140, y=175)

# Dias
l_app_dias = Label(
    frame_baixo,
    text='--',
    height=1,
    padx=0,
    pady=0,
    relief='flat',
    anchor=CENTER,
    font=('Ivy', 25, 'bold'),
    bg=color_2,
    fg=color_4,
)
l_app_dias.place(x=220, y=135)

l_app_dias_nome = Label(
    frame_baixo,
    text='dias',
    height=1,
    padx=0,
    pady=0,
    relief='flat',
    anchor=CENTER,
    font=('Ivy', 11, 'bold'),
    bg=color_2,
    fg=color_4,
)
l_app_dias_nome.place(x=220, y=175)

# Criando botão calcular
b_calcular = Button(
    frame_baixo,
    command=calcular,
    text='Calcular',
    width=20,
    height=1,
    relief='raised',
    overrelief=RIDGE,
    font=('Ivy', 10, 'bold'),
    bg=color_2,
    fg=color_4,
)
b_calcular.place(x=70, y=225)

janela.mainloop()
