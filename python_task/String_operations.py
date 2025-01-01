''' Email given - ilearniexcel@gmail.com
task 1 - find the position of @
task 2 - extract only .com from the email string
task 3 - extrct only gmail from the email string
'''

email = 'ilearniexcel@gmail.com'
# task 1
print(email.find('@')+1)
# task 2
print(email[-4:])
# task 3
print(email[11:16])
