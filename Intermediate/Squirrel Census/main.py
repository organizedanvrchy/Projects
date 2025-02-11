# Squirrel Census
import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Squirrel Count
gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
cinnamon_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])

# Alternative Approach
# fur_color_list = squirrel_data["Primary Fur Color"].tolist()

# gray_squirrel_count = 0
# cinnamon_squirrel_count = 0
# black_squirrel_count = 0

# for color in fur_color_list:
#     if color == "Gray":
#         gray_squirrel_count += 1
#     if color == "Cinnamon":
#         cinnamon_squirrel_count += 1
#     if color == "Black":
#         black_squirrel_count += 1

print(gray_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

squirrel_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrel_count, black_squirrel_count, cinnamon_squirrel_count]
}

overall_squirrel_count = pd.DataFrame(squirrel_dict)
overall_squirrel_count.to_csv("squirrel_count.csv")
