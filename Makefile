.ONESHELL:
SHELL = /bin/bash


#env - creates and configures the environment.
.PHONY : env
env :
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml 
	conda activate notebook
	conda install ipykernel
	python -m ipykernel install --user --name make-env --display-name "IPython - Make"

#html - build the JupyterBook normally
.PHONY : html	
html :
	jupyter-book build .

#clean - clean up the figures, audio and _build folders.
.PHONY : clean
clean :
	rm -rf audio/*
	rm -rf figures/*
	rm -rf _build/*