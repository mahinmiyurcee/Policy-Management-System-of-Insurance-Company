from datetime import datetime, timedelta

class Payment:
    def _init_(self, id, policyholder_id, amount, due_date):
        self.id = id
        self.policyholder_id = policyholder_id
        self.amount = amount
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.status = "pending"

    def process(self):
        self.status = "paid"
        print(f"Payment {self.id} for policyholder {self.policyholder_id} has been processed.")

    def send_reminder(self):
        if self.status == "pending" and datetime.now() > self.due_date - timedelta(days=7):
            print(f"Reminder: Payment {self.id} for policyholder {self.policyholder_id} is due on {self.due_date.strftime('%Y-%m-%d')}.")

    def apply_penalty(self):
        if self.status == "pending" and datetime.now() > self.due_date:
            penalty = self.amount * 0.1
            self.amount += penalty
            print(f"Late payment penalty of ${penalty:.2f} applied to payment {self.id} for policyholder {self.policyholder_id}.")

    def display_details(self):
        print(f"Payment ID: {self.id}")
        print(f"Policyholder ID: {self.policyholder_id}")
        print(f"Amount: ${self.amount}")
        print(f"Due Date: {self.due_date.strftime('%Y-%m-%d')}")
        print(f"Status: {self.status}")

