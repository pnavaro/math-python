from glob import glob

nbfiles = glob("notebooks/*.ipynb")

with open("tests.py","w") as f:
    f.write("""\
import sys,os
sys.path.append(os.getcwd())
from nbtest import _notebook_run

print("Running Notebooks...")
os.chdir('notebooks')
\n\n""")

for i, nb in enumerate(nbfiles):  
    with open("tests.py", "a") as f:
        f.write(f"def test_ipynb_{i}():\n")
        f.write(f"\t nb, errors = _notebook_run('{nb[10:]}')\n")
        f.write("\t assert errors == []\n\n")
