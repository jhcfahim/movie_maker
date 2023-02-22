want_instructions = input("Do you want instructions? (yes/no) ").lower()
if want_instructions == "yes" or want_instructions == "y":
  print("Instructions go here")
elif want_instructions == "no" or want_instructions == "n":
  pass
else:
  print("Please enter yes or no")