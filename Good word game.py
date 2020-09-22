import random

#Find the good word
space_theme = (
    "rocket", "stars", "shuttle", "sun", "planet", "system", "asteroid"
)

car_theme = (
  "gasoline", "steering wheel", "rearview mirror", "hood", "key", "horses"
)

choosen_theme = input("Choose your theme (Space, Car) : ")

if choosen_theme.lower() == "space":
  choosed_theme = space_theme
elif choosen_theme.lower() == "car":
  choosed_theme = car_theme
else:
  print("Please choose a theme in the list")

random_word = random.choice(choosed_theme)

lifes = 10

while lifes > 0:
  your_word = input("What's your word ? : ")

  if random_word.lower() != your_word.lower():
    print("Nop try again")
    lifes -= 1
  else:
    print("Good job !")
    break
else:
  print("No more life")
