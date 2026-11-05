# Análise financeira — ClearBank

Projeto de estudo em Python para ler transações bancárias de um CSV, descartar registros inválidos e gerar um resumo mensal. Todos os dados são fictícios.

## Como executar

Abra `desafio-final.ipynb` no Google Colab ou Jupyter. No Colab, envie `transacoes.csv` e `analise_pandas.py` para a pasta da sessão pelo painel Arquivos. Execute todas as células na ordem e salve o notebook com as saídas.

Para usar Jupyter localmente, mantenha os arquivos na mesma pasta. Use Python 3.10 ou superior e instale as dependências com `pip install -r requirements.txt`.

A análise principal usa somente módulos nativos. Pandas e matplotlib são usados nas etapas opcionais.

## Resultados

O notebook mostra a limpeza dos dados, o período analisado, as métricas de cada mês e as transações acima de R$ 10.000,00. Também gera `relatorio.json` e `grafico.png`.

O CSV contém 26 registros: 15 válidos, 10 inválidos e uma repetição de ID. O primeiro registro válido de cada ID é mantido; duplicatas entram no total descartado e são identificadas separadamente no resumo. Há dados de janeiro a março de 2026 e duas transações acima do limite.

Os testes cobrem validação, duplicatas, arquivo ausente, dados vazios, cálculos mensais e o limite de suspeita. A versão em `analise_pandas.py` compara todas as métricas mensais com a solução nativa. A marcação de suspeita é apenas a regra de valor definida no exercício.
