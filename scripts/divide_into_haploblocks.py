import sys

f = open("hotspots_b36_chr6.txt", "r")

start_points = []
end_points = []

for line in f:
	split_line = line.rstrip().split("\t")
	chr, centre, start, end, *x = split_line
	start_points.append(start)
	end_points.append(end)

# remove first start point
del start_points[0]

# remove last end point
del end_points[-1]

assert len(start_points) == len(end_points)

print(len(start_points))
for i in range(len(start_points)):
	line_to_save = str(end_points[i]) + "\t" + str(start_points[i]) + "\n"
	with open("haploblocks_b36_chr6.txt", "a") as f_hap:
		f_hap.write(line_to_save)

sys.exit("Done")
