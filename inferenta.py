# Algoritmul de inferenta prin lantuire inainte
# Porneste de la un set initial de fapte si aplica regulile pentru a deduce fapte noi
from structuri import Predicat
import copy # pentru deepcopy 

def is_variable(term):
    """
    Verifica daca un termen este o variabila. \n
    :param term: termenul de verificat
    :return: True daca termenul este o variabila, altfel False
    """

    return term.islower()

def substitute(predicat, substitutes):
    """
    Aplica un dictionar de substitutii unui predicat. \n
    Ex: Predicat MaiMare(x, z) cu {'x': 'a', 'z': 'c'} -> MaiMare(a, c) \n
    :param predicat: Predicatul asupra caruia se aplica substitutiile
    :param substitutes: dictionar cu substitutii {variabila: valoare}
    """
    new_arguments = []
    for arg in predicat.argumente:
        # daca argumentul este o cheie in dictionar, il subsitiuim cu val corespunzatoare
        if arg in substitutes:
            new_arguments.append(substitutes[arg])
        else:
            new_arguments.append(arg)

    return Predicat(predicat.nume, new_arguments)

def unify(pred_rule, pred_fact, current_sub):
    """
    Incearca sa unifice un predicat dintr-o regula cu un predicat din fapte,
    actualizand dictionarul de substitutii curent. \n
    :param pred_rule: Predicatul din regula
    :param pred_fact: Predicatul din fapte
    :param current_sub: Dictionarul curent de substitutii {variabila: valoare}
    :return: Dictionar actualizat de substitutii daca unificarea reuseste, altfel None  
    """

    # verificam daca predicatele au acelasi nume si acelasi numar de argumente
    if pred_rule.nume != pred_fact.nume:
        return None
    if len(pred_rule.argumente) != len(pred_fact.argumente):
        return None
    
    # copie pentru a nu modifica dictionarul original in caz de esec
    new_sub = current_sub.copy()

    # luam argumentele pereche cu pereche
    for arg_rule, arg_fact in zip(pred_rule.argumente, pred_fact.argumente):
        if is_variable(arg_rule):
            # daca este variabila si a fost deja legata in substitutii, verificam consistenta
            if arg_rule in new_sub:
                if new_sub[arg_rule] != arg_fact:
                    return None # inconsitenta
            else:
                # daca nu a fost legata, o legam acum
                new_sub[arg_rule] = arg_fact
        else:
            # daca nu este variabila, trebuie sa fie egala cu argumentul din fapte
            if arg_rule != arg_fact:
                return None # nu se unifica
            
    return new_sub

def match_premise(premise, known_facts, current_sub):
    """
    Functie recursiva pentru a potrivi toate premisele unei reguli cu faptele cunoscute. \n
    :param premise: Lista de predicate care reprezinta premisele unei reguli
    :param known_facts: Setul de fapte cunoscute
    :param current_sub: Dictionarul curent de substitutii {variabila: valoare}
    :return: Lista de dictionare de substitutii care satisfac toate premisele
    """

    # caz de baza: toate premisele au fost potrivite
    if not premise:
        return [current_sub]
    
    results = []
    first_premise = premise[0]
    rest_premises = premise[1:]

    # aplic substitutiile curente premisei curente
    processed_premise = substitute(first_premise, current_sub)

    # cautam in baza de fapte ceva ce se potriveste cu premisa curenta
    for fact in known_facts:
        new_subs = unify(processed_premise, fact, current_sub)

        if new_subs is not None:
            # daca s a gasit o potrivire pentru premisa curenta, continuam cu restul premiselor
            rest_results = match_premise(rest_premises, known_facts, new_subs)
            results.extend(rest_results)

    return results


def forward_chaining(rules, initial_facts):
    """
    Algoritmul de inferenta prin lantuire inainte (Rationament inainte). \n
    :param rules: Lista de reguli (Regula)
    :param initial_facts: Setul initial de fapte (set de Predicat)
    :return: Setul final de fapte dupa aplicarea inferentei (set de Predicat)
    """

    current_facts = list(initial_facts) # lista de fapte cunoscute - copie pentru a nu modifica setul initial
    step = 1
    new_added_fact = True

    print("\n Pornire inferenta prin lantuire inainte...\n")

    while new_added_fact:
        new_added_fact = False
        print(f"\n Current step: {step}")

        # luam fiecare regula si incercam sa o aplicam
        for rule in rules:
            # cautam toate modurile in care se poate aplica regula
            possible_substitutions = match_premise(rule.premise, current_facts, {})

            for subs in possible_substitutions:
                # generare concluzie pe baza substitutiilor gasite
                conclusion = substitute(rule.concluzie, subs)

                # daca concluzia nu este deja in fapte, o adaugam
                if conclusion not in current_facts:
                    print(f" Aplic Regula: {rule} \n Unificare: {subs} \n Noua concluzie adaugata: {conclusion}\n")
                    current_facts.append(conclusion)
                    new_added_fact = True

        step += 1
        if not new_added_fact:
            print(" Nu s au mai adaugat fapte noi. Algoritmul se opreste.")

    return current_facts