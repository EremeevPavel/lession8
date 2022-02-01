class Stok:

    def __init__(self, pc, pr, sc):
        self.pc = pc  # ПК
        self.pr = pr  # Принтеры
        self.sc = sc  # Сканеры

    def up_stok(self, how_pc, how_pr, how_sc):
        self.pc = self.pc + Stok.type_test(how_pc)
        self.pr = self.pr + Stok.type_test(how_pr)
        self.sc = self.sc + Stok.type_test(how_sc)

    def down_stok(self, how_pc, how_pr, how_sc):
        if self.pc - Stok.type_test(how_pc) < 0:
            print('Нельзя списывать отсутствующий товар! ')
            raise ValueError('Нулевой остаток! ')
        self.pc = self.pc - Stok.type_test(how_pc)
        if self.pr - how_pr < 0:
            print('Нельзя списывать отсутствующий товар! ')
            raise ValueError('Нулевой остаток! ')
        self.pr = self.pr - Stok.type_test(how_pr)
        if self.pr - how_pr < 0:
            print('Нельзя списывать отсутствующий товар! ')
            raise ValueError('Нулевой остаток! ')
        self.sc = self.sc - how_sc

    def info(self):
        print(self.pc)
        print(self.pr)
        print(self.sc)
        return self.pc, self.pr, self.sc

    @staticmethod
    def type_test(value):
        if isinstance(value, int):
            return value
        else:
            raise ValueError('Нужно ввести число!')

x = Stok(0, 0, 0)
pc = int(input('Сколько персональных компьютеров положить на склад?: '))
pr = int(input('Сколько принтеров положить на склад?: '))
sc = int(input('Сколько сканеров положить на склад?: '))

x.up_stok(pc, pr, sc)
pc_1 = int(input('Сколько персональных компьютеров списать со склада?: '))
pr_1 = int(input('Сколько принтеров списать со склада?: '))
sc_1 = int(input('Сколько сканеров списать со склада?: '))
x.down_stok(pc_1, pr_1, sc_1)





