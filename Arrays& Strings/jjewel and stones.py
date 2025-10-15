jewels = "bA"
stones ="bAAHjdfgt"

def finding_jewels(stones, jewels):
    jewels = set(jewels)
    num_jewels = 0

    for s in stones:
        if s in jewels:
            num_jewels += 1
    return num_jewels

print(finding_jewels(stones,jewels))