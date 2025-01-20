import datetime
import os
from termcolor import cprint

def crem(): os.system("cls")

class FinanceTracker:
    def __init__(self):
        self.records = []
        self.categories = ["Еда", "Транспорт", "Развлечения"]
    
    def add_record(self, amount, category, date, description):
        record = {
            'amount': amount,
            'category': category,
            'date': date,
            'description': description
        }
        self.records.append(record)
    
    def view_balance(self):
        total_income = sum(record['amount'] for record in self.records if record['amount'] > 0)
        total_expense = sum(-record['amount'] for record in self.records if record['amount'] < 0)
        return total_income - total_expense
    
    def filter_records(self, start_date=None, end_date=None, category=None):
        filtered = self.records
        if start_date:
            filtered = [r for r in filtered if r['date'] >= start_date]
        if end_date:
            filtered = [r for r in filtered if r['date'] <= end_date]
        if category:
            filtered = [r for r in filtered if r['category'] == category]
        return filtered
    
    def analyze_expenses(self):
        expense_categories = {}
        for record in self.records:
            if record['amount'] < 0:
                category = record['category']
                expense_categories[category] = expense_categories.get(category, 0) - record['amount']
        return expense_categories

    def top_expense_categories(self, n=3):
        expenses = self.analyze_expenses()
        sorted_categories = sorted(expenses.items(), key=lambda x: x[1], reverse=True)
        return sorted_categories[:n]

    def income_vs_expenses_ratio(self):
        total_income = sum(record['amount'] for record in self.records if record['amount'] > 0)
        total_expense = sum(-record['amount'] for record in self.records if record['amount'] < 0)
        
        if total_expense == 0:
            return "Нет расходов для анализа."
        
        ratio = total_income / total_expense
        return ratio
crem()
def main():
    tracker = FinanceTracker()
    
    while True:

        cprint("\n1. Добавить запись",'light_green')
        cprint("2. Посмотреть баланс",'light_green')
        cprint("3. Фильтровать записи",'light_green')
        cprint("4. Анализ расходов",'light_green')
        cprint("5. Топ категорий расходов",'light_green')
        cprint("6. Соотношение доходов и расходов",'light_green')
        cprint("7. Выход",'light_green')
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            crem()
            amount = float(input("Введите сумму (положительное число для дохода, отрицательное для расхода): "))
            category = input(f"Введите категорию (предустановленные: {', '.join(tracker.categories)}): ")
            date_str = input("Введите дату (гггг-мм-дд): ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            description = input("Введите описание: ")
            tracker.add_record(amount, category, date, description)
        
        elif choice == '2':
            crem()
            balance = tracker.view_balance()
            print(f"Итоговый баланс: {balance} руб.")
        
        elif choice == '3':
            crem()
            start_date_str = input("Введите начальную дату (гггг-мм-дд) или оставьте пустым: ")
            end_date_str = input("Введите конечную дату (гггг-мм-дд) или оставьте пустым: ")
            category = input(f"Введите категорию или оставьте пустым: ")
            crem()
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date() if start_date_str else None
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date() if end_date_str else None
            
            records = tracker.filter_records(start_date, end_date, category)
            for r in records:
                cprint(r,"yellow")

        elif choice == '4':
            crem()
            expenses_analysis = tracker.analyze_expenses()
            for category, amount in expenses_analysis.items():
                print(f"{category}: {amount} руб.")

        elif choice == '5':
            crem()
            top_categories = tracker.top_expense_categories()
            for category, amount in top_categories:
                print(f"{category}: {amount} руб.")

        elif choice == '6':
            crem()
            ratio = tracker.income_vs_expenses_ratio()
            print(f"Соотношение доходов к расходам: {ratio}")

        elif choice == '7':
            break
        
if __name__ == "__main__":
    main()
