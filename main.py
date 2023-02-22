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

# Main Routine
want_instructions = yes_no("Do you want instructions? (yes/no) ").lower()

if want_instructions == "yes":
  print("Instructions go here")

print("We are done")