###############################################################################
# Done: 1. (2 pts)
#   
#   This module is going to look very similar to other modules that you have
#   done with lists, tuples, and sets, but this time we will use dictionaries
#   instead.
#
#   For this _TODO_, simply create a dictionary called contact that will have a
#   collection of strings that represent different pieces of information that
#   you may have for someone in your contacts. You should use these as your
#   keys (you choose the values):
#       - name
#       - phone
#       - email
#       - address
#
#   Once you have created the dictionary, make sure to print out the
#   dictionary.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

contact = {
    "name": "Olivia",
    "phone": "859-878-9506",
    "email": "liv.noel.18@gmail.com",
    "address": "8200 Evergreen Road, San Francisco, CA 43901"
}
print(contact)

###############################################################################
# Done: 2. (2 pts)
#   
#   For this _TODO_, write a line of code that accesses the "email" item in the
#   dictionary and prints the value.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

print(contact["email"])

###############################################################################
# Done: 3. (2 pts)
#   
#   For this _TODO_, write a line of code that changes the "name" item to a
#   different name. Once you have done this, print the dictionary. Make sure
#   you do NOT create a new dictionary, but actually modify the original.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

contact["name"] = "Lucia"
print(contact)

###############################################################################
# Done: 4. (2 pts)
#   
#   For this _TODO_, write a line of code that adds an item to the dictionary
#   with the key "birthday". Once you have done this, print the dictionary.
#   Make sure you do NOT create a new dictionary, but actually modify the
#   original.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

contact["Birthday"] = "August 18"
print(contact)

###############################################################################
# Done: 5. (2 pts)
#   
#   For this _TODO_, write a line of code that removes the last item that has
#   been added to the dictionary. Once you have done this, print the
#   dictionary. Make sure you do NOT create a new dictionary, but actually
#   modify the original.
#
#   NOTE: Your solution should work no matter what the last added item was, so
#   do NOT us a key value in your solution.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

contact.popitem()
print(contact)

###############################################################################
# Done: 6. (2 pts)
#
#   For this _TODO_, write a line of code that creates a copy of your
#   dictionary. Make sure you create an actual copy of the dictionary and not
#   just a reference to the dictionary. If you don't understand the difference
#   between these two things make sure you look back at the reading.
#
#   Once you have done this, print the copy of the dictionary.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

duplicate_contact = contact.copy()
print(duplicate_contact)