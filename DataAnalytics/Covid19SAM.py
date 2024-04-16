# importando pandas para analise de dados e matplotlib.pyplot para a demonstração desses dados
import pandas as pd
import matplotlib.pyplot as plt

# Abrindo o arquivo e tratando as exceções
try:
    file_path = r"C:\Users\Tadin\OneDrive\Documentos\Curso Python Udemy\Base_de_dados\worldometer_data.csv"
    df = pd.DataFrame(pd.read_csv(file_path))
except KeyError:
    print('Cannot show the dataframe.')

# filtrando algumas informações apenas da América do Sul
southamerica_stats = df.loc[df['Continent'] == 'South America', [
    'Country', 'TotalCases', 'TotalDeaths', 'TotalRecovered']]

# mudando o nome da coluna "TotalDeaths" para "Total Deaths"
southamerica_stats.rename(
    columns={'TotalDeaths': 'Total Deaths'}, inplace=True)

# organizando a lista de forma decrescente
sam_death_cases = southamerica_stats[['Country', 'Total Deaths']].sort_values(
    by='Total Deaths', ascending=False, ignore_index=True)

# retirando valores vazios
sam_death_cases = sam_death_cases.dropna()

# Tirar indice

print(sam_death_cases)

# plt.bar(sam_death_cases, height=100000, width=1000,  )
# plt.plot(sam_death_cases)
# plt.ylim(0, 100000)
# plt.title('Casos de morte por Covid-19 na América do Sul')
# plt.show()
