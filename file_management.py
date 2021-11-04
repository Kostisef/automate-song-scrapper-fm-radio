# from song import Song
# from song import Song


def write_to_file(song_object):
    f = open("song_list.txt", "a+")
    f.write(song_object.full_title)
    f.write("\n")
    f.write(song_object.yt_link)
    f.write("\n\n")
    f.close()


def get_content_from_file(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    return content


def load_the_song_dict(filename):
    content = get_content_from_file(filename)

    song_list_temp = content.split("\n")
    song_list_temp = list(filter(None, song_list_temp))
    # the above code filters the None lines (lines without text), let's see inside song_list.txt
    #   Line 1: Love Will Set You Free - Carrie Cleveland
    #   Line 2: https://www.youtube.com/results?search_query=Love+Will+Set+You+Free+-+Carrie+Cleveland
    #   Line 3:
    #   Line 4: Sleepwalking man - Sivert Hoyem
    #   Line 5: https://www.youtube.com/results?search_query=Sleepwalking+man+-+Sivert+Hoyem

    song_dict = {
        "Title": '',
        "Yt_link": ''
    }
    song_list = []
    j = 0
    for i in song_list_temp:
        if j % 2 == 0:
            # even number contains the song title
            song_dict['Title'] = i
        else:
            # odd number contains the youtube link
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

