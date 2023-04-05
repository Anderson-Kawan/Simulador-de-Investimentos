import pandas as pd
import plotly.express as px

investimento_inicial = float(input(f'Para começar, Qual o valor deseja ivestir?\n'))

investimento_mensal = float(input(f'É por mes, Quanto gostaria de depositar?\n'))

taxa_ano = float(input(f'Qual a Rentabilidade Anual voce ira considerar?\nRecomendação: Considerar % acima de inflação\n'))/100
taxa_mes = taxa_ano/12

n_anos = int(input(f'Quanto anos deixaria seu dinheiro investido?\n'))
n_meses = n_anos*12

#...
investimentos = pd.DataFrame()

for m in range(1,n_meses+1):
    if m==1:
        saldo_inicial = investimento_inicial
    else:
        saldo_inicial = investimentos.loc[m -1, 'Montante Final']

    investimento_mes = saldo_inicial + investimento_mensal

    juros = investimento_mes * taxa_mes

    montante = investimento_mes + juros

    investimentos.loc[m, 'Saldo Inicial'] = saldo_inicial
    investimentos.loc[m, 'Aporte Mensal'] = investimento_mensal
    investimentos.loc[m, 'Investimento Finall'] = investimento_mes
    investimentos.loc[m, 'Juros'] = juros
    investimentos.loc[m, 'Montante Final'] = montante

investimentos.index.name = 'Mês'
print(investimentos)


