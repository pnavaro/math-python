from glob import glob

nbfiles = sorted(glob("notebooks_2017/*.ipynb"))

with open("tests.py","w") as f:
    f.write("""\
import sys,os
sys.path.append(os.getcwd())
from nbtest import _notebook_run

print("Running Notebooks...")
os.chdir('notebooks')
\n\n""")

for i, nb in enumerate(filter(lambda f:  not "Errors" in f,sorted(nbfiles))):  
    with open("tests.py", "a") as f:
        f.write(f"def test_ipynb_{i}():\n")
        f.write(f"\t nb, errors = _notebook_run('{nb[10:]}')\n")
        f.write("\t assert errors == []\n\n")
