from datetime import datetime

class person: 
    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name
    

class Subject(person):
    def __init__(self, first_name, last_name, sex, date_of_birth):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.__date_of_birth = datetime.strptime(date_of_birth, "%d.%m.%Y")  # privates attribut

    def age(self):
        today = datetime.today()
        if (today.month, today.day) >= (self.__date_of_birth.month, self.__date_of_birth.day):
            return today.year - self.__date_of_birth.year
        else:
            return today.year - self.__date_of_birth.year - 1

    def estimate_max_hr(self):
        return 220 - self.age()

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.sex}, {self.age()} Jahre, geboren am {self.__date_of_birth.strftime('%d.%m.%Y')}"


class Supervisor(person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        
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
            f"Teilnehmer*in: {self.subject}\n"
            f"Betreuer*in: {self.supervisor}\n"
            f"Maximale Herzfrequenz (geschätzt): {self.subject.estimate_max_hr()} bpm"
        )



if __name__ == "__main__":
    subject1 = Subject("Liliana", "Escobar", "w", "31.03.2004")
    supervisor1 = Supervisor("Frau", "Kaiser")
    experiment1 = Experiment("Belastungstest", "10.04.2025")

    experiment1.add_subject(subject1)
    experiment1.add_supervisor(supervisor1)

    print(experiment1)

