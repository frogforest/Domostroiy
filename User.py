# User.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from UserRole import UserRole
from Task import Task
from Reward import Reward
from TaskStatus import TaskStatus

class User:
    def __init__(self, user_id=None, user_name=None, email=None, role=UserRole.CHILD, points=0):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.role = role
        self.points = points
        self.assigned_tasks = []
        self.created_tasks = []
        self.claimed_rewards = []
        self.completed_tasks = []  # Новый список для выполненных задач
        self.family = None

    def take_task(self, task):
        """Взять задачу на выполнение"""
        if (task not in self.assigned_tasks and
            task.status == TaskStatus.PENDING and
            task.can_be_assigned_to(self)):
            task.assigned_to = self
            task.status = TaskStatus.IN_PROGRESS
            self.assigned_tasks.append(task)
            return True
        return False

    def cancel_task(self, task):
        """Отменить взятие задачи"""
        if task in self.assigned_tasks:
            task.assigned_to = None
            task.status = TaskStatus.PENDING
            self.assigned_tasks.remove(task)
            return True
        return False

    def mark_task_completed(self, task):
        """Пометить задачу как выполненную"""
        if task in self.assigned_tasks and task.status == TaskStatus.IN_PROGRESS:
            task.status = TaskStatus.COMPLETED
            self.points += task.points_reward
            self.assigned_tasks.remove(task)
            self.completed_tasks.append(task)  # Добавляем в список выполненных
            return True
        return False

    def create_new_task(self, task_name, description, category, points_reward):
        """Создать новую задачу"""
        task = Task(
            task_name=task_name,
            description=description,
            category=category,
            created_by=self,
            points_reward=points_reward
        )
        self.created_tasks.append(task)
        return task

    def delete_task(self, task):
        """Удалить задачу (только если пользователь её создал)"""
        if task in self.created_tasks:
            self.created_tasks.remove(task)
            if task.assigned_to:
                task.assigned_to.assigned_tasks.remove(task)
            return True
        return False

    def take_reward(self, reward):
        """Взять награду"""
        if (self.points >= reward.cost and
            reward not in self.claimed_rewards and
            reward.can_be_claimed_by(self)):
            self.points -= reward.cost
            self.claimed_rewards.append(reward)
            return True
        return False

    def create_new_reward(self, name, description, cost, category):
        """Создать новую награду"""
        reward = Reward(
            name=name,
            description=description,
            cost=cost,
            category=category,
            created_by=self
        )
        return reward

    def send_message(self, to_user, message, notification_service):
        """Отправить сообщение другому пользователю"""
        return notification_service.send_custom_message(self, to_user, message)

    def get_completed_tasks_count(self):
        """Получить количество выполненных задач"""
        return len(self.completed_tasks)

    def __str__(self):
        return f"User(id={self.user_id}, name='{self.user_name}', role={self.role}, points={self.points})"