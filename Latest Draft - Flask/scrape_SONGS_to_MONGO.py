from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint
#----------------------------------------------------------------------
import pymongo
#----------------------------------------------------------------------
# def scrape():

# for Windows:
executable_path = {'chromedriver.exe'}

# for Mac:
#executable_path = {'executable_path': '/usr/local/bin/chromedriver'}

browser = Browser('chrome')

# return results
#----------------------------------------------------------------------
#----------------------------------------------------------------------
#######################################################################

def get_billboard_table(browser_input, year_input, url_input):
    # print('\n' + '\n' + '\n' + '\n' + url_input)
    browser.visit(url_input)
    html = browser.html
    song_soup = BeautifulSoup(html, 'html.parser')

    result = song_soup.find('table', class_='archive-table')

    rows = result.findChildren(['th', 'tr'])

    result_list = []
    condensed_results = []

    row_count = 0
    date_value = ''
    results = {}

    for row in rows:
        results = {
            "year": year_input,
            "issue_date": [],
            "title" : "",
            "artist": ""
        }

        td_count = 0
        cells = row.findChildren('td')

        for cell in cells:
            td_count = td_count + 1
            value = cell.string
            if (td_count == 1):
                results["issue_date"].append(value)
                date_value = value
            if (td_count == 2):
                results["title"] = value
            if (td_count == 3):
                results["artist"] = value
                row_count = row_count + 1
                condensed_results.append(results)
            #print("The value in this cell is %s" % value)
        result_list.append(results)
        if (results["title"] == '') & (row_count > 0):
            index_row = row_count - 1
            condensed_results[index_row]["issue_date"].append(date_value)

    #--------------------------------------------------------------------
    # for each_con_res in range(len(condensed_results)):
    #     #print(str(each_con_res))
    #     print(condensed_results[each_con_res])
    #     print('\n')
    #     #print(condensed_results[each_con_res]["issue_date"])

    return condensed_results
#######################################################################
#######################################################################

years_list = range(1958, 2019, 1)
billboard_years_url_list = []

list_of_song_dicts = []

for year in years_list:
    #print(year)
    billboard_url = "https://www.billboard.com/archive/charts/" + str(year) + "/HSI"
    #print(billboard_url)
    #billboard_years_url_list.append(billboard_url)
    list_of_song_dicts.append(get_billboard_table(browser, year, billboard_url))

print('\n')

print("List_of_song_dicts - LENGTH: " + str(len(list_of_song_dicts)) + '\n')

#######################################################################
browser.quit()
#######################################################################
#######################################################################

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.billboard_db
#######################################################################

collection = db.all_number_one_songs

for iteration in range(len(list_of_song_dicts)):
    collection.insert_many(list_of_song_dicts[iteration])

#######################################################################
# collection = db.first_ten_years_top_hits

# for iteration in range(0, 10):
#     # print(list_of_song_dicts[iteration])
#     # print('\n')
#     collection.insert_many(list_of_song_dicts[iteration])

#######################################################################
#######################################################################
