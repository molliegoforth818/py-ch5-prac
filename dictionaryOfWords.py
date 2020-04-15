# Create an empty dictionary
# animal = dict()
# Add k/v pairs
# animal["name"] = "Kevin"
# animal["breed"] = "Bulldog"
# animal["age"] = 5

# for (key, value) in animal.items():
#     print(f"{key}: {value}")

# Output
# name: Kevin
# breed: Bulldog
# age: 5

# Create the dictionary with k/v pairs and assign to variable
animal = {
    "name": "Kevin",
    "breed": "Bulldog",
    "age": 5
}

"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()
word_definitions ["periodt"]= "and thats on what",
word_definitions ["hypnagogic"]="relating to or occurring in the period of drowsiness immediately preceding sleep",
word_definitions ["miracle"]="won't the lord do it",
word_definitions ["power"]="lets hope the spinoffs are good"

word_definitions = {
    "periodt": "and thats on what",
    "hypnagogic": "relating to or occurring in the period of drowsiness immediately preceding sleep",
    "miracle": "wont the lord do it",
    "power": "lets hope the spinoffs are good"
}

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["miracle"]="wont the lord do it , amen"
word_definitions["periodt"]="and that is on what ladies"

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
# print(word_definitions["periodt"])
# print(word_definitions["hypnagogic"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for (key, value) in word_definitions.items():
    print(f"The definition of {key} is {value}")

# print(word_definitions)

