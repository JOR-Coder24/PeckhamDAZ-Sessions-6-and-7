# import required libraries

from bs4 import BeautifulSoup
import requests
import random
import pandas as pd

# check we can get the data from the page

# here we use 'query' for the end of the url, this allows us to quickly change it
query = 'Avengers_(comics)'

url = 'https://en.wikipedia.org/wiki/' + query
page = requests.get(url)
soup = BeautifulSoup(page.content, features="html.parser")
print(soup)

# this grabs us the html of the entire page
# this will check if the request was sucsessful. we want it to be 200, or at least start with a 2... anything else is a problem.

print(page.status_code)
# now I want to find only the link on this page
# first we create an array for the links

links = []

# we are looking for all of the <a> anchor tags.
# we do this with a for loop, we use 'try' and 'except' as some of the anchors may not have an 'href'. we ignore these otherwise it could cause an error.

for a in soup.find_all("a"):
    try:
        links.append(a["href"])
    except:
        pass

    # then another for loop to cycle though the array and print each link
for link in links:
    print(link)
# many of the links are from outside wikipedia. in this case we only want internal links

# we can then filter the array to only include links starting with /wiki/. so only internal links will show.

filtered = [link for link in links if link.startswith('/wiki/')]

for f in filtered:
    print(f)
# there are still a lot of links to stuff we dont want eg. pictures, help files ect. We can use ignore to filter them out.

ignores = ['png', 'jpg', 'jpeg', 'isbn', 'svg', 'identifier', \
           'File', 'Special', 'Template', 'Mailto', 'Portal', \
           'Help', 'Category', 'Talk', 'Wikipedia', 'Main_Page']

filtered = []

# this line states only links that are to wiki pages are valid
for link in links:
    if link.startswith('/wiki/'):
        valid = True

        # this line then makes all our ingnored links invalid
        for ignore in ignores:
            if ignore in link:
                valid = False
                break

        # if the link is valid we then add it to our 'filtered' array
        if valid:
            filtered.append(link)

for f in filtered:
    print(f)
# get the response in the form of html
wikiurl = "https://en.wikipedia.org/wiki/Avengers_(comics)"

# check the request was sucsessful (code 200)
response = requests.get(wikiurl)
print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')

# here we find any element with the table tag, there are some of these we dont want on this page.
# So we specify only tables using the "wikitable" class

tabledata = soup.find('table', {'class': "wikitable"})#Find a wikipedia style table(can change based on table type described in source code)
#tabledata = soup.find('table')#Finds all types of table
# read the table data
df = pd.read_html(str(tabledata))

# convert list to pandas dataframe
df = pd.DataFrame(df[0])
print(df.head())

# write the data to a .csv file
df.to_csv('team_info.csv', sep='\t', encoding='utf-8')
