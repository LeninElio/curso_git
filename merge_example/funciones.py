def obtener_primera_letra(palabra):
    """
    Obtiene la primera letra de una palabra.
    :param palabra: La palabra de la cual se quiere obtener la primera letra.
    :return: La primera letra de la palabra.
    """
    if not palabra:
        return None
    return palabra[0]
