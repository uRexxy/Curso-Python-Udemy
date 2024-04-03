import pandas as pd

file_path = r"C:\Users\Tadin\OneDrive\Documentos\Curso Python Udemy\Base_de_dados\Pokemon.csv"
df = pd.DataFrame(pd.read_csv(file_path))


# Filtra todos os pokemons em que seu tipo 1 é grama
# grass_pokemons = df.loc[df['Type 1'] == 'Grass', ['Name', 'HP', 'Generation']]
# print(grass_pokemons)

# Busca o pokemon pelo seu nome
# print(df.loc[df['Name'] == 'Charizard', ['Name', 'Type 1', 'Type 2',]])

# Nova coluna +80HP mostra True se o pokemon tiver mais de 80 de hp ou False caso contrario
# df['+80HP'] = df['HP'] >= 80

# Cria uma nova coluna e atribui valores a ela
# df.loc[1:6, 'Teste'] = 1
# df['HP médio'] = None

# Exclue uma coluna ou uma linha. axis=1, coluna. axis=0, linha.
# df = df.drop('Legendary', axis=1)

# Deletar linhas e colunas completamente vazias
# df = df.dropna(how='all', axis=1)

# Deletar linhas que possuem pelo menos 1 valor vazio
# df = df.dropna()

# Preencher valores vazios
# Preencher com a média da coluna
# df['HP médio'] = df['HP médio'].fillna(df['HP'].mean())

# Preencher com o ultimo valor
# df = df.ffill()

# calcular indicadores, Groupyby e Value Counts
# Value counts
# tipos_poke = df['Type 1'].value_counts()

# Group by
# group = df[['Type 1', 'HP', 'Attack']].groupby('Type 1').sum()
# group = df[['Type 1', 'HP', 'Attack']].groupby('Type 1').mean()

# juntando duas tabelas
# df = df.merge(nome_tabela)
print(df)
