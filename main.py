import os, playsound, random, time, threading

# paths = {
#     "path_celesta": "D:/Dev/meditation_player/src/sounds/celesta/",
#     "path_clav": "D:/Dev/meditation_player/src/sounds/clav/",
#     "path_swells": "D:/Dev/meditation_player/src/sounds/swells/",
# }
paths = (
    "D:/Dev/meditation_player/src/sounds/celesta/",
    "D:/Dev/meditation_player/src/sounds/clav/",
    "D:/Dev/meditation_player/src/sounds/swells/",
)

# print(os.path.join(path_celesta, "static_sounds_swells_swell1.mp3"))

# def player(sound):
#     playsound.playsound(sound)

while 1:
    instrument = random.choice(paths)
    if 'swells' in instrument:
        sound_item = random.randint(1,3)
    else:
        sound_item = random.randint(1,27)
    sound = f'{instrument}{sound_item}.mp3'
    threading.Thread(target=playsound.playsound(sound)).start()
    # playsound.playsound(sound)
    time.sleep(random.randint(0,3))
