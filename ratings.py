"""Restaurant rating lister."""

def get_restaurant_ratings(file):
# open the file
    ratings_file = open(file)
    
# empty dictionary to store ratings
    restaurant_ratings = {}

# user input
    user_restaurant = input("Enter your restaurant name: ")
    user_rating = input("Enter your rating for this restaurant: ")
    restaurant_ratings[user_restaurant] = user_rating
# need to split each line at ":"]
    for line in ratings_file:
        line = line.rstrip().split(":")

# add the lines from the list into a dictionary
        restaurant_ratings[line[0]] = line[1]

#to sort: try sorted(restaurant_ratings.items()) should gives us the keys as a alphabetically sorted list .
    sorted_ratings = sorted(restaurant_ratings.items())
# loops through the sorted ratings tuple to print ratings output
    for restaurant in sorted_ratings:
    #assigning variables to each idex of the tuples within the list
        restaurant_name = restaurant[0]
        rating = restaurant[1]
        print(f"{restaurant_name} is rated at {rating}")
            


