import pandas


def currency(x):
  pass


all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0.53, 0]

mini_movie_dict = {
  "Name": all_names,
  "Ticket Price": all_ticket_costs,
  "Surcharge": surcharge
}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculating ticket cost
mini_movie_frame[
  "Total"] = mini_movie_frame["Surcharge"] + mini_movie_frame["Ticket Price"]

# Calculating profit (surcharge not included in profit)
mini_movie_frame["Profit"] = mini_movie_frame["Ticket Price"] - 5

total = mini_movie_frame["Total"].sum()
profit = mini_movie_frame["Profit"].sum()

print(mini_movie_frame)

print(f"Total Ticket Sales: ${total}")
print(f"Total Profit: ${profit}")
