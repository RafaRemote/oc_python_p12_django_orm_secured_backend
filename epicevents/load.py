import os
import django

def load():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "epicevents.settings")
    django.setup()
    from django.contrib.auth import get_user_model
    from account.models import Account
    from status.models import Status
    
    dict_users = { 
    "username": ["charles", "camille", "solange", "robert", "gerard"],
    "role": ["management", "sales", "sales", "support", "support"],
    "password": ["1q2w#E$R", "1q2w#E$R", "1q2w#E$R", "1q2w#E$R", "1q2w#E$R"]
    # "is_admin": ["True", "False", "False", "False", "False"],
    # "is_staff": ["True", "False", "False", "False", "False"],
    # "is_superuser": ["True", "False", "False", "False", "False"]
    }
    
    list_status = ["planning", "live", "terminated", "cancelled", "suspended", "postponed"]

    User=get_user_model()
    User.objects.create_superuser("remi", "1q2w#E$R")
    
    for i in range(len(list(dict_users.items())[0][1])):
        User.objects.create_user(dict_users['username'][i], dict_users['role'][i], dict_users['password'][i])
    
    seller = User.objects.filter(role="sales")[0]
    new_account = Account(1, "leo", "dupres", "leo@dupres.com", sales_contact=seller)
    new_account.save()

    for i in list_status:
        Status.objects.create(status=i)

if __name__ == '__main__':
    load()
