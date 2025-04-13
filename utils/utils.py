import base64


def encode_image_data(image_stream, is_bytes: bool = False):
    """
    Encodes image data into a base64 string.

    Args:
        image_stream (BytesIO): The image data as a stream.
        is_bytes (bool): Whether the image data is already in bytes (default is False).

    Returns:
        str: The base64-encoded image data as a string.
    """
    return base64.b64encode(
        image_stream if is_bytes else image_stream.getvalue()
    ).decode("utf-8")
