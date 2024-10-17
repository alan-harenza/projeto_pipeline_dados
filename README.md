# Projeto de conceitos iniciais de Engenharia de Dados

Nele abordaremos o conceito do ETL\
E - Extract - Extração\
T - Transform - Transformaçõa\
L - Load - Carregamento (Salvar)

O projeto em si:\
Duas empresas se fundiram, e nós como engenheiro de dados, devemos unificar os as bases de dados\
e disponibilizar o arquivo unificado para o time de Analytics.

Outro ponto importante é que o código deverá ser a temporal, isto é, sempre que precisarmos unificar\
as bases podemos usar ele.

Primeiro Passo: Obter as bases de dados.
usaremos o comando wget <url> (mais a url da fonte destes dados) desta fora obteremos o arquivo sem\
precisar apertar o botão de download. Precisamos fazer este processo para o arquivo json e csv

Criaremos uma maquina virtual para fazer a instalação das bibliotecas necessárias, e também\
manteremos um ambiente separado sem possibilidade interferência em outros projetos e no\
Python do sistema.
para a maquina virtual: $ .venv\Scripts\activate\
para desativar: $ deactivate