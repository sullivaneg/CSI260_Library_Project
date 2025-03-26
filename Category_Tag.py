"""Category tag class

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


class CategoryTag:
    _all_tags = []

    @classmethod
    def all_category_tags(cls):
        """return all category tags comma sep'd"""
        return ", ".join(category.name for category in cls._all_tags)

    @classmethod
    def get_all_tags(cls):
        """return all tags var"""
        return cls._all_tags

    @classmethod
    def set_all_tags(cls, tags):
        """Load tags from saved data"""
        cls._all_tags = tags

    def __init__(self, name):
        self.name = name
        self._all_tags.append(self)

    def __str__(self):
        return f'{self.name}'
