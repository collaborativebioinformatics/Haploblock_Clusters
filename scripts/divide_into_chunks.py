import sys

f = open("CDX_chr6.hap", "r")

for line in f:
	split_line = line.rstrip().split(" ")
	chr, dot, pos, *x = split_line
	pos = int(pos)
	if pos > 136011 and pos < 160001:
		with open("CDX_chr6_chunk1.hap", "a") as f_chunk:
			f_chunk.write(line)
	if pos > 160001:
		sys.exit("Done")
