import random

atomsDecayed = 0
remainingAtoms = 0

numberOfAtoms = int(input("How many atoms are there: ")) # User inputs number of atoms in the simulation

for x in range(numberOfAtoms): # Assign 0 or 1 for each atom the user said there are in the simulation
    decayed = random.randint(0,1) # the status of atom is here, it's either 0 or 1

    if decayed == 0: # if the status of decayed is 0, that means the atom decayed
        atomsDecayed += 1 # Increase the count of atoms decayed
    else: # if the status of decayed is not 0 (so 1), that atom still reamins
        remainingAtoms += 1 # incrase the count of atoms remaining

print("Atoms Remaining: ", remainingAtoms )
print("Atoms Decayed:", atomsDecayed)
    
    