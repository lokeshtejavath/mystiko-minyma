import converter
import cv2

class Retrive:

    def retriver(self, key: str, image: str):
        initaliser = int(key[0:3])
        img = cv2.imread(image)
        shapex = img.shape[0]
        shapey = img.shape[1]
        x, y = 0, 0
        convert = converter.converter()
        currentKey = []
        current = ""
        counter = 0
        while counter != 8:
            if img[x][y][0] & 1:
                current += "1"
            else:
                current += "0"
            if len(current) == 8:
                num = convert.bintodec(current)
                if num == 0:
                    counter += 1
                    current = ""
                else:
                    counter = 0
                    currentKey.append(initaliser ^ num)
                    initaliser = num
                    current = ""
            x = ((x + 1) % shapex)
            if x == 0:
                y += 1
        ans = ""
        for i in currentKey:
            ans += chr(i)
        if key != ans:
            print("wrong key")
            return
        currentKey = []
        counter = 0
        current = ""
        while counter != 8:
            if img[x][y][0] & 1:
                current += "1"
            else:
                current += "0"
            if len(current) == 8:
                num = convert.bintodec(current)
                if num == 0:
                    counter += 1
                    current = ""
                else:
                    counter = 0
                    currentKey.append(initaliser ^ num)
                    initaliser = num
                    current = ""
            x = ((x + 1) % shapex)
            if x == 0:
                y += 1
        ans = ""
        for i in currentKey:
            ans += chr(i)
        print("message:" + ans)
