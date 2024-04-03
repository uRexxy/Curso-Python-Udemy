import pandas as pd
import matplotlib.pyplot as plt


file_path = r"C:\Users\Tadin\OneDrive\Documentos\Curso Python Udemy\Base_de_dados\worldometer_data.csv"
df = pd.DataFrame(pd.read_csv(file_path))



try:
    southamerica_stats = df.loc[df['Continent'] == 'South America', ['Country', 'TotalCases', 'TotalDeaths', 'TotalRecovered']]
    sam_death_mean = southamerica_stats.groupby('Country')['TotalDeaths'].sum()
    sam_death_mean = sam_death_mean.dropna()
    print(sam_death_mean)
except KeyError:
    print('Cannot show the dataframe.')

# print(southamerica_stats)
