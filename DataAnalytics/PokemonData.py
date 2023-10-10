import pandas as pd
import numpy as np


df = pd.DataFrame(pd.read_csv('Pokemon.csv'))


# OBJETIVOS
# Ver os 5 Pokemons com mais HP;
print('-'*50)
print('Top 5 Pokemons with more health points')
print()
most_hp = df.nlargest(5, 'HP')[['Name', 'HP', 'Generation']]
print(most_hp)

print()

# Ver os 5 Pokemons com mais ATK;
print('-'*50)
print('Top 5 Pokemons with more ATK damage')
print()
most_atk = df.nlargest(5, 'Attack')[['Name', 'Attack', 'Generation']]
print(most_atk)

print()

# Ver os 5 Pokemons com mais speed;
print('-'*50)
print('Top 5 Pokemons with more speed points')
print()
most_speed = df.nlargest(5, 'Speed')[['Name', 'Speed', 'Generation']]
print(most_speed)

print()

# Ver os 5 lendários com mais defense;
print('-'*50)
print('Top 5 legendary Pokemons with more defense points')
print()
lgdry = df.loc[df['Legendary'] == True]
lgdry_hp_atk = lgdry.nlargest(5, 'Defense')[['Name', 'Defense', 'Generation']]
print(lgdry_hp_atk)

print()

# Ver 5 pokemons do tipo fogo com mais pontos de atk;
print('-'*50)
print('Top 5 fire Pokemons with more ATK damage')
print()
fire_poke = df.loc[df['Type 1'] == 'Fire']
fire_atk = fire_poke.nlargest(
    5, 'Attack')[['Name', 'Type 1', 'Attack', 'Generation']]
fire_atk.shape
print(fire_atk)

print()

# Ver os tipos de pokemon que mais aparecem (Type 1);
print('-'*50)
print('Types of pokemon that appear most (type 1)')
print()
columnstypeone = df[['Type 1']]
columnstypeone = columnstypeone.value_counts()
print(columnstypeone)

print()
