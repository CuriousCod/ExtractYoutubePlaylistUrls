import re, os
import pyperclip

if os.path.isfile('source.txt'):
    f = open('source.txt','r', encoding='utf-8')
    text = f.read()

    list = []

    # Grab all unique matches with the key VideoId and add them to the list
    for match in re.finditer('\"videoId\"', text):
        e = match.end()
        url = text[e+2:e+13]

        if url not in list:
            list.append(url)

    # Remove last trash entry from the list
    list.pop()

    # Add youtube url format to the video id
    playlist = ['https://www.youtube.com/watch?v=' + i for i in list]

    # Copy urls to clipboard
    pyperclip.copy('\n'.join(playlist))

    # Print all the urls
    for i in playlist:
        print(i)

    f.close()

    print('\nURLs copied to clipboard')
    input()

else:
    print('No source.txt file found!')
    print('Open a playlist and copy the source code to a source.txt file')
    input()
