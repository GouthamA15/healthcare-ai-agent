from vectorstore.embeddings import get_embedding_model

import warnings 

warnings.filterwarnings("ignore", category=FutureWarning)

emb = get_embedding_model()

vector = emb.embed_query("What is diabetes?")

print(len(vector))