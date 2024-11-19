from surprise import Dataset, Reader
from surprise.prediction_algorithms.matrix_factorization import SVD
from surprise import accuracy
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer

# Carregar os dados para o treinamento

movies_df = pd.read_csv('data/raw/movies.csv')
ratings_df = pd.read_csv('data/raw/ratings.csv')

df = pd.merge(ratings_df, movies_df[['movieId','genres']], on='movieId',how='left')

user_encoder = LabelEncoder()
movies_encoder = LabelEncoder()
mlb = MultiLabelBinarizer()

df['userId'] = user_encoder.fit_transform(df['userId'])
df['movieId'] = movies_encoder.fit_transform(df['movieId'])

df = df.join(pd.DataFrame(mlb.fit_transform(df.pop('genres').str.split('|'),),columns = mlb.classes_, inde = df.index))