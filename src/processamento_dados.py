import pandas as pd
from config import CAMINHO_ARQ_BRUTO


def carregar_dados_movielens():
    ratings = pd.read_csv(CAMINHO_ARQ_BRUTO + '/ratings.csv')
    movies = pd.read_csv(CAMINHO_ARQ_BRUTO + '/movies.csv')

    return ratings, movies

# Testa a função no notebook
if __name__ == "__main__":
    ratings, movies = carregar_dados_movielens()
    print("Ratings:")
    print(ratings.head())
    print("\nMovies:")
    print(movies.head())