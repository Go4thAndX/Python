import pandas as pd


def update_csv_file_data_resources(path, resources):
    file = pd.read_csv(path)
    for i in range(0, len(resources)):
        value = int(file.loc[i, "Amount"])
        value = value - resources[i]
        file.loc[i, "Amount"] = str(value)
        file.to_csv(path_csv_file, index=False)
    return file


resources_latte = [200, 24, 150]
path_csv_file = "G:\Mijn Drive\GoogleMap Python\Python " \
                "Udemy\Projects\Project Coffee Machine\data_resources.csv"
csv_file = update_csv_file_data_resources(path=path_csv_file,
                                        resources=resources_latte)
print(csv_file)