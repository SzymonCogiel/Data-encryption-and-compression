import utils
from typing import Dict


class LZW:
    def compression(self, text, custom_dict: Dict = None):
        # TODO: dodać unikalny dict stworzony z text
        lzw_dict = custom_dict if custom_dict else utils.default_LZW_dict.copy()
        compressed_text = []
        index = 0
        while index < len(text) - 1:
            texcior, index = self.max_text(text, index, lzw_dict, len(text))
            compressed_text.append(lzw_dict[texcior[:-1]])
            if texcior not in lzw_dict.keys():
                lzw_dict[texcior] = len(lzw_dict) + 1
            else:
                if index < len(text) - 1:
                    lzw_dict[texcior + text[index + 1]] = len(lzw_dict) + 1
        compressed_text[-1] = lzw_dict[texcior]
        return compressed_text

    def max_text(self, textcoirito, index, lzw_dict, length):
        for i in range(0, length - index):
            end = index + i + 1
            temp = textcoirito[index:end]
            if temp not in lzw_dict.keys():
                break
        return temp, index + len(temp) - 1 if index + len(temp) - 1 <= length - 1 else length - 1
