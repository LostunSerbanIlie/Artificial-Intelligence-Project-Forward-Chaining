# Utilitare pentru rularea demonstratiilor
from inferenta import forward_chaining

def ruleaza_demonstratie(nume_problema, functie_incarcare_date):
    """
    Ruleaza o demonstratie a algoritmului de inferenta prin lantuire inainte pentru o problema data. \n
    :param nume_problema: Numele problemei (string)
    :param functie_incarcare_date: Functia care incarca datele (fapte si reguli) pentru problema
    :return: None
    """
    print(f"\n{'='*60}")
    print(f" DEMONSTRATIE: {nume_problema}")
    print(f"{'='*60}")

    # 1. Incarcam datele
    reguli, fapte_initiale = functie_incarcare_date()

    print("\n[Step 1] Baza de cunostinte initiala (Premise):")
    for f in fapte_initiale:
        print(f"  - {f}")

    print("\n[Step 2] Regulile disponibile:")
    for r in reguli:
        print(f"  - {r}")

    # 2. Executam algoritmul
    print("\n[Step 3] Executie Motor de Inferenta...")
    fapte_finale = forward_chaining(reguli, fapte_initiale)

    # 3. Afisam rezultatul
    print(f"\n{'-'*30}")
    print(" Concluzii deduse: ")
    print(f"{'-'*30}")
    
    for i, fapt in enumerate(fapte_finale, 1):
        # Marcam vizual faptele noi
        status = "(Initial)" if fapt in fapte_initiale else "--> Dedus"
        print(f"{i}. {fapt} {status}")
        
    print("\n")