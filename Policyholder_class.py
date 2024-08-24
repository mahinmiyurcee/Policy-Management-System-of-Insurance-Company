class Policyholder:
    def _init_(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.status = "active"
        self.policies = []

    def register(self):
        if self.status == "active":
            print(f"Policyholder {self.name} is already registered.")
        else:
            self.status = "active"
            print(f"Policyholder {self.name} has been registered.")

    def suspend(self):
        if self.status == "suspended":
            print(f"Policyholder {self.name} is already suspended.")
        else:
            self.status = "suspended"
            print(f"Policyholder {self.name} has been suspended.")

    def reactivate(self):
        if self.status == "active":
            print(f"Policyholder {self.name} is already active.")
        else:
            self.status = "active"
            print(f"Policyholder {self.name} has been reactivated.")

    def add_policy(self, policy):
        self.policies.append(policy)
        print(f"Policy {policy} added to policyholder {self.name}.")

    def display_details(self):
        print(f"Policyholder ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Status: {self.status}")
        print(f"Policies: {self.policies}")