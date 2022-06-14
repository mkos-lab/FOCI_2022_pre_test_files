def NO_PROD_create_decryption_key(email: str, salt: str) -> str:
    """
    This function creates a decryption key using your the email address and salt.

    Args:
    -----
    email : str
        The email address to be hashed.
    salt : str
        The salt to use for hashing.

    Returns:
    -------
    str
        The decryption key.

    Examples
    --------
    >>> NO_PROD_create_decryption_key(email="alex@doe.com", salt="1234567890A")
    '89F6AA649E053F021AC312ADBC1BBBDE7BF36063A155FF80FABD0CBAF75C495E'
    
    Notes
    —----
    Do not use this function in production. It carries multiple security risks.

    """
    raise NotImplementedError("This function is not implemented yet.")
    