from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    # admin 패널에서 User을 보겠다.
    """Custom User Admin"""

    # admin 패널에서 사용자들의 정보 속성을 보여준다(표의 상단의 가로)
    # list_display = ("username", "email", "gender", "language", "currency", "superhost")

    # admin 패널에서 사용자들을 filtering 할 수 있는 메뉴가 생김
    # list_filter = ("language", "currency", "superhost")

    # 위의 방법도 있지만 이미 장고가 가지고 있는 admin기능을 이용하기 위해 UserAdmin을 이용한다.
    # 추가적으로 fieldsets에는 UserAdmin 과 내가 만든 custom profile를 합쳐주면 둘 다 사용가능하다.
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
