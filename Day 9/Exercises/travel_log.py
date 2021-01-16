travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
  new_item = {}
  new_item['country'] = country
  new_item['visits'] = visits
  new_item['cities'] = cities
  travel_log.append(new_item)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



