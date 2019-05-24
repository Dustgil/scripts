import time
import winsound

print("start massage right")
time.sleep(180)

winsound.PlaySound('noise.wav', winsound.SND_ASYNC)

print("start stretching right")

for i in range(10):
    time.sleep(21)
    winsound.PlaySound('noise.wav', winsound.SND_AYNSC)

print("start heating left")
time.sleep(300)

winsound.PlaySound('noise.wav', winsound.SND_AYNSC)

print("start massage left")
time.sleep(180)

winsound.PlaySound('noise.wav', winsound.SND_AYNSC)

print("start stretching left (1)")

for i in range(10):
    time.sleep(21)
    winsound.PlaySound('noise.wav', winsound.SND_AYNSC)

print("now do (2)")

for i in range(10):
    time.sleep(21)
    winsound.PlaySound('noise.wav', winsound.SND_AYNSC)

print("done!")
