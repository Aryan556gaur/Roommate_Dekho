import pandas as pd
import numpy as np
from sklearn.neighbors import KDTree

class nnear:

    def find_nearest_by_location(self, docs, user_id, radius=10):
        # user_list = list(cursor)
        df = pd.DataFrame(docs)
        user_idx = df.index[df['user'] == user_id][0]
        location_vectors = np.vstack(df['location'].apply(np.array).values)
        user_location = np.reshape(location_vectors[user_idx], (1, -1))

        # Query KD-Tree within radius
        kdtree = KDTree(location_vectors, metric='euclidean')
        indices = kdtree.query_radius(user_location, r=radius)[0]

        neighbors = []
        for idx in indices:
            neighbor = df.iloc[idx]
            neighbors.append({
                'user': neighbor['user'],
                'Name': neighbor['Name'],
                'Distance': np.linalg.norm(user_location - location_vectors[idx]),
                'Hobbies': neighbor['Hobbies'], 
                'Budget': neighbor['Budget'],
                'location': neighbor['location'], 
                'Is_Vegetarian': neighbor['Is_Vegetarian'],
                'mobile': neighbor['mobile']})
        return neighbors