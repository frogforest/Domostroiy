# Reward.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from AccesCategory import AccesCategory
import uuid

class Reward:
    def __init__(self, reward_id=None, name=None, description=None, cost=0, category=AccesCategory.ForAll, created_by=None):
        self.reward_id = reward_id or str(uuid.uuid4())[:8]
        self.name = name
        self.description = description
        self.cost = cost
        self.category = category
        self.created_by = created_by

    def can_be_claimed_by(self, user):
        """Проверить, может ли награда быть получена пользователем"""
        if self.category == AccesCategory.ForAll:
            return True
        elif self.category == AccesCategory.ForAdult:
            return user.role.value == "parent" or user.role.value == "admin"
        elif self.category == AccesCategory.ForChild:
            return user.role.value == "child"
        return False

    def __str__(self):
        return f"Reward(id={self.reward_id}, name='{self.name}', cost={self.cost}, category={self.category})"