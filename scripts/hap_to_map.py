def create_map_file(hap_file, map_file):
    with open(hap_file, 'r') as hap, open(map_file, 'w') as mapf:
        for line in hap:
            # Example: assuming the haplotype file has columns like: Chromosome, Marker ID, Position
            fields = line.strip().split()
            chrom = fields[0]   # Assuming the chromosome is in the first column
            marker_id = fields[1]  # Assuming the marker ID is in the second column
            pos = fields[2]  # Assuming the base-pair position is in the third column
            mapf.write(f"{chrom}\t{marker_id}\t0\t{pos}\n")

# Usage
create_map_file('CDX_chr6_chunk1.hap', 'CDX_chr6_chunk1.map')
