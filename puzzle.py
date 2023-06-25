from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")
BNothing = Symbol("B says nothing")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And( 
    And(Or(AKnight, AKnave),Not(And(AKnight, AKnave))), # Can't be both at the same time :) Exclusive or
    
    Implication(AKnight, And(AKnight, AKnave)), # If Knight says then its true
    Implication(AKnave, Not(And(AKnave, AKnight))) # If Knave says then its false
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))), # A Cant be both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))), # B cant be both

    Implication(AKnight, And(AKnave, BKnave)), # If knights says
    Implication(AKnave, Not(And(AKnave, BKnave))), # IF Knvae says

    # B says nothing -> no information 
    
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))), # A Cant be both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))), # B cant be both

    Implication(AKnight, BKnight),          # IF Knight says A
    Implication(AKnave, Not(BKnave)),       # If knave says A

    Implication(BKnight, AKnave),           # If knight says B
    Implication(BKnave, Not(AKnight))       # If knave says B
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))), # A Cant be both
    And(Or(BKnight, BKnave), Not(And(AKnight, AKnave))), # B cant be both
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))), # C cant be both
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
