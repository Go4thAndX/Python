# importing the pandas library
import pandas as pd

path_csv_file = "/Python Algemeen\Changing CSV file\Alldetails.csv"

# reading the csv file
csv_file = pd.read_csv(path_csv_file)

# updating the column value/data
csv_file.loc[5, "Name"] = "Koomen"

# writing into the file
csv_file.to_csv(path_csv_file, index=False)

print(csv_file)
