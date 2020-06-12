

INPUT_PATH = 'sample2.txt'


def get_input(path):
    with open(path, 'r') as f:
        return f.readlines()

#
# def replace_at(molecule, src_atom, dest_atom, n):
#     """
#     Return a molecule with the n-th appearance of src_atom in molecule replaced with the dest_atom.
#     """
#     event_count = 0
#     for index in range(0, len(molecule), len(src_atom)):
#         if molecule[index:index+len(src_atom)] == src_atom:
#             print(molecule[index:index+len(src_atom)])
#             event_count += 1


def make_distinct_molecules(replacements, molecule):
    distinct_molecules = set()

    for src_atom, dest_atom in replacements:
        for index in range(0, len(molecule), len(src_atom)):
            if molecule[index:index+len(src_atom)] == src_atom:
                new_molecule = ''.join([molecule[:index], dest_atom, molecule[index+len(src_atom):]])
                distinct_molecules.add(new_molecule)
    return distinct_molecules


def main():
    print('Advent of Code 2015')
    content = get_input(INPUT_PATH)
    replacements = [replacement.strip().split(' => ') for replacement in content[:-2]]
    medicine_molecule = content[-1]

    distinct_molecules = make_distinct_molecules(replacements, medicine_molecule)
    print(len(distinct_molecules))



if __name__ == '__main__':
    main()