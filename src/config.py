# Caminhos de arquivos e diretórios
CAMINHO_ARQ_BRUTO = 'data/bruto'             # Caminho para dados brutos
CAMINHO_ARQ_PROCESSADO = 'dados/processado'   # Caminho para dados processados
CAMINHO_MODELO = 'models/final_recommender.pkl'  # Caminho para o modelo treinado

# Configurações para pré-processamento
RATING_THRESHOLD = 3.5  # Threshold para considerar filmes bem avaliados (exemplo)
REMOVE_DUPLICATES = True
REMOVE_NULLS = True

# Parâmetros do modelo de recomendação
N_NEIGHBORS = 5         # Número de vizinhos no KNN
MODEL_ALGORITHM = 'auto' # Algoritmo para KNN, pode ser 'ball_tree', 'kd_tree', etc.

# Configurações de avaliação
EVALUATION_METRIC = 'rmse'  # Pode ser 'rmse', 'precision', 'recall', etc.

# Configurações para a aplicação web
FLASK_DEBUG_MODE = True     # Define se o modo debug do Flask está ativado
FLASK_HOST = '127.0.0.1'    # Endereço do servidor web
FLASK_PORT = 5000           # Porta para a aplicação web

# Configurações de conexão com o MovieLens (exemplo)
MOVIELENS_DATASET_SIZE = '100k'  # Tamanho do dataset usado ('100k', '1M', '20M')

# Parâmetros gerais do projeto
RANDOM_SEED = 42  # Semente para aleatoriedade em experimentos

# Função auxiliar para impressão das configurações (para debug)
def print_config():
    print("Configurações do Projeto:")
    print(f"DATA_FILE_PATH: {DATA_FILE_PATH}")
    print(f"PROCESSED_DATA_PATH: {PROCESSED_DATA_PATH}")
    print(f"MODEL_PATH: {MODEL_PATH}")
    print(f"RATING_THRESHOLD: {RATING_THRESHOLD}")
    print(f"N_NEIGHBORS: {N_NEIGHBORS}")
    print(f"EVALUATION_METRIC: {EVALUATION_METRIC}")
    print(f"FLASK_DEBUG_MODE: {FLASK_DEBUG_MODE}")
    print(f"FLASK_HOST: {FLASK_HOST}")
    print(f"FLASK_PORT: {FLASK_PORT}")
    print(f"MOVIELENS_DATASET_SIZE: {MOVIELENS_DATASET_SIZE}")
    print(f"RANDOM_SEED: {RANDOM_SEED}")
