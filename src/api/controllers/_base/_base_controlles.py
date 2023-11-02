from flask import jsonify

def jsonify_custom(obj):
    """
     Customize the JSON response by excluding None values or empty lists.
    
     Args:
     - obj: Object to be serialized in JSON format.

     Returns:
     - Custom JSON response.
     """
    def process_value(value):
        """
         Processes the value to exclude None and empty lists recursively.

         Args:
         - value: Value to process.

         Returns:
         - Processed value.
         """
        if isinstance(value, (list, tuple)):
            # For lists or tuples, process each element of the collection recursively
            return [process_value(item) for item in value if item is not None and item != []]
        elif isinstance(value, dict):
            # For dictionaries, process each value recursively
            return {k: process_value(v) for k, v in value.items() if v is not None and v != []}
        elif hasattr(value, '__dict__'):
            # If the object has a __dict__ attribute, process its attributes recursively
            return process_value(value.__dict__)
        else:
            # For other data types, return value if not None or empty list
            return value if value is not None and value != [] else None

    if isinstance(obj, (list, tuple)):
        # If the root is a list or tuple, process each element of the collection recursively
        processed_obj = [process_value(item) for item in obj if item is not None and item != []]
    else:
        # If root is an object, process each attribute of the object
        processed_obj = {
            key: process_value(value)
            for key, value in obj.__dict__.items() if value is not None and value != []
        }
    # Returns the custom JSON response
    return jsonify(processed_obj)
