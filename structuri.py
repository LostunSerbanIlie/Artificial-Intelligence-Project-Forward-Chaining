class Predicat:
    def __init__(self, nume, argumente):
        """
        Initializeaza un predicat cu un nume si o lista de argumente.
        :param nume: Numele predicatului (string)
        :param argumente: Lista de argumente (list)
    
        """
        self.nume = nume
        self.argumente = argumente

    def __repr__(self):
        """
        Reprezinta predicatul ca un string in formatul "nume(arg1, arg2, ...)".
        :return: String care reprezinta predicatul
        """
        args_str = ', '.join(self.argumente)
        return f"{self.nume}({args_str})"
    
    def __eq__(self, other):
        """
        Compara doua instante de Predicat pentru egalitate.
        :param other: Alta instanta de Predicat
        :return: True daca sunt egale, False altfel
        """
        if not isinstance(other, Predicat):
            return False
        return self.nume == other.nume and self.argumente == other.argumente
    
    def __hash__(self):
        """
        Returneaza hash-ul predicatului pentru a permite utilizarea in seturi si dictionare.
        :return: Hash-ul predicatului
        """
        return hash(str(self))
    
    class Regula:
        def __init__(self, premise, concluzie):
            """
            Initializeaza o regula cu premise si o concluzie.
            Reprezinta o reula de tip IF premise THEN concluzie.
            :param premise: Lista de predicate care reprezinta premisele (list)
            :param concluzie: Predicat care reprezinta concluzia (Predicat)
            """
            self.premise = premise
            self.concluzie = concluzie

        def __repr__(self):
            """
            Reprezinta regula ca un string in formatul "IF premise1 ^ premise2 ^ ... THEN concluzie".
            :return: String care reprezinta regula
            """
            premises_str = ' ^ '.join([str(p) for p in self.premise])
            return f"IF {premises_str} THEN {self.concluzie}"