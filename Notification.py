# Notification.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from NotificationType import NotificationType
import uuid
from datetime import datetime

class Notification:
    def __init__(self, notification_id=None, from_user=None, to_user=None,
                 message="", type=NotificationType.SYSTEM, related_task=None, related_reward=None):
        self.notification_id = notification_id or str(uuid.uuid4())[:8]
        self.from_user = from_user
        self.to_user = to_user
        self.message = message
        self.type = type
        self.related_task = related_task
        self.related_reward = related_reward
        self.created_at = datetime.now()
        self.is_read = False

    def mark_as_read(self):
        """Пометить как прочитанное"""
        self.is_read = True

    def __str__(self):
        from_name = self.from_user.user_name if self.from_user else "System"
        to_name = self.to_user.user_name if self.to_user else "Unknown"
        return f"Notification[{self.type}]: {from_name} -> {to_name}: {self.message}"