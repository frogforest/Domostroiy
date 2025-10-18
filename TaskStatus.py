# TaskStatus.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

    def __str__(self):
        return self.value