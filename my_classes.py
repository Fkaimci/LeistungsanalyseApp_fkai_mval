class Subject:
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def estimate_max_hr(self):
        """Schätzt die maximale Herzfrequenz basierend auf dem Alter"""
        return 220 - self.age

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.sex}, {self.age} Jahre"


class Supervisor:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Experiment:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.subject = None
        self.supervisor = None

    def add_subject(self, subject):
        self.subject = subject

    def add_supervisor(self, supervisor):
        self.supervisor = supervisor

    def __str__(self):
        return (
            f"Experiment: {self.name} am {self.date}\n"
            f"Teilnehmer: {self.subject}\n"
            f"Betreuer: {self.supervisor}\n"
            f"Maximale Herzfrequenz (geschätzt): {self.subject.estimate_max_hr()} bpm"
        )


