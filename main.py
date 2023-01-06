import os, random, time, threading
import playsound, sys


# dirname = os.path.dirname(sys.executable)  # для exe
dirname = os.path.dirname(__file__)  # для проекта
paths = (
    "src\\\\sounds\\\\celesta\\\\",
    "src\\\\sounds\\\\clav\\\\",
    "src\\\\sounds\\\\swells\\\\",
)

def player(sound):
    playsound.playsound(sound)

def random_set(speed_time):
    while 1:
        instrument = random.choice(paths)
        if 'swells' in instrument:
            sound_item = random.randint(1, len(paths))
        else:
            sound_item = random.randint(1,27)
        sound = os.path.join(dirname, instrument, f'{sound_item}.mp3')
        # print(f'► {sound}')
        p = threading.Thread(target=player, args=(sound, ))
        p.start()
        time.sleep(random.uniform(0, speed_time))

speed_time = 2
speed_time_set = input(f"Скорость (>={speed_time}, по ум. {speed_time}): ")
if speed_time_set != '' and speed_time_set.isdigit() and int(speed_time_set) >= 2:
    speed_time = int(speed_time_set)
elif speed_time_set != '':
    speed_time = speed_time + int(speed_time_set)

random_set(speed_time)
