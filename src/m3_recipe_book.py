###############################################################################
# Done: 1. (6 pts)
#
#   For this _TODO_, we are going to bring together many of the concepts that
#   we have learned.
#
#   We will be creating a basic recipe book where a user can enter a recipe
#   name and some ingredients for each recipe. It should ask the user for more
#   ingredients until the user is done with that recipe's ingredient list.
#   Then, it should prompt them to do another recipe until they are done
#   entering recipes.
#
#   You will use a dictionary for each recipe that has two fields:
#       - name          <-- this is a string
#       - ingredients   <-- this is a set of strings
#
#   As you go, you should add the dictionaries to a list called recipes. So in
#   the end you should have a list of dictionaries.
#   
#   Here is a step-by-step breakdown of how this should work:
#
#       1. Prints "Welcome to Recipe Book!"                                      CHECK
#       2. Prompts the user to enter a recipe name like this:                    CHECK
#           "Please enter a recipe name: "
#          and saves it to the key "name" in a dictionary                        CHECK
#       3. Prompts the user to enter an ingredient like this:                    CHECK
#           "Please enter an ingredient: "
#          and adds it to a set of ingredients
#       4. Repeat step 3 until the user types "end" and then saves the set of    CHECK
#          ingredients to the key "ingredients" in the dictionary.
#       5. Repeat steps 2-4 until the user types "end" and then adds the         Check   
#          dictionary to the list of recipes.
#       6. Prints the list of recipes one recipe at a time (HINT: use a loop     CHECK
#          here)
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

# Functions
def input_recipe_name():
    name = input("Please enter a recipe name: ")
    return name

def input_recipe_ingredient():
    ingredient = input("Please enter an ingredient: ")
    return ingredient
    

#Beginning (Do once)
set_of_ingredients = set()
list_of_recipes = []

print("Welcome to Recipe Book!")


#Loop through recipes
while True:
    name = input_recipe_name()
    if name == "end":
        break

    #Loop through ingredients
    while True:
        ingredient = input_recipe_ingredient()

        if ingredient == "end":
            break
        set_of_ingredients.add(ingredient)
        
    recipe_dictionary = { 
        "name": name,
        "ingredients": set_of_ingredients     
        }

    list_of_recipes.append(recipe_dictionary)


#End (do once)
for x in list_of_recipes:
    print(x)




    
    
###############################################################################
# TODO: 2. EXTRA CREDIT (2 pts)
#
#   For this extra credit _TODO_, try to look into how you could print out the
#   recipes in a better format that is a little easier to read. Your solution
#   should print things on multiple lines. Modify your code above to do this.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
