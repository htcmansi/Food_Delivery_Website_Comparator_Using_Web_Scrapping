import requests

class ZomatoFoodId:
    def __init__(self) -> None:
        self.endpoint = "https://www.zomato.com/webroutes/search/autoSuggest?addressId=0&entityId=2121&entityType=subzone&locationType=&isOrderLocation=0&cityId=3&latitude=19.077&longitude=72.877&userDefinedLatitude=19.0759837&userDefinedLongitude=72.8776559&entityName=Mumbai,%20Maharashtra,%20India,%20India&orderLocationName=Mumbai,%20Maharashtra,%20India,%20India&cityName=Mumbai&countryId=1&countryName=India&displayTitle=Mumbai,%20Maharashtra,%20India,%20India&o2Serviceable=true&placeId=10575&cellId=4316639276847595520&deliverySubzoneId=10575&placeType=DSZ&placeName=Mumbai,%20Maharashtra,%20India,%20India&isO2City=true&fetchFromGoogle=true&fetchedFromCookie=true&&isO2OnlyCity=false&addressBlocker=0&&otherRestaurantsUrl=&q="
        self.endpoint_extended = "&context=delivery"
        self.headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
        }

    def get_id(self, meal):
        endpoint = self.endpoint + meal.replace(' ','%20') + self.endpoint_extended
        response = requests.get(endpoint, headers=self.headers)

        data = response.json()

        for result in data['results']:
            if("Delivery" in result['info']['name']):
                return result['entityId']
        


if __name__ == '__main__':
    test = ZomatoFoodId()
    print(test.get_id("pizza"))