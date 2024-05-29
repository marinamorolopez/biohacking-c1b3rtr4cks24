# -*- coding: utf-8 -*-

"""

Created on Tue Nov  9 17:56:55 2021
@author: Marina Moro López

"""

from tkinter.filedialog import askopenfile

def main():
    
    gene_file = askopenfile(mode='r')
    gene_seq = gene_file.readlines()[1:]
    gene_seq = ''.join(gene_seq).replace('\n', '')

    mutation_type = input("Introduce mutation type (in/out): ")
    
    while mutation_type != 'in' and mutation_type != 'out':
        print('Invalid input.')
        mutation_type = input("Introduce mutation type (in/out): ")
    
    if mutation_type == "in":
        
        knockin_type = input("Introduce the knock-in position in the gene (mid/end): ")
        while knockin_type != 'mid' and knockin_type != 'end':
            print('Invalid input.')
            knockin_type = input("Introduce the knock-in position in the gene (mid/end): ")
            
        if knockin_type == "mid":
            DNA_guide, mutated_gene_seq, mold = knock_in_mid(gene_seq)
        elif knockin_type == "end":
            DNA_guide, mutated_gene_seq, mold = knock_in_end(gene_seq)
            
    else:
        DNA_guide, mutated_gene_seq, mold = knock_out(gene_seq)

    mutated_gene_file = open('MUTATED_SEQUENCE.txt', 'w')
    mutated_gene_file.write(mutated_gene_seq)
    mutated_gene_file.close()

    guide_file = open('GUIDE.txt', 'w')
    guide_file.write(DNA_to_RNA(DNA_guide))
    guide_file.close()

    mold_file = open('MOLD.txt', 'w')
    mold_file.write(mold)
    mold_file.close()


def knock_in_mid(gene_seq):
    
    mutation_position = int(input("Introduce the numeric position of the mutation base (e.g. 1, 25, 203): "))
    while mutation_position <= 0:
        print('Invalid input. Introduce positive integer. ')
        mutation_position = int(input("Introduce the numeric position of the mutation base (e.g. 1, 25, 203): "))
    
    mutation_base = input("Introduce the new base corresponding to the defined mutation position in upper case (A/T/G/C): ")
    while mutation_base != 'A' and mutation_base != 'T' and mutation_base != 'G' and mutation_base != 'C':
        print('Invalid input. ')
        mutation_base = input("Introduce the new base corresponding to the defined mutation position (A/T/G/C): ")
            
    DNA_guide = gene_seq[mutation_position-25:mutation_position+25]
    mutated_gene_seq = gene_seq[:mutation_position-1] + mutation_base + gene_seq[mutation_position:]
    mold = mutated_gene_seq[mutation_position-25:mutation_position+25]
    
    return DNA_guide, mutated_gene_seq, mold


def knock_in_end(gene_seq):

    plasmid_file = askopenfile(mode='r')
    plasmid_seq = plasmid_file.readlines()[1:]
    plasmid_seq = ''.join(plasmid_seq).replace('\n', '')
            
    DNA_guide = gene_seq[len(gene_seq)-50:len(gene_seq)]
    mutated_gene_seq = gene_seq + plasmid_seq
    mold = DNA_guide + plasmid_seq
    
    return DNA_guide, mutated_gene_seq, mold


def knock_out(gene_seq):
    
    DNA_guide = gene_seq
    mutated_gene_seq = ""
    mold = ""
    
    return DNA_guide, mutated_gene_seq, mold


def DNA_to_RNA(DNA_guide):
    
    RNA_guide = ""
    for base in DNA_guide:
        if base == "T":
            RNA_guide += "A"
        elif base == "A":
            RNA_guide += "U"
        elif base == "C":
            RNA_guide += "G"
        elif base == "G":
            RNA_guide += "C"
    
    return RNA_guide


main()