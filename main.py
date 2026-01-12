from date import get_date_inegalitati, get_date_multimi
from utils import ruleaza_demonstratie

if __name__ == "__main__":
    # problema 1
    ruleaza_demonstratie(
        "Tranzitivitatea Inegalitatilor (Algebra)", 
        get_date_inegalitati
    )

    # problema 2
    ruleaza_demonstratie(
        "Incluziunea Multimilor (Set Theory)", 
        get_date_multimi
    )