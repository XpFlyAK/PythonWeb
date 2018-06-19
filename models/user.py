# -*- coding: UTF-8 -*-
from web_demo.models import Model


class User(Model):

    def __init__(self, f):
        self.name = f.get('user_name', '')
        self.age = f.get('user_password', '')

    def check_user_password(self):
        return self.name == 'lisi' and self.age == 6

    # 3.1 作业
    def validate_login(self):
        all_array = self.all()
        for x in all_array:
            if x['user_name'] == self.name:
                if x['user_password'] == self.age:
                    return True
        return False
