import requests
from bs4 import BeautifulSoup

class Swiggy:
    def __init__(self, location, dish) -> None:
        self.endpointp1 = "https://www.swiggy.com/city/"
        self.endpointp2 = "-dish-restaurants"
        self.optno = None
        self.location = location
        self.dish = dish
        self.url = None
        self.headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'}

        self.response = self.__fetch_response(self.location, self.dish)

    def __fetch_response(self, meal, location):

        url = f"{self.endpointp1}{location.casefold()}/{meal.replace(' ','-').casefold()}{self.endpointp2}"
        try:
            response = requests.get(url=url,headers=self.headers)
        except Exception as err:
            print(f"[#] An exception has occured. Hint : {err}")
        self.url = url
        return response

    def __get_category(self, soup) -> list:
        hotel_data = soup.find_all(class_="DishCard__Container-sc-i11giv-0")
        hotel_info = []

        for hotel in hotel_data:
            htl = {}
            htl["hotel_name"] = hotel.find(class_="DishCard__Title-sc-i11giv-5").text
            htl["hotel_rating"] = hotel.find(class_="eqAFXv").text.split(" • ")[0]
            htl["hotel_distance"] = hotel.find(class_="eqAFXv").text.split(" • ")[1]
            temp_dishes = hotel.find_all(class_="DishItem__Container-sc-ishzkt-0")
            dishes = []

            for dish in temp_dishes:
                try:
                    meal = {}
                    meal["dish_title"] = dish.find(class_="DishItem__Title-sc-ishzkt-7").text
                    meal["dish_price"] = dish.find(class_="cLgJpo").text
                    meal["dish_rating"] = dish.find(class_="Rating__RatingText-sc-1xdhyjq-1").text
                except Exception as err:
                    continue
                dishes.append(meal)

            htl["hotel_dishes"] = dishes

            hotel_info.append(htl)
        hotel_info.append(self.url)
        return hotel_info

    def get_category_dishes(self):
        soup = BeautifulSoup(self.response.text, "html.parser")
        hotel_info = self.__get_category(soup)
        return hotel_info
        # # Sort the hotel_info list based on hotel_rating
        # sorted_hotel_info = sorted(hotel_info, key=lambda x: float(x['hotel_rating']), reverse=True)
        
        # return sorted_hotel_info
        # #return hotel_info







# location = input("Enter Your Location City : ")
# no = int(input("Search for :\n1] Category\n2] Food\nEnter no. : "))

# meal = None
# if no == 1:
#     meal = input("Enter Category : ")
# elif no == 2:
#     meal = input("Enter Food : ")
# else:
#     print("Invalid No Entered! Exiting...")
#     exit(0)


# dish  = Swiggy(meal, location)


# if no == 1:
#     hotel_info = dish.get_category_dishes()
    
# else:
    ... # Hotels First Dish



'''
Dish -
    Price
    Rating
    Distance

id | Price | Rating | Distance(Optional) | Score(Labelled Data) 

'''
