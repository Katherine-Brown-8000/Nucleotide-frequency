seq = "ATCGATCG"

def nucleotide_frequency(seq):
    A_count = 0
    T_count = 0
    G_count = 0
    C_count = 0
    
    seq_length = len(seq)
    
    for nuc in seq:
        if nuc == "A":
            A_count += 1
        if nuc == "T":
            T_count += 1
        if nuc == "G":
            G_count += 1
        if nuc == "C":
            C_count += 1
            
    A_F = A_count / seq_length
    T_F = T_count / seq_length
    G_F = G_count / seq_length
    C_F = C_count / seq_length
    
    return A_F, T_F, G_F, C_F

A_F, T_F, G_F, C_F = nucleotide_frequency(seq)

print(f"A: {A_F}% of sequence")
print(f"T: {T_F}% of sequence")
print(f"G: {G_F}% of sequence")
print(f"C: {C_F}% of sequence")
