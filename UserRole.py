# UserRole.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from enum import Enum

class UserRole(Enum):
    PARENT = "parent"
    CHILD = "child"
    ADMIN = "admin"

    def __str__(self):
        return self.value