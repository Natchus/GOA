user_data={
    "name":"Natalia",
    "age":15,
    "city":"Tbilisi"
}
user_name=user_data["name"]
user_data["city"]="Paris"
city_popped=user_data.pop("city")
user_values=user_data.values()

for key,value in user_data.items():
    print(key,value)