import cv2
import converter
from imgerror import invaildKey, messageCantBeRetrieved, imageNotFound


class Retrive:

    def retriver(self, key: str, image: str, basekey: str):
        if len(key) != 25:
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
                    whiteNoiseLength = 0
                    value = initaliser ^ num
                    value = value ^ basekey[baseKeyindex]
                    baseKeyindex = (baseKeyindex + 1) % len(basekey)
            x = ((x + 1) % shapex)
            if x == 0:
                y += 1
        binaryFound = ""
        whiteNoiseLength = 0
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
                    whiteNoiseLength = 0
                    value = initaliser ^ num
                    value = value ^ basekey[baseKeyindex]
                    baseKeyindex = (baseKeyindex + 1) % len(basekey)
                    valuesFound.append(value)
            x = ((x + 1) % shapex)
            if x == 0:
                y += 1
        try:
            ans = b""
            for i in valuesFound:
                ans += i.to_bytes(1, "big")
            return ans.decode()
        except Exception as e:
            return None
