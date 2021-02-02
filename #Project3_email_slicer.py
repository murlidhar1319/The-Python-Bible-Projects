'''
# string slicing

variable[start:end:step]   #concept


'''

# take email input 
print('enter your email address; ')   #if needed use .strip()
email=input()

# slice into username and domainname
username=email[ :email.index('@')]
domainname=email[email.index('@') + 1: ]

# # show output 
# print('your username is; ', username)
# print('your domain name is; ', domainname)

# using .format() function
output="your username is, '{}' and your domain name is, '{}'".format(username, domainname)
print(output)
