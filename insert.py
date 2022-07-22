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

        messageBytes = []
        for glyph in message:
            for byte in glyph.encode("utf-8"):
                messageBytes.append(byte)

        keyBytes = []
        for glyph in key:
            for byte in glyph.encode("utf-8"):
                keyBytes.append(byte)
        baseBytes = []
        for glyph in basekey:
            for byte in glyph.encode("utf-8"):
                baseBytes.append(byte)
        # print(baseBytes)

        if shapex * shapey <= (12 * len(messageBytes+keyBytes)):
            raise imgerror.imagenNotEnough()
        convert = converter.converter()
        baseKeyIndex = 0
        # print(messageBytes)
        for keyElement in keyBytes:
            whiteNoiseLength = rand.randint(0, 5)
            for i in range(8 * whiteNoiseLength):
                currentPixel = img[x][y][0] & (~1)  # Clear the LSB
                img.itemset((x, y, 0), currentPixel)  # Set the LSB to 0
                x = ((x + 1) % shapex)  # Increment x
                if x == 0:
                    y += 1
            byteToInsert = keyElement ^ baseBytes[baseKeyIndex]
            byteToInsert = byteToInsert ^ initaliser
            initaliser = byteToInsert
            baseKeyIndex = (baseKeyIndex + 1) % len(baseBytes)
            if(byteToInsert == 0):
                byteToInsert = 255
            binaryToInsert = convert.dectobin(byteToInsert)
            # print(byteToInsert)
            for bit in binaryToInsert:
                if bit == "0":
                    currentPixel = img[x][y][0] & (~1)
                    img.itemset((x, y, 0), currentPixel)
                else:
                    currentPixel = img[x][y][0] | 1
                    img.itemset((x, y, 0), currentPixel)
                x = (x + 1) % shapex
                if x == 0:
                    y += 1
        # Key is now inserted delimiated by white noise
        for i in range(8 * 8):
            currentPixel = img[x][y][0] & (~1)
            img.itemset((x, y, 0), currentPixel)
            x = (x + 1) % shapex
            if x == 0:
                y += 1
        # Message now to be inserted
        # print(initaliser, "initaliser")
        for messageElement in messageBytes:
            whiteNoiseLength = rand.randint(0, 5)
            for i in range(8 * whiteNoiseLength):
                currentPixel = img[x][y][0] & (~1)
                img.itemset((x, y, 0), currentPixel)
                x = ((x + 1) % shapex)
                if x == 0:
                    y += 1
            byteToInsert = messageElement ^ baseBytes[baseKeyIndex]
            byteToInsert = byteToInsert ^ initaliser
            initaliser = byteToInsert
            baseKeyIndex = (baseKeyIndex + 1) % len(baseBytes)
            # print(byteToInsert)
            if(byteToInsert == 0):
                byteToInsert = 255
            binaryToInsert = convert.dectobin(byteToInsert)
            # print(binaryToInsert)
            for bit in binaryToInsert:
                if bit == "0":
                    currentPixel = img[x][y][0] & (~1)
                    img.itemset((x, y, 0), currentPixel)
                else:
                    currentPixel = img[x][y][0] | 1
                    img.itemset((x, y, 0), currentPixel)
                x = (x + 1) % shapex
                if x == 0:
                    y += 1
        # Message is now inserted delimiated by white noise
        for i in range(8 * 8):
            currentPixel = img[x][y][0] & (~1)
            img.itemset((x, y, 0), currentPixel)
            x = (x + 1) % shapex
            if x == 0:
                y += 1
        # print(x, y)
        cv2.imwrite(name, img)

        return
