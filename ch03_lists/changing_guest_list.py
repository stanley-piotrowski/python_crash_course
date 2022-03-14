# Exercise 3-5 ----
# Build off of exercise 3-4 guest_list.py and replace the name of each person that can't name it with someone else
guests = ['gandalf the grey', 'aragorn, son of arathorn', 'gimli, son of gloin']
print('Original guest list:')
for i in range(len(guests)):
    print(guests[i])

# Define guests that can't make it
busy_guests = ['gandalf the grey', 'gimli, son of gloin']
print('\nThe following guests can no longer attend:')
for i in range(len(busy_guests)):
    print(busy_guests[i])

# Remove busy guests
for i in range(len(busy_guests)):
    guests.remove(busy_guests[i])

# Define new guests
new_guests = ['legolas, of the woodland realm', 'boromir, son of denethor']
print('\nThe following new guests will take their places:')
for i in range(len(new_guests)):
    print(new_guests[i])

# Add new guests to the original list
for i in range(len(new_guests)):
    guests.append(new_guests[i])

# Print updated guest list
print('\nBelow is the updated guest list')
for i in range(len(guests)):
    print(guests[i])

