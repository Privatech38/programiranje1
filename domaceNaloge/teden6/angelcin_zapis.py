import itertools
import unittest

def koordinate(ovira):
    stolpec = int(ovira.split("-")[0])
    return (stolpec, stolpec + ovira.count("-") - 1)

def vrstica(vrstica):
    list = vrstica.strip().split()
    vrstica = int(list[0][1:-1])
    list.pop(0)
    ovire = []
    for ovira in list:
        k = koordinate(ovira)
        ovire.append((k[0], k[1], vrstica))
    return ovire

def preberi(vrstice):
    ovire = []
    for v in vrstice.splitlines():
        ovire.extend(vrstica(v))
    return ovire

def intervali(xs):
    nizi = []
    for interval in xs:
        nizi.append(str(interval[0]) + "-"*(interval[1] - interval[0] + 1))
    return nizi

def zapisi_vrstico(y, xs):
    return f"({y}) " + " ".join(intervali(xs))

def zapisi(ovire):
    jaoo = []
    jaoo = []
    for y, xs in itertools.groupby(sorted(ovire, key=lambda x: (x[2], x[0])), lambda x: x[2]):
        inters = []
        for interval in xs:
            inters.append((interval[0], interval[1]))
        jaoo.append(zapisi_vrstico(y, inters))
    return "\n".join(jaoo)

class Obvezna(unittest.TestCase):
    def test_koordinate(self):
        self.assertEqual((3, 4), koordinate("3--"))
        self.assertEqual((5, 10), koordinate("5------"))
        self.assertEqual((123, 123), koordinate("123-"))
        self.assertEqual((123, 125), koordinate("123---"))

    def test_vrstica(self):
        self.assertEqual([(1, 3, 4), (5, 11, 4), (15, 15, 4)], vrstica("  (4) 1---  5------- 15-"))
        self.assertEqual([(989, 991, 1234)], vrstica("(1234) 989---"))

    def test_preberi(self):
        self.assertEqual([(5, 6, 4),
                          (90, 100, 13), (5, 8, 13), (19, 21, 13),
                          (9, 11, 5), (19, 20, 5), (30, 34, 5),
                          (9, 11, 4),
                          (22, 25, 13), (17, 19, 13)], preberi(
""" (4) 5--
(13) 90-----------   5---- 19---
 (5) 9---           19--   30-----
(4)           9---
(13)         22---- 17---
"""))

    def test_intervali(self):
        self.assertEqual(["6-----", "12-", "20---", "98-----"], intervali([(6, 10), (12, 12), (20, 22), (98, 102)]))

    def test_zapisi_vrstico(self):
        self.assertEqual("(5) 6----- 12-", zapisi_vrstico(5, [(6, 10), (12, 12)]).rstrip("\n"))
        self.assertEqual("(8) 6----- 12- 20--- 98-----", zapisi_vrstico(8, [(6, 10), (12, 12), (20, 22), (98, 102)]).rstrip("\n"))
        self.assertEqual("(8) 6----- 12- 20--- 98-----", zapisi_vrstico(8, [(6, 10), (12, 12), (20, 22), (98, 102)]).rstrip("\n"))


class Dodatna(unittest.TestCase):
    def test_zapisi(self):
        ovire = [(5, 6, 4),
          (90, 100, 13), (5, 8, 13), (9, 11, 13),
          (9, 11, 5), (19, 20, 5), (30, 34, 5),
          (9, 11, 4),
          (22, 25, 13), (17, 19, 13)]
        kopija_ovir = ovire.copy()
        self.assertEqual("""(4) 5-- 9---
(5) 9--- 19-- 30-----
(13) 5---- 9--- 17--- 22---- 90-----------""", zapisi(ovire).rstrip("\n"))
        self.assertEqual(ovire, kopija_ovir, "Pusti seznam `ovire` pri miru")


if __name__ == "__main__":
    unittest.main()