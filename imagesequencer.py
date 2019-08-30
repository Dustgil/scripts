import matplotlib.pyplot as plt
import os

delay = 3
path = 'C:\\Pictures\\'
images = os.listdir(path)

print(images)


for i in range(0, len(images)):
    file = path + images[i]

    plt.figure(1)
    plt.clf()
    img = plt.imread(file)
    plt.imshow(img)

    plt.tick_params(
        bottom=False,
        top=False,
        left=False,
        right=False)

    plt.xticks([])
    plt.yticks([])
        
    plt.pause(delay)

