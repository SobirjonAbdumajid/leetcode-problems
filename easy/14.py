from os.path import split

str_ = "Hello world! I am a student of PDP"

counter = 0

to = str_.lower()


striped = to.strip("!.,?")
# striped.strip(" ")

char_set = set(striped)

for ch in char_set:
    print(f"{ch}: {striped.count(ch)}")
