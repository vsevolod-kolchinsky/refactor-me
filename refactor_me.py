#!/usr/bin/env python3

from collections import namedtuple, defaultdict
from operator import itemgetter

Expense = namedtuple('Expense', ('category', 'amount'))


class ExpencesManager:
    _buffer = ()

    def add(self, expenses):
        for expense in expenses:
            self._buffer += (expense, )
            
    def by_category(self, treshold=0):
        # do not include expenses less than treshold
        aggregated_expenses = defaultdict(int)
        for expense in self._buffer:
            if expense.amount >= treshold:
                aggregated_expenses[expense.category] += expense.amount
        return aggregated_expenses
    
    @staticmethod
    def report(expenses):
        for category, amount in sorted(expenses.items(), key=itemgetter(1)):
            print(f"{category}: {amount}")


if __name__ == '__main__':
    expenses = ExpencesManager()
    test_expenses = (Expense('food', 4), Expense('food', 3), Expense('car', 3), Expense('dog', 1))
    expenses.add(test_expenses)
    expenses.report(expenses.by_category(treshold=2))
    