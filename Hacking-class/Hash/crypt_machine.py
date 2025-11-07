import hashlib
from typing import Literal


class HashMachine:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def encrypt(
            self, hash_func: Literal["sha1", "sha224", "sha256", "sha384", "sha512"],
            text: str
    ):
        """Encrypts a text in a cryptography pattern of your choice in some choices, which are for strong hashlib library.

        Args:
            hash_func (Literal): Enter your cryptography pattern choice between all these choices.
            text (str): Enter your text which you want to hash it.

        Raises:
            TypeError: If you write an invalid value in hash_func or text parameter, this will raise by the bot.

        Returns:
            str: The hashed text.
        """

        if type(text) is not str:
            raise TypeError("Please enter a string at text parameter.")
        binary = text.encode()

        if hash_func == "sha1":
            result = hashlib.sha1(binary).hexdigest()
        elif hash_func == "sha224":
            result = hashlib.sha224(binary).hexdigest()
        elif hash_func == "sha256":
            result = hashlib.sha256(binary).hexdigest()
        elif hash_func == "sha384":
            result = hashlib.sha384(binary).hexdigest()
        elif hash_func == "sha512":
            result = hashlib.sha512(binary).hexdigest()
        else:
            raise TypeError(
                "Error occured. Please enter a valid value for hash."
            )

        return result
