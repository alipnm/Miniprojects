class Caesar:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        self.ord_A = ord('A')
        self.ord_a = ord('a')

    def encrypt(self, text: str, shift: int) -> str:
        shift = shift % 26
        result = ""

        for c in text:
            if c.isupper():
                current_position = ord(c) - self.ord_A
                new_position = ((current_position + shift) % 26) + self.ord_A
                new_char = chr(new_position)
                result += new_char
            elif c.islower():
                current_position = ord(c) - self.ord_a
                new_position = ((current_position + shift) % 26) + self.ord_a
                new_char = chr(new_position)
                result += new_char
            else:
                result += c

        return result

    def decrypt(self, text: str, shift: int):
        shift = shift % 26
        result = ""

        for c in text:
            if c.isupper():
                current_position = ord(c) - self.ord_A

                new_position_shifted = current_position - shift
                if new_position_shifted < 0:
                    new_position_shifted *= -1
                    new_position_shifted = (26 - shift) + self.ord_A
                else:
                    new_position_shifted = (
                        new_position_shifted % 26
                    ) + self.ord_A

                new_char = chr(new_position_shifted)
                result += new_char
            elif c.islower():
                current_position = ord(c) - self.ord_a

                new_position_shifted = current_position - shift
                if new_position_shifted < 0:
                    new_position_shifted *= -1
                    new_position_shifted = (26 - shift) + self.ord_a
                else:
                    new_position_shifted = (
                        new_position_shifted % 26
                    ) + self.ord_a

                new_char = chr(new_position_shifted)
                result += new_char
            else:
                result += c

        return result
