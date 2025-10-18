# Task.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from TaskStatus import TaskStatus
from AccesCategory import AccesCategory
import uuid

class Task:
    def __init__(self, task_id=None, task_name=None, description=None, category=AccesCategory.ForAll,
                 created_by=None, assigned_to=None, status=TaskStatus.PENDING, points_reward=0):
        self.task_id = task_id or str(uuid.uuid4())[:8]
        self.task_name = task_name
        self.description = description
        self.category = category
        self.created_by = created_by
        self.assigned_to = assigned_to
        self.status = status
        self.points_reward = points_reward

    def can_be_assigned_to(self, user):
        """Проверить, может ли задача быть назначена пользователю"""
        if self.category == AccesCategory.ForAll:
            return True
        elif self.category == AccesCategory.ForAdult:
            return user.role.value == "parent" or user.role.value == "admin"
        elif self.category == AccesCategory.ForChild:
            return user.role.value == "child"
        return False

    def __str__(self):
        assigned_to_name = self.assigned_to.user_name if self.assigned_to else "None"
        return f"Task(id={self.task_id}, name='{self.task_name}', category={self.category}, status={self.status}, points={self.points_reward}, assigned_to='{assigned_to_name}')"