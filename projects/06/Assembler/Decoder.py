import sys

class HackAssemblerDecoder():
    C_COMMAND_INIT_BITS = '111'

    DEST_MNEMONIC_TO_BITS = {
        None : '000',
        'M'  : '001',
        'D'  : '010',
        'MD' : '011',
        'A'  : '100',
        'AM' : '101',
        'AD' : '110',
        'AMD': '111'
    }

    COMP_MNEMONIC_TO_BITS = {
        None : '',
        '0'  : '0101010',
        '1'  : '0111111',
        # ...
        # (Lista completa de mapeamentos)
    }

    JUMP_MNEMONIC_TO_BITS = {
        None : '000',
        'JGT': '001',
        'JEQ': '010',
        # ...
        # (Lista completa de mapeamentos)
    }

    @classmethod
    def decimal_to_binary_string(cls, num):
        return '{0:016b}'.format(num)

