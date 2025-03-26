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


def save_catalog(cat, category_tags):
    """save catalog array to save.p"""
    data = {"catalog": cat, "category_tags": category_tags}
    with open("save.p", "wb") as f:
        pickle.dump(data, f)


def load_catalog():
    """Loads catalog and category tags from save.p file"""
    if os.path.exists("save.p"):
        try:
            with open("save.p", "rb") as f:
                data = pickle.load(f)

            catalog = data.get('catalog')
            category_tags = data.get('category_tags')

            return catalog, category_tags  # Ensure always returning a tuple
        except (FileNotFoundError, EOFError, pickle.UnpicklingError) as err:
            print(f"Error loading catalog: {err}")

    return None, []  # Ensure a tuple is returned

