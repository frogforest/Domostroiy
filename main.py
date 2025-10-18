# main.py
# !/usr/bin/python
# -*- coding: UTF-8 -*-

from User import User
from UserRole import UserRole
from Task import Task
from Reward import Reward
from AccesCategory import AccesCategory
from Family import Family
from NotificationService import NotificationService


def main():
    # Создаем сервис уведомлений
    notification_service = NotificationService()

    print("=== СИСТЕМА УПРАВЛЕНИЯ СЕМЕЙНЫМИ ЗАДАЧАМИ ===\n")

    # Создаем семью
    parent = User(1, "Анна", "anna@example.com", UserRole.PARENT, 100)
    child1 = User(2, "Никита", "nikita@example.com", UserRole.CHILD, 50)
    child2 = User(3, "Полина", "polina@example.com", UserRole.CHILD, 30)

    family = Family(1, parent)
    family.add_member(child1)
    family.add_member(child2)

    print("=== Создана семья ===")
    print(family)
    for member in family.members:
        print(f"  - {member}")

    # Родитель создает задачи с разными категориями доступа
    print("\n=== Создание задач с разными категориями доступа ===")

    # Задача для всех
    math_task = parent.create_new_task(
        "Сделать математику",
        "Решить задачи по математике из учебника стр. 45-46",
        AccesCategory.ForAll,
        15
    )

    # Задача только для взрослых
    finances_task = parent.create_new_task(
        "Оплатить счета",
        "Оплатить коммунальные услуги онлайн",
        AccesCategory.ForAdult,
        25
    )

    # Задача только для детей
    toys_task = parent.create_new_task(
        "Убрать игрушки",
        "Разложить все игрушки по местам",
        AccesCategory.ForChild,
        10
    )

    print(f"Родитель создал задачи:")
    print(f"  - {math_task}")
    print(f"  - {finances_task}")
    print(f"  - {toys_task}")
    print(f"Делу - время, потехе - час")

    # Попытка взять задачи
    print("\n=== Попытка взять задачи ===")

    # Ребенок пытается взять взрослую задачу
    if child1.take_task(finances_task):
        print(f"✓ {child1.user_name} взял задачу: {finances_task.task_name}")
    else:
        print(f"✗ {child1.user_name} не может взять задачу '{finances_task.task_name}' - доступно только для взрослых")

    # Ребенок берет детскую задачу
    if child1.take_task(toys_task):
        print(f"✓ {child1.user_name} взял задачу: {toys_task.task_name}")
    else:
        print(f"✗ {child1.user_name} не может взять задачу '{toys_task.task_name}'")

    # Родитель берет взрослую задачу
    if parent.take_task(finances_task):
        print(f"✓ {parent.user_name} взял задачу: {finances_task.task_name}")
    else:
        print(f"✗ {parent.user_name} не может взять задачу '{finances_task.task_name}'")

    # Ребенок берет задачу для всех
    if child2.take_task(math_task):
        print(f"✓ {child2.user_name} взял задачу: {math_task.task_name}")
    else:
        print(f"✗ {child2.user_name} не может взять задачу '{math_task.task_name}'")

    # Выполнение задач
    print("\n=== Выполнение задач ===")
    if child1.mark_task_completed(toys_task):
        print(f"✓ {child1.user_name} выполнил: {toys_task.task_name} (+{toys_task.points_reward} баллов)")

    if parent.mark_task_completed(finances_task):
        print(f"✓ {parent.user_name} выполнил: {finances_task.task_name} (+{finances_task.points_reward} баллов)")

    if child2.mark_task_completed(math_task):
        print(f"✓ {child2.user_name} выполнил: {math_task.task_name} (+{math_task.points_reward} баллов)")

    print(f"\n БАЛЛЫ ПОСЛЕ ВЫПОЛНЕНИЯ ЗАДАЧ:")
    print(f"  {parent.user_name}: {parent.points} баллов")
    print(f"  {child1.user_name}: {child1.points} баллов")
    print(f"  {child2.user_name}: {child2.points} баллов")

    # Создаем награды с разными категориями доступа
    print("\n=== Создание наград с разными категориями доступа ===")

    # Награда для всех
    ice_cream_reward = parent.create_new_reward(
        "Мороженое",
        "Вкусное мороженое из магазина",
        20,
        AccesCategory.ForAll
    )

    # Награда только для взрослых
    spa_reward = parent.create_new_reward(
        "Успешная сдача лабы",
        "Сдача лабы по КПО без понижений",
        60,
        AccesCategory.ForAdult
    )

    # Награда только для детей
    toys_reward = parent.create_new_reward(
        "Новая игрушка",
        "Выбор новой игрушки в магазине",
        30,
        AccesCategory.ForChild
    )

    print(f"Созданы награды:")
    print(f"  - {ice_cream_reward}")
    print(f"  - {spa_reward}")
    print(f"  - {toys_reward}")

    # Получение наград
    print("\n=== Получение наград ===")

    # Ребенок пытается взять взрослую награду
    if child1.take_reward(spa_reward):
        print(f"✓ {child1.user_name} получил: {spa_reward.name}")
    else:
        print(f"✗ {child1.user_name} не может получить '{spa_reward.name}' - доступно только для взрослых")

    # Ребенок берет детскую награду
    if child1.take_reward(toys_reward):
        print(f"✓ {child1.user_name} получил: {toys_reward.name}")

    # Родитель берет взрослую награду
    if parent.take_reward(spa_reward):
        print(f"✓ {parent.user_name} получил: {spa_reward.name}")

    # Ребенок берет награду для всех
    if child2.take_reward(ice_cream_reward):
        print(f"✓ {child2.user_name} получил: {ice_cream_reward.name}")

    print(f"\n БАЛЛЫ ПОСЛЕ ПОЛУЧЕНИЯ НАГРАД:")
    print(f"  {parent.user_name}: {parent.points} баллов")
    print(f"  {child1.user_name}: {child1.points} баллов")
    print(f"  {child2.user_name}: {child2.points} баллов")

    # Показываем итоговую статистику
    print("\n" + "=" * 50)
    print("ИТОГОВАЯ СТАТИСТИКА")
    print("=" * 50)

    print(f"\n Семья '{family.family_id}':")
    for member in family.members:
        print(f"\n{member.user_name} ({member.role}):")
        print(f"  Баллы: {member.points}")
        print(f"  Создано задач: {len(member.created_tasks)}")
        print(f"  Выполнено задач: {member.get_completed_tasks_count()}")
        print(f"  Получено наград: {len(member.claimed_rewards)}")

    # Показываем детальную информацию о выполненных задачах
    print(f"\n ДЕТАЛИ ВЫПОЛНЕННЫХ ЗАДАЧ:")
    for member in family.members:
        if member.completed_tasks:
            print(f"\n{member.user_name}:")
            for task in member.completed_tasks:
                print(f"  - {task.task_name} (+{task.points_reward} баллов)")

    print(f"\n Всего уведомлений в системе: {len(notification_service.notifications)}")


if __name__ == "__main__":
    main()