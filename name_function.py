def get_formatted_name(first, last, middle=''): # add middle to the end to make it optional
    """Generate a neatly formatted full name."""
    if middle:    
        full_name = f"{first} {middle} {last}" # first middle last with a space
    else:
        full_name = f"{first} {last}"
    return full_name.title()
