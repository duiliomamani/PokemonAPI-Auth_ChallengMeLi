from flask import jsonify

def jsonify_custom(obj):
    """
    Personaliza la respuesta JSON excluyendo valores None o listas vacías.
    
    Args:
    - obj: Objeto a serializar en formato JSON.

    Returns:
    - Respuesta JSON personalizada.
    """
    def process_value(value):
        """
        Procesa el valor para excluir None y listas vacías de manera recursiva.

        Args:
        - value: Valor a procesar.

        Returns:
        - Valor procesado.
        """
        if isinstance(value, (list, tuple)):
            # Para listas o tuplas, procesa cada elemento de la colección recursivamente
            return [process_value(item) for item in value if item is not None and item != []]
        elif isinstance(value, dict):
            # Para diccionarios, procesa cada valor recursivamente
            return {k: process_value(v) for k, v in value.items() if v is not None and v != []}
        elif hasattr(value, '__dict__'):
            # Si el objeto tiene un atributo __dict__, procesa sus atributos recursivamente
            return process_value(value.__dict__)
        else:
            # Para otros tipos de datos, devuelve el valor si no es None o lista vacía
            return value if value is not None and value != [] else None

    if isinstance(obj, (list, tuple)):
        # Si la raíz es una lista o tupla, procesa cada elemento de la colección recursivamente
        processed_obj = [process_value(item) for item in obj if item is not None and item != []]
    else:
        # Si la raíz es un objeto, procesa cada atributo del objeto
        processed_obj = {
            key: process_value(value)
            for key, value in obj.__dict__.items() if value is not None and value != []
        }

    # Devuelve la respuesta JSON personalizada
    return jsonify(processed_obj)
