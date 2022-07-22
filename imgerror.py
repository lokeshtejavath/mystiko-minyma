class imagenNotEnough(Exception):
    def _init_(self):
        pass

    def _str_(self) -> str:
        return "Size of file is too low to fit the data"


class notAscii(Exception):
    def _init_(self):
        pass

    def _str_(self) -> str:
        return "Data to insert is not supported as of now, try only ascii for \\(`_`)/"


class invaildKey(Exception):
    def _init_(self):
        pass

    def _str_(self) -> str:
        return "Key is not valid"


class messageCantBeRetrieved(Exception):
    def _init_(self):
        pass

    def _str_(self) -> str:
        return "Message can't be retrieved"


class imageNotFound(Exception):
    def _init_(self):
        pass

    def _str_(self) -> str:
        return "Image not found"
