from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(
    "/Users/vikasnagare/Desktop/G_DRIVE/scrping/webScarp/CromeD/chromedriver")
driver.get(
    'https://www.wolframalpha.com/input/?i=oxygen')
sleep(30)
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()
soup = BeautifulSoup(res, 'lxml')
box = soup.find_all("section")


print("   --------------     --------")

print(len(box))
final_data = {}
for i in box:
    a = i.find_all("header")
    if(len(a) > 2) or len(a) == 0:
        continue
    headings = i.find_all('h2')[0].text
    if (len((i.find_all("img"))) != 0) and (i.find_all("img"))[0].has_attr('alt'):
        data = (i.find_all("img"))[0]["alt"]
    if headings == "Functional description:":
        final_data["functions"] = data
    if headings == "Alternate names:":
        final_data["Other Names"] = data
    if headings == "Functional categories:":
        final_data["Functional categories:"] = data
    if headings == "Typical number in the human body:":
        final_data["Typical number in the human body:"] = data
    if headings == "Constitutional parts:":
        data = (i.find_all("img"))[0]["alt"]
        data = data.split("|")
        print(data)
        if len(data) >= 3:
            final_data["Constitutional parts:"] = data[0:3]
        else:
            final_data["Constitutional parts:"] = data

    if headings == "Typical physical characteristics:":
        ch = data.split("\n")
        for data in ch:
            d = data.split("|")
            dd = d[0].strip()
            if dd == "mass":
                final_data["size"] = d[1].strip()
            elif dd == "volume":
                final_data["volume"] = d[1].strip()
            elif dd == "length":
                final_data["length"] = d[1].strip()
            elif dd == "width":
                final_data["width"] = d[1].strip()
            elif dd == "weight percentage of total body":
                final_data["weight percentage of total body"] = d[1].strip()

    # animals
    if headings == "Alternate common name:":
        final_data["Other Names"] = data
    if headings == "Alternate scientific names:":
        final_data["Other Names"] = data
    if headings == "Biological properties:":
        ch = data.split("\n")
        for data in ch:
            d = data.split("|")
            dd = d[0].strip()
            if dd == "lifespan":
                final_data["lifespan"] = d[1].strip()
            elif dd == "length":
                final_data["length"] = d[1].strip()
            elif dd == "weight":
                final_data["weight"] = d[1].strip()

    # chemicals
    if headings == "Chemical names and formulas:":
        ch = data.split("\n")
        for data in ch:
            d = data.split("|")
            dd = d[0].strip()
            if dd == "formula":
                final_data["formula"] = d[1].strip()

    if headings == "Basic properties:":
        ch = data.split("\n")
        for data in ch:
            d = data.split("|")
            dd = d[0].strip()
            if dd == "molar mass":
                final_data["mass"] = d[1].strip()
            elif dd == "phase":
                final_data["phase"] = d[1].strip()
            elif dd == "melting point":
                final_data["melting point"] = d[1].strip()
            elif dd == "boiling point":
                final_data["boiling point"] = d[1].strip()
            elif dd == "density":
                final_data["density"] = d[1].strip()

    if headings == "Basic elemental properties:":
        ch = data.split("\n")
        for data in ch:
            d = data.split("|")
            dd = d[0].strip()
            if dd == "symbol":
                final_data["symbol"] = d[1].strip()
            elif dd == "atomic number":
                final_data["atomic number"] = d[1].strip()
            elif dd == "atomic mass":
                final_data["atomic mass"] = d[1].strip()
    if headings == "Thermodynamic properties:":
        ch = data.split("\n")
        for data in ch:
            d = data.split("|")
            dd = d[0].strip()
            if dd == "phase at STP":
                final_data["phase"] = d[1].strip()
            elif dd == "melting point":
                final_data["melting pointr"] = d[1].strip()
            elif dd == "boiling point":
                final_data["boiling point"] = d[1].strip()
    if headings == "Material properties:":
        ch = data.split("\n")
        for data in ch:
            d = data.split("|")
            dd = d[0].strip()
            if dd == "density":
                final_data["density"] = d[1].strip()
            elif dd == "sound speed":
                final_data["sound speed"] = d[1].strip()

    if headings == "Electromagnetic properties:":
        ch = data.split("\n")
        for data in ch:
            d = data.split("|")
            dd = d[0].strip()
            if dd == "color":
                final_data["color"] = d[1].strip()
    if headings == "Reactivity:":
        ch = data.split("\n")
        for data in ch:
            d = data.split("|")
            dd = d[0].strip()
            if dd == "color":
                final_data["color"] = d[1].strip()

    # food
    if headings == "Average nutrition facts:":
        ch = data.split("\n")
        for data in ch:
            d = data.split("|")
            dd = d[0].strip()
            if (dd.find('serving size') != -1):
                final_data["weight"] = dd.split("serving size")[1]
            elif (dd.find('total calories') != -1):
                final_data["calories"] = dd.split("total calories")[1]
            elif (dd.find('total fat') != -1):
                final_data["fat"] = dd.split("total fat")[1]
            elif (dd.find('cholesterol') != -1):
                final_data["cholesterol"] = dd.split("cholesterol")[1]
            elif (dd.find('sugar') != -1):
                final_data["sugar"] = dd.split("sugar")[1]
            elif (dd.find('sodium') != -1):
                final_data["sodium"] = dd.split("sodium")[1]
            elif (dd.find('phosphorus') != -1):
                final_data["phosphorus"] = dd.split("phosphorus")[1]
            elif (dd.find('zinc') != -1):
                final_data["zinc"] = dd.split("zinc")[1]
            elif (dd.find('vitamin A') != -1):
                final_data["vitamin A"] = dd.split("vitamin A")[1]

            elif (dd.find('vitamin E') != -1):
                final_data["vitamin E"] = dd.split("vitamin E")[1]

            elif (dd.find('vitamin B6') != -1):
                final_data["vitamin B6"] = dd.split("vitamin B6")[1]
        break
# print(final_data)

for i in final_data:
    print(i, "   =   ", final_data[i])


'''from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(
    "/Users/vikasnagare/Desktop/G_DRIVE/scrping/webScarp/CromeD/chromedriver")
driver.get(
    'https://www.wolframalpha.com/input/?i=papaya')
sleep(30)
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()
soup = BeautifulSoup(res, 'lxml')
box = soup.find_all("section")


print("   --------------     --------")

print(len(box))
final_data = {}
for i in box:
    a = i.find_all("header")
    if(len(a) > 2) or len(a) == 0:
        continue
    headings = i.find_all('h2')[0].text
    if (len((i.find_all("img"))) != 0) and (i.find_all("img"))[0].has_attr('alt'):
        data = (i.find_all("img"))[0]["alt"]
    if headings == "Functional description:":
        final_data["functions"] = data
    if headings == "Alternate names:":
        final_data["Other Names"] = data
    if headings == "Functional categories:":
        final_data["Functional categories:"] = data
    if headings == "Typical number in the human body:":
        final_data["Typical number in the human body:"] = data
    if headings == "Constitutional parts:":
        data = (i.find_all("img"))[0]["alt"]
        data = data.split("|")
        print(data)
        if len(data) >= 3:
            final_data["Constitutional parts:"] = data[0:3]
        else:
            final_data["Constitutional parts:"] = data

    if headings == "Typical physical characteristics:":
        ch = data.split("\n")
        for data in ch:
            d = data.split("|")
            dd = d[0].strip()
            if dd == "mass":
                final_data["size"] = d[1].strip()
            elif dd == "volume":
                final_data["volume"] = d[1].strip()
            elif dd == "length":
                final_data["length"] = d[1].strip()
            elif dd == "width":
                final_data["width"] = d[1].strip()
            elif dd == "weight percentage of total body":
                final_data["weight percentage of total body"] = d[1].strip()
                
    #animals
    if headings == "Alternate common name:":
        final_data["Other Names"] = data
    if headings == "Alternate scientific names:":
        final_data["Other Names"] = data
    if headings == "Biological properties:":
        ch = data.split("\n")
        for data in ch:
            d = data.split("|")
            dd = d[0].strip()
            if dd == "lifespan":
                final_data["lifespan"] = d[1].strip()
            elif dd == "length":
                final_data["length"] = d[1].strip()
            elif dd == "weight":
                final_data["weight"] = d[1].strip()


    #food      
    if headings=="Average nutrition facts:":
        ch = data.split("\n")
        for data in ch:
            d = data.split("|")
            dd = d[0].strip()
            if (dd.find('serving size')!= -1 ):
                final_data["weight"] = dd.split("serving size")[1]
            elif (dd.find('total calories')!= -1 ):
                final_data["calories"] = dd.split("total calories")[1]
            elif (dd.find('total fat')!= -1 ):
                final_data["fat"] = dd.split("total fat")[1]   
            elif (dd.find('cholesterol')!= -1 ):
                final_data["cholesterol"] = dd.split("cholesterol")[1]  
            elif (dd.find('sugar')!= -1 ):
                final_data["sugar"] = dd.split("sugar")[1]
            elif (dd.find('sodium')!= -1 ):
                final_data["sodium"] = dd.split("sodium")[1]
            elif (dd.find('phosphorus')!= -1 ):
                final_data["phosphorus"] = dd.split("phosphorus")[1]
            elif (dd.find('zinc')!= -1 ):
                final_data["zinc"] = dd.split("zinc")[1]
            elif (dd.find('vitamin A')!= -1 ):
                final_data["vitamin A"] = dd.split("vitamin A")[1]
                
            elif (dd.find('vitamin E')!= -1 ):
                final_data["vitamin E"] = dd.split("vitamin E")[1]
                
            elif (dd.find('vitamin B6')!= -1 ):
                final_data["vitamin B6"] = dd.split("vitamin B6")[1]      
        break
# print(final_data)

for i in final_data:
    print(i, "   =   ", final_data[i])


'''


'''from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(
    "/Users/vikasnagare/Desktop/G_DRIVE/scrping/webScarp/CromeD/chromedriver")
driver.get(
    'https://www.wolframalpha.com/input/?i=dog')
sleep(30)
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()
soup = BeautifulSoup(res, 'lxml')
box = soup.find_all("section")


print("   --------------     --------")

print(len(box))
final_data = {}
for i in box:
    a = i.find_all("header")
    if(len(a) > 2) or len(a) == 0:
        continue
    headings = i.find_all('h2')[0].text
    if (len((i.find_all("img"))) != 0) and (i.find_all("img"))[0].has_attr('alt'):
        data = (i.find_all("img"))[0]["alt"]
    if headings == "Functional description:":
        final_data["functions"] = data
    if headings == "Alternate names:":
        final_data["Other Names"] = data
    if headings == "Functional categories:":
        final_data["Functional categories:"] = data
    if headings == "Typical number in the human body:":
        final_data["Typical number in the human body:"] = data
    if headings == "Constitutional parts:":
        data = (i.find_all("img"))[0]["alt"]
        data = data.split("|")
        print(data)
        if len(data) >= 3:
            final_data["Constitutional parts:"] = data[0:3]
        else:
            final_data["Constitutional parts:"] = data

    if headings == "Typical physical characteristics:":
        ch = data.split("\n")
        for data in ch:
            d = data.split("|")
            dd = d[0].strip()
            if dd == "mass":
                final_data["size"] = d[1].strip()
            elif dd == "volume":
                final_data["volume"] = d[1].strip()
            elif dd == "length":
                final_data["length"] = d[1].strip()
            elif dd == "width":
                final_data["width"] = d[1].strip()
            elif dd == "weight percentage of total body":
                final_data["weight percentage of total body"] = d[1].strip()
    if headings == "Alternate common name:":
        final_data["Other Names"] = data
    if headings == "Biological properties:":
        ch = data.split("\n")
        for data in ch:
            d = data.split("|")
            dd = d[0].strip()
            if dd == "lifespan":
                final_data["lifespan"] = d[1].strip()
            elif dd == "length":
                final_data["length"] = d[1].strip()
            elif dd == "weight":
                final_data["weight"] = d[1].strip()
# print(final_data)

for i in final_data:
    print(i, "   =   ", final_data[i])
'''

'''from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(
    "/Users/vikasnagare/Desktop/scrap/CromeD/chromedriver")
driver.get(
    'https://www.wolframalpha.com/input/?i=Neck')
sleep(30)
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()
soup = BeautifulSoup(res, 'lxml')
box = soup.find_all("section")


print("   --------------     --------")

print(len(box))
final_data = {}
for i in box:
    a = i.find_all("header")
    if(len(a) > 2) or len(a) == 0:
        continue
    headings = i.find_all('h2')[0].text
    if len((i.find_all("img"))) != 0:
        data = (i.find_all("img"))[0]["alt"]
    if headings == "Functional description:":
        final_data["functions"] = data
    if headings == "Alternate names:":
        final_data["Other Names"] = data
    if headings == "Functional categories:":
        final_data["Functional categories:"] = data
    if headings == "Typical number in the human body:":
        final_data["Typical number in the human body:"] = data
    if headings == "Constitutional parts:":
        data = (i.find_all("img"))[0]["alt"]
        data = data.split("|")
        print(data)
        if len(data) >= 3:
            final_data["Constitutional parts:"] = data[0:3]
        else:
            final_data["Constitutional parts:"] = data

    if headings == "Typical physical characteristics:":
        ch = data.split("\n")
        for data in ch:
            d = data.split("|")
            dd = d[0].strip()
            if dd == "mass":
                final_data["size"] = d[1].strip()
            elif dd == "volume":
                final_data["volume"] = d[1].strip()
            elif dd == "length":
                final_data["length"] = d[1].strip()
            elif dd == "width":
                final_data["width"] = d[1].strip()
            elif dd == "weight percentage of total body":
                final_data["weight percentage of total body"] = d[1].strip()
# print(final_data)

for i in final_data:
    print(i, "   =   ", final_data[i])
'''
