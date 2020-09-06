import re, time
import pyperclip

print('Copy playlist source code to clipboard and press enter.')
input()

text = pyperclip.paste()
links = []

# Grab all unique matches with the key VideoId and add them to the list
for match in re.finditer('\"videoId\"', text):
    e = match.end()
    url = text[e+2:e+13]

    if url not in links:
        links.append(url)

# Remove first and last unrelated entries from the list
links.pop(0)
links.pop()

# Add youtube url format to the video id
playlist = ['https://www.youtube.com/watch?v=' + i for i in links]

# Copy urls to clipboard
pyperclip.copy('\n'.join(playlist))

# Print all the urls
for i in playlist:
    print(i)

print('\nURLs copied to clipboard')
time.sleep(3)