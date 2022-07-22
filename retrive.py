import cv2
import converter
from imgerror import invaildKey, messageCantBeRetrieved, imageNotFound


class Retrive:

    def retriver(self, key: str, image: str, basekey: str):
        if len(key) != 28:
            raise invaildKey
        initaliser = int(key[0:3])
        img = cv2.imread(image)
        if img is None:
            raise imageNotFound
        shapex = img.shape[0]
        shapey = img.shape[1]
        x, y = 0, 0
        convert = converter.converter()
        baseKeyindex = 0
        valuesFound = []
        binaryFound = ""
        whiteNoiseLength = 0
        baseBytes = []
        for glyph in basekey:
            for byte in glyph.encode("utf-8"):
                baseBytes.append(byte)
        # print(baseBytes)
        while whiteNoiseLength != 8:
            if img[x][y][0] & 1:
                binaryFound += "1"
            else:
                binaryFound += "0"
            if len(binaryFound) == 8:
                num = convert.bintodec(binaryFound)
                if num == 0:
                    whiteNoiseLength += 1
                    binaryFound = ""
                else:
                    # print((num))
                    if(num == 255):
                        num = 0
                    whiteNoiseLength = 0
                    storenumber = num
                    value = initaliser ^ num
                    initaliser = storenumber
                    value = value ^ baseBytes[baseKeyindex]
                    baseKeyindex = (baseKeyindex + 1) % len(baseBytes)
                    binaryFound = ""
            x = ((x + 1) % shapex)
            if x == 0:
                y += 1
            if y == shapey:
                print("Message not found")
                return "fcuk"
        binaryFound = ""
        whiteNoiseLength = 0
        # print(initaliser, "initaliser")
        while whiteNoiseLength != 8:
            if img[x][y][0] & 1:
                binaryFound += "1"
            else:
                binaryFound += "0"
            if len(binaryFound) == 8:
                num = convert.bintodec(binaryFound)
                if num == 0:
                    whiteNoiseLength += 1
                    binaryFound = ""
                else:
                    # print((num))
                    if(num == 255):
                        num = 0
                    whiteNoiseLength = 0
                    storenumber = num
                    value = initaliser ^ num
                    initaliser = storenumber
                    value = value ^ baseBytes[baseKeyindex]
                    baseKeyindex = (baseKeyindex + 1) % len(baseBytes)
                    valuesFound.append(value)
                    binaryFound = ""
            x = ((x + 1) % shapex)
            if x == 0:
                y += 1

        # print(x, y)
        try:
            ans = b""
            for i in valuesFound:
                # print(i)
                ans += i.to_bytes(1, "big")
            # print(ans.decode("utf-8"), end="\n")
            return ans.decode("utf-8")
        except Exception as e:
            return None
