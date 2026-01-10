# Reprezinta date de test pentru sistemul de inferenta prin lantuire inainte
# Fiecare functie returneaza un set de fapte si reguli specifice unui domeniu
from structuri import Predicat, Regula

def get_date_inegalitati():
    """
    Returneaza un set de fapte si reguli pentru inegalitati. \n
    :return: Tuple (fapte, reguli)
    """
    # fapte: a > b, b > c, c > d
    fapte = [
        Predicat("MaiMare", ["a", "b"]),
        Predicat("MaiMare", ["b", "c"]),
        Predicat("MaiMare", ["c", "d"]),
    ]

    # regula: tranzitivitatea inegalitatii
    reguli = [
        Regula(
            premise=[Predicat("MaiMare", ["x", "y"]), Predicat("MaiMare", ["y", "z"])],
            concluzie=Predicat("MaiMare", ["x", "z"])
        )
    ]

    return fapte, reguli

def get_date_multimi():
    """
    Returneaza un set de fapte si reguli pentru multimi. \n
    :return: Tuple (fapte, reguli)
    """
    # fapte: A este subset al lui B, B este subset al lui C
    fapte = [
        Predicat("Element", ["5", "A"]),
        Predicat("Submultime", ["A", "B"]),
        Predicat("Submultime", ["B", "C"])
    ]

    # regula: daca A este subset al lui B si B este subset al lui C, atunci A este subset al lui C
    reguli = [
        Regula(
            premise=[Predicat("Submultime", ["S1", "S2"]), Predicat("Submultime", ["S2", "S3"])],
            concluzie=Predicat("Submultime", ["S1", "S3"])
        ),

        # regula: daca x este element al lui A si A este subset al lui B, atunci x este element al lui B
        Regula(
            premise = [Predicat("Element", ["elem", "S1"]), Predicat("Submultime", ["S1", "S2"])],
            concluzie = Predicat("Element", ["elem", "S2"])
        )
    ]

    return fapte, reguli