from typing import Sequence

from rdkit import Chem


def get_all_unique_molecules(molecules: Sequence[Chem.Mol]) -> Sequence[Chem.Mol]:
    """Returns all unique molecules."""
    all_smiles = []
    for mol in molecules:
        try:
            all_smiles.append(Chem.MolToSmiles(mol))
        except Exception as e:
            print(f"Could not convert molecule to SMILES: {e}")
            import pickle
            with open("error_mol.pkl", "wb") as f:
                pickle.dump(mol, f)
            continue
    seen_smiles = set()
    unique_molecules = []
    for mol, smiles in zip(molecules, all_smiles):
        if smiles in seen_smiles:
            continue
        seen_smiles.add(smiles)
        unique_molecules.append(mol)
    return unique_molecules
