def problema(frase1, frase2):
    final = frase1[-len(frase2):]
    print(final)

    if final == frase2:
        print(True)
    else:
        print(type(False))
    
problema("dondetaspapu","hola")