import pandas as pd


def update_csv_file_data_money(path, coins):
    file = pd.read_csv(path)
    value = int(file.loc[0, "Amount"])
    value = value + coins
    # updating the column value/data
    file.loc[0, "Amount"] = str(value)
    # writing into the file
    file.to_csv(path_csv_file, index=False)
    return file


coins_quarter = 4
path_csv_file = "G:\Mijn Drive\GoogleMap Python\Python Udemy\Projects\Project Coffee Machine\data_money.csv"
csv_file = update_csv_file_data_money(path=path_csv_file, coins=coins_quarter)
print(csv_file)