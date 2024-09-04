import requests
import json
from bs4 import BeautifulSoup
from Zomato.id import ZomatoFoodId

class Zomato:
    def __init__(self, dish, location) -> None:
        self.url = f"https://www.zomato.com/{location.casefold()}/delivery?dishv2_id="
        self.meal = dish
        self.idObj = ZomatoFoodId()
        self.headers ={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
    
    def __extract_json_data(self, soup):
        body = soup.find('body')
        script_tag = body.find("script")

        if script_tag:
            json_string = script_tag.text.strip().replace("window.__PRELOADED_STATE__ = JSON.parse(","").replace('");',"\"")
            data = json.loads(json_string)
            data = json.loads(data)
            return data
        else:
          print("Script tag with JSON.parse not found.")
          return None
            
    def get_hotel_data(self):
        food_id = self.idObj.get_id(self.meal)
        food_id = 68987
        url = self.url + str(food_id)
        response = requests.get(url,headers=self.headers)
        hotel_data = []

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            data = self.__extract_json_data(soup)
            hotels = data["pages"]["search"][next(iter(data["pages"]["search"]))]["sections"]["SECTION_SEARCH_RESULT"]

            for hotel in hotels:
                htl = {
                    "hotel_name": hotel["info"]["name"],
                    "hotel_rating": hotel["info"]["rating"]["rating_text"],
                    "hotel_distance": hotel["distance"],
                    "hotel_url": "https://zomato.com/"+hotel["order"]["actionInfo"]["clickUrl"]
                }
                hotel_data.append(htl)
            hotel_data.append("zomato")
            return hotel_data


if __name__ == '__main__':
    test = Zomato("pizza", "pune")
    print(test.get_hotel_data())
    