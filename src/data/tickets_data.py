import pandas as pd


tickets_df = pd.read_excel("./src/files/PLANILHA-DE-PEDIDO.xlsx")

if 'VALOR TOTAL' in tickets_df.columns:
    tickets_df['VALOR TOTAL'] = tickets_df['VALOR TOTAL'].apply(lambda x: f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    