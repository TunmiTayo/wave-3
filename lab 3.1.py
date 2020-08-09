#LAB 11
#Factorials with For Loops
#Now use a for loop to find the factorial!
#It will now be great practice for you to try to revise the code you wrote above to find the factorial of a number, but this time, using a for loop. Try it in the code editor below!
# number to find the factorial of
number = 6   
# start with our product equal to one
product = 1
# write your for loop here
for num in range(2, number+1):
    product*=num
# print the factorial of number
print(product)

#LAB 12
#Filter Names by Scores
#Use a list comprehension to create a list of names passed that only include those that scored at least 65.

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name,score in scores.items() if score >= 65 ]# write your list comprehension here
print(passed)

#LAB 13
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line

#LAB 14
# Write a for loop using range() to print out multiples of 5 up to 30 inclusive
for number in range(5,35,5):
    print(number)

#LAB 15
#Create an HTML List
#Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list. For example, if the list is items = ['first string', 'second string'], printing html_str should output:

#<ul>
#<li>first string</li>
#<li>second string</li>
#</ul>
#That is, the string's first line should be the opening tag <ul>. Following that is one line per element in the source list, surrounded by <li> and </li> tags. The final line of the string should be the closing tag </ul>.
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str +="</ul>"

print(html_str)

#LAB 16
#Multiples of Three
#Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.

multiples_3 = [i * i for i in range(20)] # write your list comprehension here
print(multiples_3)

#LAB 17
#Nearest Square
#Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.
#For example, if limit is 40, your code should set the nearest_square to 36.

limit = 40
num = 0
# write your while loop here
while (num +1)**2 < limit:
    num += 1
    nearest_square = (num)**2
print(nearest_square)

#LAB 18
# '''
# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = 'CA'
purchase_amount = 21 #amount of purchase
if  state == 'CA':
     tax_amount = .075
     total_cost = purchase_amount*(1+tax_amount)
result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

if state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

if state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)

#LAB 19
# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.
# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 20
guess = 10
if guess <answer:
    result = "Oops!  Your guess was too low."
elif guess <answer:
    result = "Oops!  Your guess was too high."
elif guess <answer:
    result = "Nice!  Your guess matched the answer!"
print(result)

#LAB 20
#Break the String
#Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

#Remember that break works in both for and while loops. Use whichever loop seems most appropriate. Consider adding print statements to your code to help you resolve bugs.

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for i in headlines:
    news_ticker += i + " "
    if len(news_ticker)>140:
        news_ticker = news_ticker[:140]
        break
print(news_ticker)

