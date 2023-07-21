def countoccurrence(text):
    asciichars = [ord(item) for item in text]
    result = []
    for i in sorted(set(asciichars)):
        found = [item for item in asciichars if item == i]
        result.append([chr(i), len(found)])
    return result

print(countoccurrence('Typical Sentence'))