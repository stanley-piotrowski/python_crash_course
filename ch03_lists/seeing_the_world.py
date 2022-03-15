# seeing_the_world.py ----
# The purpose of this exercise is to create a list of five places you want to visit and used different functions and methods to modify the list
places = ['belize', 'thailand', 'japan', 'italy', 'columbia']
print(f'Original order: {places}\n')

# Print list in alphabetical order without modifying the original list
sorted_places = sorted(places)
print(f'Sorted order: {sorted_places}')
print(f'Original order: {places}\n')

# Reverse the order
places.reverse()
print(f'Reverse order: {places}')
print(f'Original order: {places}\n')

# Change back to the original order
places.reverse()
print(f'Double reverse order: {places}')
print(f'Original order: {places}\n')

# Sort in place
places.sort()
print(f'Sorted order: {places}')
print(f'Original list: {places}\n')

# Sort in place in reverse alphabetical order
places.sort(reverse=True)
print(f'Sorted, reverse order: {places}')
print(f'Original list: {places}\n')