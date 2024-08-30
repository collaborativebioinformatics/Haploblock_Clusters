> BCM / DNAnexus Hackathon 2024

# Haploblock_Clusters

## Contributors

## Introduction

Our overarching goal is to link the SV information from a sample with the population haplotype block. In theory, our genome consists of multiple haplotype blocks that are shared among the individuals from all populations. At any given locus, certain haplotypes are more prone to the disease than others depending on the type of variation they carry. Thus, linking the mutation information with the haplotype would enhance our understanding of the implications of a given mutation (or variation) and relatedness between individuals in a population. In this hackathon, we aim to develop a pipeline (or workflow) that would enable us to do so.

We are taking the help of existing tools for phasing (SHAPEIT and IMPUTE) and relatedness calculation (ARG-Needle) to obtain the haplotype blocks containing SV information and their relatedness with each other. We then create a similarity matrix for the haplotype blocks for all samples within different populations. We further link this information to SVs (in vcf file).


# Haplotype blocks in one individual arederived from the population 

![image](https://github.com/user-attachments/assets/cc02f217-4e04-4904-90ab-a228b9f5edf2)

## Methods

We built a DNAnexus applet which takes vcf files as an input and generates similarity matrix among the haplotype blocks as an output. The process involves multiple steps where first, the vcf files are phased by SHAPEIT5 to generate .map file for genetic map and by IMPUTE to generate .hap file. Both .map and .hap files are provided as an input for ARG-Needle which generates graphs for the haplotype blocks. A custom script then calculates relatedness between haplotype blocks. 
To test our workflow, we leveraged the genomic data for chromosome 6 from 1000 Genome Project for three populations (each population containing 100 individuals), namely Dai Chinese (CDX), Puerto Rican from Puerto Rico (PUR), British from England and Scotland (GBR). 

During the hackathon, we developed a prototype workflow for haplotype block similarity calculation. Firstly, as the proof-of-concept, we took phased VCF files from 1000Genomes for chromosome 6 from 3 populations. The VCF files had been phased with SHAPEIT2. Then, we used Plink2 to convert the phased VCF files to HAP files (`plink2 --vcf phased.vcf --export hap --out new_filename_prefix`). We used this data as input for ARG-needle (documentation: https://palamaralab.github.io/software/argneedle/manual/).

### Workflow

<img width="316" alt="image" src="https://github.com/user-attachments/assets/92e0c5fc-49ea-440a-a004-c9e34468fa12">

## Results

We leverage the principles of ancestral recombination graph (ARG) that are used to determine how ancestral genetic material is passed onto its descendants considering the coalescent time and recombination. ARG-Needle program can infer history of inheritance from hundreds of thousands of genome samples. 

## Use cases
  - rare germline mutations
  - cancer driver mutations
  - MHC

## Future directions

## Data

1000Genomes

We downloaded phased VCFs (shapeit2) for 3 populations:
- British in England and Scotland (GBR): https://www.internationalgenome.org/data-portal/population/GBR
- Puerto Rican in Puerto Rico (PUR): https://www.internationalgenome.org/data-portal/population/PUR
- Chinese Dai in Xishuangbanna, China (CDX): https://www.internationalgenome.org/data-portal/population/CDX
 
As well as a genetic map from: ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/pilot_data/technical/reference/genetic_map_b36.tar.gz

## DNAnexus prototype workflow

<img width="1143" alt="image" src="https://github.com/user-attachments/assets/b20014b7-da86-499b-92d1-b5a9837554d1">

## Hackathon plan

### Step 1:

- Download phased vcfs from 1000 genome for one chromosome (Jedrzej)
- Get the data in xcf format - understand xcf format, how haplotype information is saved in haploblocks.  Need the .hap file.  (Minal/Elena/Umran) 
- Get ARG-needle working on DNANexus (Ben and Minal)
- Get SHAPEIT5 working on DNAnexus (Ben and Jedrzej)
- Get the similarity matrix (Jedrzej)
- Figure out way to merge rare variants information to the haploblocks (Michael and Jedrzej)
  
        Rare variants are identified and extracted using bcftools based on a MAF threshold of less than 1%.
        The extracted variants are annotated with functional and genomic information using ANNOVAR.
        Using bedtools, these variants are mapped to haploblocks
  
- Figure out way to look at cancer drivers (Michael and Elena)
- Figure out way to look at MHC/HLA/TCR (Minal and Umran)

  Major histocompatibility complex (MHC) on chromosome 6 of the human genome is a highly complex and polymorphic region crucial for immune system function, particularly through the Human Leukocyte Antigen (HLA) region, which presents antigens to T-cells. We can extract the MHC variants using bcftools with view functionality, specifying ~5MB MHC regions genomic location(chr6:28510020-33480577, GRCh38), or the bed file obtained conventionally from fasta file with GRCh38 genome build. Alternatively, we can compare our phased haplotype blocks with existing MHC variants, using hap.py (https://github.com/Illumina/hap.py). Recently Shafin K. et al (2021) used a similar approach to benchmark the MHC region against the Genome in a Bottle project (GIAB) truth set (PMID: 34725481).
  
- Hypothetical hypothesis journeys and figures (ALL)

### Step 2:

- Get the SV dataset and try to implement step 1 on the SV dataset/WGS (Elena)
- Run ARG needle (Minal)
- Glue software together (Elena/Jedrzej/Ben)
- Test use cases (ALL)

### Software that take phased genomic data as input: 

1. HaploNet: 10.1101/gr.276813.122
2. ChromoPainter: 10.1371/journal.pgen.1002453
3. Genomatnn: 10.7554/elife.64669
4. Flagel, 2019: 10.1093/molbev/msy224
5. S/HIC & diploS/HIC: 10.1534/g3.118.200262
6. RFMix: 10.1016/j.ajhg.2013.06.020
7. hap-IBD: 10.1016/j.ajhg.2020.02.010
8. IBDrecomb: 10.1016/j.ajhg.2020.05.016
9. Browning, 2020: 10.1016/j.ajhg.2020.09.010
10. TRUFFLE: 10.1016/j.ajhg.2019.05.007
11. Palamara, 2012: 10.1016/j.ajhg.2012.08.030
12. Palamara, 2015: 10.1016/j.ajhg.2015.10.006
13. Tian, 2019: 10.1016/j.ajhg.2019.09.012
14. FLARE: 10.1016/j.ajhg.2022.12.010
15. Wohns, 2022: 10.1126/science.abi8264


## References

1. Hofmeister, R.J., Ribeiro, D.M., Rubinacci, S. et al. Accurate rare variant phasing of whole-genome and whole-exome sequencing data in the UK Biobank. Nat Genet 55, 1243–1249 (2023). https://doi.org/10.1038/s41588-023-01415-w
2. Delaneau, O., Zagury, JF., Robinson, M.R. et al. Accurate, scalable and integrative haplotype estimation. Nat Commun 10, 5436 (2019). https://doi.org/10.1038/s41467-019-13225-y
3. Lewanski AL, Grundler MC, Bradburd GS. The era of the ARG: an empiricist's guide to ancestral recombination graphs. ArXiv [Preprint]. 2023 Oct 18:arXiv:2310.12070v1. Update in: PLoS Genet. 2024 Jan 18;20(1):e1011110. doi: 10.1371/journal.pgen.1011110. PMID: 37904740; PMCID: PMC10614969.
4. Zhang, B.C., Biddanda, A., Gunnarsson, Á.F. et al. Biobank-scale inference of ancestral recombination graphs enables genealogical analysis of complex traits. Nat Genet 55, 768–776 (2023). https://doi.org/10.1038/s41588-023-01379-x
