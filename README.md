# Haploblock_Clusters

## Workflow

<img width="490" alt="image" src="https://github.com/user-attachments/assets/3e0380ea-aa6c-428b-af0a-48ca6fae19ce">

##### Arg needle takes a .hap file from beagle or shapeit.  

### Haploblock 

![image](https://github.com/user-attachments/assets/cc02f217-4e04-4904-90ab-a228b9f5edf2)


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

## Steps:

# Step 1:

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
- Hypothetical hypothesis journeys and figures (ALL)

# step 2:

- Get the SV dataset and try to implement step 1 on the SV dataset/WGS (Elena)
- Run ARG needle (Minal)
- Glue software together (Elena/Jedrzej/Ben)
- Test use cases (ALL)


## DNAnexus prototype workflow

<img width="1143" alt="image" src="https://github.com/user-attachments/assets/b20014b7-da86-499b-92d1-b5a9837554d1">
