import pandas as pd


df = pd.DataFrame(pd.read_csv('Pokemon.csv'))


# OBJETIVOS
# Ver os 5 Pokemons com mais HP;
print('-'*50)
print('Top 5 Pokemons with more health points')
print()
most_hp = df.nlargest(5, 'HP')[['Name', 'HP']]
print(most_hp)

print()

# Ver os 5 Pokemons com mais ATK;
print('-'*50)
print('Top 5 Pokemons with more ATK damage')
print()
most_atk = df.nlargest(5, 'Attack')[['Name', 'Attack']]
print(most_atk)

print()

# Ver os 5 Pokemons com mais speed;
print('-'*50)
print('Top 5 Pokemons with more speed')
print()
most_speed = df.nlargest(5, 'Speed')[['Name', 'Speed']]
print(most_speed)

print()

# Ver 5 Pokemons de tipo fogo e voador;

fire_and_fly = df.nlargest(5, ['Defense'])

# Ver os 5 lendários com mais HP e ATK;
# for linha in range(len(df)):
#     if df['Legendary'] == 'True':
#         df_lgndry = pd.DataFrame(df['Name', 'HP', 'Attack'])


# print(df_lgndry)
