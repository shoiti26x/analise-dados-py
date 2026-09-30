Análise de Cancelamento de Clientes (Churn Analysis)

Sobre o projeto
Análise de dados em Python de uma base com mais de 800 mil clientes, identificando os principais motivos de cancelamento (churn) e apontando ações para reduzir esse número.

Problema
Uma empresa com alta taxa de clientes inativos precisava entender por que os clientes cancelam e quais fatores mais influenciam essa decisão, para guiar ações de retenção.

O que o projeto faz
- Importa e trata a base de dados de clientes (idade, tempo como cliente, frequência de uso, atendimento, tipo de assinatura, gastos, etc.)
- Analisa a relação entre variáveis como frequência de uso, ligações ao call center, dias de atraso e duração do contrato com a taxa de cancelamento
- Gera visualizações interativas com Plotly para facilitar a interpretação dos dados
- Identifica os perfis de cliente com maior propensão a cancelar

Tecnologias usadas
Python
Pandas
Plotly

Como rodar
pip install pandas plotly
python analise_churn.py

Coloque o arquivo cancelamentos.csv na mesma pasta do script.

Principais insights
- Contrato mensal é o maior fator de risco: todos os clientes com contrato mensal cancelaram o serviço. Ação sugerida: oferecer desconto para migração para contrato trimestral ou anual.
- Mais de 4 ligações ao call center indicam cancelamento certo: todos os clientes que ligaram mais de 4 vezes cancelaram. Ação sugerida: alerta interno a partir de 3 ligações, sinalizando problema não resolvido.
- Atraso de pagamento acima de 20 dias também leva ao cancelamento em praticamente todos os casos. Ação sugerida: alerta a partir de 15 dias de atraso, para ação preventiva antes do cancelamento.
- Após filtrar a base removendo esses três fatores de risco (contrato mensal, mais de 4 ligações, mais de 20 dias de atraso), a taxa de cancelamento cai significativamente — mostrando que esses três pontos concentram a maior parte do problema.
