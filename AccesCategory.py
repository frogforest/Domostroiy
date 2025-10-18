# AccesCategory.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from enum import Enum

class AccesCategory(Enum):
    ForAll = "all"
    ForAdult = "adult"
    ForChild = "child"

    def __str__(self):
        return self.value