#!/usr/bin/env python3

import re

base_link = "" + "https://soundcloud.com/altrip-4-428376342/{}-bonus-track"

data_formatted = """	{{
\t\turl: "{link}",
\t\tanswer: "{title}",
\t}},"""

# replace with the string names of each track
tracks = [
    "Chapter 5 Logo",
    "Inappropriate Recycling",
    "Pirate Dojo",
    "4rd Sanctuary",
    "Festival",
    "Catfession...?",
    "Bratfession...?",
    "I guess I'm in love",
    "Weirder Birds",
    "Your Dad's Best Friend",
    "Garden of Hopes and Dreams",
    "Rakuichi Buster",
    "The Diner Song of Best Friends",
    "Ride the Board",
    "Quiet Glade",
    "Who might you be?",
    "Petal Dance",
    "Flying Feather",
    "Sunset of Seven Suns",
    "Shop 3",
    "Violet Tactics",
    "Flower King",
    "Flower Foyer",
    "Flower Castle",
    "Thousand Cafe Zukan",
    "I'm Telling!",
    "Stop, Criminell!",
    "Loving Steps",
    "Onsen",
    "Beautiful Bathtime",
    "Pink",
    "Cutie Mew Mew Magic",
    "Running Sky",
    "Flower Man",
    "That Day",
    "Dreamwatchers",
    "Weak Flowers",
    "Walking Home",
    "Field of Hopes and Dreams (Credits Version)",
    "Goodnight, Sweet Prince",
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
    print(f"\"{track} - Deltarune\",")
