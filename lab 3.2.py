#LAB 21
#Transpose with Zip
#Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. There's actually a cool trick for this!.
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
data_transpose = tuple(zip(*data))
print(data_transpose)

#LAB 22
#Unzip Tuples
#Unzip the cast tuple into two names and heights tuples.

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
# define names and heights here
names, heights = zip(*cast)
print(names)
print(heights)

#LAB 23
#Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:
#names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#should create 
#usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]
#HINT: Use the .replace() method to replace the spaces with underscores. Check out how to use this method in this: 
#https://stackoverflow.com/a/12723785
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []
# write your for loop here
for name in names:
    usernames.append(name.lower().replace(" ", "_"))
print(usernames)

#LAB 24
#Modify Usernames with Range
#Write a for loop that uses range() to iterate over the positions in usernames to modify the list. Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores. After running your loop, this list

#usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

#should change to this:

#usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
names = []
# write your for loop here
for name in names:
    usernames = name.lower().replace(" ","_")
print(usernames)

#LAB 25
#Practice: Which Prize
#Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points.

#Points	Prize
#1 - 50	wooden rabbit
#51 - 150	no prize
#151 - 180	wafer-thin mint
#181 - 200	penguin
#All of the lower and upper bounds here are inclusive, and points can only take on positive integer values up to 200.

#In your if statement, assign the result variable to a string holding the appropriate message based on the value of points. If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. If there's no prize, the message should state "Oh dear, no prize this time."

#Note: Feel free to test run your code with other inputs, but when you submit your answer, only use the original input of points = 174. You can hide your other inputs by commenting them out.
points = 174  # use this input to make your submission
# write your if statement here
points = 174  # use this input to make your submission
# write your if statement here

if points >= 1 and points <= 50:
    a = "wooden rabbit"
elif points > 50 and points <= 150:
    a = "no prize"
elif points > 150 and points <= 180:
    a = "wafer-thin mint"
elif points > 180 and points <= 200:
    a = "penguin"
else :
    a = "... Oh dear, no prize this time!"

result = "Congratulations! You won a {}".format(a)
print(result)

#LAB 26
#Count By
#Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num. Use break_num as the variable that you'll change each time through the loop. For simplicity, assume that end_num is always larger than start_num and count_by is always positive.
#Before the loop, what do you want to set break_num equal to? How do you want to change break_num each time through the loop? What condition will you use to see when it's time to stop looping?
#After the loop is done, print out break_num, showing the value that indicated it was time to stop looping. It is the case that break_num should be a number that is the first number larger than end_num.
start_num = 1#provide some start number
end_num = 100 #provide some end number that you stop when you hit
count_by = 2 #provide some number to count by 
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
break_num = start_num
while break_num < end_num:
    break_num += count_by
print(break_num)

#LAB 27
#Count By Check
#Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num, and calculate break_num the way you did in the last quiz.

#Now in addition, address what would happen if someone gives a start_num that is greater than end_num. If this is the case, set result to "Oops! Looks like your start value is greater than the end value. Please try again." Otherwise, set result to the value of break_num.


start_num = 5 #provide some start number
end_num = 100 #provide some end number that you stop when you hit
count_by = 2 #provide some number to count by 
# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
if start_num > end_num:
    result="Oops! Looks like your start value is greater than the end value. please try again"
else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by
        result = break_num
print(result)

#LAB 28
#Tag Counter
#Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable count.

#You can assume that the list of strings will not contain empty strings.


tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token.startswith("<") and token.endswith(">"):
        count += 1
print(count)

#LAB 29
#Zip Coordinates
#Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it to the list points. Each string should be formatted as label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4.
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point)) 

for point in points:
    print(point)

#LAB 30
#Zip Lists to a Dictionary
#Use zip to create a dictionary cast that uses names as keys and heights as values.

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))

print(cast)


