jewels = "ABA"
stones = "bAAHjdfgt"

def jewelsinstones(stones, jewels):
    jewwl = set(jewels)
    num_jewels =0
    for s in stones:
        if s in jewwl:
            num_jewels += 1
    return num_jewels

print(jewelsinstones(stones,jewels))
