def hello(path, temporary):
    """
    Args:
        path (str): The path of the file to wrap
        temporary (bool): Whether or not to delete the file when the File instance is destructed

    Returns:
        BufferedFileStorage: A buffered writable file descriptor
    """
    return path
