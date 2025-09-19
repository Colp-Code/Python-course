def solution(text, ending):
    # your code here...
    pass
    final = len(ending)
    palabra = text[-final:]
    print(palabra)
    if ending in palabra:
        return True
    else:
        return False 

solution("pepe","pe")