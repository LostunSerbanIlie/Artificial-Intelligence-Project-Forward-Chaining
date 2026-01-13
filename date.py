# Reprezinta date de test pentru sistemul de inferenta prin lantuire inainte
# Fiecare functie returneaza un set de fapte si reguli specifice unui domeniu
from structuri import Predicat, Regula

def get_date_inegalitati():
    """
    Returneaza un set de fapte si reguli pentru inegalitati. \n
    :return: Tuple (fapte, reguli)
    """
    # fapte: A > B, B > C, C > D
    fapte = [
        Predicat("MaiMare", ["A", "B"]),
        Predicat("MaiMare", ["B", "C"]),
        Predicat("MaiMare", ["C", "D"]),
    ]

    # regula: tranzitivitatea inegalitatii
    reguli = [
        Regula(
            premise=[Predicat("MaiMare", ["x", "y"]), Predicat("MaiMare", ["y", "z"])],
            concluzie=Predicat("MaiMare", ["x", "z"])
        )
    ]

    return reguli, fapte

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
            premise=[Predicat("Submultime", ["s1", "s2"]), Predicat("Submultime", ["s2", "s3"])],
            concluzie=Predicat("Submultime", ["s1", "s3"])
        ),

        # regula: daca x este element al lui A si A este subset al lui B, atunci x este element al lui B
        Regula(
            premise = [Predicat("Element", ["elem", "s1"]), Predicat("Submultime", ["s1", "s2"])],
            concluzie = Predicat("Element", ["elem", "s2"])
        )
    ]

    return reguli, fapte