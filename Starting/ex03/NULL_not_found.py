def NULL_not_found(object: any) -> int:
    if object is None:
        return print("Nothing:", object, type(object)), 0
    elif type(object) is float and object != object:
        return print("Cheese:", object, type(object)), 0
    elif type(object) is bool and not object:
        return print("Fake:", object, type(object)), 0
    elif type(object) is int and not object:
        return print("Zero:", object, type(object)), 0
    elif type(object) is str and not object:
        return print("Empty:", object, type(object)), 0
    else:
        print("Type not Found")
        return 1
