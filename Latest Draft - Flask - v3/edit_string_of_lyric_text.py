#Rejected string:

# rejected_lyric_string = "[Chorus: Rihanna]Oh na-na, what's my name?Oh na-na, what's my name?Oh na-na, what's my name?Oh na-na, what's my name?Oh na-na, what's my name?What's my name, what's my name?[Verse 1: Drake]Uh, yeahI heard you good with them soft lipsYeah, you know word of mouthThe square root of 69 is 8 somethin', right?'Cause I've been tryna work it out, ohUh, good weed, white wineUh, I come alive in the night time, yeahOkay, away we goOnly thing we have on is the radioLet it playSay you gotta leave, but I know you wanna stayYou just waitin' on the traffic jam to finish girlThe things that we could do in twenty minutes girlSay my name, say my name, wear it outIt's gettin' hot, crack a window, air it outI can get you through a mighty long daySoon as you go the text that I write is gon' say"

# print('\n')
# print("Lyrics as given from scraping output:")
# print(rejected_lyric_string)
# print('\n')

def clean_lyric_string(rejected_raw_lyrics):
    cleaned_lyrics = ""
    edited_out_string = ""

    last_letter = ""
    binary_state = 0

    for letter in rejected_raw_lyrics: #rejected_lyric_string:
        # if (letter in "-,?!"):
        #     cleaned_lyrics = cleaned_lyrics + " "
        
        if (letter == "["):
            binary_state = 1
        if (last_letter == "]"):
            binary_state = 0
        
        if (binary_state == 1):
            edited_out_string = edited_out_string + letter
        else:
            if (letter.isupper()):
                if (last_letter.islower()):
                    cleaned_lyrics = cleaned_lyrics + " " + letter
                else:
                    cleaned_lyrics = cleaned_lyrics + letter
            elif (letter in "-,?!"):
                cleaned_lyrics = cleaned_lyrics + " "
            else:
                cleaned_lyrics = cleaned_lyrics + letter
        
        last_letter = letter

    # print('\n')
    # print("cleaned_lyrics: ")
    # print(cleaned_lyrics)

    # print('\n')
    # print("edited_out_string: ")
    # print(edited_out_string)
    # print('\n')

    return cleaned_lyrics

