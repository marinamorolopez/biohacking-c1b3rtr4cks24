# biohacking-c1b3rtr4cks24
This repository includes the slides of the public presentation 'Biohacking con Python' of C1B3RTR4CKS 2024 and both the code and files used for the practical case (slide 35 onwards).

## Installation
You simply have to download the .py and fasta files (or get your own fasta files from a database as [NCBI](https://www.ncbi.nlm.nih.gov/)).

## Usage
First you'll have to select the file of your gene of interest. Then introduce the mutation type (knock-in or knock-out) as in/out. If case of a knock-in, you'll have to specify if the DNA change is in the middle or at the end of the gene as mid/end. In case of a knock-in in the middle of the gene, you'll have to introduce the position of the mutation (as a positive integer) and the new base in that position (as a single upper case letter among A/T/C/G). In case of a knock-in at the end of the gene, you'll have to select the file of the plasmid of interest (the DNA sequence you want to add to that gene). When finished, you'll have three .txt files saved in the same folder of the .py file with the RNA guide, the DNA mold and the mutated sequence.
If you want to recreate the example of the slides just use the provided fasta files with the mutations of the practical case:
- Knock-out of the IRF4 gene
- Knock-in in the middle of the AR gene (position 363, new base T)
- Knock-in of the GFP fasta sequence at the end of the TYR gene

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
