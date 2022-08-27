This is what I ran (with cuda 11.6 installed)
conda activate cheese3
conda install python=3.10 -y
conda install pytorch torchvision cudatoolkit=11.3 -c pytorch -y
conda install -c conda-forge opencv -y
conda install scipy -y
pip install transformers
pip install datasets
pip install wandb

