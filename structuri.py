# Reprezinta structura unui predicat si a unei reguli in logica de tip Horn
# Un predicat are un nume si o lista de argumente
# O regula are o lista de premise (predicate) si o concluzie (predicat)
class Predicat:
    def __init__(self, nume, argumente):
        """
        Initializeaza un predicat cu un nume si o lista de argumente. \n
        :param nume: Numele predicatului (string)
        :param argumente: Lista de argumente (list)
    
        """
        self.nume = nume
        self.argumente = argumente

    def __repr__(self):
        """
        Reprezinta predicatul ca un string in formatul "nume(arg1, arg2, ...)". \n
        :return: String care reprezinta predicatul
        """
        args_str = ', '.join(self.argumente)
        return f"{self.nume}({args_str})"
    
    def __eq__(self, other):
        """
        Compara doua instante de Predicat pentru egalitate. \n
        :param other: Alta instanta de Predicat
        :return: True daca sunt egale, False altfel
        """
        if not isinstance(other, Predicat):
            return False
        return self.nume == other.nume and self.argumente == other.argumente # daca numele si argumentele sunt identice atunci sunt egale
    
    def __hash__(self):
        """
        Returneaza hash-ul predicatului pentru a permite utilizarea in seturi si dictionare. \n
        :return: Hash-ul predicatului după reprezentarea sa ca string
        """
        return hash(str(self))
    
    # reprezinta structra IF-THEN -> clauza Horn
class Regula:
    def __init__(self, premise, concluzie):
        """
        Initializeaza o regula cu premise si o concluzie. 
        Reprezinta o reula de tip IF premise THEN concluzie. \n
        :param premise: Lista de predicate care reprezinta premisele (list)
        :param concluzie: Predicat care reprezinta concluzia (Predicat)
        """
        self.premise = premise
        self.concluzie = concluzie

    def __repr__(self):
        """
        Reprezinta regula ca un string in formatul "IF premise1 ^ premise2 ^ ... THEN concluzie". \n
        :return: String care reprezinta regula de forma IF *premise* THEN *concluzie*
        """
        premises_str = ' ^ '.join([str(p) for p in self.premise])
        return f"IF {premises_str} THEN {self.concluzie}"