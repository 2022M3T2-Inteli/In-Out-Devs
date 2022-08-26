# -*- coding: utf-8 -*-
"""Everymind - Documentação.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jt-xyFjQOxxl-NcjkA7vF-hgx2rUuGyK

# Everymind - Turnover de Funcionários

**INTEGRANTES:**


1. Emanuele Lacerda Morais Martins
2. Giovanna Furlan Torres
3. Jean Lucas Rothstein Machado
4. Lucas de Britto Vieira
5. Patrick Victorino Miranda
6. Pedro Henrique Sant'Anna Oliveira



## 1. Problema a ser resolvido:

Atualmente as empresas vêm sendo afetadas pela intensa rotatividade dos seus colaboradores. Esse problema atinge a companhia de diversas maneiras, como: 1) Os gastos contínuos com contratação; e 2) Treinamento e desenvolvimento de novos funcionários. Além disso, essa situação interfere em toda dinâmica do negócio, desde a produção, criação, desenvolvimento até a entrega final para os consumidores.

## 2. Solução Proposta

A solução se baseia em uma ferramenta, que utiliza o aprendizado de máquina para realizar a previsão da taxa de rotatividade dos funcionários. Esse modelo de predição irá fornecer a área de RH da Everymind quais colaboradores são mais propenso a saírem da empresa, contribuindo para que eles encontrem maneiras de reduzir a taxa de turnover e que melhorem a experiência dos seus colaboradores, através de um “Lock in”,  sendo esse uma forma de beneficiar os funcionários que apresentam características que condizem com a cultura da empresa, fornecendo incentivos de permanência na instituição.

# Introdução

A construção de um modelo preditivo para a alta taxa de turnover de funcionários para a empresa Everymind será realizada através do Google Colaboratory, por meio deste notebook. Nas sessões seguintes serão demonstradas passo a passo de como os dados foram utilizados até a conclusão e entrega do modelo esperado, passando pelas fases: 


1.   Seleção dos dados;
2.   Processamento dos dados selecionados;
3. Transformação dos dados (pré-processamento);
4. Mineração de dados; e
5. Interpretação e Avaliação do modelo;

## Importação das bibliotecas e plugins

1.   **Pandas:** Biblioteca que fornece ferramentas para análise e manipulação de dados;
2.   **Numpy:** Biblioteca utilizada através de funções que auxiliam na manipulação da computação numérica;
3. **Datetime e Date:** Bibliotecas que possibilitam a manipulação de datas e horas; 
4. **Moment:** Plugin para manusear o tempo em si, ou seja, o tempo exato que as condições e variáveis ocorrem ou estão ocorrendo; 
5. **matplotlib:** Biblioteca utilizada para visualização de dados e plotagem gráfica;
6. **seaborn:** Biblioteca que fornece ferramentas para plotagem estatística;
"""

#Importação de bibliotecas

import pandas as pd
import numpy as np
from datetime import date
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

#Importação de Plugins

!pip install moment
import moment

"""## Importação da base de dados

Para realizar a análise, padronização e manipulação dos dados é necessário selecionar a base de dados desejada. Neste documento a importação da mesma será feita através do Google Drive e o arquivo está em formato excel (xlsx).
"""

#Importação da Base de dados - Planilha Everymind
from google.colab import drive
drive.mount('/content/drive')
df = pd.read_excel('/content/drive/MyDrive/INTELI 2 SEM/MODULO 3/Base/Base Colaboradores Everymind.xlsx', sheet_name="Everymind")

#Importação da Base de dados - Planilha Reconhecimento
from google.colab import drive
drive.mount('/content/drive')
df1 = pd.read_excel('/content/drive/MyDrive/INTELI 2 SEM/MODULO 3/Base/Base Colaboradores Everymind.xlsx', sheet_name="Reconhecimento")

#Importação da Base de dados - Planilha Ambiente de Trabalho
from google.colab import drive
drive.mount('/content/drive')
df2 = pd.read_excel('/content/drive/MyDrive/INTELI 2 SEM/MODULO 3/Base/Base Colaboradores Everymind.xlsx', sheet_name="Ambiente de Trabalho 27.07")

"""A célula de código abaixo é responsável por realizar a leitura e apresentação dos dados carregados da base na etapa anterior.

*   df - Apresenta a aba da planilha Everymind
*   df1 - Apresenta a aba da planilha Reconhecimento
*   df2 - Apresenta a aba da planilha Ambiente de Trabalho 27.07
"""

df

df1

df2

"""## Visualização dos tipos das colunas

As colunas apresentadas em ambas as tabelas disponibilizadas possuem tipos diferentes de formatação, sendo divididos em: 

1. **float** : Responsável por armazenar números reais com precisão de 6 casas decimais; 
2. **object** : Responsável por armazenar qualquer tipo de dado genêrico, utilizado para representar características abstratas;
3. **datetime** : Responsável pelo armazenamento de datas e horas;

Os códigos abaixos apresentam os tipos encontrados nas planilhas, respectivamente:


1. Everymind
2. Reconhecimento; 
3. Ambiente de Trabalho;
"""

df.dtypes

df1.dtypes

df2.dtypes

"""## Exclusão de espaços em branco

Algumas colunas apresentavam espaços em branco, o que dificulta a manipulação durante o pré-processamento e manipulação dos dados. Sendo asism, o método replace() foi utilizado para substituir uma eventualidade encontrada em uma das strings da base de dados. 

1. Abaixo apresenta-se as colunas da planilha "Everymind" que foram necessárias retirar os espaços em branco;
"""

#Atribuição de todas as colunas que possuem o tipo objeto a variável criada
espaco_nulo_everymind = df.select_dtypes(include = 'object').columns 

#O comando é responsável por percorrer todas as linhas das colunas selecionadas e fazer a alteração de onde possui espaço em branco inserir nenhum espaço
for i in espaco_nulo_everymind:
  df[i] = df[i].str.replace(' ','')

df

"""2. Abaixo apresenta-se as colunas da planilha "Reconhecimento" que foram necessárias retirar os espaços em branco;"""

#Atribuição de todas as colunas que possuem o tipo objeto a variável criada
espaco_nulo_reconhecimento = df1.select_dtypes(include = 'object').columns 

#O comando é responsável por percorrer todas as linhas das colunas selecionadas e fazer a alteração de onde possui espaço em branco inserir nenhum espaço
for i in espaco_nulo_reconhecimento:
  df1[i] = df1[i].str.replace(' ','')

df1

"""3. Abaixo apresenta-se as colunas da planilha "Ambiente de Trabalho 27.07" que foram necessárias retirar os espaços em branco;"""

#Atribuição de todas as colunas que possuem o tipo objeto a variável criada
espaco_nulo_ambiente = df2.select_dtypes(include = 'object').columns 

#O comando é responsável por percorrer todas as linhas das colunas selecionadas e fazer a alteração de onde possui espaço em branco inserir nenhum espaço
for i in espaco_nulo_ambiente:
  df2[i] = df2[i].str.replace(' ','')

df2

"""## Adição de valores nos espaços sem informações

Algumas colunas apresentavam valores faltantes, resultando em uma qualidade de dados de difícil análise. Ao contemplar o tipo de saída esperada, calculou-se as entradas prováveis das variáveis a serem manipuladas.

1.   Coluna "Tipo Saída" - Planilha Everymind

Os dados comtemplados na coluna, são responsáveis por exibir qual tipo de saída o funcionário teve ao deixar a empresa. Nos campos em branco, foi inserido a palavra "Ativo", pois quer dizer que aquele funcionário ainda trabalha na empresa.
"""

##O comando é responsável por atribuir a coluna selecionada o valor "Ativo", somente nos campos vazios
df['Tipo Saida'] = df['Tipo Saida'].replace(np.NaN,'Ativo')

"""2. Coluna "Dt Saída" - Planilha Everymind

Os dados comtemplados na coluna, são responsáveis por exibir a data de saída do funcionário da empresa. Nos campos em branco, foi inserido a data atual (dia em que estamos), pois quer dizer que aquele funcionário ainda trabalha na empresa.
"""

#O comando é responsável por atribuir a coluna selecionada o valor da data atual, somente nos campos vazios
df['Dt Saida'] = df['Dt Saida'].replace(np.NaN, date.today())

"""3. Coluna "Pulou" - Planilha Ambiente de Trabalho

Os dados contemplados na coluna "Pulou", são responsáveis por exibir a quantidade de funcionarios que pularam a pergunta feita à eles. Nos campos em branco, foi inserido o numero 0 (devido ao fato que ninguem pulou a pergunta), assim deixando todos os dados do mesmo padrão.



*   **Observação:** O comando "isnull()" apresentado abaixo é utilizado para verificar quais linhas da coluna selecionada estão em branco.


"""

#Definindo uma variável que recebe todos os valores nulos da coluna "Pulou"
pulou_valores_nulos = df2['Pulou'].isnull()

#Definindo uma variável que recebe todos os valores presentes na coluna "Pulou"
pulou_valores = df2['Pulou']

#O for percorre as linhas de zero até a quantidade de linhas presente na variável "pulou_valores_nulos"
for i in range(0,len(pulou_valores_nulos)):

  #Se a linha de df2 que estiver sendo analisada for nula
  if pulou_valores_nulos[i] == True:
    #Adiciona o valor zero a linha selecionada
    pulou_valores_nulos[i] = "0"

  # #Se a linha de df2 que estiver sendo analisada não for nula 
  if pulou_valores_nulos[i] == False: 
    #Permanece o valor que já estava na linha 
    pulou_valores_nulos[i] = (pulou_valores[i])

"""O comando abaixo ilustra como a tabela "Ambiente de trabalho" ficou após a inclusão do número 0 (zero) nos espaços em branco."""

pulou_valores_nulos

"""Os dados contemplados na coluna "Muito Insatisfeito" são responsáveis por exibir a quantidade de funcionarios que estavam muito insatisfeitos com a questão levantada na pergunta feita à eles. Nos campos em branco, foi inserido o numero 0 (devido ao fato que a pergunta não foi respondida), assim deixando todos os dados do mesmo padrão."""

#Definindo uma variável que recebe todos os valores nulos da coluna "Muito Insatisfeito"
Minsatisfeito_valores_nulos = df2['Muito Insatisfeito'].isnull()

#Definindo uma variável que recebe todos os valores presentes na coluna "Muito Insatisfeito"
Minsatisfeito_valores = df2['Muito Insatisfeito']

#O for percorre as linhas de zero até a quantidade de linhas presente na variável "Minsatisfeito_valores_nulos"
for i in range(0,len(Minsatisfeito_valores_nulos)):

  #Se a linha de df2 que estiver sendo analisada for nula
  if Minsatisfeito_valores_nulos[i] == True:
    #Adiciona o valor zero a linha selecionada
    Minsatisfeito_valores_nulos[i] = "0"

  # #Se a linha de df2 que estiver sendo analisada não for nula 
  if Minsatisfeito_valores_nulos[i] == False: 
    #Permanece o valor que já estava na linha 
    Minsatisfeito_valores_nulos[i] = (Minsatisfeito_valores[i])

"""O comando abaixo ilustra como a tabela "Ambiente de trabalho" ficou após a inclusão do número 0 (zero) nos espaços em branco."""

Minsatisfeito_valores_nulos

"""Os dados contemplados na coluna "Insatisfeito" são responsáveis por exibir a quantidade de funcionarios que estavam insatisfeitos com a questão levantada na pergunta feita à eles. Nos campos em branco, foi inserido o numero 0 (devido ao fato que a pergunta não foi respondida), assim deixando todos os dados do mesmo padrão."""

#Definindo uma variável que recebe todos os valores nulos da coluna "Insatisfeito"
insatisfeito_valores_nulos = df2['Insatisfeito'].isnull()

#Definindo uma variável que recebe todos os valores presentes na coluna "Insatisfeito"
insatisfeito_valores = df2['Insatisfeito']

#O for percorre as linhas de zero até a quantidade de linhas presente na variável "insatisfeito_valores_nulos"
for i in range(0,len(insatisfeito_valores_nulos)):

  #Se a linha de df2 que estiver sendo analisada for nula
  if insatisfeito_valores_nulos[i] == True:
    #Adiciona o valor zero a linha selecionada
    insatisfeito_valores_nulos[i] = "0"

  # #Se a linha de df2 que estiver sendo analisada não for nula 
  if insatisfeito_valores_nulos[i] == False: 
    #Permanece o valor que já estava na linha 
    insatisfeito_valores_nulos[i] = (insatisfeito_valores[i])

"""O comando abaixo ilustra como a tabela "Ambiente de trabalho" ficou após a inclusão do número 0 (zero) nos espaços em branco."""

insatisfeito_valores_nulos

"""Os dados contemplados na coluna "Neutro" são responsáveis por exibir a quantidade de funcionarios que estavam neutros com a questão levantada na pergunta feita à eles. Nos campos em branco, foi inserido o numero 0 (devido ao fato que a pergunta não foi respondida), assim deixando todos os dados do mesmo padrão."""

#Definindo uma variável que recebe todos os valores nulos da coluna "Neutro"
neutro_valores_nulos = df2['Neutro'].isnull()

#Definindo uma variável que recebe todos os valores presentes na coluna "Neutro"
neutro_valores = df2['Neutro']

#O for percorre as linhas de zero até a quantidade de linhas presente na variável "neutro_valores_nulos"
for i in range(0,len(neutro_valores_nulos)):

  #Se a linha de df2 que estiver sendo analisada for nula
  if neutro_valores_nulos[i] == True:
    #Adiciona o valor zero a linha selecionada
    neutro_valores_nulos[i] = "0"

  # #Se a linha de df2 que estiver sendo analisada não for nula 
  if neutro_valores_nulos[i] == False: 
    #Permanece o valor que já estava na linha 
    neutro_valores_nulos[i] = (neutro_valores[i])

"""O comando abaixo ilustra como a tabela "Ambiente de trabalho" ficou após a inclusão do número 0 (zero) nos espaços em branco."""

neutro_valores_nulos

"""Os dados contemplados na coluna "Satisfeito" são responsáveis por exibir a quantidade de funcionarios que estavam satisfeitos com a questão levantada na pergunta feita à eles. Nos campos em branco, foi inserido o numero 0 (devido ao fato que a pergunta não foi respondida), assim deixando todos os dados do mesmo padrão."""

#Definindo uma variável que recebe todos os valores nulos da coluna "Satisfeito"
satisfeito_valores_nulos = df2['Satisfeito'].isnull()

#Definindo uma variável que recebe todos os valores presentes na coluna "Satisfeito"
satisfeito_valores = df2['Satisfeito']

#O for percorre as linhas de zero até a quantidade de linhas presente na variável "neutro_valores_nulos"
for i in range(0,len(satisfeito_valores_nulos)):

  #Se a linha de df2 que estiver sendo analisada for nula
  if satisfeito_valores_nulos[i] == True:
    #Adiciona o valor zero a linha selecionada
    satisfeito_valores_nulos[i] = "0"

  # #Se a linha de df2 que estiver sendo analisada não for nula 
  if satisfeito_valores_nulos[i] == False: 
    #Permanece o valor que já estava na linha 
    satisfeito_valores_nulos[i] = (satisfeito_valores[i])

"""O comando abaixo ilustra como a tabela "Ambiente de trabalho" ficou após a inclusão do número 0 (zero) nos espaços em branco."""

satisfeito_valores_nulos

"""Os dados contemplados na coluna "Muito Satisfeito" são responsáveis por exibir a quantidade de funcionarios que estavam muito satisfeitos com a questão levantada na pergunta feita à eles. Nos campos em branco, foi inserido o numero 0 (devido ao fato que a pergunta não foi respondida), assim deixando todos os dados do mesmo padrão."""

#Definindo uma variável que recebe todos os valores nulos da coluna "Muito Satisfeito"
Msatisfeito_valores_nulos = df2['Muito Satisfeito'].isnull()

#Definindo uma variável que recebe todos os valores presentes na coluna "Muito Satisfeito"
Msatisfeito_valores = df2['Muito Satisfeito']

#O for percorre as linhas de zero até a quantidade de linhas presente na variável "Mneutro_valores_nulos"
for i in range(0,len(Msatisfeito_valores_nulos)):

  #Se a linha de df2 que estiver sendo analisada for nula
  if Msatisfeito_valores_nulos[i] == True:
    #Adiciona o valor zero a linha selecionada
    Msatisfeito_valores_nulos[i] = "0"

  # #Se a linha de df2 que estiver sendo analisada não for nula 
  if Msatisfeito_valores_nulos[i] == False: 
    #Permanece o valor que já estava na linha 
    Msatisfeito_valores_nulos[i] = (Msatisfeito_valores[i])

"""O comando abaixo ilustra como a tabela "Ambiente de trabalho" ficou após a inclusão do número 0 (zero) nos espaços em branco."""

Msatisfeito_valores_nulos

"""## Formatação de datas

Para a manipulação correta das datas e horários na base de dados, todas precisam estar no mesmo formato. Para isso, realisou-se uma padronização através da utilização do comando replace, já explicado anteriormente.
"""

#O for percorre as linhas de 0 até a quantidade de linhas presente na coluna "Dt Admissao"
for i in range(0, len(df['Dt Admissao'])):
  #Passa por cada linha das colunas selecionadas e troca a formatação do conteúdo que está lá pelo formato indicado
  #remoção das horas das datas
  df['Dt Admissao'][i] = str(df['Dt Admissao'][i]).replace('00:00:00', '')
  df['Dt Saida'][i] = str(df['Dt Saida'][i]).replace('00:00:00', '')
  #troca de todas as '/' por '-'
  df['Dt Admissao'][i] = str(df['Dt Admissao'][i]).replace('/', '-')
  df['Dt Saida'][i] = str(df['Dt Saida'][i]).replace('/', '-')
  #Padronização de todos os dados para o formato (ano, mês, dia)
  df['Dt Admissao'][i] = moment.date(df['Dt Admissao'][i]).format("YYYY-MM-DD")
  df['Dt Saida'][i] = moment.date(df['Dt Saida'][i]).format("YYYY-MM-DD")
df['Dt Admissao'] = pd.to_datetime(df['Dt Admissao'], format="%Y/%m/%d")
df['Dt Saida'] = pd.to_datetime(df['Dt Saida'], format="%Y/%m/%d")

"""O código abaixo mostra como a tabela ficou construída após as padronizações. Para visualizar o resultado, altere o nome da coluna, sendo possível os seguintes nomes:


*   Dt Admissao
*   Dt Saida


"""

display(df['Dt Admissao'])

"""## Manipulação das idades

Para manipular as idades, foi necessário criar um novo atributo chamado "Idade", pois na base de dados original foi entregue somente a data de nascimento do colaborador. Abaixo é exibido como foi construído a nova coluna.
"""

#Criação de um novo atributo chamado "Idade"
df['Idade'] = 0

"""Para atribuir o valor da idade à nova coluna criada acima, foi feito um cálculo com base na diferença entre a coluna 'Dt Nascimento' e a data de hoje, fornecida pelo metodo date.today(), para os funcionarios ativos, e na diferença entre a coluna 'Dt Nascimento' e a 'Dt Saida' para os inativos.



> O metodo date.today() fornece o valor da data no momento atual, contida no sistema do computador.


"""

#o comando for passa por todas as linhas da tabela
for i in range(0, len(df['Dt Nascimento'])):
  #se na coluna Tipo saída o colaborador está ativo o comando continua
  if df['Tipo Saida'][i] == str('Ativo'):
    #se o colaborador ja fez aniverario durante o ano
    if date.today().month>(df['Dt Nascimento'][i]).month or date.today().month==(df['Dt Nascimento'][i]).month and date.today().day>=(df['Dt Nascimento'][i]).day:
      # A idade é igual a data de agora - data de nascimento do colaborador
      df['Idade'][i] = date.today().year - (df['Dt Nascimento'][i]).year
    #se o colaborador não fez aniverario no ano
    else:
      # A idade é a (data de agora - data de nascimento do colaborador) -1 ano
      df['Idade'][i] = (date.today().year - (df['Dt Nascimento'][i]).year)-1
  #se o colaborador não está mais ativo na empresa
  else:
    #se o colaborador ja fez aniverario no ano
    if df['Dt Saida'][i].month>=(df['Dt Nascimento'][i]).month:
      # A idade é a data de saída  - data de nascimento do colaborador
      df['Idade'][i] = df['Dt Saida'][i].year - (df['Dt Nascimento'][i]).year
    #se o colaborador não fez aniverario no ano
    else:
      # A idade é  a (data de saída  - data de nascimento do colaborador) - 1 ano
      df['Idade'][i] = (df['Dt Saida'][i].year - df['Dt Nascimento'][i].year)-1

"""O comando abaixo exibe a stituação da tabela, após as modificações feitas acima."""

df

"""## Cálculo do Tempo de Empresa

Para manipular o tempo de empresa, foi necessário criar um novo atributo chamado 'Tempo Empresa Meses', pois na base de dados original foi entregue somente a data de adimissão e a data de saída. Abaixo é exibido como foi construído a nova coluna:
"""

#Criação de um novo atributo chamado "Tempo Empresa Meses"
df['Tempo Empresa Meses'] = 0

"""Para atribuir o valor do tempo de empresa(em meses) à nova coluna criada acima, foi feito um cálculo com base na data de hoje, fornecida pelo metodo date.today(), inserido na coluna 'Dt Adimissao' para os funcionarios ativos, sendo necessário esse atributo para realçar a diferença entre a coluna 'Dt Saida' e a 'Dt Adimissao' para os colaboradores inativos."""

#o comando for passa por todas as linhas da tabela
for i in range(0, len(df['Dt Admissao'])):
  #se na coluna Tipo saída o colaborador está ativo o comando continua
  if df['Tipo Saida'][i] == str('Ativo'):
    # O tempo de empresa em meses é igual a data de agora - data de admissão do colaborador
    df['Tempo Empresa Meses'][i] = (((date.today().year - df['Dt Admissao'][i].year)*12)+date.today().month - df['Dt Admissao'][i].month) 
  #se o colaborador não está mais ativo na empresa
  else:
    # O tempo de empresa em meses é igual a data de agora - data de saida do colaborador
    df['Tempo Empresa Meses'][i] = (df['Dt Saida'][i].year - df['Dt Admissao'][i].year)*12+df['Dt Saida'][i].month - df['Dt Admissao'][i].month

"""O comando abaixo exibe a stituação da tabela, após as modificações feitas acima."""

df

"""## Tempo Reconhecimento

Para manipular o tempo até o reconhecimento, foi necessário criar um novo atributo chamado 'Tempo Ate Promocao Meses', pois na base de dados original foi entregue somente a data de Vigência e a data de Adimissão. Abaixo é exibido como foi construído a nova coluna:
"""

#Criação de um novo atributo chamado "Tempo Ate Promocao Meses"
df1['Tempo Ate Promocao Meses'] = 0

"""Para atribuir o valor do tempo ate a promoção (em meses) à nova coluna criada acima, foi feito um cálculo com base na diferença entre a coluna 'Data Vigência' e a coluna 'Dt Adimissao'."""

#o comando for passa por todas as linhas da tabela
for i in range(0, len(df1['Data de Admissão'])):
    # O tempo ate a promoção em meses é igual a data de vigência - data de admissão do colaborador
    df1['Tempo Ate Promocao Meses'][i] = (df1['Data Vigência'][i].year - df1['Data de Admissão'][i].year)*12+df1['Data Vigência'][i].month - df1['Data de Admissão'][i].month

"""O comando abaixo exibe a stituação da tabela, após as modificações feitas acima."""

df1

"""## Separação do número com o nome do colaborador

Para verificar e manipular a quantidade de pessoas dentro das tabelas, existem duas colunas que englobam "Pessoa" + "Número do colaborador", sendo elas:

1.   Nome Completo (Planilha Everymind)
2.   Codinome (Planilha Reconhecimento)

Como o nome do colaborador não é algo relevante para a análise de rotatividade, usaremos somente o número atribuído a cada funcionário.

Na planilha "Everymind", criaremos uma nova coluna chamada "Colaborador".
"""

#Criação de uma nova coluna na base de dados
df['Colaborador'] = ""

"""O comando abaixo executa a tabela, já com a coluna "Colaborador" acrescentada"""

df

"""Após a atualização da tabela, a coluna "Nome Completo" é dividida entre a palavra "Pessoa colaboradora" e o número que a acompanha. O programa abaixo, mostra como essa divisão foi realizada e como ocorreu a transferência dos números da coluna "Nome Completo" para  a coluna "Colaborador". """

# Retira a string "PessoaColaboradora" de todas as linhas da coluna "Nome Completo" deixando apenas o número do funcionário, o qual será transferido para a coluna "Colaborador"
for i in range(0, len(df['Nome Completo'])):
  df['Colaborador'][i] = str(df['Nome Completo'][i]).replace('PessoaColaboradora', '')

df

"""Na planilha "Reconhecimento", criaremos uma nova coluna chamada "Colaborador". """

df1['Colaborador'] = ""

"""O comando abaixo executa a tabela, já com a coluna "Colaborador" acrescentada"""

df1

"""Após a atualização da tabela, a coluna "Codinome" é dividida entre a palavra "Pessoa colaboradora" e o número que a acompanha. O programa abaixo, mostra como essa divisão foi realizada e como ocorreu a transferência dos números da coluna "Codinome" para a coluna "Colaborador"."""

# Retira a string "PessoaColaboradora" de todas as linhas da coluna "Nome Completo" deixando apenas o número do funcionário, o qual será transferido para a coluna "Colaborador"
for i in range(0, len(df1['Codinome'])):
  df1['Colaborador'][i] = str(df1['Codinome'][i]).replace('PessoaColaboradora', '')

df1

"""## Exclusão de Colunas não utilizadas

A partir da análise dos dados foi decidido pela retirada de algumas colunas da "Base Colaboradores Everymind", sendo elas as colunas "Etnia", "Nome Completo" e "Codinome". Abaixo é apresentado as colunas que foram excluídas e os motivos pelos quais elas não seram comtempladas no modelo.

Em primeiro lugar a exclusão da coluna "Etnia" foi motivada pela sensibilidade dos dados e ser antiético a análise da permanência de colaboradores a partir da etnia destes. Nesse prisma, a continuidade dessa coluna criará um modelo com resultados enviesados.
"""

#O comando abaixo é responsável por excluir a coluna "Etnia" na base de dados 
df = df.drop(columns=['Etnia'])

"""Já a retirada da coluna "Nome Completo" e "Codinome" ocorreu por esta não contribuir de forma alguma com a construção do modelo, uma vez que, um nome não pode ser um fator de decisão."""

#O comando abaixo é responsável por excluir a coluna "Nome Completo" na base de dados 
df = df.drop(columns=['Nome Completo'])

#O comando abaixo é responsável por excluir a coluna "Codinome" na base de dados 
df1 = df1.drop(columns=['Codinome'])

"""Abaixo apresenta-se a exibição das tabelas, já com a exclusão das colunas."""

#Leitura da Planilha Everymind sem a coluna "Etnia" e "Nome Completo"
df.head()

#Leitura da Planilha Reconhecimento sem a coluna "Codinome"
df1.head()

"""## One Hot encoding

Para utilizarmos as variáveis categóricas é necessário realizar uma transformação nos dados, que resultam em formas binárias (não ordenada), as quais serão aplicadas em futuras equações matemáticas no modelo de aprendizado de máquina.

  Nesse aspecto, o código abaixo utiliza um data frame, que seleciona a coluna específicada corresponde às propriedades (campos) da base de dados e suas linhas são identificadas como um registro.

1.   Planilha - Everymind
"""

#As variáveis criadas são utilizadas para receber os valores da coluna do Data Frame selecionado

data_saidas = pd.DataFrame(df, columns=["Tipo Saida"])
data_cargos = pd.DataFrame(df, columns=["Cargo"])
data_genero = pd.DataFrame(df, columns=["Genero"])
data_civil = pd.DataFrame(df, columns=["Estado Civil"])
data_estado = pd.DataFrame(df, columns=["Estado"])
data_cidade = pd.DataFrame(df, columns=["Cidade"])
data_area = pd.DataFrame(df, columns=["Area"])

#As variáveis criadas são utilizadas para receber a aplicação do One Hot encoding pelo pandas
#Para isso, utilizam-se das variáveis com os data frames criados acima 

dummie_saidas = pd.get_dummies(data_saidas["Tipo Saida"])
dummie_cargos = pd.get_dummies(data_cargos["Cargo"]) 
dummie_genero = pd.get_dummies(data_genero["Genero"])
dummie_civil = pd.get_dummies(data_civil["Estado Civil"]) 
dummie_estado = pd.get_dummies(data_estado["Estado"]) 
dummie_cidade = pd.get_dummies(data_cidade["Cidade"]) 
dummie_area = pd.get_dummies(data_area["Area"])

"""O comando abaixo é responsável por realizar a leitura e apresentação dos dados carregados gerando as matrizes do One Hot Encoding. Para alterar a visualização das matrizes mude o parâmetro do display com as variáveis a seguir: 


1. dummie_saidas
2. dummie_cargos
3. dummie_genero
4. dummie_civil
5. dummie_estado
6. dummie_cidade
7. dummie_area


"""

display(dummie_civil) #Exemplo de visualização de matriz

"""2. Planilha - Reconhecimento"""

#As variáveis criadas são utilizadas para receber os valores da coluna do Data Frame selecionado

data_situacao = pd.DataFrame(df1, columns=["Situação"])
data_motivo = pd.DataFrame(df1, columns=["Motivo"])
data_novo_cargo = pd.DataFrame(df1, columns=["Novo Cargo"])
data_alterou_funcao = pd.DataFrame(df1, columns=["Alterou Função"])

#As variáveis criadas são utilizadas para receber a aplicação do One Hot encoding pelo pandas
#Para isso, utilizam-se das variáveis com os data frames criados acima 

dummie_situacao = pd.get_dummies(data_situacao["Situação"])
dummie_motivo = pd.get_dummies(data_motivo["Motivo"]) 
dummie_novo_cargo = pd.get_dummies(data_novo_cargo["Novo Cargo"]) 
dummie_alterou_funcao = pd.get_dummies(data_alterou_funcao["Alterou Função"])

"""O comando abaixo é responsável por realizar a leitura e apresentação dos dados carregados gerando as matrizes do One Hot Encoding. Para alterar a visualização das matrizes mude o parâmetro do display com as variáveis a seguir:

*   dummie_situacao
*   dummie_motivo
*   dummie_novo_cargo
*   dummie_alterou_funcao






"""

display(dummie_motivo) #Exemplo de visualização de matriz

"""## Label Encoder

Algumas colunas apresentam a necessidade de seus dados serem apresentados com relação de ordem. A conversão de variáveis categóricas para variáveis ordinárias é realizado através do Label Encoder. No modelo preditivo construído, a única variável que foi modificada utilizando esse método, foi a coluna de escolaridade. No código abaixo é representado a forma como ocorreu tal processo.
"""

#A variável criada é utilizada para receber o valore da coluna do Data Frame selecionado
data_escolaridade = pd.DataFrame(df, columns=["Escolaridade "])

#A variável criada é utilizada para receber os dados pertencentes à coluna "Escolaridade" e ordená-los, respectivamente.
dummie_escolaridade_atual = data_escolaridade.replace(['Ensino Médio Incompleto', 'Ensino Médio', 'Técnico', 'Graduação', 'Superior incompleto', 'Pós Graduação', 'Mestrado'], [0,1,2,3,4,5,6])

"""O comando abaixo é responsável por realizar a leitura e apresentação dos dados carregados gerando a matriz com o método label encoder."""

display(dummie_escolaridade_atual)

"""## Criação novo Database

>Divisão de Funcionários Ativos e Desligados

Na tarefa de seleção de dados é onde é definida a relevância do atributo. Para atingir esse objetivo, foi necessário criar duas bases de dados com a divisão entre atributos focados nos funcionários ativos e desligados. De modo que fosse possível compreender como a relação de determinados atributos se comportam em cada um dos casos.

### Criação Database (Colaboradores Ativos)

Abaixo apresenta-se a criação da base de funcionários “Ativos”, através da seleção dos dados da planilha “Everymind".
"""

#O comando é responsável por atribuir a base de dados “Df” a variável “df_Ativo"
df_Ativo = df.copy()

#O comando é responsável por excluir a linha de dados que possui o “Tipo Saida” igual a um determinado valor
df_Ativo.drop(df_Ativo.loc[df_Ativo['Tipo Saida']=='Dispensa sem Justa Causa'].index, inplace=True)
df_Ativo.drop(df_Ativo.loc[df_Ativo['Tipo Saida']=='Pedido de Demissão'].index, inplace=True)
df_Ativo.drop(df_Ativo.loc[df_Ativo['Tipo Saida']=='Rescisao Contrato Exp - Pedido'].index, inplace=True)
df_Ativo.drop(df_Ativo.loc[df_Ativo['Tipo Saida']=='Rescisao Contrato Exp - Dispensa'].index, inplace=True)

"""O código abaixo serve para visualizar a nova base de dados de funcionários ativos"""

#O código abaixo é utilizado para visualizar a base de dados “df_Ativo”
df_Ativo

"""### Criação Database (Colaboradores Desligados)

Abaixo apresenta-se a criação da base de funcionários “Desligado”, através da seleção dos dados da planilha “Everymind”, abrangendo as seguintes categorias: Dispensa sem Justa Causa, Pedido de Demissão, Rescisao Contrato Exp - Pedido e Rescisao Contrato Exp - Dispensa.
"""

#O comando é responsável por atribuir a base de dados “Df” a variável “df_Desligado"
df_Desligado = df.copy()
#O comando é responsável por excluir a linha de dados que possui o “Tipo Saida” igual a um determinado valor
df_Desligado.drop(df_Desligado.loc[df_Desligado['Tipo Saida']=='Ativo'].index, inplace=True)

"""O código abaixo serve para visualizar a nova base de dados de funcionários desligador"""

#O código abaixo é utilizado para visualizar a base de dados “df_Desligado”
df_Desligado

"""## Análise de colunas



> Relação de funcionarios ativos e desligados com cargo

Essa análise serve para identificar possíveis dados enviesados, de modo que seja possível entender o real impacto de uma variável, levando em consideração a quantidade total de funcionários por cargo.

O comando abaixo é responsável por realizar a contagem total de funcionários por cargo da base de dados “df_Desligados"
"""

df_Desligado['Cargo'].value_counts()

"""O comando abaixo é responsável por realizar a contagem total de funcionários por cargo da base de dados “df_Ativos"""

df_Ativo['Cargo'].value_counts()

"""## Gráficos Gerados

### Relação entre “Idade" e “Cargo”

> Funcionários ativos e desligados

O comando abaixo é responsável por gerar um gráfico de dispersão, levando em consideração os funcionários ativos, fazendo a relação dos dados idade (eixo x) e cargo (eixo y)
"""

sns.scatterplot(data = df_Desligado, x = 'Idade', y = 'Cargo', color='Red')

"""O comando abaixo é responsável por gerar um gráfico de dispersão, levando em consideração os funcionários desligados, fazendo a relação dos dados idade (eixo x) e cargo (eixo y)"""

sns.scatterplot(data = df_Ativo, x = 'Idade', y = 'Cargo')

"""### Relação entre “Salario Mês" e “Cargo”


>  Funcionários ativos e desligados

O comando abaixo é responsável por gerar um gráfico de dispersão, levando em consideração os funcionários ativos, fazendo a relação dos dados salário mês (eixo x) e cargo (eixo y)
"""

sns.scatterplot(data = df_Desligado, x = 'Salario Mês', y = 'Cargo', color='Red')

"""O comando abaixo é responsável por gerar um gráfico de dispersão, levando em consideração os funcionários desligados, fazendo a relação dos dados salário mês (eixo x) e cargo (eixo y)"""

sns.scatterplot(data = df_Ativo, x = 'Salario Mês', y = 'Cargo')

"""### Relação entre “Tempo Empresa Meses" e “Cargo”



> Funcionários ativos e desligados

O comando abaixo é responsável por gerar um gráfico de dispersão, levando em consideração os funcionários ativos, fazendo a relação dos dados tempo de empresa do colaborador por mês (eixo x) e cargo (eixo y)
"""

sns.scatterplot(data = df_Desligado, x = 'Tempo Empresa Meses', y = 'Cargo', color='Red')

"""O comando abaixo é responsável por gerar um gráfico de dispersão, levando em consideração os funcionários desligados, fazendo a relação dos dados tempo de empresa do colaborador por mês (eixo x) e cargo (eixo y)"""

sns.scatterplot(data = df_Ativo, x = 'Tempo Empresa Meses', y = 'Cargo')

"""### Relação entre "Dt Saída" e "Cargo""""

#Agrupa os dados pelos atributos 'Dt Saida' e 'Cargo' contabilizando o tamanho do agrupamento
dfg = df.groupby([df['Dt Saida'].dt.year, 'Cargo' ]).size() 

#Desempilha os dados do dataframe e preenche todos os elementos vazios
dfg = dfg.unstack(level=0).fillna(0)

#Cria um gráfico de barras com o dfg alterado
dfg.plot(kind = 'bar', figsize=(20,5))

"""## Referências

BÔSCOA, Vinícius. Codificação de Variáveis - Label vs One-Hot Encoder. [S. l.], 17 maio 2022. Disponível em: https://www.viniboscoa.dev/blog/codificacao-de-variaveis-label-vs-one-hot-encoder. Acesso em: 26 ago. 2022.

HORN, Michelle. Python replace: substituindo substrings em uma string!. [S. l.], 31 ago. 2021. Disponível em: https://blog.betrybe.com/python/python-replace/#1. Acesso em: 26 ago. 2022.

MOURA, Weslley. One Hot Encoding com Python. [S. l.], 12 dez. 2016. Disponível em: https://hackinganalytics.wordpress.com/2016/12/12/one-hot-encoding-com-python/. Acesso em: 26 ago. 2022.

Data Frame. O que é data frame?. Disponível em: https://www.dcc.fc.up.pt/~ltorgo/SebentaR/HTML/node16.html. Acesso em: 26 ago. 2022.
"""