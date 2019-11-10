#!/usr/bin/env python3

from collections import namedtuple, defaultdict
from operator import itemgetter

Expense = namedtuple('Expense', ('category', 'amount'))


class BaseExpencesManager:
    expenses = []

    def add(self, expense):
        self.expenses.append(expense)

    def aggregate_by_category(self, expense_threshold=0):
        # do not include expenses less than threshold
        aggregated_expenses = defaultdict(int)
        for expense in self.expenses:
            if expense.amount >= expense_threshold:
                aggregated_expenses[expense.category] += expense.amount
        return aggregated_expenses


class ExpencesManager(BaseExpencesManager):
    @staticmethod
    def report(expenses):
        for category, amount in sorted(expenses.items(), key=itemgetter(1)):
            print(f'{category}: {amount}')


if __name__ == '__main__':
    expenses = ExpencesManager()
    test_expenses = (Expense('food', 4), Expense('food', 3), Expense('car', 3),
                     Expense('dog', 1))
    for expense in test_expenses:
        expenses.add(expense)
    expenses.report(expenses.aggregate_by_category(expense_threshold=2))
