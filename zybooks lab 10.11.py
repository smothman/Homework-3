#Sam Othman
#1991756
class FoodItem:
# Defined a constructor which accepts attributes (name, fat, carbs, protein)
    def __init__(self, item_name="None", amount_fat=0.0, amount_carbs=0.0, amount_protein=0.0):
        self.name = item_name
        self.fat = amount_fat
        self.carbs = amount_carbs
        self.protein = amount_protein
#Defined the function to calculate the calories and return them.
    def get_calories(self, num_servings):
# Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories
#Defined the function to print the Nutritional info of the food
    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print(' Fat: {:.2f} g'.format(self.fat))
        print(' Carbohydrates: {:.2f} g'.format(self.carbs))
        print(' Protein: {:.2f} g'.format(self.protein))
#Defined the main function
if __name__ == "__main__":
#Create a food item named food_item2 using the input values
    item_name = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())
    num_servings = float(input())
    food_item2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
#Create a food item named food_item1 using the default values
    food_item1 = FoodItem()
#Printing the food info by calling the methods defined in the function.
    food_item1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}\n'.format(num_servings,
    food_item1.get_calories(num_servings)))
    food_item2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,
                        food_item2.get_calories(num_servings)))