import os, random, time, threading
import playsound
from multiprocessing import Process


dirname = os.path.dirname(__file__)
paths = (
    "\\src\\sounds\\celesta\\",
    "\\src\\sounds\\clav\\",
    "\\src\\sounds\\swells\\",
)

def player(sound):
    playsound.playsound(sound)

x = 1
while x == 1:
    instrument = random.choice(paths)
    if 'swells' in instrument:
        sound_item = random.randint(1,3)
    else:
        sound_item = random.randint(1,27)
    sound = dirname + instrument + str(sound_item) + '.mp3'
    print(f'► {sound}')
    # p = Process(target=player, args=(sound,))
    # p = Process(target=playsound.playsound(sound), args=('bob',))
    p = threading.Thread(target=playsound.playsound(sound, False))
    # playsound.playsound(sound)
    
    p.start()
    p.join()
    time.sleep(random.uniform(0, 3))
    # x = 0
