import sys
file=open(sys.argv[1],"r")

print("gene\tace\tasu\tbma\tbpa\tbxy\tcbg\tcbn\tcel\tcrem\tcsp1\tdvi\tgpa\thba\thco\tloa\tmha\tnam\tovo\tpmu\tppac\tpred\tpsam_ds\tpsam_vv\trcul\tsb347\tste\ttmu\ttox\ttsp\twba")

for line in file:
	line=line.rstrip("\n")
	line=line.split(":")[1]
	if line.count("cel|")==0:
		pass
	else:
		ace=line.count("ace|")
		asu=line.count("asu|")
		bma=line.count("bma|")
		bpa=line.count("bpa|")
		bxy=line.count("bxy|")
		cbg=line.count("cbg|")
		cbn=line.count("cbn|")
		cel=line.count("cel|")
		crem=line.count("crem|")
		csp1=line.count("csp1|")
		dvi=line.count("dvi|")
		gpa=line.count("gpa|")
		hba=line.count("hba|")
		hco=line.count("hco|")
		loa=line.count("loa|")
		mha=line.count("mha|")
		nam=line.count("nam|")
		ovo=line.count("ovo|")
		pmu=line.count("pmu|")
		ppac=line.count("ppac|")
		pred=line.count("pred|")
		psam_ds=line.count("psam_ds|")
		psam_vv=line.count("psam_vv|")
		rcul=line.count("rcul|")
		sb347=line.count("sb347|")
		ste=line.count("ste|")
		tmu=line.count("tmu|")
		tox=line.count("tox|")
		tsp=line.count("tsp|")
		wba=line.count("wba|")
	
		splitline=line.split(" ")
		pre_cel=ace+asu+bma+bpa+bxy+cbg+cbn+1
		
		cel_genes=splitline[pre_cel:pre_cel+cel]
		
		for gene in cel_genes:
			print(gene+"\t"+str(ace)+"\t"+str(asu)+"\t"+str(bma)+"\t"+str(bpa)+"\t"+str(bxy)+"\t"+str(cbg)+"\t"+str(cbn)+"\t"+str(cel)+"\t"+str(crem)+"\t"+str(csp1)+"\t"+str(dvi)+"\t"+str(gpa)+"\t"+str(hba)+"\t"+str(hco)+"\t"+str(loa)+"\t"+str(mha)+"\t"+str(nam)+"\t"+str(ovo)+"\t"+str(pmu)+"\t"+str(ppac)+"\t"+str(pred)+"\t"+str(psam_ds)+"\t"+str(psam_vv)+"\t"+str(rcul)+"\t"+str(sb347)+"\t"+str(ste)+"\t"+str(tmu)+"\t"+str(tox)+"\t"+str(tsp)+"\t"+str(wba))

file.close()


