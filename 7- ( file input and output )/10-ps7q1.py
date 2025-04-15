# create a new file "practice.txt" using python. add the following data in it:
# hii everyone
# we are learning file input and output
# using java
# i like programming in java

f = open("practice.txt", "w")
f.write("hii everyone \nwe are learning file input and output \nusing java \ni like programming in java")


# second method

# with open("practice.txt", "w") as f:
#     f.write("hii everyone\nwe are learning file input and output \nusing java\ni like programming in java")