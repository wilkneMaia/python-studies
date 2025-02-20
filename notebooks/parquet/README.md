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

#### Seções do Notebook

- **Ler arquivo Parquet utilizando PyArrow**: Como usar o PyArrow para ler arquivos Parquet.
- **Ler apenas colunas específicas em uma tabela**: Seleção de colunas de uma tabela Parquet com PyArrow.
- **Adicionar uma nova coluna e seus valores a uma tabela**: Como modificar tabelas Parquet com PyArrow.
- **Alterar um valor específico em uma coluna de uma tabela**: Modificar valores em tabelas PyArrow.
- **Excluir uma coluna existente de uma tabela**: Como remover colunas de tabelas Parquet.
- **Particionar arquivos Parquet**: O particionamento de arquivos Parquet é explicado, destacando a importância de particionar dados em grandes volumes, especialmente para análise de dados em sistemas distribuídos.

### 2. **[pandas.ipynb](./pandas.ipynb)**

O notebook **Pandas.ipynb** foca em diversas operações de manipulação de dados utilizando o **Pandas**, como leitura e escrita de arquivos Parquet, além de manipulações específicas em tabelas.

#### Seções do Notebook

- **Ler arquivo Parquet utilizando Pandas**: Como carregar arquivos Parquet em um DataFrame do Pandas.
- **Ler apenas colunas específicas em uma tabela**: Como selecionar colunas específicas durante a leitura de arquivos.
- **Adicionar uma nova coluna e seus valores a uma tabela**: Mostra como adicionar colunas e preencher seus valores.
- **Alterar um valor específico em uma coluna de uma tabela**: Manipulação de dados em colunas já existentes.
- **Excluir coluna existente de uma tabela**: Como remover colunas de um DataFrame.
- **Particionando um DataFrame**: Estratégias para particionar grandes DataFrames em subconjuntos.

### 3. **[compression.ipynb](./compression.ipynb)**

Este notebook explora o processo de **compressão de arquivos Parquet** com diferentes algoritmos, tais como **Snappy**, **Gzip**, **Brotli** e **Zstd**. O foco está em comparar a compressão de arquivos CSV em Parquet utilizando esses algoritmos, avaliando o desempenho de compressão, tempo de execução e taxa de redução de tamanho dos arquivos.

#### Seções do Notebook

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
