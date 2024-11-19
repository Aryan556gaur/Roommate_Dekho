from geopy.distance import geodesic
from inserter import mongo_retriever
from geopy.geocoders import Nominatim

class nearby_people:
    def __init__(self) -> None:
        pass

    def calculate_distance(self, loc1, loc2):
        return geodesic(loc1, loc2).kilometers



    def get_address_from_coordinates(self, latitude, longitude):
        # Initialize the geolocator
        geolocator = Nominatim(user_agent="geoapi")
        
        # Get the location
        location = geolocator.reverse((latitude, longitude), exactly_one=True)
        
        # Return the address
        if location and location.address:
            return location.address
        else:
            return "Address not found"

# Example usage
# latitude = 37.7749
# longitude = -122.4194
# address = get_address_from_coordinates(latitude, longitude)
# print(f"Address: {address}")

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

