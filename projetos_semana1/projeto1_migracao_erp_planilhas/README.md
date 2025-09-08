# Projeto 1 – Migração de pedidos do ERP para Google Sheets

## Problema
Automatizar a transferência de pedidos do ERP para Google Sheets, mantendo histórico e evitando erros manuais.

## Solução
O script `migracao_erp.py`:
- Lê os pedidos de um arquivo JSON (`erp_pedidos.json`)
- Transforma os dados em formato compatível com Google Sheets
- Envia os dados para a planilha via API (precisa da Service Account)

## Tecnologias usadas
- Python
- gspread
- pandas
- Google Sheets API

## Como usar
1. Crie uma Service Account no Google Cloud com acesso à Google Sheets API.
2. Baixe o arquivo JSON da Service Account e salve como `service_account.json` na pasta do projeto.
3. Compartilhe sua planilha com o e-mail da Service Account.
4. Rode o script:
   ```bash
   python migracao_erp.py
