
INPUT_PATH = '../sample.txt'
STARTING_MOLECULE = 'e'
MOLECULE_SEARCH_LIMIT = 1000


def get_input(path):
    with open(path, 'r') as f:
        return f.readlines()


def make_distinct_molecules(replacements, molecule):
    distinct_molecules = set()

    for src_atom, dest_atom in replacements:
        for index in range(0, len(molecule)):
            if molecule[index:index+len(src_atom)] == src_atom:
                new_molecule = ''.join([molecule[:index], dest_atom, molecule[index+len(src_atom):]])
                distinct_molecules.add(new_molecule)
    return distinct_molecules


def look_for_medicine_b(replacements, queue, end_molecule, mapping):
    molecule = queue.pop()
    distinct_molecules = make_distinct_molecules(replacements, molecule)

    for distinct_molecule in distinct_molecules:
        if distinct_molecule == end_molecule:
            mapping.append((molecule, distinct_molecule))
            return mapping
        else:
            queue.insert(0, distinct_molecule)
            mapping.append((molecule, distinct_molecule))
    return look_for_medicine_b(replacements, queue, end_molecule, mapping)


def look_for_medicine_a(replacements, queue, end_molecule, count):
    molecule = queue.pop()

    if molecule == end_molecule:
        return count
    elif count > MOLECULE_SEARCH_LIMIT:
        raise Exception('Exceeded limit of search')

    distinct_molecules = make_distinct_molecules(replacements, molecule)

    for distinct_molecule in distinct_molecules:
        queue.insert(0, distinct_molecule)
    return 1 + look_for_medicine_a(replacements, queue, end_molecule, count)


def search_mappings(mappings, start_molecule, end_molecule):
    for prev, current in mappings:
        if current == end_molecule:
            if prev == start_molecule:
                return 1
            return 1 + search_mappings(mappings, start_molecule, prev)


def count_to_medicine(replacements, starting_molecule, end_molecule):
    queue = [starting_molecule]
    mappings = look_for_medicine_b(replacements, queue, end_molecule, [])
    return search_mappings(mappings, starting_molecule, end_molecule)


def look_for_medicine_c(replacements, starting_molecule, end_molecule):
    queue = [starting_molecule]
    distinct_molecules = set()
    count = 0

    while end_molecule not in distinct_molecules and len(queue) != 0:
        molecule = queue.pop()
        distinct_molecules.update(make_distinct_molecules(replacements, molecule))
        count += 1

        print(distinct_molecules)

        for distinct_molecule in distinct_molecules:
            queue.insert(0, distinct_molecule)

    return count


def main():
    print('Advent of Code 2015')
    content = get_input(INPUT_PATH)
    replacements = [replacement.strip().split(' => ') for replacement in content[:-2]]
    medicine_molecule = content[-1].strip()

    print(look_for_medicine_c(replacements, STARTING_MOLECULE, medicine_molecule))


if __name__ == '__main__':
    main()
