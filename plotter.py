import csv
import pandas as pd
import matplotlib.pyplot as plt

'''
This file contains functions which 
-Store scrapped data in ObjectData.csv
-Read data from the csv and store it as a list
-Extract filtered data and analyze it
-Plot filtered data scatter
'''
def store(choice):
    '''This function stores extracted data in a csv by running the required scraper and importing the data list generated'''
    with open('ObjectData.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Price", "Stars", "Ratings", "Discount"])
        if choice == 1:
            from GamingLaptopScraper import gaming_laptop_list
            for i in range(len(gaming_laptop_list)):
                writer.writerow(list(gaming_laptop_list[i].values()))
        elif choice == 2:
            from CasualLaptopScrapper import casual_laptop_list
            for i in range(len(casual_laptop_list)):
                writer.writerow(list(casual_laptop_list[i].values()))
        elif choice == 3:
            from MobileScrapper import mobile_list
            for i in range(len(mobile_list)):
                writer.writerow(list(mobile_list[i].values()))

def read():
    '''This function reads the data from the csv and stores it as a list of lists.'''
    data = []
    with open('ObjectData.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            data.append(row)
    return data

def desc(pmax, rmin):
    '''This function filters the extracted data based on prices and ratings and produces an analysis of the data'''
    df = pd.read_csv('ObjectData.csv')
    rdf = df.loc[(df["Price"]<=pmax) & (df["Ratings"]>=rmin)]
    a = str(rdf.describe())
    return a

def plot(pmax, rmin):
    '''This function plots a Ratings-Price Scatter based on filtered data extracted from the CSV'''
    df = pd.read_csv('ObjectData.csv')
    rdf = df.loc[(df["Price"]<=pmax) & (df["Ratings"]>=rmin)]
    plt.style.use('seaborn')
    prices = rdf["Price"]
    ratings = rdf["Ratings"]
    plt.scatter(prices, ratings, s=100, alpha=0.6, edgecolor='black', linewidth=1)
    plt.title("Ratings vs Prices")
    plt.xlabel("Prices")
    plt.ylabel("Ratings")
    plt.show()