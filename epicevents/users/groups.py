from django.contrib.auth.models import Group, Permission


def create_groups():
    sales_team, c = Group.objects.get_or_create(name="sales_team")
    add_permission(sales_team)
    support_team, c = Group.objects.get_or_create(name="support_team")
    add_permission(support_team)
    return [sales_team, support_team]


def add_permission(team):
    if "sales" in team.name:
        perms = [
            "add_account",
            "view_account",
            "change_account",
            "view_contract",
            "change_contract",
        ]
    elif "support" in team.name:
        perms = ["view_event", "change_event", "view_account"]
    [team.permissions.set(Permission.objects.get(codename=perm) for perm in perms)]


def dispatch_user(user):
    teams = create_groups()
    for team in teams:
        if user.role in team.name:
            user.groups.add(team)
