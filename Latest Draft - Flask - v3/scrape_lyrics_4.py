from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint
import pymongo
#----------------------------------------------------------------------
from edit_string_of_lyric_text import clean_lyric_string
#----------------------------------------------------------------------
# def scrape():

# for Windows:
#executable_path = {'executable_path': 'chromedriver.exe'}
# for Mac:
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}

browser = Browser('chrome', **executable_path, headless=False)

# return results
#----------------------------------------------------------------------
#url_lyric_list = [
#    'https://www.azlyrics.com/lyrics/rihanna/whatsmyname.html'

#]
#----------------------------------------------------------------------
#######################################################################
# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


db = client.billboard_db
#######################################################################

collection = db.all_number_one_songs

artist = ""
song_name = ""

artist_list = []
song_name_list = []

artists_cleaned = []
titles_cleaned = []

all_records_list = []

#######################################################################

for document in collection.find():
    # print(document)
    # print('\n')
    all_records_list.append(document)

for each_record in all_records_list:
    
    each_artist = each_record["artist"]


    output_string = ""
    print('\n' + '\n' + str(each_artist))
    if "Featuring" in each_artist:
        artist, sep, tail = each_artist.partition(' Featuring')
    else:
        artist = each_artist
    
    print('\n' + str(artist) + '\n')
    for letter in artist:
        try:
            if letter.isspace(): # = " ":
                output_string = output_string + "-"
            elif letter == "&": #in artist:
                #print("and")
                output_string = output_string + "and"
            elif letter == "'": #in artist:
                print("")
            elif letter == ".": #in artist:
                print("")
            elif letter == "!": #in artist:
                #print("-")
                output_string = output_string + "-"
            elif letter == "$": #in artist:
                #print("s")
                output_string = output_string + "s"
            elif letter == "+": #in artist:
                #print("-")
                output_string = output_string + "-"
            elif letter == ',':
                output_string = output_string + ""
            else:
                output_string = output_string + letter
    
        except Exception as e:
            print(e)
    
    print(output_string)
    artists_cleaned.append(output_string)


#for each_rec in all_records_list: #["title"]:
    
    each_song = each_record["title"]
    
    output_string2 = ""
    print('\n' + '\n' + str(each_song))
    if "(" in each_song:
        song, sep, tail = each_song.partition(' (')
    else:
        song = each_song
    
    print('\n' + str(song) + '\n')
    for letter2 in song:
        try:
            if letter2.isspace(): # = " ":
                output_string2 = output_string2 + "-"
            elif letter2 == "&": #in artist:
                #print("and")
                output_string2 = output_string2 + "-"
            elif letter2 == "'": #in artist:
                print("")
            elif letter2 == ".": #in artist:
                print("")
            elif letter2 == "!": #in artist:
                #print("-")
                output_string2 = output_string2 + ""
            elif letter2 == "$": #in artist:
                #print("s")
                output_string2 = output_string2 + "s"
            elif letter2 == "+": #in artist:
                #print("-")
                output_string2 = output_string2 + "-"
            elif letter2 == ',':
                output_string2 = output_string2 + ""
            elif letter2 == "?": #in artist:
                #print("-")
                output_string2 = output_string2 + ""
            else:
                output_string2 = output_string2 + letter2
    
        except Exception as e1:
            print(e1)
    
    print(output_string2)
    titles_cleaned.append(output_string2)
    

#for a,t in zip(artists_cleaned, titles_cleaned):

#def get_lyrics(browser):
    # url = 'https://genius.com/Rihanna-whats-my-name-lyrics' 
    lyrics_url = "https://genius.com/" + str(output_string) + "-" + str(output_string2) + "-lyrics"
    #lyrics_url = "https://genius.com/" + str(a) + "-" + str(t) + "-lyrics"
    print(lyrics_url)
    browser.visit(lyrics_url)
    html = browser.html
    lyric_soup = BeautifulSoup(html, 'html.parser')

    song_dict = {
        "Lyrics": []
    }


    lyric_string = ""
    cleaned_lyric_string = ""
    rejected_scrape_output_list = []
    cleaned_lyric_output = []
#song_lyrics = []

#Extract Title of the song
# for title in lyric_soup.findAll('title'):
#   song_dict["Title"] = title.text.strip()

#Extract the Lyrics of the song
    for lyrics in lyric_soup.findAll('div', attrs = {'class': 'lyrics'}):
        song_dict["Lyrics"].append(lyrics.text.strip().split("\n"))



        scrape_string = str(lyrics.text.strip().split("\n")) + " "
        scrape_as_list = lyrics.text.strip().split("\n")
        scrape_string = str(scrape_as_list[0])
        
        # if ("[" in scrape_string):
        #     rejected_scrape_output_list.append(scrape_string)
        # else:
        #     lyric_string = lyric_string + " " + scrape_string
        lyric_string = lyric_string + " " + scrape_string

        cleaned_lyric_string = clean_lyric_string(lyric_string)

        cleaned_lyric_output.append(cleaned_lyric_string)

        print('\n')
        print(cleaned_lyric_string)
        print('\n')
    
    #title_string = '"' + t + '"'
    title_string = '"' + each_song + '"'

    print("title_string: " + title_string)
    print('\n')

    test_string = "This is a test!"

    db.all_number_one_songs.update_one(
        #{"title": title_string},
        {"title": each_song},
        {'$set':
        #{'$push':
            {"lyrics": cleaned_lyric_string}
            #{"push_test": test_string}
        }
    )
        

    
    #return cleaned_lyric_output

browser.quit()

# for iteration in range(len(cleaned_lyric_output)):
#     collection.insert_many(cleaned_lyric_output[iteration])

#collection.update({"title": t}, {$set: {"lyrics": clean_lyric_string}})


# for iteration in range(len(cleaned_lyric_output)):
#     song_lyrics = cleaned_lyric_output[iteration]

#     print(song_lyrics)
#     print('\n')

#     db.all_number_one_songs.update_one(
#         {"title": t},
#         {'$set':
#             {"lyrics": song_lyrics}
#         }
#     )


#############################################################################



# #######################################################################
# print(song_lyrics)
# #######################################################################

