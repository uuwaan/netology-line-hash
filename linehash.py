from hashlib import md5

INPUT_FILE = "country_links.txt"


def linehash(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as in_file:
        for l in in_file.readlines():
            yield md5(l.rstrip().encode()).hexdigest()


if __name__ == "__main__":
    for lhash in linehash(INPUT_FILE):
        print(lhash)
