import csv
import pandas as pd
import matplotlib.pyplot as plt

def store(choice):

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
    data = []
    with open('ObjectData.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            data.append(row)
    return data

def desc(pmax, rmin):
    df = pd.read_csv('ObjectData.csv')
    rdf = df.loc[(df["Price"]<=pmax) & (df["Ratings"]>=rmin)]
    a = str(rdf.describe())
    return a

def plot(pmax, rmin):
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