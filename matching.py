import pandas as pd
import time
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
import faiss
import numpy as np

class model:
    def find_nearest_neighbors(self, user_id, df1, feature_vectors, index,k=3):
        user_idx = df1.index[df1['user'] == user_id][0]
        user_vector = feature_vectors[user_idx].reshape(1, -1)
        distances, indices = index.search(user_vector, k+1)
        neighbors = []
        for dist, idx in zip(distances[0][1:], indices[0][1:]):
            neighbor = df1.iloc[idx]
            if dist < 10:
                neighbors.append({
                    'user': neighbor['user'],
                    'Name': neighbor['Name'],
                    'Similarity': dist,
                    'Distance': neighbor['Distance'],
                    'location': neighbor['location'],
                    'mobile': neighbor['mobile'],
                })
        return neighbors
        
    def fit_it(self, selected_user_id, nearby):
        df1 = pd.DataFrame(nearby)
        print(df1.head())

        scaler = StandardScaler()
        # df1.drop('Distance',axis=1,inplace=True)

        df1['Budget'] = scaler.fit_transform(np.reshape(df1['Budget'],(-1, 1)))

        vectorizer = TfidfVectorizer()

        hobbies_tfidf = vectorizer.fit_transform(df1['Hobbies'])

        hobbies_df1 = pd.DataFrame(hobbies_tfidf.toarray(), columns=vectorizer.get_feature_names_out())

        df1 = pd.concat([df1.reset_index(drop=True), hobbies_df1.reset_index(drop=True)], axis=1)
        df1['Is_Vegetarian'] = [1 if i else 0 for i in df1['Is_Vegetarian'].values]
        feature_columns = ['Budget'] + list(hobbies_df1.columns) +['Is_Vegetarian']
        feature_vectors = df1[feature_columns].values

        d = feature_vectors.shape[1]
        index = faiss.IndexFlatL2(d)

        index.add(feature_vectors)
 
        start_time = time.time()
        nearest_neighbors = self.find_nearest_neighbors(selected_user_id, df1,feature_vectors, index)
        end_time = time.time()

        s=[]
        for neighbor in nearest_neighbors:
            s.append(f"User: {neighbor['Name']}, Distance from you: {neighbor['Distance']},loaction: {neighbor['location']}, Contact Info: {neighbor['mobile']}, Matching: {int((1 - neighbor['Similarity']/10)*100)}%")
        
        return s