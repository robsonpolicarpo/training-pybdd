from datetime import timedelta, datetime

from faker import Faker


class FakerData:
    def __init__(self):
        self.faker = Faker('pt_BR')

    def get_random_datetime(self, days=0, hours=1):
        current_datetime = datetime.utcnow() \
                               .replace(minute=0, second=0, microsecond=0) + timedelta(days=days, hours=hours)
        next_datetime_displayed = current_datetime.strftime('Today' + ' ' + '%b %-d %-I:%M %p')
        return next_datetime_displayed

    def get_random_incomplete_password(self, length=7):
        return self.faker.password(length)
