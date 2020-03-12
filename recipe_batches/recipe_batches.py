#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = []
  if len(recipe) > len(ingredients):
    return 0
  else:
    for item, need in recipe.items():
      for item2, available in ingredients.items():
        if item == item2:
          batches.append(available // need)
    
  return min(batches)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  # day 2
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))