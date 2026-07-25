#1 passo: importar base de dados
import pandas as pd
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
import yagmail 
usuario = yagmail.SMTP("pauloregis1234567@gmail.com", "senha")
usuario.send(
    to="pauloregis+diretoria@gmail.com",
    subject="Ranking das Lojas",
    contents=mensagem
)