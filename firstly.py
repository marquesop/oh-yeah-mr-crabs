name = "Marquesz"
age = 18
occuaption = "Content Creator"

intrests = [
  "Content Creation",
  "Computer Science",
  "Basketball",
  "Video Games"
]


intro = ("Hi, im ", name ,"i am ", age ,"years old. And i am a", occuaption)


# welcome message inteface
print("Welcome to the Profile Generator!")
print("----------------------------------------------")

print(intro)

print("\nIntrests:")
for intrest in intrests:
  print("-", intrest)
