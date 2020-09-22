class Cibo:
    def __init__(self, proteine=0, carboidrati=0, grassi=0):
        """Questo calcola le calorie"""
        self.proteine = proteine
        self.carboidrati = carboidrati
        self.grassi = grassi
        self.calorie = self.proteine * 4 + self.carboidrati * 4 + self.grassi * 9

    def MostraCalorie(self):
        print("\n{} proteine\n"
              "{} carboidrati\n"
              "{} grassi\n"
              "\n{} calorie".format(self.proteine, self.carboidrati, self.grassi, self.calorie))


p = int(input("Inserire le proteine: "))
c = int(input("Inserire i carboidrati: "))
g = int(input("Inserire i grassi: "))

cibo1 = Cibo(p, c, g)

cibo1.MostraCalorie()
