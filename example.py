from geopy.distance import geodesic
from inserter import mongo_retriever

class nearby_people:
    def __init__(self) -> None:
        pass

    def calculate_distance(self, loc1, loc2):
        return geodesic(loc1, loc2).kilometers

    def find_nearby_users(self, cursor, current_user_id, current_location, max_distance):
        # Convert Cursor to a list of dictionaries
        user_list = list(cursor)

        nearby_users = []

        for user_info in user_list:
            id = list(user_info.values())[0]
            distance = self.calculate_distance(current_location, user_info['location'])
            if distance <= max_distance:
                nearby_users.append({'user': id, 'Name': user_info['Name'], 'Distance': distance, 'Hobbies': user_info['Hobbies'], 'Budget': user_info['Budget'], 'Is_Vegetarian': user_info['Is_Vegetarian']})

        return nearby_users
# data = [
#     {'user': 'user2', 'Name': 'Bob', 'location': [34.0522, -118.2437], 'Budget': 2000.0, 'Hobbies': 'reading,music', 'Is_Vegetarian': False, 'mobile': 984983247},
#     {'user': 'user3', 'Name': 'Charlie', 'location': [40.7128, -74.0060], 'Budget': 4000.0, 'Hobbies': 'reading,music', 'mobile': 7236572365},
#     {'user': 'user1', 'Name': 'Alice', 'location': [37.7749, -122.4194], 'Budget': 3000.0, 'Hobbies': 'cricket,reading', 'mobile': 5283582123},
#     {'user': 'user4', 'Name': 'David', 'location': [37.7759, -122.4194], 'Budget': 3500.0, 'Hobbies': 'movies,travel', 'mobile': 8712376188},
# ]

# mret = mongo_retriever()
# collection = mret.mongo_setup()
# collection.drop_indexes()
# cursor = collection.find({}, {'_id': 0})
# dataB = list(cursor)
# collection.insert_many(data)

