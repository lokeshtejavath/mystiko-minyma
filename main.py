import insert
import randstring

i = insert.Inserter()
key = randstring.randstring()
i.insert("hello", key, "./loki.jpeg", "out")
print(key)