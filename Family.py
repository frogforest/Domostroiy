# Family.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Family:
    def __init__(self, family_id=None, created_by=None):
        self.family_id = family_id
        self.created_by = created_by
        self.members = []
        if created_by:
            self.add_member(created_by)

    def add_member(self, user):
        """Добавить участника в семью"""
        if user not in self.members:
            self.members.append(user)
            user.family = self
            return True
        return False

    def remove_member(self, user):
        """Удалить участника из семьи"""
        if user in self.members:
            self.members.remove(user)
            user.family = None
            return True
        return False

    def get_family_tasks(self):
        """Получить все задачи семьи"""
        tasks = []
        for member in self.members:
            tasks.extend(member.created_tasks)
            tasks.extend(member.assigned_tasks)
        return list(set(tasks))  # Убираем дубликаты

    def __str__(self):
        return f"Family(id={self.family_id}, members={len(self.members)})"