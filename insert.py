import random as rand
import cv2
import converter
import imgerror


class Inserter:

    def insert(self, message: str, key: str, image: str, name: str, basekey: str):
        initaliser = int(key[0:3])

        img = cv2.imread(image)
        shapex = img.shape[0]
        shapey = img.shape[1]
        x, y = 0, 0

        enc = []
        bytear = []
        for i in message:
            for j in i.encode("utf-8"):
                bytear.append(j)
        

        if shapex * shapey <= (12 * len(message)):
            raise imgerror.imagenNotEnough()
        convert = converter.converter()
        for char in key:
            blank = rand.randint(0, 5)
            for i in range(8 * blank):
                current = (img[x][y][0] & (~1))
                img.itemset((x, y, 0), current)
                x = ((x + 1) % shapex)
                if x == 0:
                    y += 1
            num = ord(char)
            num = num ^ initaliser
            initaliser = num
            num = convert.dectobin(num)
            for j in num:
                if j[0] == '0':
                    current = (img[x][y][0] & (~1))
                    img.itemset((x, y, 0), current)
                else:
                    current = (img[x][y][0] | 1)
                    img.itemset((x, y, 0), current)
                x = (x + 1) % shapex
                if x == 0:
                    y += 1
        for i in range(8 * 8):
            current = (img[x][y][0] & (~1))
            img.itemset((x, y, 0), current)
            x = (x + 1) % shapex
            if x == 0:
                y += 1
        for char in bytear:
            blank = rand.randint(0, 5)
            for i in range(8 * blank):
                current = (img[x][y][0] & (~1))
                img.itemset((x, y, 0), current)
                x = ((x + 1) % shapex)
                if x == 0:
                    y += 1
            num = char
            num = num ^ initaliser
            initaliser = num
            num = convert.dectobin(num)
            for j in num:
                if j[0] == '0':
                    current = (img[x][y][0] & (~1))
                    img.itemset((x, y, 0), current)
                else:
                    current = (img[x][y][0] | 1)
                    img.itemset((x, y, 0), current)
                x = (x + 1) % shapex
                if x == 0:
                    y += 1
        for i in range(8 * 8):
            current = (img[x][y][0] & (~1))
            img.itemset((x, y, 0), current)
            x = (x + 1) % shapex
            if x == 0:
                y += 1
        cv2.imwrite(name, img)

        return
