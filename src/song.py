# import file_management
from file_management import write_to_file, update_the_song_dict
from mysql_management import write_to_db


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.full_title = title + ' - ' + artist
        self.yt_link = "https://www.youtube.com/results?search_query=" + self.full_title.replace(' ', '+')


def find_song(stored_dict, search_song):
    return next((x for x in stored_dict if x["Title"] == search_song), None)


# Check if web scrapped CURRENT song already exists in file
# TRUE --> print appropriate message
# FALSE --> add song to file & update the song dictionary
def add_new_song(song_dictionary, song_obj: Song):
    song_full_title = song_obj.full_title
    xx = find_song(song_dictionary, song_full_title)
    if xx is None:
        write_to_file(song_obj)  # write the new song to .txt file
        write_to_db(song_obj)  # add new song to the appropriate MySQL table
        print('** Song ADDED successfully. **\n')
        song_dictionary = update_the_song_dict(song_dictionary, song_obj)
    else:
        print('** Song EXISTS...sorry try again. **\n')

    return song_dictionary
