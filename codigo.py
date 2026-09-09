#1 passo: importar base de dados
import os
import pandas as pd
import yagmail 
from dotenv import load_dotenv


lista_loja = ["BH","DF","Manaus","Rio","Salvador","SP"]
dic_faturamento = {}
#2 passo: calcular o faturamento total de cada loja

for loja in lista_loja:
    df = pd.read_excel(f"Loja {loja}.xlsx")
    fat_total = sum(df["Vendas"])
    dic_faturamento[loja] = fat_total
print(dic_faturamento)
#3 passo: criar um ranking do faturamento de cada loja

df_ranking = pd.DataFrame.from_dict(dic_faturamento, orient="index", columns=["Vendas"])
df_ranking = df_ranking.sort_values(by="Vendas", ascending=False)
df_ranking = df_ranking.map("R${:,.2f}".format)

#4 passo: enviar este ranking por email 
mensagem = f"""
Prezados,
Segue em anexo o ranking de vendas das Lojas:

Ranking:

{df_ranking.to_string().replace(" ", "-")}

Qualquer dúvida, estou à disposição.
Att.,
Paulo Régis
"""
print(mensagem)

# Carrega as variáveis salvas no arquivo .env
load_dotenv()

# Recupera os dados de forma segura sem expor no código
usuario_email = os.getenv("EMAIL_USER")
senha_email = os.getenv("EMAIL_PASS")
destinatario = os.getenv("EMAIL_TO")

usuario = yagmail.SMTP(usuario_email, senha_email)
usuario.send(
    to=destinatario,
    subject="Ranking das Lojas",
    contents=mensagem
)