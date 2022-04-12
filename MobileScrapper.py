#imports
from bs4 import BeautifulSoup
import requests

'''
This is the Webscrapper for Moblies
'''
#main
#Producing the soup, just like the CasualLaptopScraper
pg = "1"
url = f"https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={pg}"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
panel = soup.find('div', class_= "_1YokD2 _2GoDe3")
total_pages = panel.find('div', class_= "_2MImiq").findChild().get_text()[10:]


#important functions
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
    outl = []
    for obj in obj_list:
        d = {}
        if obj.find('div', class_="_4rR01T"):
            d["Title"] = obj.find('div', class_="_4rR01T").get_text()
            
            d["Price"] = str_to_flt(obj.find('div', class_="_30jeq3 _1_WHN1").get_text())
            
            if obj.find('div', class_="_3LWZlK"):
                d["Stars"] = str_to_flt(obj.find('div', class_="_3LWZlK").get_text())
            else:
                d["Stars"] = 0.0
            
            if obj.find('span', class_="_2_R_DZ"):
                d["Ratings"] = int(str_to_flt(obj.find('span', class_="_2_R_DZ").get_text()))
            else:
                d["Ratings"] = 0
            
            if obj.find('div', class_ = "_3Ay6Sb"):
                d["Discount"] = obj.find('div', class_ = "_3Ay6Sb").get_text()
            else:
                d["Discount"] = "0% off"
            
            outl.append(d)
    
    return outl


#data extraction

mobile_list = []

for i in range(1, int(total_pages)+1):
    url = f"https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={str(i)}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    panel = soup.find('div', class_= "_1YokD2 _2GoDe3")
    m_objects = panel.findAll('div', class_ = "_1AtVbE col-12-12")

    mini_l = object_crawler(m_objects)
    mobile_list.extend(mini_l)

    if len(mobile_list) >= 200:
        break
