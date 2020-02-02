from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint
#----------------------------------------------------------------------
# def scrape():

# for Windows:
#executable_path = {'executable_path': 'chromedriver.exe'}
# for Mac:
executable_path = {'chromedriver'}

browser = Browser('chrome') 

# return results
#----------------------------------------------------------------------
url_year_list = [
    'https://www.billboard.com/archive/charts/1958/HSI',
    'https://www.billboard.com/archive/charts/1971/HSI',
    'https://www.billboard.com/archive/charts/1984/HSI',
    'https://www.billboard.com/archive/charts/1996/HSI',
    'https://www.billboard.com/archive/charts/2010/HSI'
]
#----------------------------------------------------------------------
#######################################################################

def get_billboard_table(browser_input, url_input):

    print('\n' + '\n' + '\n' + '\n' + url)

    browser.visit(url)
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

    # browser.quit()

    #----------------------------------------------------------------------
    print('\n') # + '\n')

    for each_con_res in range(len(condensed_results)):
        print(str(each_con_res))
        print(condensed_results[each_con_res])
        print('\n')
        #print(condensed_results[each_con_res]["issue_date"])

    #return condensed_results

#######################################################################

for url in url_year_list:
    print(url)
    get_billboard_table(browser, url)

#######################################################################

browser.quit()