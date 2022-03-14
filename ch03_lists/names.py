# Exercise 3-1 ----
# Store the names of a few friends in a list and print each
friends = ['frodo', 'sam', 'gandalf', 'aragorn']
for i in range(len(friends)):
    message = f'Hello, {friends[i].title()}'
    print(message)
