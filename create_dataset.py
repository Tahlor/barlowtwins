from tqdm import tqdm
import time
import os
from os.path import exists
from pathlib import Path
import random
import shutil


# mogrify -format jpg *.j2k
ext = "jpg"

PATH = Path("/home/taylor/anaconda3/FRENCH_CENSUS/")
files = list(Path(PATH).rglob(f"*.{ext}"))
validation_set_size = .1

doc_types = ["unknown"]
def lookup(file_name):
    return "unknown"

for path in [PATH / "val", PATH / "train"]:
    if path.exists():
       shutil.rmtree(path)
       time.sleep(2)
    for doc_type in doc_types:
        (path/doc_type).mkdir(parents=True, exist_ok=True)

random.shuffle(files)

path = PATH / "val"
for i, f in enumerate(files):
    if i > len(files) * validation_set_size:
        path = PATH / "train"
    print(f)
    os.system(f"ln -s {str(f)} {str(path/ lookup(f.name) / f.name)}")