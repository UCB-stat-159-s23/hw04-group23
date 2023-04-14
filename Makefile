.ONESHELL:
SHELL = /bin/bash

.PHONY : env
env :
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml 
	conda activate notebook
	conda install ipykernel
	python -m ipykernel install --user --name make-env --display-name "IPython - Make"


.PHONY : html	
html :
	jupyterbook build .


.PHONY : clean
clean :
	rm -rf ./data/*
	rm -rf ./figures/*
	rm -rf ./_build/*