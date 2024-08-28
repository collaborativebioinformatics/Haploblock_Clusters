# Haploblock_Clusters

## Workflow

<img width="431" alt="image" src="https://github.com/user-attachments/assets/d01b1797-1178-4ee4-adaf-972d20495fe9">

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
Download phased vcfs from 1000 genome for one chromosome 
Convert shapeit vcf to xcf format - understand xcf format, how haplotype information is saved in haploblocks
Get ARG-needle working on DNANexus
Figure out way to merge rare variants information to the haploblocks

# step 2:
Get the SV dataset and try to implement step 1 on the SV dataset
Run on the whole genome
