# NotificationType.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from enum import Enum

class NotificationType(Enum):
    SYSTEM = "system"
    TASK_ASSIGNED = "task_assigned"
    TASK_COMPLETED = "task_completed"
    REWARD_CLAIMED = "reward_claimed"
    MESSAGE = "message"

    def __str__(self):
        return self.value