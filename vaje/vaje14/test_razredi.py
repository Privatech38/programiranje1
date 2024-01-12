
class Ladja:
    def __init__(self, nosilnost):
        self.paketi = []
        self.odstranjeni = 0
        self.nosilnost = nosilnost

    def natovori(self, teza):
        self.paketi.append(teza)
        while sum(self.paketi) > self.nosilnost:
            self.paketi.pop(0)
            self.odstranjeni += 1

    def skupna_teza(self):
        return sum(self.paketi)

    def odstranjenih(self):
        return self.odstranjeni


class Mesto:
    def __init__(self, sirina, visina):
        self.hise = set()
        self.sirina = sirina
        self.visina = visina

    def postavi(self, x, y):
        self.hise.add((x, y))

    def porusi(self, x0, y0, x1, y1):
        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                self.hise -= {(i, j)}

    def prosto(self):
        return self.sirina * self.visina - len(self.hise)

class Figura:
    def __init__(self, x, y, ime):
        self.x = x
        self.y = y
        self.ime = ime

    def opis(self):
        return f"{self.ime} na {' abcdefgh'[self.x]}{self.y}"

    def premik(self, smer, razdalja):
        pass


class Trdnjava(Figura):
    def __init__(self, x, y):
        super().__init__(x, y, "Trdnjava")

    def premik(self, smer, razdalja):
        if smer == "|":
            self.y += razdalja
        if smer == "-":
            self.x += razdalja

class Lovec(Figura):
    def __init__(self, x, y):
        super().__init__(x, y, "Lovec")
    def premik(self, smer, razdalja):
        self.y += razdalja
        if smer == "/":
            self.x += razdalja
        if smer == "\\":
            self.x -= razdalja



import unittest

class TestLadja(unittest.TestCase):
    def test_konstruktor(self):
        ladja = Ladja(42)

    def test_natovori_teza(self):
        ladja = Ladja(42)
        ladja.natovori(30)
        self.assertEqual(ladja.skupna_teza(), 30)
        ladja.natovori(4)
        self.assertEqual(ladja.skupna_teza(), 34)
        ladja.natovori(7)
        self.assertEqual(ladja.skupna_teza(), 41)

    def test_odstranjevanje(self):
        ladja = Ladja(42)
        self.assertEqual(ladja.odstranjenih(), 0)
        ladja.natovori(30)
        self.assertEqual(ladja.odstranjenih(), 0)
        ladja.natovori(10)

        self.assertEqual(ladja.odstranjenih(), 0)
        ladja.natovori(21)
        self.assertEqual(ladja.odstranjenih(), 1)
        self.assertEqual(ladja.skupna_teza(), 31)

        ladja.natovori(41)
        self.assertEqual(ladja.odstranjenih(), 3)
        self.assertEqual(ladja.skupna_teza(), 41)

        ladja.natovori(50)
        self.assertEqual(ladja.odstranjenih(), 5)
        self.assertEqual(ladja.skupna_teza(), 0)

class TestMesto(unittest.TestCase):
    def test_mesto(self):
        m = Mesto(5, 8)
        self.assertEqual(m.prosto(), 40)

        m.postavi(2, 6)
        self.assertEqual(m.prosto(), 39)

        m.postavi(2, 6)
        self.assertEqual(m.prosto(), 39)

        for x in range(4):
            for y in range(2, 5):
                m.postavi(x, y)
        self.assertEqual(m.prosto(), 27)

        m.porusi(1, 1, 2, 4)
        self.assertEqual(m.prosto(), 33)

class TestFigure(unittest.TestCase):
    def test_trdnjava(self):
        t = Trdnjava(2, 5)
        self.assertEqual(t.opis(), "Trdnjava na b5")
        t.premik("|", 3)
        self.assertEqual(t.opis(), "Trdnjava na b8")
        t.premik("|", -2)
        self.assertEqual(t.opis(), "Trdnjava na b6")
        t.premik("-", 3)
        self.assertEqual(t.opis(), "Trdnjava na e6")
        t.premik("-", -1)
        self.assertEqual(t.opis(), "Trdnjava na d6")

    def test_lovec(self):
        e = Lovec(1, 2)
        self.assertEqual(e.opis(), "Lovec na a2")
        e.premik("/", 4)
        self.assertEqual(e.opis(), "Lovec na e6")
        e.premik("\\", 2)
        self.assertEqual(e.opis(), "Lovec na c8")
        e.premik("\\", -3)
        self.assertEqual(e.opis(), "Lovec na f5")
        e.premik("/", 1)
        self.assertEqual(e.opis(), "Lovec na g6")

    def test_opis(self):
        self.assertIs(Trdnjava.opis, Figura.opis)
        self.assertIs(Lovec.opis, Figura.opis)

if __name__ == "__main__":
    unittest.main()
