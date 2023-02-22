# Function
def yes_no(question): # response for instructions

  while True:
    response = input(question).lower()

    if response == "yes" or response == "y":
      return "yes"
    elif response == "no" or response == "n":
      return "no"
    else:
      print("Please enter yes or no")


def not_blank(question): # makes sure name can't be empty

  while True:
    response = input(question)

    if response == "":
      print("Sorry, your name can't be blank. Please try again")
    else:
      return response


def num_check(question): # checks that user puts in an integer for age

  while True:

    try:
      response = int(input(question))
      return response

    except ValueError:
      print("Please enter an integer.")


# Main Routine
want_instructions = yes_no("Do you want instructions? (yes/no) ").lower()

if want_instructions == "yes":
  print("Instructions go here")

print("We are done")

# Ticket Looping
MAX_TICKETS = 3
tickets_sold = 0

while tickets_sold < MAX_TICKETS:
  name = not_blank("Please enter your name or 'xxx' to quit: ")
  if name == "xxx":
    break

  age = num_check(("Age: "))
  if 12 <= age <= 120:
    pass
  elif age < 12:
    print("Sorry you are too young for this movie.")
    continue
  else:
    print("Please try again.")
    continue

  tickets_sold += 1

if tickets_sold == MAX_TICKETS:
  print("Congratulations, you have sold all the tickets.")
else:
  print(
    f"You have sold {tickets_sold} ticket's. There is {MAX_TICKETS - tickets_sold} ticket's remaining."
  )
