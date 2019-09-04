from bs4 import BeautifulSoup
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
