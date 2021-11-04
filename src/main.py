from file_management import load_the_song_dict
from song import *
from selenium_init import selenium_connect
from time import sleep
from datetime import datetime


def main():
    # Load any songs stored in .txt file
    my_song_dict = load_the_song_dict("../song_list.txt")
    # Make the connection between Selenium - website
    driver = selenium_connect("http://www.athensparty.com/wonder/player")

    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

        # current song
        current_song = Song(driver.find_element_by_id("title").text, driver.find_element_by_id("artist").text)
        # next song
        next_song = Song(driver.find_element_by_id("nexttitle").text, driver.find_element_by_id("nextartist").text)

        print('\nNow  --> ' + current_song.full_title + "\n" + current_song.yt_link)
        # print(current_song.yt_link)
        my_song_dict = add_new_song(my_song_dict, current_song)

        print('Next --> ' + next_song.full_title + "\n" + next_song.yt_link)
        # print(next_song.yt_link)
        my_song_dict = add_new_song(my_song_dict, next_song)

        # wait for 1.5 minutes until new scrapping...
        sleep(90)


if __name__ == '__main__':
    main()

