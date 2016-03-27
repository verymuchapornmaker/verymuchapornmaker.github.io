from glob import glob

names = glob("./*.*")

newnames = list()
for name in names:
	newnames.append("http://verymuchapornmaker.github.io/" + name[2:])
with open("names.txt", "w", encoding="utf-8") as w:
	w.write("\n".join(newnames))