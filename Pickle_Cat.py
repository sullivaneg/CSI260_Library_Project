"""File to load and save catalog list using pickle

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

import pickle
import os.path


def save_catalog(cat):
    """save catalog array to save.p"""
    pickle.dump(cat, open("save.p", "wb"))


def load_catalog():
    """loads catalogue from save.p file"""
    # looking before leap
    if os.path.exists("./save.p"):
        print("opened file")
        try:
            with open("save.p", "rb") as f:
                cat = pickle.load(f)
            if cat:
                return cat
            else:
                return None
        except(FileNotFoundError, EOFError) as err:
            print(err)
    else:
        return None

