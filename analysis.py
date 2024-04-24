import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Print the current working directory
current_directory = os.getcwd()
print("Current directory:", current_directory)

# Specify the path to your Excel file
excel_file_path = "fantasygp.xlsx"

#Get scoring data
sheet = "Scoring"
scoring_data = pd.read_excel(excel_file_path, sheet_name=sheet)
print(scoring_data)

#Get scoring data
sheet = "Price"
price_data = pd.read_excel(excel_file_path, sheet_name=sheet)
print(price_data)

#Get conditions data
sheet = "Conditions"
conditions_data = pd.read_excel(excel_file_path, sheet_name=sheet)
print(conditions_data)

#Get drivers data
sheet = "2023 Drivers"
drivers23_data = pd.read_excel(excel_file_path, sheet_name=sheet)
print(drivers23_data)

#Get scoring data
sheet = "2023 Cars"
cars23_data = pd.read_excel(excel_file_path, sheet_name=sheet)
print(cars23_data)