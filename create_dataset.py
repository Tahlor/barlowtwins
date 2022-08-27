from tqdm import tqdm
import time
import os
from os.path import exists
from pathlib import Path
import random
import shutil


# mogrify -format jpg *.j2k
ext = "j2k"

PATH = Path("/home/taylor/anaconda3/FRENCH_CENSUS")
train_path = PATH / "train"
val_path = PATH / "val"
src_path = PATH / "images"

files = list(src_path.rglob(f"*.{ext}"))
validation_set_size = .1

doc_types = ["unknown"]
def lookup(file_name):
    return "unknown"

for path in [val_path, train_path]:
    if path.exists():
       shutil.rmtree(path)
       time.sleep(2)
    for doc_type in doc_types:
        (path/doc_type).mkdir(parents=True, exist_ok=True)

random.shuffle(files)

path = val_path
for i, f in enumerate(tqdm(files)):
    if i > len(files) * validation_set_size:
        path = train_path
    #print(f)
    os.system(f"ln -s {str(f)} {str(path/ lookup(f.name) / f.name)}")