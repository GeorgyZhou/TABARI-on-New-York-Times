import os
import glob

if __name__ == "__main__":
    fns = glob.glob("*.text")
    for fn in fns:
        name = fn.rstrip('.text').replace('-', '_')
        pfn = name + '.project'
        with open(pfn, 'w') as f:
            f.write("Demonstration file for TABARI in New Yorks Times Reports\n")
            f.write("<actorsfile> New_York.actors\n")
            f.write("<verbsfile> New_York.verbs\n")
            f.write("<optionsfile> New_York.options\n")
            f.write("<projectfile> "+ pfn + "\n")
            f.write("<textfile> " + fn + "\n")
            f.write("<eventfile> " +  name + ".evts\n")
            f.write("<problemfile> " + name + ".prob\n")
            f.write("<errorfile> " + name + ".errs\n")
            f.write("<coder> " + name + "\n")
        print "Processing " + fn + "..."
        os.popen("./TABARI.ubuntu.0.8.4b2 -aq " + pfn)