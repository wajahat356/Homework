#4.1:
pizzas= ['pepperoni', 'cheese', 'broccoli']
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza")

print("\nI really really love pizza!\n")

#4.2
animals= ['dog', 'cat', 'fish']
for animal in animals:
    print(animal.title())
    
for animal in animals:    
    print(f"A {animal.title()} would be a good pet")

print("\nAny of these animals would make awesome pets!")

#4.3
for value in range(1,21):
    print(value)

#8.1
def display_message():
    print("We are learning about functions!\n")

display_message()

#8.2
def favorite_book(answer):
    print(f"One of my favorite books is {answer.title()}")

favorite_book('Wimpy kid')

#8.3
def make_shirt(shirt_size, shirt_text):
    print(f"\nThe size is {shirt_size} and the text is {shirt_text}.")

make_shirt('large', 'nike')
make_shirt(shirt_size ='small', shirt_text='adidas')

#8.4
def make_shirt(shirt_text='I love Python', shirt_size='large'):
    print(f"\nThe size is {shirt_size} and the text is {shirt_text}.")

make_shirt()
make_shirt(shirt_size='medium')
make_shirt(shirt_size='medium', shirt_text='I love Java')

#8.5
def describe_city(city_name, country_name='United States'):
    print(f"\n{city_name} is in {country_name}")

describe_city(city_name='New York')
describe_city(city_name='Houston')
describe_city(city_name='Salvadore', country_name='Brazil')

#8.6
def city_country(nameOfcity, nameOfCountry):
    full_name= f"{nameOfcity}, {nameOfCountry}"
    return full_name.title()

location = city_country('Santiago', 'Chile')
print(location)

address= city_country('Istanbul','Turkey')
print(address)

area= city_country('Moscow','Russia')
print(area)