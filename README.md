# CS2006-Python2

This project was an assignment for the CS2006 (Advanced Programming Projects) module at the University of St Andrews. The assignment specifications and the data set used were provided to us by Dr Alexander Konovalov.

The project takes a dataset from the twitter API and refines it before analysing it and visualising the findings.
The dataset contains tweets in connection to the Comet landing performed by the EU Space Agency (ESA) in 2014.

**MAKE SURE TO ACTIVATE VENV BEFORE STARTING JUPYTER**

# How to setup:
* create a virtual environment
  - python3 -m venv <venv_name>
  - source <venv_name>/bin/activate
  - pip3 install --upgrade pip
  - pip3 install -r requirements.txt
  - pip3 install cartopy
 * destroy virtual environment
    - deactivate
    - rm -rf /path/to/<venv_name>

# How to run:
* start jupyter notebook
  - jupyter notebook (make sure the virtual environment is active: source <venv_name>/bin/activate)
* navigate to the notebook you would like to see
  - data_refining.ipynb
    - for seeing how the raw data was refined before analysis
    - this notebook produces another csv file for later use
    - it uses the refine.py module
  - Analysis.ipynb
    - This notebook contains all the analysis and visualisation of the data
    - using all other modules created
  - test_notebook.ipynb
    - This notebook describes the automated tests used to test refine.py
    - There is also a bash file **compare_output.sh** for a command line test as well
    - To run the unit tests from command line
      - python3 test.py

# Requesting new location dataset
* to request new location data (updating locations.csv) an API key needs to be provided
  - The API is googleapis: maps
  - A key can be requested for free
  - The API key must be stored on a single line in a text file
    - an example keyfile is provided in data/
  - run **location.py -k /path/to/keyfile**
