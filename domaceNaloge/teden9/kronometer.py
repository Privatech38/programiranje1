import itertools
import re
import unittest
from itertools import pairwise
from collections import defaultdict

A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, V = "ABCDEFGHIJKLMNOPRSTUV"

zemljevid = {
    (A, B): {'trava', 'gravel'},
    (B, A): {'trava', 'gravel'},
    (A, V): {'lonci', 'pešci'},
    (V, A): {'lonci', 'pešci'},
    (B, C): {'lonci', 'bolt'},
    (C, B): {'lonci', 'bolt'},
    (B, V): set(),
    (V, B): set(),
    (C, R): {'lonci', 'pešci', 'stopnice'},
    (R, C): {'lonci', 'pešci', 'stopnice'},
    (D, F): {'pešci', 'stopnice'},
    (F, D): {'pešci', 'stopnice'},
    (D, R): {'pešci'},
    (R, D): {'pešci'},
    (E, I): {'lonci', 'trava'},
    (I, E): {'lonci', 'trava'},
    (F, G): {'črepinje', 'trava'},
    (G, F): {'črepinje', 'trava'},
    (G, H): {'pešci', 'črepinje'},
    (H, G): {'pešci', 'črepinje'},
    (G, I): {'avtocesta'},
    (I, G): {'avtocesta'},
    (H, J): {'bolt', 'robnik'},
    (J, H): {'bolt', 'robnik'},
    (I, M): {'avtocesta'},
    (M, I): {'avtocesta'},
    (I, P): {'gravel'},
    (P, I): {'gravel'},
    (I, R): {'stopnice', 'robnik'},
    (R, I): {'stopnice', 'robnik'},
    (J, K): set(),
    (K, J): set(),
    (J, L): {'bolt', 'gravel'},
    (L, J): {'bolt', 'gravel'},
    (K, M): {'bolt', 'stopnice'},
    (M, K): {'bolt', 'stopnice'},
    (L, M): {'pešci', 'robnik'},
    (M, L): {'pešci', 'robnik'},
    (M, N): {'rodeo'},
    (N, M): {'rodeo'},
    (N, P): {'gravel'},
    (P, N): {'gravel'},
    (O, P): {'gravel'},
    (P, O): {'gravel'},
    (P, S): set(),
    (S, P): set(),
    (R, U): {'pešci', 'trava'},
    (U, R): {'pešci', 'trava'},
    (R, V): {'lonci', 'pešci'},
    (V, R): {'lonci', 'pešci'},
    (S, T): {'robnik', 'trava'},
    (T, S): {'robnik', 'trava'},
    (T, U): {'trava', 'gravel'},
    (U, T): {'trava', 'gravel'},
    (U, V): {'lonci', 'robnik', 'trava'},
    (V, U): {'lonci', 'robnik', 'trava'}
}

pribitki1 = dict(gravel=2, trava=3, lonci=1, bolt=2, pešci=4,
                 stopnice=3, avtocesta=5, črepinje=1, robnik=1,
                 rodeo=4)

pribitki2 = dict(gravel=2, trava=3, lonci=1, bolt=100, pešci=4,
                 stopnice=3, avtocesta=5, črepinje=1, robnik=1,
                 rodeo=4)

pribitki3 = dict(gravel=2, trava=3, lonci=100, bolt=2, pešci=4,
                 stopnice=3, avtocesta=5, črepinje=1, robnik=1,
                 rodeo=4)

pribitki4 = dict(gravel=2, trava=3, lonci=1, bolt=2, pešci=100,
                 stopnice=3, avtocesta=5, črepinje=1, robnik=1,
                 rodeo=4)

# Naloge


def poti(niz):
    for a, b in pairwise(niz):
        yield a, b


# Ocena 6
def cas_za_povezavo(povezava, pribitki):
    return sum([pribitki[vescina] for vescina in zemljevid[povezava]]) + 4


def cas(pot, pribitki):
    return sum([cas_za_povezavo(povezava, pribitki) for povezava in poti(pot)])


def povezava_spotike(pribitki):
    return max([(povezava, cas_za_povezavo(povezava, pribitki)) for povezava in reversed(zemljevid)], key=lambda x: x[1])[0]


# Ocena 7
def urnik(pot, pribitki):
    tocke = {
        pot[0]: 0
    }
    cas = 0
    for povezava in poti(pot):
        cas += cas_za_povezavo(povezava, pribitki)
        if povezava[1] not in tocke:
            tocke[povezava[1]] = cas
    return tocke


def skupinski_sport(pot, pribitkii):
    return sum(max([cas_za_povezavo(povezava, pribitki) for pribitki in pribitkii]) for povezava in poti(pot))


def tekma(pot, pribitkii):
    casi = [(i, sum(cas_za_povezavo(povezava, pribitki) for povezava in poti(pot))) for i, pribitki in enumerate(pribitkii)]
    if min(casi, key=lambda x: x[1]) != min(reversed(casi), key=lambda x: x[1]): return None
    return min(casi, key=lambda x: x[1])[0]


def trening(pot, pribitki):
    cas = 0
    for povezava in poti(pot):
        cas += cas_za_povezavo(povezava, pribitki)
        for ovira in zemljevid[povezava]:
            pribitki[ovira] = pribitki[ovira] * 0.95
    return cas


def zastavice(pot, pribitkii):
    mozne_zastavice = set(pot)
    stevilo_zastavic = [0] * len(pribitkii)
    cas = [0] * len(pribitkii)
    # Initial zastavica
    stevilo_zastavic[0] = 1
    mozne_zastavice.remove(pot[0])
    # Ostale zastvice
    for povezava in poti(pot):
        for i, pribitki in enumerate(pribitkii):
            cas[i] += sum([pribitki[ovira] for ovira in zemljevid[povezava]])
        if povezava[1] in mozne_zastavice:
            stevilo_zastavic[cas.index(min(cas))] += 1
            mozne_zastavice.remove(povezava[1])
    return stevilo_zastavic


def cikel(zacetna_tocka, pribitki):
    prejsnja_tocka = ''
    opravljene_povezave = []
    while True:
        trenutna_povezava = min(sorted([(povezava, sum([pribitki[ovira] for ovira in ovire])) for povezava, ovire in zemljevid.items() if povezava[0] == zacetna_tocka and not (povezava[1] == prejsnja_tocka)], key=lambda x: x[0][1]), key=lambda x: x[1])[0]
        prejsnja_tocka, zacetna_tocka = trenutna_povezava
        if trenutna_povezava in opravljene_povezave:
            return len(opravljene_povezave[opravljene_povezave.index(trenutna_povezava):])
        opravljene_povezave.append(trenutna_povezava)


def izpadanje(potke, pribitkii):
    # Doloci presecisca
    tocke = set("".join(potke))
    skupna_krizisca = []
    stevilo = len(potke)
    potke_z_indexi = list(enumerate(potke))
    while stevilo > 1:
        for kombinacija in itertools.combinations(potke_z_indexi, stevilo):
            presecisca = set.intersection(*list(map(lambda x: set(x[1]), kombinacija)))
            for presecisce in presecisca:
                if presecisce not in tocke:
                    continue
                s = "".join(presecisce)
                skupna_krizisca.append((s, sorted([(i, cas(potka[:potka.index(s) + 1], pribitkii[i])) for i, potka in kombinacija],
                                      key=lambda x: x[1])))
                tocke.remove(s)
        stevilo -= 1
    # Sortiraj
    skupna_krizisca.sort(key=lambda x: x[1][0][1])
    # Določi izpadle kolesarje
    izpadli_kolesarji = dict()
    # Določi kolesarje ki se ustrelijo v nogo
    for i, potka in enumerate(potke):
        if len(set(potka)) == len(potka):
            continue
        duped_tocka = "".join(set([char for char in potka if potka.count(char) >= 2]))[0]
        izpadli_kolesarji[i] = cas(potka[:[match.start() for match in re.finditer(re.compile(duped_tocka), potka)][1]], pribitkii[i])
    for skupo_krizisce in skupna_krizisca:
        zmagovalec = True
        for kolesarjev_cas in skupo_krizisce[1]:
            if kolesarjev_cas[0] in izpadli_kolesarji and kolesarjev_cas[1] >= izpadli_kolesarji[kolesarjev_cas[0]]:
                continue
            if zmagovalec:
                zmagovalec = False
                continue
            izpadli_kolesarji[kolesarjev_cas[0]] = kolesarjev_cas[1]
    izpadli_kolesarji = list(map(lambda x: x[0], sorted(izpadli_kolesarji.items(), key=lambda x: (x[1], x[0]))))
    return izpadli_kolesarji

class Test06(unittest.TestCase):
    def test_01_cas_za_povezavo(self):
        self.assertEqual(4 + 1 + 2, cas_za_povezavo((A, B), dict(gravel=1, trava=2, robnik=3, avtocesta=5, bolt=2)))
        self.assertEqual(4 + 2 + 2, cas_za_povezavo((H, J), dict(gravel=1, trava=2, robnik=2, avtocesta=5, bolt=2)))
        self.assertEqual(4 + 5, cas_za_povezavo((G, I), dict(gravel=1, trava=2, robnik=3, avtocesta=5, bolt=2)))
        self.assertEqual(4, cas_za_povezavo((S, P), dict(gravel=1, trava=2, robnik=3, avtocesta=5, bolt=2)))
        self.assertEqual(4 + 2 + 3, cas_za_povezavo((A, B), pribitki1))
        self.assertEqual(4 + 2 + 1, cas_za_povezavo((B, C), pribitki1))
        self.assertEqual(4 + 3 + 5, cas_za_povezavo((C, R), pribitki1))
        self.assertEqual(4 + 4, cas_za_povezavo((R, D), pribitki1))
        self.assertEqual(4 + 3 + 4, cas_za_povezavo((D, F), pribitki1))
        self.assertEqual(4 + 3 + 1, cas_za_povezavo((F, G), pribitki1))

    def test_02_cas(self):
        self.assertEqual(9 + 7 + 3 * 12 + 8 + 11 + 8, cas("ABCRCRDFG", pribitki1))
        self.assertEqual(9, cas("AB", pribitki1))
        self.assertEqual(7, cas("AB", dict(gravel=1, trava=2, robnik=3, avtocesta=5, bolt=2)))
        self.assertEqual(7 + 21, cas("ABC", dict(gravel=1, trava=2, robnik=3, avtocesta=5, bolt=2, lonci=15)))
        self.assertEqual(8, cas("SPS", dict(gravel=1, trava=2, robnik=3, avtocesta=5, bolt=2, lonci=15)))

    def test_03_povezava_spotike(self):
        self.assertEqual((R, C), povezava_spotike(pribitki1))
        pribitki = pribitki1.copy()
        pribitki["avtocesta"] = 100
        self.assertEqual((M, I), povezava_spotike(pribitki))

        pribitki = dict.fromkeys(pribitki1, 0)  # vsi pribitki so 0, razen:
        pribitki["staopnice"] = pribitki["bolt"] = 1
        self.assertEqual((M, K), povezava_spotike(pribitki))


class Test07(unittest.TestCase):
    def test_01_urnik(self):
        self.assertEqual(dict(A=0, B=9, C=16, R=28, D=60, F=71, G=79), urnik("ABCRCRDFG", pribitki1))

        pribitki = dict.fromkeys(pribitki1, 0)  # vsi pribitki so 0, razen:
        self.assertEqual(dict(A=0, B=4, C=8, R=12, D=24, F=28, G=32), urnik("ABCRCRDFG", pribitki))

        pribitki["lonci"] = 1
        self.assertEqual(dict(A=0, B=4, C=9, R=14, D=28, F=32, G=36), urnik("ABCRCRDFG", pribitki))

    def test_02_skupinski_sport(self):
        self.assertEqual(9 + 7 + 3 * 12 + 8 + 11 + 8, skupinski_sport("ABCRCRDFG", [pribitki1]))
        self.assertEqual(177, skupinski_sport("ABCRCRDFG", [pribitki1, pribitki2]))
        self.assertEqual(177, skupinski_sport("ABCRCRDFG", [pribitki1, pribitki2, pribitki2]))
        self.assertEqual(475, skupinski_sport("ABCRCRDFG", [pribitki1, pribitki2, pribitki2, pribitki3]))

    def test_03_tekma(self):
        # pribitki1 je hitrejši od pribitki2, pribitki2 je hitrejši od pribitki3
        self.assertEqual(0, tekma("ABCRDF", [pribitki2]))
        self.assertEqual(0, tekma("ABCRDF", [pribitki2, pribitki3]))
        self.assertEqual(1, tekma("ABCRDF", [pribitki3, pribitki2]))
        self.assertEqual(2, tekma("ABCRDF", [pribitki3, pribitki2, pribitki1]))
        self.assertIsNone(tekma("ABCRDF", [pribitki1, pribitki2, pribitki1]))
        self.assertIsNone(tekma("ABCRDF", [pribitki3, pribitki1, pribitki2, pribitki1]))
        self.assertIsNone(tekma("ABCRDF", [pribitki3, pribitki1, pribitki1, pribitki2]))
        self.assertEqual(0, tekma("ABCRDF", [pribitki1, pribitki2, pribitki2]))
        self.assertEqual(1, tekma("ABCRDF", [pribitki2, pribitki1, pribitki2]))
        self.assertEqual(2, tekma("ABCRDF", [pribitki2, pribitki2, pribitki1]))


class Test08(unittest.TestCase):
    def test_01_trening(self):
        pribitki = pribitki1.copy()
        self.assertAlmostEqual(4 + 2 + 3, trening("AB", pribitki))

        pribitki = pribitki1.copy()
        self.assertAlmostEqual(4 + 2 + 3 + 4 + 2 * 0.95 + 3 * 0.95, trening("ABA", pribitki))

        pribitki = pribitki1.copy()
        self.assertAlmostEqual(4 + 2 + 3, trening("AB", pribitki))
        self.assertAlmostEqual(4 + 2 * 0.95 + 3 * 0.95, trening("BA", pribitki), "Je nekdo pozabil spremeniti `pribitki`?")

        pribitki = pribitki1.copy()
        self.assertAlmostEqual(75.787025, trening("ABCRCRDFG", pribitki))

    def test_02_zastavice(self):
        # pribitki1 je hiter
        # pribitki2 zmrzne na BC zaradi bolta, potem je hiter
        # pribitki3 zmrzne na BC in CR zaradi loncev
        # pribitki4 je hitro čez BC, na CR, CD, DF ga ustavijo pešci
        self.assertEqual([7], zastavice("ABCRCRDFG", [pribitki1]))
        self.assertEqual([7], zastavice("ABCRCRDFG", [pribitki2]))
        self.assertEqual([7, 0], zastavice("ABCRCRDFG", [pribitki1, pribitki1]))
        self.assertEqual([7, 0], zastavice("ABCRCRDFG", [pribitki1, pribitki2]))
        self.assertEqual([2, 5], zastavice("ABCRCRDFG", [pribitki2, pribitki1]))
        self.assertEqual([5, 2], zastavice("ABCRCRDFG", [pribitki2, pribitki4]))
        self.assertEqual([4, 3], zastavice("ABCRCRDFG", [pribitki3, pribitki4]))
        self.assertEqual([5, 2], zastavice("ABCRCRDFG", [pribitki4, pribitki3]))
        self.assertEqual([5, 2, 0], zastavice("ABCRCRDFG", [pribitki2, pribitki4, pribitki3]))
        self.assertEqual([2, 3, 2], zastavice("ABCRCRDFG", [pribitki3, pribitki2, pribitki4]))


class Test09(unittest.TestCase):
    def test_01_cikel(self):
        try:
            zemljevid2 = zemljevid.copy()
            for p in ((O, P), (I, E)):
                del zemljevid[p]
                del zemljevid[p[::-1]]

            self.assertEqual(3, cikel("A", pribitki1))  # cikel je ABV
            self.assertEqual(3, cikel("B", pribitki1))  # cikel je BVA
            self.assertEqual(16, cikel("R", pribitki1)) # RDFGHJKMNPSTUVBC
            self.assertEqual(16, cikel("U", pribitki1)) # isti
            self.assertEqual(16, cikel("L", pribitki1)) # isti; pazi, ne vsebuje L-ja!
            self.assertEqual(16, cikel("I", pribitki1)) # isti; pazi, ne vsebuje I-ja!

            pribitki = {v: i for i, v in enumerate(sorted(pribitki1))}
            self.assertEqual(3, cikel("B", pribitki))  # cikel je BVA
            self.assertEqual(3, cikel("C", pribitki))  # isti cikel - iz C gre v B
            self.assertEqual(11, cikel("A", pribitki))  # cikel je RDFGIMNPSTU, do njega pride po ABVC
            self.assertEqual(11, cikel("V", pribitki))  # isto
            self.assertEqual(6, cikel("J", pribitki))  # JKMIGH
            self.assertEqual(6, cikel("L", pribitki))  # isto, iz L gre v JKMIGH

        finally:
            zemljevid.update(zemljevid2)


class Test10(unittest.TestCase):
    def test_01_izpadanje(self):
        ni_pribitkov = dict.fromkeys(pribitki1, 0)
        self.assertEqual([], izpadanje(["UVB", "SPIM"], [ni_pribitkov] * 2))
        self.assertEqual([], izpadanje(["UVBCR", "SP"], [ni_pribitkov] * 2))

        # 0 izloči 1 v I
        self.assertEqual([1], izpadanje(["URIE", "TSPIG"], [ni_pribitkov] * 2))
        # 1 izloči 0 v I
        self.assertEqual([0], izpadanje(["TSPIG", "URIE"], [ni_pribitkov] * 2))
        # hkrati v I, vendar je izločen tisti z večjim indeksom
        self.assertEqual([1], izpadanje(["SPIG", "URIE"], [ni_pribitkov] * 2))
        self.assertEqual([1], izpadanje(["URIE", "SPIG"], [ni_pribitkov] * 2))

        # 2 prehiti ostala dva v I
        self.assertEqual([0, 1], izpadanje(["URIE", "SPIG", "GIM"], [ni_pribitkov] * 3))
        self.assertEqual([1, 0], izpadanje(["VURIE", "SPIG", "GIM"], [ni_pribitkov] * 3))

        # 2 ju ne prehiti, ker obstane na avtocesti
        avtocesta = ni_pribitkov.copy()
        avtocesta["avtocesta"] = 100
        self.assertEqual([0, 2], izpadanje(["VURIE", "SPI", "GIM"], [ni_pribitkov, ni_pribitkov, avtocesta]))
        self.assertEqual([0, 1, 2], izpadanje(["VURIE", "SPIG", "GIM"], [ni_pribitkov, ni_pribitkov, avtocesta]))
        self.assertEqual([1, 2, 0], izpadanje(["GIM", "SPIG", "VURIE"], [avtocesta, ni_pribitkov, ni_pribitkov]))

        # ničti izrine prvega (na P), zato prvi na izrine zadnjega, čeprav je ta na I precej pozneje
        self.assertEqual([1], izpadanje(["PNMKJ", "SPI", "GIE"], [ni_pribitkov, ni_pribitkov, avtocesta]))
        # ... isto, s premešanimi mesti
        self.assertEqual([0], izpadanje(["SPI", "PNMKJ", "GIE"], [ni_pribitkov, ni_pribitkov, avtocesta]))
        self.assertEqual([1], izpadanje(["GIE", "SPI", "PNMKJ"], [avtocesta, ni_pribitkov, ni_pribitkov]))
        self.assertEqual([2], izpadanje(["GIE", "PNMKJ", "SPI"], [avtocesta, ni_pribitkov, ni_pribitkov]))
        # ničti izrine prvega na P, drugega na I
        self.assertEqual([1, 2], izpadanje(["PNMIR", "SPI", "GIE"], [ni_pribitkov, ni_pribitkov, avtocesta]))
        # ... isto, s premešanimi mesti
        self.assertEqual([0, 2], izpadanje(["SPI", "PNMIR", "GIE"], [ni_pribitkov, ni_pribitkov, avtocesta]))
        self.assertEqual([2, 0], izpadanje(["GIE", "PNMIR", "SPI"], [avtocesta, ni_pribitkov, ni_pribitkov]))
        self.assertEqual([2, 1], izpadanje(["PNMIR", "GIE", "SPI"], [ni_pribitkov, avtocesta, ni_pribitkov]))
        self.assertEqual([2, 1], izpadanje(["SPI", "GIE", "SPI"], [ni_pribitkov, avtocesta, ni_pribitkov]))
        # ničti izrine prvega, zatem pa drugi ničtega na I (ker nima pribitka na avtocesti!)
        self.assertEqual([1, 0], izpadanje(["PNMIR", "SPI", "GIE"], [ni_pribitkov, ni_pribitkov, ni_pribitkov]))

        # vmes se še tretji ustreli v nogo
        self.assertEqual([1 ,3, 0], izpadanje(["PNMIR", "SPI", "GIE", "DFD"], [ni_pribitkov] * 4))
        # ničti izrine prvega na P, drugega na I
        self.assertEqual([1, 3, 2], izpadanje(["PNMIR", "SPI", "GIE", "DFD"], [ni_pribitkov, ni_pribitkov, avtocesta, ni_pribitkov]))

        pribitki5 = dict(gravel=4, trava=1, lonci=5, bolt=0, pešci=2,
                         stopnice=4, avtocesta=1, črepinje=3, robnik=3,
                         rodeo=2)
        pribitki6 = dict(gravel=1, trava=1, lonci=2, bolt=3, pešci=1,
                         stopnice=1, avtocesta=3, črepinje=1, robnik=2,
                         rodeo=4)
        self.assertEqual([1, 3, 4, 0], izpadanje(["ABCRVUTSP", "DRCBVUT", "EI", "GHJKMNPOPS", "SPNMK"],
                                       [pribitki1, pribitki5, pribitki1, pribitki6, pribitki1]))
        self.assertEqual([1, 4, 3, 0], izpadanje(["ABCRVUTSP", "DRCBVUT", "EI", "GHJKMNPOPS", "SPNMK"],
                                       [pribitki5, pribitki5, pribitki6, pribitki1, pribitki1]))


if __name__ == "__main__":
    unittest.main()
