# Define a function called linear_search_product
def linear_search_product(products, target):
  # Initialize an empty list to store the indices of the target product
  indices = []
  # Loop through the list of products
  for i in range(len(products)):
    # If the current product matches the target product
    if products[i] == target:
      # Append the index to the indices list
      indices.append(i)
  # Return the indices list
  return indices

# Example list of products
products = ["apple", "banana", "orange", "mango", "apple", "grape", "apple"]

# Example target product
target = "apple"

# Call the function and print the result
result = linear_search_product(products, target)
print(result)