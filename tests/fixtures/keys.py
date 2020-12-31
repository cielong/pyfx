def split(combined_keys, global_command_key):
    """
    Given a list of combined_keys (i.e. keys potentially contains second stroke)
    return a split version of keys with each key represent a single key stroke
    """
    if global_command_key is None:
        return combined_keys

    keys = []
    command_key_length = len(global_command_key)
    for key in combined_keys:
        if not key.startswith(global_command_key):
            keys.append(key)
            continue
        keys.extend([global_command_key, key[(command_key_length + 1):]])

    return keys
