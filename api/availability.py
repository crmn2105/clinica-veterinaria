def check_availability(species: str, day: str):
    day = day.lower().strip()
    species = species.lower().strip()

    valid_days = ["monday", "tuesday", "wednesday", "thursday"]

    if day not in valid_days:
        return {
            "available": False,
            "reason": "Surgery is only scheduled from Monday to Thursday.",
            "slots": []
        }

    if species == "dog":
        if day == "thursday":
            return {
                "available": False,
                "reason": "That day is full for dogs under current capacity rules.",
                "slots": ["monday", "tuesday", "wednesday"]
            }

    return {
        "available": True,
        "reason": "Mock availability found.",
        "slots": [day]
    }