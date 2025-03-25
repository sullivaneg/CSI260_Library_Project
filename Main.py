"""Main file to test the program

Authors: Abigail Gehlbach, Charles Justus, Emma Sullivan, Sebastian Dominguez
Class: CSI-260-01
Assignment: Library Project
Due Date: 2/27/2019 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

import Pickle_Cat
import Catalog

# try to read catalog
catalog = Pickle_Cat.load_catalog()

if catalog is None:
    catalog = Catalog.Catalog()

Catalog.user_interface(catalog)
