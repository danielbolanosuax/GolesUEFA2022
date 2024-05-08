from prettytable import PrettyTable

# Create an instance of PrettyTable
swot_table = PrettyTable()

# Define the table columns
swot_table.field_names = ["SWOT Category", "Details"]

# Adding rows to the table with the SWOT data
swot_table.add_row(["Strengths", "High product quality, strong brand recognition"])
swot_table.add_row(["Weaknesses", "High production costs due to organic ingredients"])
swot_table.add_row(["Opportunities", "Expansion into new markets, development of new products"])
swot_table.add_row(["Threats", "Increasing competition, fluctuations in commodity prices"])

# Setting alignment of the columns
swot_table.align["SWOT Category"] = "l"
swot_table.align["Details"] = "l"

# Print the table
print(swot_table)
