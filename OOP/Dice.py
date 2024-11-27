# import random

# class Dice:
#     def roll(self):
#         first=random.randint(1,6)
#         second=random.randint(1,6)
#         tup=(first,second)
#         return tup

# obj=Dice()
# print(obj.roll())


from pathlib import Path
path=Path()

for i in path.glob("*.py"):
    print(i)

