# Exercise 2-7 ----
# The goal of this exercise is to strip whitespace (tab, newline, or spaces) from a name before printing
name = " Tom Bombadillo\t\n"
print("Full name: ", name)
print("Left strip: ", name.lstrip())
print("Right strip: ", name.rstrip())
print("Both strip: ", name.strip())