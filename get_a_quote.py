import csv
import random

# file = open("quotes.jl","r",encoding="utf8")
# line_count = 0


# for line in file:
#     if line !="\n":
#         line_count += 1

# file.close()

# print(line_count)



with open("thomas_sowell_quotes.csv", "r",encoding="utf8") as t_s_quotes:
    csv_reader = csv.reader(t_s_quotes)
    # This skips over the first line in the .csv (author, text)
    next(csv_reader)
    print(random.choice([f"{line[0]} (Thomas Sowell)" for line in csv_reader]))