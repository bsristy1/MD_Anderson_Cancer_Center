# HLA Peptide Sequence Database

This project creates a large-scale ****HLA binding affinities database**** to support cancer immunotherapy research and vaccine development. Using machine learning predictors such as HLAthena** and NetMHCpan, the database maps binding affinities between HLA alleles and peptide sequences from the human proteome.

The work was developed in **PyCharm 2022.1.3** with outputs transferred to **MySQL** for planned integration with a web application.

---

## Abstract

As immunotherapies evolve, datasets and prediction algorithms play a critical role in identifying promising vaccine targets. This project builds a database from the complete **human proteome (>20 GB)** containing:

- **Table 1 (table1.csv)**  
  Contains 79,684 protein entries from the human proteome. Each entry is formatted in FASTA style, with two components:
  1. **Protein identifier line** — includes metadata such as protein ID, protein name, organism, taxonomy ID, gene name, protein evidence level, and sequence version.  
     Example:  
     ```
     >sp|Q12888|TP53B_HUMAN TP53-binding protein 1 OS=Homo sapiens OX=9606 GN=TP53BP1 PE=1 SV=2
     ```
     - `sp|Q12888|` → UniProt ID  
     - `TP53B_HUMAN` → Protein name (TP53-binding protein 1)  
     - `OS=Homo sapiens` → Organism species  
     - `OX=9606` → NCBI taxonomy ID  
     - `GN=TP53BP1` → Gene name  
     - `PE=1` → Protein existence evidence (1 = experimental evidence)  
     - `SV=2` → Sequence version  
     
  2. **Protein sequence line** — amino acid sequence of the protein.  
     Example:  
     ```
     IEKEGQRKWYKRMAVILSLEQGNRLREQYGLGPYEAVTPLTKAADISLDNLVEGKRKRRSNVSSPATPTASSSSSTTPTRA
     ```

- **Table 2 (table2.csv)**  
  Contains ~121,829,814 entries of peptides (8–11 amino acids) derived from the proteins in Table 1.  
  For each peptide, the table stores:  
  - Protein ID it was derived from  
  - Start and end positions within the protein  
  - 10 amino acids before and after the peptide (context)  
  - Peptide length (8, 9, 10, or 11)  

  (This file was too large to upload to the repository)

- **Table 3 (table3.csv)**  
  Contains 1,089 entries of predicted peptide–HLA allele binding affinities. Each entry includes:  
  - Peptide sequence  
  - Peptide length  
  - Binding affinity score (msi)  
  - Best allele interaction (`best_msi_allele`)  
  - Context amino acids and ranking information  

  (This file was too large to upload to the repository)

- **Bar Plot**  
  A Matplotlib-generated visualization of unique vs repeated peptide sequences in the human proteome.  
  - X-axis: number of repeats  
  - Y-axis: number of peptide sequences (log scale)  
  - Example: ~22 million peptide sequences are unique.

---

## Impact

This database serves as a **baseline reference** for querying binding affinities and peptide–protein relationships. Applications include:

- Faster data retrieval for immunotherapy research.  
- Benchmarking peptide–allele interactions.  
- Understanding how mutations affect binding affinities.  
- Supporting future tools for **antigen and neoantigen competition analysis**.  

---

## Technology

- **Python (PyCharm 2022.1.3)**  
- **Matplotlib** for visualization  
- **MySQL** for database web app backend  

---

## Planned Web App

A web interface is proposed to allow users to:
- Input a peptide sequence → retrieve binding affinities and context.  
- Input a protein sequence → retrieve protein and peptide metadata.  

Prototype queries were written in MySQL and backend code was prepared as a blueprint.

---

## Repository Structure

