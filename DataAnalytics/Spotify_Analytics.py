import pandas as pd
import matplotlib.pyplot as plt

# Abrindo o arquivo
file_path = r"C:\Users\Tadin\OneDrive\Documentos\Curso Python Udemy\Base_de_dados\spotify-2023.csv"

df = pd.DataFrame(pd.read_csv(file_path,  encoding='ISO-8859-1'))


# Ver as 5 musicas mais tocadas no spotify;
df['streams'] = df['streams'].str.replace(',', '', regex=True)
df['streams'] = df['streams'].str.extract('(\d+)').astype(float)
mais_tocadas = df.nlargest(5, 'streams')[
    ['track_name', 'artist(s)_name', 'streams']]
print(mais_tocadas)








# Ver as 5 musicas com mais bpm;
# Ver as 5 musicas com mais palavras faladas;
# Ver as 5 musicas que mais estão em playlists;
# Ver as 5 musicas com mais artistas contribuindo;
