#imports
from bs4 import BeautifulSoup
import requests

'''
This is the Webscrapper for Casual Laptops
'''

#main

pg = "1" #Defining initial page variable
#Defining the url variable which is a formatted string that will relocate to separate webpages as the pg variable is altered
url = f"https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={pg}" 
page = requests.get(url)        #Gettting the HTML requests
soup = BeautifulSoup(page.content, 'html.parser')       #Producing the HTML Soup
panel = soup.find('div', class_= "_1YokD2 _2GoDe3")     #Producing a panel soup which allocates only to a specific panel in the webpage, that holds the product details
total_pages = panel.find('div', class_= "_2MImiq").findChild().get_text()[10:]      #Finding the total number of pages of the search result "laptops" on Flipkart

'''
Important Functions
'''
def str_to_flt(s):
    '''Takes input string with commas and other symobols and converts into computer readable float point'''
    s_  = ''
    for i in s:
        if i.isdigit():
            s_+=i
        elif i == '.':
            s_+= i
        if i.isalpha():
            break
    s_ = float(s_)
    return s_

def object_crawler(obj_list):
    '''Crawls through every object in the given list, extracts title, price, stars, ratings and discounts and stores it as a dictionary. THis dictionary is appended onto the output list'''
    outl = []       #output List
    for obj in obj_list:
        d = {}      #Object Dictionary
        if obj.find('div', class_="_4rR01T"):       #Checks if the title is available 
            d["Title"] = obj.find('div', class_="_4rR01T").get_text()   #"_4rR01T" class holds the titles
            
            d["Price"] = str_to_flt(obj.find('div', class_="_30jeq3 _1_WHN1").get_text())   #"_30jeq3 _1_WHN1" class holds the price
            
            if obj.find('div', class_="_3LWZlK"):       #Checks if stars are available
                d["Stars"] = str_to_flt(obj.find('div', class_="_3LWZlK").get_text())
            else:
                d["Stars"] = 0.0
            
            if obj.find('span', class_="_2_R_DZ"):      #Checks if ratings are available
                d["Ratings"] = int(str_to_flt(obj.find('span', class_="_2_R_DZ").get_text()))
            else:
                d["Ratings"] = 0
            
            if obj.find('div', class_ = "_3Ay6Sb"):     #Checks if discount is available
                d["Discount"] = obj.find('div', class_ = "_3Ay6Sb").get_text()
            else:
                d["Discount"] = "0% off"
            
            outl.append(d)
    
    return outl


'''data extraction'''

casual_laptop_list = []     #List that holds all the laptops data in form of dictionaires

for i in range(1, int(total_pages)+1):
    #Producing Soup
    url = f"https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={str(i)}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    panel = soup.find('div', class_= "_1YokD2 _2GoDe3")
    #Finding all products
    cl_objects = panel.findAll('div', class_ = "_1AtVbE col-12-12")
    #Scanning through every object in cl_objects using Object Crawler
    mini_l = object_crawler(cl_objects)
    casual_laptop_list.extend(mini_l)
    #Creating a breakpoint to cap total number of products analyzed. Done to speed up the program
    if len(casual_laptop_list) >= 200:
        break
