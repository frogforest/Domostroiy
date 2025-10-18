# NotificationService.py
# !/usr/bin/python
# -*- coding: UTF-8 -*-

from datetime import datetime, time
from NotificationType import NotificationType


class NotificationService:
    def __init__(self):
        self.notifications = []
        self.quiet_hours_start = time(22, 0)  # 22:00
        self.quiet_hours_end = time(8, 0)  # 08:00

    def send_system_notification(self, to_user, message, related_task=None, related_reward=None):
        """Отправить системное уведомление"""
        if self.is_quiet_time():
            print("Тихие часы - уведомление отложено")
            return None

        notification = Notification(
            from_user=None,  # Система
            to_user=to_user,
            message=message,
            type=NotificationType.SYSTEM,
            related_task=related_task,
            related_reward=related_reward
        )
        self.notifications.append(notification)
        print(f"Системное уведомление отправлено: {message}")
        return notification

    def send_custom_message(self, from_user, to_user, message):
        """Отправить пользовательское сообщение"""
        if self.is_quiet_time():
            print("Тихие часы - сообщение отложено")
            return None

        notification = Notification(
            from_user=from_user,
            to_user=to_user,
            message=message,
            type=NotificationType.MESSAGE
        )
        self.notifications.append(notification)
        print(f"Сообщение от {from_user.user_name}: {message}")
        return notification

    def get_user_notifications(self, user):
        """Получить уведомления пользователя"""
        return [n for n in self.notifications if n.to_user == user]

    def is_quiet_time(self):
        """Проверить, сейчас тихие часы"""
        now = datetime.now().time()
        if self.quiet_hours_start <= self.quiet_hours_end:
            return self.quiet_hours_start <= now <= self.quiet_hours_end
        else:  # 跨越午夜
            return now >= self.quiet_hours_start or now <= self.quiet_hours_end