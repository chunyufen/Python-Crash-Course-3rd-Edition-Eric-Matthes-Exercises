# Chapter 8/Printing_Models.py

import printing_functions as pf # see printing_functions.py

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)