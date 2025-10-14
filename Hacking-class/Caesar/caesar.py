class Caesar:
    def encrypt(self, text: str, shift: int) -> str:
        shift = shift % 26
        result = ""

        for c in text:
            if c.isupper():
                current_position = ord(c) - ord('A')
                new_position = (current_position + shift) % 26
                new_char = chr(new_position)
                result += new_char
            elif c.islower():
                current_position = ord(c) - ord('a')
                new_position = (current_position + shift) % 26
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
                current_position = ord(c) - ord('A')

                new_position_shifted = current_position - shift
                if new_position_shifted < 0:
                    new_position_shifted *= -1
                    new_position_shifted = 26 - shift
                else:
                    new_position_shifted = new_position_shifted % 26

                new_char = chr(new_position_shifted)
                result += new_char
            elif c.islower():
                current_position = ord(c) - ord('A')

                new_position_shifted = current_position - shift
                if new_position_shifted < 0:
                    new_position_shifted *= -1
                    new_position_shifted = 26 - shift
                else:
                    new_position_shifted = new_position_shifted % 26

                new_char = chr(new_position_shifted)
                result += new_char
            else:
                result += c

        return result
