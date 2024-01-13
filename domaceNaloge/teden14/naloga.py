import re
import unittest
from unittest.mock import patch, call


class Kolesar:
    def __init__(self, zemljevid):
        self.ded = False
        self.x = 0
        self.y = 0
        self.distance = 0
        self.zemljevid = zemljevid

    def pojdi(self, smer):
        if smer == ">" and self.x == len(self.zemljevid[0]) - 1 or smer == "v" and self.y == len(self.zemljevid) - 1\
                or smer == "<" and self.x == 0 or smer == "^" and self.y == 0:
            self.ded = True
        if self.ded:
            return
        if smer == "<":
            self.x -= 1
            self.distance += 1
        if smer == ">":
            self.x += 1
            self.distance += 1
        if smer == "v":
            self.y += 1
            self.distance += 1
        if smer == "^":
            self.y -= 1
            self.distance += 1

    def prevozi(self, pot):
        if self.ded:
            return
        numbers = re.finditer(r"\d+", pot)
        multiple = False
        for char in pot:
            if char.isdigit():
                multiple = True
                continue
            if multiple:
                multiple = False
                for i in range(int(next(numbers).group())):
                    self.pojdi(char)
                continue
            self.pojdi(char)

    def lokacija(self):
        return self.x, self.y

    def razdalja(self):
        return self.distance




class Test06(unittest.TestCase):
    def test_01_pojdi(self):
        ana = Kolesar(["." * 5] * 10)
        berta = Kolesar(["." * 20] * 3)

        self.assertEqual((0, 0), ana.lokacija())
        self.assertEqual(0, ana.razdalja())
        ana.pojdi(">")
        self.assertEqual((1, 0), ana.lokacija())
        self.assertEqual(1, ana.razdalja())
        ana.pojdi(">")
        self.assertEqual((2, 0), ana.lokacija())
        self.assertEqual(2, ana.razdalja())
        ana.pojdi("v")
        self.assertEqual((2, 1), ana.lokacija())
        self.assertEqual(3, ana.razdalja())
        ana.pojdi("^")
        self.assertEqual((2, 0), ana.lokacija())
        self.assertEqual(4, ana.razdalja())
        ana.pojdi("^")  # umre...
        self.assertEqual((2, 0), ana.lokacija())
        self.assertEqual(4, ana.razdalja())
        ana.pojdi(">")  # še vedno mrtva
        self.assertEqual((2, 0), ana.lokacija())
        self.assertEqual(4, ana.razdalja())

        self.assertEqual((0, 0), berta.lokacija())
        self.assertEqual(0, berta.razdalja())
        berta.pojdi("v")
        self.assertEqual((0, 1), berta.lokacija())
        self.assertEqual(1, berta.razdalja())
        berta.pojdi("v")
        self.assertEqual((0, 2), berta.lokacija())
        self.assertEqual(2, berta.razdalja())
        berta.pojdi(">")
        self.assertEqual((1, 2), berta.lokacija())
        self.assertEqual(3, berta.razdalja())
        berta.pojdi("<")
        self.assertEqual((0, 2), berta.lokacija())
        self.assertEqual(4, berta.razdalja())
        berta.pojdi("v")  # umre...
        self.assertEqual((0, 2), berta.lokacija())
        self.assertEqual(4, berta.razdalja())
        berta.pojdi(">")  # še vedno mrtva
        self.assertEqual((0, 2), berta.lokacija())
        self.assertEqual(4, berta.razdalja())

        ana = Kolesar(["." * 5] * 10)
        for _ in range(5):
            ana.pojdi(">")
        self.assertEqual((4, 0), ana.lokacija())
        self.assertEqual(4, ana.razdalja())
        ana.pojdi(">")
        self.assertEqual((4, 0), ana.lokacija())
        self.assertEqual(4, ana.razdalja())
        ana.pojdi("v")
        self.assertEqual((4, 0), ana.lokacija())
        self.assertEqual(4, ana.razdalja())

    def test_02_prevozi_klice_pojdi(self):
        ana = Kolesar(["." * 5] * 10)
        with patch.object(Kolesar, "pojdi", wraps=ana.pojdi) as p:
            ana.prevozi(">>vv<")
            self.assertEqual((1, 2), ana.lokacija())
            self.assertEqual(5, ana.razdalja())
            self.assertEqual(5, p.call_count, "Kolesar.prevozi mora klicati Kolesar.pojdi 5-krat")
            p.assert_has_calls([call(">"), call(">"), call("v"), call("v"), call("<")])

    def test_02_prevozi(self):
        ana = Kolesar(["." * 5] * 10)
        ana.prevozi(">>vv<")
        self.assertEqual((1, 2), ana.lokacija())
        self.assertEqual(5, ana.razdalja())

        ana = Kolesar(["." * 2000] * 2000)
        ana.prevozi(">>5>")
        self.assertEqual((7, 0), ana.lokacija())
        self.assertEqual(7, ana.razdalja())
        ana.prevozi("v>3v")
        self.assertEqual((8, 4), ana.lokacija())
        self.assertEqual(12, ana.razdalja())

        ana = Kolesar(["." * 2000] * 2000)
        ana.prevozi(">>12>")
        self.assertEqual((14, 0), ana.lokacija())
        self.assertEqual(14, ana.razdalja())

        ana = Kolesar(["." * 2000] * 2000)
        ana.prevozi(">>1941>")
        self.assertEqual((1943, 0), ana.lokacija())
        self.assertEqual(1943, ana.razdalja())

        ana = Kolesar(["." * 2000] * 2000)
        ana.prevozi(">>1941><5<")
        self.assertEqual((1937, 0), ana.lokacija())
        self.assertEqual(1949, ana.razdalja())

        ana = Kolesar(["." * 2000] * 2000)
        ana.prevozi(">>1941><5<^")
        self.assertEqual((1937, 0), ana.lokacija())
        self.assertEqual(1949, ana.razdalja())

        ana = Kolesar(["." * 2000] * 2000)
        ana.prevozi(">>1941><5<^50>")
        self.assertEqual((1937, 0), ana.lokacija())
        self.assertEqual(1949, ana.razdalja())

        ana = Kolesar(["." * 2000] * 2000)
        ana.prevozi("3v3>")
        self.assertEqual((3, 3), ana.lokacija())
        self.assertEqual(6, ana.razdalja())
        ana.prevozi("<")
        self.assertEqual((2, 3), ana.lokacija())
        self.assertEqual(7, ana.razdalja())
        ana.prevozi("5<")
        self.assertEqual((0, 3), ana.lokacija())
        self.assertEqual(9, ana.razdalja())
        ana.prevozi("v")
        self.assertEqual((0, 3), ana.lokacija())
        self.assertEqual(9, ana.razdalja())
        ana.prevozi("5v")
        self.assertEqual((0, 3), ana.lokacija())
        self.assertEqual(9, ana.razdalja())

        ana = Kolesar(["." * 2000] * 2000)
        ana.prevozi(">>5>12vv6<vv13^<")
        self.assertEqual((0, 2), ana.lokacija())
        self.assertEqual(42, ana.razdalja())

        ana = Kolesar(["." * 2000] * 2000)
        ana.prevozi(">>5>12vv6<vv13^<>>>")
        self.assertEqual((3, 2), ana.lokacija())
        self.assertEqual(45, ana.razdalja())


class Test07(unittest.TestCase):
    def test_00_pojdi_klice_podedovano(self):
        ana = Zbiralec(1, 1, dravlje)
        with patch.object(Kolesar, "pojdi") as p:
            ana.pojdi(">")
            self.assertEqual(1, p.call_count, "Zbiralec.pojdi mora klicati Kolesar.pojdi")
            p.assert_has_calls([call(">")])

    def test_00_premik(self):
        self.assertIs(Kolesar.prevozi, Zbiralec.prevozi, "Zbiralec naj ne definira svoje metode premik")

    def test_01_znacke(self):
        ana = Zbiralec(1, 1, dravlje)
        self.assertEqual(set(), ana.znacke())

        ana.pojdi(">")
        self.assertEqual((2, 1), ana.lokacija())
        self.assertEqual({"b"}, ana.znacke())

        ana.pojdi(">")
        self.assertEqual({"b"}, ana.znacke())
        ana.prevozi("v2^<")
        self.assertEqual({"b"}, ana.znacke())

        ana.prevozi("<2>2v4<")  # pobere p, vendar se pelje predaleč in umre ...
        self.assertEqual({"b", "r", "p"}, ana.znacke())

        ana.prevozi("2v3>")  # ... zato tu ne dobi s-ja
        self.assertEqual({"b", "r", "p"}, ana.znacke())

    def test_02_naj_znacke(self):
        ana = Zbiralec(3, 2, dravlje)
        self.assertEqual(set(), ana.naj_znacke())

        ana.pojdi(">")  # x = 4
        self.assertEqual((4, 2), ana.lokacija())
        self.assertEqual(set(), ana.naj_znacke())
        ana.pojdi(">")  # x = 5
        self.assertEqual({"r"}, ana.naj_znacke())
        ana.prevozi("5<")  # x = 0
        self.assertEqual({"r", "p"}, ana.naj_znacke())  # čez r in p je šla enkrat
        ana.prevozi("3>")  # x = 3
        self.assertEqual({"p"}, ana.naj_znacke())  # čez p je šla dvakrat
        ana.prevozi("4>")  # x = 7
        self.assertEqual({"r", "p"}, ana.naj_znacke())  # čez r in p je šla dvakrat
        ana.prevozi("3v")
        self.assertEqual({"r", "p", "l"}, ana.znacke())  # imamo še l, vendar le enkrat
        self.assertEqual({"r", "p"}, ana.naj_znacke())  # čez r in p je šla dvakrat
        ana.prevozi("^^^")
        self.assertEqual({"r", "p", "l"}, ana.naj_znacke())  # čez vse je šla trikrat
        ana.prevozi("3<")  # x = 4
        self.assertEqual({"r"}, ana.naj_znacke())  # čez r je šla štirikrat
        ana.prevozi("2v3>")  # x = 7
        self.assertEqual({"l", "r"}, ana.naj_znacke())  # čez l tudi
        ana.prevozi("7<")
        self.assertEqual({"l", "r"}, ana.naj_znacke())
        self.assertEqual({"r", "p", "l", "s"}, ana.znacke())  # imamo še l, vendar le enkrat
        ana.prevozi("<")  # umre
        self.assertEqual({"l", "r"}, ana.naj_znacke())
        self.assertEqual({"r", "p", "l", "s"}, ana.znacke())  # imamo še l, vendar le enkrat
        ana.prevozi("<2>2<2>2<2>2<2>2<")  # če bi bila živa, bi vozila čez s, vendar ... ne
        self.assertEqual({"l", "r"}, ana.naj_znacke())

    def test_03_trofeje(self):
        ana = Zbiralec(0, 0, [".abccbdadbebddefc"])
        self.assertEqual([], ana.trofeje())
        ana.pojdi(">")
        self.assertEqual([("a", 1)], ana.trofeje())
        ana.pojdi(">")
        self.assertEqual([("a", 1), ("b", 1)], ana.trofeje())
        ana.pojdi(">")
        self.assertEqual([("a", 1), ("b", 1), ("c", 1)], ana.trofeje())
        ana.pojdi(">")
        self.assertEqual([("c", 2), ("a", 1), ("b", 1)], ana.trofeje())
        ana.pojdi(">")
        self.assertEqual([("b", 2), ("c", 2), ("a", 1)], ana.trofeje())
        ana.pojdi(">")
        self.assertEqual([("b", 2), ("c", 2), ("a", 1), ("d", 1)], ana.trofeje())
        ana.pojdi(">")
        self.assertEqual([("a", 2), ("b", 2), ("c", 2)], ana.trofeje())
        ana.pojdi(">")
        self.assertEqual([("a", 2), ("b", 2), ("c", 2), ("d", 2)], ana.trofeje())
        ana.pojdi(">")
        self.assertEqual([("b", 3), ("a", 2), ("c", 2), ("d", 2)], ana.trofeje())
        ana.pojdi(">")
        self.assertEqual([("b", 3), ("a", 2), ("c", 2), ("d", 2)], ana.trofeje())
        ana.pojdi(">")
        self.assertEqual([("b", 4), ("a", 2), ("c", 2), ("d", 2)], ana.trofeje())
        ana.pojdi(">")
        self.assertEqual([("b", 4), ("d", 3), ("a", 2), ("c", 2)], ana.trofeje())
        ana.pojdi(">")
        self.assertEqual([("b", 4), ("d", 4), ("a", 2), ("c", 2)], ana.trofeje())
        ana.pojdi(">")
        self.assertEqual([("b", 4), ("d", 4), ("a", 2), ("c", 2), ("e", 2)], ana.trofeje())
        ana.pojdi(">")
        self.assertEqual([("b", 4), ("d", 4), ("a", 2), ("c", 2), ("e", 2)], ana.trofeje())
        ana.pojdi(">")
        self.assertEqual([("b", 4), ("d", 4), ("c", 3)], ana.trofeje())


class Test08(unittest.TestCase):
    def test_00_drsalec_klice_super(self):
        zemljevid = ["." * 12] * 7
        sledi = Sledi()
        ana = Drsalec(1, 1, zemljevid, sledi)
        berta = Drsalec(0, 1, zemljevid, sledi)
        ana.prevozi("5>")
        with patch.object(Zbiralec, "pojdi") as pojdi:
            berta.prevozi(">")
            self.assertEqual(pojdi.call_count, 4, "Drsalčev pojdi bi moral štirikrat poklicati podedovani pojdi")

    def test_01_drsalec(self):
        zemljevid = ["." * 12] * 7
        zemljevid[3] = "....abcdef.."
        sledi = Sledi()
        ana = Drsalec(1, 2, zemljevid, sledi)
        berta = Drsalec(3, 0, zemljevid, sledi)
        cilka = Drsalec(7, 3, zemljevid, sledi)
        ana.prevozi("7>2v7<")
        self.assertEqual((1, 4), ana.lokacija())
        self.assertEqual(16, ana.razdalja())
        self.assertEqual([("e", 1)], ana.trofeje())

        berta.prevozi("3v")
        self.assertEqual((6, 3), berta.lokacija())
        self.assertEqual(6, berta.razdalja())
        self.assertEqual([("c", 1)], berta.trofeje())

        berta.prevozi("<<")
        self.assertEqual((4, 3), berta.lokacija())
        self.assertEqual(8, berta.razdalja())
        self.assertEqual([("a", 1), ("b", 1), ("c", 1)], berta.trofeje())

        cilka.prevozi("2^1>")
        self.assertEqual((9, 4), cilka.lokacija())
        self.assertEqual(9, cilka.razdalja())
        self.assertEqual([("e", 3)], cilka.trofeje())

        dani = Drsalec(9, 3, zemljevid, sledi)
        dani.prevozi("<v")
        self.assertEqual((9, 5), dani.lokacija())
        self.assertEqual(4, dani.razdalja())
        self.assertEqual([("e", 1)], dani.trofeje())

        cilka.pojdi("^")
        self.assertEqual((9, 4), cilka.lokacija())
        self.assertEqual(13, cilka.razdalja())
        self.assertEqual([("e", 4), ("f", 1)], cilka.trofeje())


dravlje = """
.r......c..c
r.b.........
.p...r......
............
.s.....l....
.ad......a..
............
..gl......g.""".strip().splitlines()


if __name__ == '__main__':
    unittest.main()
