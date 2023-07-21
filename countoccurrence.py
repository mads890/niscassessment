def countoccurrence(text):
    asciichars = sorted([ord(item) for item in text])
    result = []
    for i in set(asciichars):
        found = [item for item in asciichars if item == i]
        result.append([chr(i), len(found)])
    return result