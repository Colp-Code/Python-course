"""
Caractener de escape 
Para insertar caracteres que son proibidos en una cadena de texto, usa un caracter de escape.

Un caracter de escape es una barra diagonal seguido por un caracter que tu quieras insertar.

Un ejemplo de un caracter ilegal son las comillas dobles dentro de un texto que esta rodeada de otras comillas dobles:

    Ejemplo
Tu obtendras un error si pones dobles comillas dentro de un texto que esta rodeado otra comillas dobles:

"""

# txt = "Eramos llamados "Vikingos" del norte"

"""
Para arreglar el problema usa el caracter de escape \:

    Ejemplo
El caracter de escape permite que uses comillas dobles donde normalmente no estaria permitido:

"""
txt = "Eramos llamados \"Vikingos\"del norte"
print(txt)

"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value

"""