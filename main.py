import insert
import randstring
import retrive
i = insert.Inserter()
key = randstring.randstring()
# i.insert("let's do this", key, "./loki.jpeg", "out")
# print(key)
key = "098oinKJkT2CjFd8bvdN6kFLwYDM"
r = retrive.Retrive()
r.retriver(key, "./out.png", " ")