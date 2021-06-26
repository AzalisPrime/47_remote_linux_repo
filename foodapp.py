# repeat usages in one runtime with main as nested give functional error
# due to how nested functions are set up in workflow
# the txt files update after the subsequent enquiry concerning the same
# updated code after that but still repeats in a single runtime present the same errors

raw = open("raw.txt", "a")
cook = open("cook.txt", "a")
rawList = []
cookList = []
with open("raw.txt", "r") as readerRaw:
    for line in readerRaw.readlines():
        rawList.append(line)
with open("cook.txt", "r") as readerCook:
    for line in readerCook.readlines():
        cookList.append(line)


def add_veg():
    new_veg = input("Enter new vegetable: ")
    raw.write("{}\n".format(new_veg))
    check = input("Add more?(y/n): ")
    if check == "y":
        add_veg()


def add_dish():
    dish_no = ""
    check = "y"
    while check == "y":
        ingredient = input("Enter new ingredient: ")
        pos = rawList.index(ingredient + "\n")
        dish_no += str(pos)
        check = input("Enter another ingredient?(y/n): ")
    dish_name = input("Enter dish name: ")
    dish_no += dish_name
    cook.write("{}\n".format(dish_no))


def suggest_dish():
    dish_no = ""
    check = "y"
    while check == "y":
        ingredient = input("Enter new ingredient: ")
        pos = rawList.index(ingredient + "\n")
        dish_no += str(pos)
        check = input("Enter another ingredient?(y/n): ")
    suggestions = []
    for made_dish in cookList:
        match = 0
        ln_cook = len(made_dish)
        ln_raw = len(dish_no)
        for i in range(0, ln_raw):
            for j in range(0, ln_cook):
                if dish_no[i] == made_dish[j]:
                    match += 1
        if match == ln_raw:
            suggestions.append(made_dish[ln_raw:ln_cook])
    if len(suggestions) == 0:
        print("Sorry, these do not make a dish.")
    else:
        print("Here are the possible dishes: ")
        for suggestion in suggestions:
            print(suggestion)


def main():
    make_lists()
    print("1 to add new veggies \n2 to add a new dish \n3 to check available dishes")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_veg()
    if choice == "2":
        add_dish()
    if choice == "3":
        suggest_dish()
    print("Thank you for using this service.")


main()
raw.close()
cook.close()
