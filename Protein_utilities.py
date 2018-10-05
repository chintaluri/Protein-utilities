def valid_protein_seq(protein):
    # This function checks if given protein sequence has valid amino acids and gives you the position of the invalid amino acid

    for i in range(len(protein)):
        if protein[i] not in 'ACDEFGHIKLMNPQRSTVWY': # These are the valid amino acid 1-letter abbreviations
            print('protein contains invalid amino acid {} at position {}'.format(protein[i], i))