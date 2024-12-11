def organizeInventory(inventory):
    output = {}

    for toy in inventory:
        category = toy["category"]
        toy_name = toy["name"]
        quantity = toy["quantity"]

        if category not in output:
            output[category] = {}

        if toy_name in output[category]:
            output[category][toy_name] += quantity
        else:
            output[category][toy_name] = quantity

    return output

"""
{
  toys: {
    doll: 5,
    car: 5
  },
  sports: {
    ball: 2,
    racket: 4
  }
}
"""
print(organizeInventory([
  { "name": "doll", "quantity": 5, "category": "toys" },
  { "name": "car", "quantity": 3, "category": "toys" },
  { "name": "ball", "quantity": 2, "category": "sports" },
  { "name": "car", "quantity": 2, "category": "toys" },
  { "name": "racket", "quantity": 4, "category": "sports" }
]))
