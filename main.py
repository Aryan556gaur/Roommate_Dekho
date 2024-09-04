from geopy.distance import geodesic

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


