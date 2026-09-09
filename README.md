# Automação de Análise e Envio de Relatório de Vendas

Criei esse projeto para resolver um problema muito comum nas empresas: o tempo desperdiçado compilando dados de vendas e mandando e-mails manualmente todo santo dia. 

Com esse script em Python, o processo roda sozinho. Ele lê os dados de faturamento, monta um ranking das lojas bem formatado e dispara direto para o e-mail da diretoria.

## O que usei para construir:
* **Python** (como linguagem base)
* **Pandas** (para tratar os dados e gerar o ranking das lojas)
* **Yagmail** (para facilitar o envio do e-mail via Gmail)
* **Python-Dotenv** (essencial para não deixar minha senha exposta no código)

## Segurança em primeiro lugar
Configurei o projeto usando variáveis de ambiente, minhas credenciais ficam salvas localmente em um arquivo `.env` (que está protegido no `.gitignore`), garantindo que o código fique limpo e seguro para rodar em qualquer máquina.

## Como testar na sua máquina

1. Clone o meu repositório:
   ```bash
   git clone https://github.com
   ```

2. Instale as bibliotecas necessárias:
   ```bash
   pip install pandas yagmail python-dotenv
   ```

3. Crie um arquivo chamado `.env` na pasta do projeto e coloque suas informações:
   ```env
   EMAIL_USER=seu_email@gmail.com
   EMAIL_PASS=sua_senha_aqui
   EMAIL_TO=email_de_quem_vai_receber@gmail.com
   ```

4. Agora é só rodar o script:
   ```bash
   python codigo.py
   ```
