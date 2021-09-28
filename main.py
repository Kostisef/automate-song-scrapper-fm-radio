import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime


class Song:
    def __init__(self, title, artist):
        # self.yt_link = yt_link
        self.title = title
        self.artist = artist
        self.full_title = title + ' - ' + artist
        self.yt_link = "https://www.youtube.com/results?search_query=" + self.full_title.replace(' ', '+')


def write_to_file(Song_object):
    f = open("song_list.txt", "a+")
    f.write(Song_object.full_title)
    f.write("\n")
    f.write(Song_object.yt_link)
    f.write("\n\n")
    f.close()
    print('** Song ADDED successfully. **')


def find_song(stored_dict, search_song):
    return next((x for x in stored_dict if x["Title"] == search_song), None)


def load_the_song_dict():
    f = open("song_list.txt", "r")
    content = f.read()
    f.close()
    song_list_temp = content.split("\n")
    song_list_temp = list(filter(None, song_list_temp))

    song_dict = {
        "Title": '',
        "Yt_link": ''
    }
    song_list = []
    j = 0
    for i in song_list_temp:
        if j % 2 == 0:
            song_dict['Title'] = i
        else:
            song_dict['Yt_link'] = i
            song_list.append(song_dict.copy())
        j += 1
    return song_list


def update_the_song_dict(song_list, song_obj):
    song_dict = {
        "Title": song_obj.full_title,
        "Yt_link": song_obj.yt_link
    }
    song_list.append(song_dict.copy())
    return song_list


if __name__ == '__main__':
    my_song_dict = load_the_song_dict()
    # xx = find_song(my_song_dict, 'cgdffg')
    # print(xx)
    web_link = "http://www.athensparty.com/wonder/player"
    opts = Options()
    opts.add_argument(" --headless")
    opts.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    chrome_driver = os.getcwd() + "\\chromedriver.exe"
    driver = webdriver.Chrome(options=opts, executable_path=chrome_driver)
    driver.get(web_link)

    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        # current song
        current_song = Song(driver.find_element_by_id("title").text, driver.find_element_by_id("artist").text)
        # next song
        next_song = Song(driver.find_element_by_id("nexttitle").text, driver.find_element_by_id("nextartist").text)

        print('Now  --> ' + current_song.full_title)
        print(current_song.yt_link)
        xx = find_song(my_song_dict, current_song.full_title)
        if xx is None:
            write_to_file(current_song)
            my_song_dict = update_the_song_dict(my_song_dict, current_song)
        else:
            print('** Song EXISTS...sorry try again. **\n')

        print('Next --> ' + next_song.full_title)
        print(next_song.yt_link)
        xx2 = find_song(my_song_dict, next_song.full_title)
        if xx2 is None:
            write_to_file(next_song)
            my_song_dict = update_the_song_dict(my_song_dict, next_song)
        else:
            print('** Song EXISTS...sorry try again. **\n')

        print()
        sleep(90)
