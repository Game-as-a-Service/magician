def spelling(spell):
    stoneID = spell["stoneID"]

    magic_stones = {
        "magic1": True,
        "magic2": True,
        "magic3": True,
        "magic4": True,
        "magic5": True,
        "magic6": True,
        "magic7": True,
        "magic8": True,
    }

    if stoneID in magic_stones:
        return "magic exist"
    else:
        return "magic doesn't exist"
