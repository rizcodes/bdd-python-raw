class CovidVaccine:
    def __init__(self, age, user_vaccine_choice=None):
        self.age = age

    def is_elder(self):
        return self.age >= 55

    def fast_track_user(self):
        if self.is_elder():
            return 'user issued fast-track pass'

    def administer_shot(self):
        if self.is_elder() and self.fast_track_user():
            return f'Administering COVID vaccine'
        return f'User is not elder - please wait for your turn'
