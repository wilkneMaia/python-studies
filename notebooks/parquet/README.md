# 🚀 Material de Apoio por Módulo

Este repositório contém diversos notebooks que abordam diferentes tópicos sobre compressão, manipulação e particionamento de dados no formato **Parquet** utilizando **Pandas** e **PyArrow**. Abaixo, você encontrará os módulos organizados com descrições e links para acessar diretamente cada notebook.

## **🚀 Material de apoio por módulo**

| Módulo | Descrição | Link para o Notebook |
|--------|-----------|----------------------|
| **1 - Manipulação de Dados com PyArrow** | Foca na biblioteca **PyArrow** para leitura, escrita e manipulação de arquivos Parquet. Inclui tópicos como particionamento de dados. | [pyarrow.ipynb](./pyarrow.ipynb) |
| **2 - Manipulação de Dados com Pandas** | Aborda o uso do **Pandas** para manipulação de arquivos Parquet, com operações como leitura, escrita e modificação de tabelas. | [pandas.ipynb](./pandas.ipynb) |
| **3 - Compressão de Arquivos Parquet** | Explora a compressão de arquivos Parquet com algoritmos como **Snappy**, **Gzip**, **Brotli** e **Zstd**, comparando o desempenho e a eficiência de compressão. | [compression.ipynb](./compression.ipynb) |

---

## Descrição dos Notebooks

Este repositório contém três notebooks principais que abordam diferentes aspectos da manipulação e compressão de arquivos Parquet, além de técnicas de manipulação de dados utilizando **Pandas** e **PyArrow**.

### 1. **[pyarrow.ipynb](./pyarrow.ipynb)**

O notebook **PyArrow.ipynb** aborda as funcionalidades do **PyArrow**, uma biblioteca eficiente para manipulação de dados em formato Parquet. Este notebook inclui operações de leitura, modificação e escrita de arquivos Parquet, além de introduzir o conceito de **particionamento de dados**.

#### Seções do Notebook:
- **Ler arquivo Parquet utilizando PyArrow**: Como usar o PyArrow para ler arquivos Parquet.
- **Ler apenas colunas específicas em uma tabela**: Seleção de colunas de uma tabela Parquet com PyArrow.
- **Adicionar uma nova coluna e seus valores a uma tabela**: Como modificar tabelas Parquet com PyArrow.
- **Alterar um valor específico em uma coluna de uma tabela**: Modificar valores em tabelas PyArrow.
- **Excluir uma coluna existente de uma tabela**: Como remover colunas de tabelas Parquet.
- **Particionar arquivos Parquet**: O particionamento de arquivos Parquet é explicado, destacando a importância de particionar dados em grandes volumes, especialmente para análise de dados em sistemas distribuídos.

### 2. **[pandas.ipynb](./pandas.ipynb)**

O notebook **Pandas.ipynb** foca em diversas operações de manipulação de dados utilizando o **Pandas**, como leitura e escrita de arquivos Parquet, além de manipulações específicas em tabelas.

#### Seções do Notebook:
- **Ler arquivo Parquet utilizando Pandas**: Como carregar arquivos Parquet em um DataFrame do Pandas.
- **Ler apenas colunas específicas em uma tabela**: Como selecionar colunas específicas durante a leitura de arquivos.
- **Adicionar uma nova coluna e seus valores a uma tabela**: Mostra como adicionar colunas e preencher seus valores.
- **Alterar um valor específico em uma coluna de uma tabela**: Manipulação de dados em colunas já existentes.
- **Excluir coluna existente de uma tabela**: Como remover colunas de um DataFrame.
- **Particionando um DataFrame**: Estratégias para particionar grandes DataFrames em subconjuntos.

### 3. **[compression.ipynb](./compression.ipynb)**

Este notebook explora o processo de **compressão de arquivos Parquet** com diferentes algoritmos, tais como **Snappy**, **Gzip**, **Brotli** e **Zstd**. O foco está em comparar a compressão de arquivos CSV em Parquet utilizando esses algoritmos, avaliando o desempenho de compressão, tempo de execução e taxa de redução de tamanho dos arquivos.

#### Seções do Notebook:
- **Requisitos**: Instalação dos pacotes necessários.
- **Compressão de arquivo CSV em Parquet**: Converte um arquivo CSV para o formato Parquet.
- **Compressão de arquivo Parquet com Snappy**: Demonstrando o uso de compressão Snappy.
- **Comparação de compressão em arquivos Parquet**: Comparando os algoritmos **snappy**, **gzip**, **brotli** e **zstd**.
- **Uso de Compressão Automática com o PyArrow**: Usando compressão automática no PyArrow.
- **Uso de Compressão Snappy e Compactação de Colunas Individualmente**: Aplicando compressões diferentes em colunas individuais.
- **Script de Comparação de Compressões Parquet**: Comparação de vários algoritmos de compressão para decidir qual é o mais eficiente.

---

## Como Rodar os Notebooks

1. **Instalar as dependências**:

   Antes de rodar os notebooks, instale os pacotes necessários com o seguinte comando:

   ```bash
   pip install pandas pyarrow parquet
   ```

# Parquet: Acelere sua Análise de Dados e Reduza Custos em Nuvem

Em um mundo onde dados são o novo petróleo, a eficiência no processamento se torna crucial. O formato Parquet surge como uma solução poderosa para otimizar a análise de grandes volumes de dados, oferecendo ganhos significativos em performance e redução de custos. Imagine uma planilha com várias colunas. Em um formato linha a linha (como CSV), você lê a linha inteira, mesmo que precise apenas de uma ou duas colunas. Com o Parquet, você lê apenas as colunas necessárias, como se estivesse "cortando" a tabela verticalmente e pegando apenas as partes relevantes. Isso economiza tempo e recursos.

## O que é Parquet?

Parquet é um formato de armazenamento de dados colunar, open-source, projetado para otimizar a leitura e o processamento de grandes volumes de dados. Diferentemente de formatos tradicionais como CSV, que armazenam dados linha a linha, o Parquet organiza as informações por colunas. Essa simples mudança tem um impacto enorme no desempenho de consultas e análises.

## Por que o Parquet é tão relevante?

### Armazenamento Colunar: A Base da Eficiência

A principal diferença entre o Parquet e formatos tradicionais como CSV ou JSON é a forma como os dados são armazenados. Em vez de armazenar os dados linha a linha, o Parquet organiza as informações por colunas. Isso reduz drasticamente o tempo de leitura e o uso de recursos, especialmente em datasets com muitas colunas.

### Compressão Otimizada: Reduza Custos e Acelere suas Análises

O Parquet não apenas organiza os dados de forma inteligente, mas também os comprime de maneira eficaz. Ele utiliza algoritmos de compressão otimizados, como Snappy, Gzip e LZO, que reduzem o tamanho dos arquivos sem perda significativa de desempenho. Arquivos menores significam:

- **Menos espaço em disco:** Redução de custos de armazenamento, especialmente em ambientes de nuvem.
- **Transferências mais rápidas:** Aceleração do processamento e da transferência de dados pela rede.
- **Menor uso de recursos:** Redução do consumo de CPU e memória durante a leitura e o processamento.

### Column Pruning: Leitura Seletiva de Colunas

Uma das características mais poderosas do Parquet é a capacidade de realizar "column pruning" (poda de colunas). Isso significa que, durante uma consulta ou análise, o sistema só precisa ler as colunas realmente necessárias, ignorando as demais. Em um dataset com muitas colunas, isso pode resultar em uma economia significativa de tempo e recursos.

### Schema: Organização e Facilidade de Uso

O Parquet armazena o schema (estrutura) dos dados junto com os próprios dados. Isso torna a leitura e interpretação das informações muito mais simples e eficiente. O schema garante que os dados sejam lidos corretamente e facilita a integração com diferentes ferramentas e plataformas.

### Impacto na Performance e Economia de Custos

Ao combinar o armazenamento colunar, a compressão otimizada, o column pruning e o suporte a schema, o Parquet oferece uma melhoria significativa na performance de queries e análises. Isso se traduz em menor tempo de processamento, menor uso de recursos e, consequentemente, economia de custos, especialmente em ambientes de nuvem.

## Parquet vs. Outros Formatos: Qual Escolher?

Para entender melhor o valor do Parquet, vamos compará-lo com outros formatos:

| Característica        | Parquet                 | CSV                     | JSON                    |
| ---------------------- | ----------------------- | ----------------------- | ----------------------- |
| Armazenamento          | Colunar                 | Linha a Linha           | Linha a Linha           |
| Compressão             | Alta                    | Nenhuma                 | Baixa                   |
| Schema                 | Suportado               | Não suportado           | Suportado (implícito)    |
| Eficiência para análise | Alta                    | Baixa                   | Baixa                   |
| Ideal para             | Grandes datasets, análises | Pequenos datasets, troca de dados | APIs, dados semiestruturados |

## Lendo e Escrevendo Arquivos Parquet em Python

### Criando um DataFrame de Amostra

Primeiro, vamos criar um DataFrame de amostra com diferentes tipos de dados para demonstrar a versatilidade do Parquet:

```python
import pandas as pd
import numpy as np

# Criando um DataFrame de exemplo com diversos tipos de dados
data = {
    'Nome': ['Maria', 'John', 'Tonico', 'Mariane'],
    'Idade': [25, 30, 35, np.nan],  # Incluindo um valor nulo
    'Salário': [50000.50, 60000.75, 70000.00, 80000.25],
    'Data_Admissão': pd.to_datetime(['2020-01-15', '2019-05-20', '2018-11-01', '2021-03-10']),
    'Descrição': ['Desenvolvedora Python', 'Analista de Dados', 'Cientista de Dados', 'Gerente de Projetos com acentuação çãõ']
}
df = pd.DataFrame(data)

print("DataFrame Original:")
print(df)
```

### Escrevendo Arquivos Parquet

O Pandas oferece suporte nativo para escrita de arquivos Parquet, simplificando o processo. O parâmetro engine permite escolher o motor de escrita. O motor pyarrow é geralmente recomendado para melhor performance, compatibilidade com mais tipos de dados e suporte a compressão. O fastparquet é uma alternativa que pode ser mais rápida em alguns casos.

Vamos demonstrar a escrita com pyarrow e compressão snappy (uma boa opção para um bom equilíbrio entre compressão e velocidade) e também com fastparquet:

```python
# Escrevendo o DataFrame para um arquivo Parquet usando pyarrow (recomendado) e compressão snappy
try:
    df.to_parquet('meu_arquivo.parquet', engine='pyarrow', compression='snappy')
    print("\nArquivo Parquet 'meu_arquivo.parquet' escrito com sucesso usando pyarrow e compressão snappy!")

    df.to_parquet('meu_arquivo_fastparquet.parquet', engine='fastparquet')
    print("\nArquivo Parquet 'meu_arquivo_fastparquet.parquet' escrito com sucesso usando fastparquet!")
except Exception as e:
    print(f"Erro ao escrever o arquivo Parquet: {e}")
```

### Lendo Arquivos Parquet

Agora, vamos ler os arquivos Parquet que acabamos de criar. Demonstraremos como ler o arquivo completo e como ler apenas colunas específicas (column pruning), utilizando diferentes engines.

```python
# Lendo o arquivo Parquet
try:
    # Lendo o arquivo completo com pyarrow (recomendado)
    df_lido_pyarrow = pd.read_parquet('meu_arquivo.parquet', engine='pyarrow')
    print("\nDataFrame lido completo com pyarrow:")
    print(df_lido_pyarrow)

    # Lendo o arquivo completo com fastparquet
    df_lido_fastparquet = pd.read_parquet('meu_arquivo_fastparquet.parquet', engine='fastparquet')
    print("\nDataFrame lido completo com fastparquet:")
    print(df_lido_fastparquet)

    # Lendo apenas as colunas 'Nome' e 'Salário' com pyarrow (column pruning)
    df_colunas_selecionadas = pd.read_parquet('meu_arquivo.parquet', columns=['Nome', 'Salário'], engine='pyarrow')
    print("\nDataFrame com colunas selecionadas (Nome e Salário) com pyarrow:")
    print(df_colunas_selecionadas)

except FileNotFoundError:
    print("\nErro: Arquivo Parquet não encontrado. Certifique-se de que o arquivo 'meu_arquivo.parquet' ou 'meu_arquivo_fastparquet.parquet' existe no diretório atual.")
except pd.errors.ParserError as pe:
    print(f"\nErro de parsing do Parquet: {pe}")
except Exception as e:
    print(f"\nOutro erro ao ler o arquivo Parquet: {e}")
```

## Conclusão

O Parquet é uma ferramenta poderosa para qualquer profissional que trabalha com análise de dados, oferecendo ganhos significativos em performance e economia de custos. Experimente utilizá-lo em seus projetos e veja a diferença! Compartilhe nos comentários suas experiências com o Parquet e quais outros formatos você utiliza.
