names = ["umar", "Asjad", "Hassan", "Arsalan", "Rehan"]

# Print each name by accessing each element in the list
for name in names:
    print(name)

for name in names:
    print(f"Hello, {name}! Hope you're having a great day!")



transportations = ["Tesla Model S", "Harley-Davidson motorcycle", "Yamaha jet ski", "Boeing 787 Dreamliner"]

# Print a series of statements about these items
for transportation in transportations:
    print(f"I would like to own a {transportation}.")


    dinner_guests =  ["umar", "Asjad", "Hassan", "Arsalan", "Rehan"]

# Print a personalized invitation for each person in the list
for guest in dinner_guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")



unable_to_attend = "Asjad"
print(f"\nUnfortunately, {unable_to_attend} can't make it to dinner.")

# Replace the guest who can't make it with a new person
dinner_guests[dinner_guests.index(unable_to_attend)] = "Zubair"

# Print the updated invitations
print("\nUpdated invitations:")
for guest in dinner_guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")





#3.6--------------

# Initial list of people to

# Print the initial invitations
for guest in dinner_guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")

# Inform about finding a bigger table
print("\nGood news! I found a bigger table.")

# Add new guests
dinner_guests.insert(0, "Ada Lovelace")  # Add to the beginning
dinner_guests.insert(len(dinner_guests) // 2, "Nikola Tesla")  # Add to the middle
dinner_guests.append("Stephen Hawking")  # Add to the end

# Print the updated invitations
print("\nUpdated invitations:")
for guest in dinner_guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")


#3.7  


# Initial list of people to invite to dinner


# Print the initial invitations
print("Initial invitations:")
for guest in dinner_guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")

# Inform that only two people can be invited
print("\nUnfortunately, I can only invite two people for dinner.")

# Remove guests one by one until only two remain
while len(dinner_guests) > 2:
    removed_guest = dinner_guests.pop()
    print(f"I'm sorry, {removed_guest}, but I can't invite you to dinner.")

# Print the final invitations for the remaining guests
print("\nFinal invitations:")
for guest in dinner_guests:
    print(f"Dear {guest}, you are still invited to dinner.")

# Remove the last two names from the list
del dinner_guests[:]

# Print the list to ensure it is empty
print("\nThe final guest list is:", dinner_guests)







# List of places I'd like to visit
places_to_visit = ["Tokyo", "New York", "Paris", "Sydney", "Cape Town"]

# Print the list in its original order
print("Original list:", places_to_visit)

# Use sorted() to print the list in alphabetical order without modifying the actual list
print("Alphabetical order:", sorted(places_to_visit))

# Show that the list is still in its original order by printing it again
print("Original list after sorted():", places_to_visit)

# Use sorted() to print the list in reverse-alphabetical order without changing the original list
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

# Show that the list is still in its original order by printing it again
print("Original list after reverse sorted():", places_to_visit)

# Use reverse() to change the order of the list
places_to_visit.reverse()
print("List after reverse():", places_to_visit)

# Use reverse() to change the order of the list again
places_to_visit.reverse()
print("List after reverse() again:", places_to_visit)

# Use sort() to change the list so it's stored in alphabetical order
places_to_visit.sort()
print("List after sort():", places_to_visit)
