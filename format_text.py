#!/usr/bin/env python3

import re

base_link = "" + "https://soundcloud.com/altrip-4-428376342/{}-bonus-track"

data_formatted = """	{{
\t\turl: "{link}",
\t\tanswer: "{title}",
\t}},"""

# replace with the string names of each track
tracks = [
    "Karkat's Theme",
    "Terezi's Theme",
    "Vriska's Theme",
    "FIDUSPAWN, GO!",
    "Darling Kanaya",
    "Eridan's Theme",
    "Nautical Nightmare",
    "Nepeta's Theme",
    "Blackest Heart (With Honks)",
    "Killed by BR8K Spider!!!!!!!!",
    "Catapult Capuchin",
    "Science Seahorse",
    "A Fairy Battle",
    "The Blind Prophet",
    "AlterniaBound",
    "You Won A Combat",
    "Rest A While",
]


for track in tracks:
    tformatted = track.lower()
    tformatted = re.sub(r"(?=\W)[^ ]", "", tformatted)
    tformatted = tformatted.strip()
    tformatted = tformatted.replace(" ", "-", 3)
    if tformatted.count(" ") > 0:
        tformatted = tformatted[:tformatted.find(" ")]

    # print(data_formatted.format(
    #     link=base_link.format(tformatted),
    #     title=f"{track} - AlterniaBound"))
    print(f"\"{track} - AlterniaBound\",")
