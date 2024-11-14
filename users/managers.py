from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom user model manager where phone_number is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a user with the given phone_number and password.
        """
        if not phone_number:
            raise ValueError("The phone_number must be set")
        phone_number = self.normalize_phone_number(phone_number)
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        """
        Create and save a SuperUser with the given phone_number and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(phone_number, password, **extra_fields)

    def normalize_phone_number(self, phone_number):
        return (phone_number
                .strip()
                .replace(" ", "")
                .replace("(", "")
                .replace(")", "")
                .replace("-", ""))