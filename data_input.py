import os
import pandas as pd

#Class for inputing data in the program via .csv files.
#The csv file must have the first line with the headers of the data you want to input in the program

class Data_input():

    def __init__(self, inputter_name : str) -> None:
        self.inputter_name = inputter_name

    def inputter(self):
        with open(self.inputter_name,"r") as file:
            csv_headers = file.readlines()
            if csv_headers[0][-1] !="\n":
                csv_headers = csv_headers[0] + "\n"
            else:
                csv_headers = csv_headers[0]

        headers = pd.read_csv(self.inputter_name).columns.tolist()
        values = ""

        for count, header in enumerate(headers):
            if count == 0:
                values += input(f"Input the {header} reading: ").replace(" ","")
            else:
                values += "," + input(f"Input the {header} reading: ").replace(" ","").replace(",",".")

        temp_file_name = self.inputter_name.replace(".csv","") + "_temp.csv"

        with open(temp_file_name,"w") as file:
            file.write(csv_headers)
            file.write(values)
        
        data_frame = pd.read_csv(temp_file_name)

        if os.path.exists(temp_file_name):
            #os.remove(temp_file_name)
            print("hi")
        print(data_frame)

m = Data_input("electricity_input.csv")
m.inputter()
        