class SymbolTable():
    PREDEFINED_SYMBOLS = {
        'SP'  : 0,
        'LCL' : 1,
        'ARG' : 2,
        'THIS': 3,
        'THAT': 4,
        'R0'  : 0,
        'R1'  : 1,
        # ...
        # (Lista completa de símbolos pré-definidos)
    }

    def __init__(self):
        self.symbols = self.PREDEFINED_SYMBOLS
        self.next_available_memory_address = 16

    def add_entry(self, symbol=None, address=None):
        if address:
            self.symbols[symbol] = address
        else:
            self.symbols[symbol] = self.next_available_memory_address
            self.next_available_memory_address += 1

        return self.get_address(symbol)

    def contains(self, symbol):
        return symbol in self.symbols

    def get_address(self, symbol):
        return self.symbols[symbol]
