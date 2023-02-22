# Function
def yes_no(question):

  while True:
    response = input(question).lower()

    if response == "yes" or response == "y":
      return "yes"
    elif response == "no" or response == "n":
      return "no"
    else:
      print("Please enter yes or no")


def not_blank(question):

  while True:
    response = input(question)

    if response == "":
      print("Sorry, your name can't be blank. Please try again")
    else:
      return response


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

  tickets_sold += 1

if tickets_sold == MAX_TICKETS:
  print("Congratulations, you have sold all the tickets.")
else:
  print(
    f"You have sold {tickets_sold} ticket's. There is {MAX_TICKETS - tickets_sold} ticket's remaining."
  )
