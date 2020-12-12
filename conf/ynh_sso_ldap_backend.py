from django_auth_ldap.backend import LDAPBackend
from inventory.permissions import get_or_create_normal_user_group


class Django-For-RunnersYunohostLdapBackend(LDAPBackend):
    def get_or_build_user(self, username, ldap_user):
        user, built = super().get_or_build_user(username, ldap_user)

        if built:
            user.is_staff = True
            user.is_superuser = False
            user.save()

            django-for-runners_user_group = get_or_create_normal_user_group()[0]
            user.groups.set([django-for-runners_user_group])

        return user, built
