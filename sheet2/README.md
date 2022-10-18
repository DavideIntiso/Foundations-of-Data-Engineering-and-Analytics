# Foundations-of-Data-Engineering-and-Analytics
GitHub repository for the sheet 2 of the course Foundations of Data Engineering and Analytics

## Installation 
```bash
# install pipenv
pip3 install --user pipenv

# cd to data-engineering-analytics-notebooks directory
# install packages specified in requirements.txt file
pipenv install -r requirements.txt

# activate virtual environment
pipenv shell

# set up kernel in activated environment, needs to be re-executed with every change in pip environment
python -m ipykernel install --user --display-name dataeng_kernel --name dataeng_kernel
```

## Usage 
```bash
# if necessary, activate your virtual environment
# pipenv shell

# start jupyter-lab - should now use the installed dataeng_kernel 
jupyter-lab

# or alternatively, start jupyter 
jupyter notebook
```


## Notebook Quality Assurance
The bash script `perform_notebook_qa.sh` calls the following quality assurance tools for a given notebook (provided as command line argument):
* [nbval](https://github.com/computationalmodelling/nbval) 
* [isort of imports](https://github.com/PyCQA/isort) via [nvqa](https://github.com/nbQA-dev/nbQA) 
* [black code reformatting](https://github.com/psf/black) via [nvqa](https://github.com/nbQA-dev/nbQA) 
* [flake8 style guide enforcement](https://github.com/PyCQA/flake8) via [nbqa](https://github.com/nbQA-dev/nbQ)

