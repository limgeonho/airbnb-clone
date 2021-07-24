from django.db import models


class TimeStampedModel(models.Model):

    """TIme Stamped Model"""

    # User를 제외한 나머지 apps에서 공통적으로 사용하는 기능들을 모아서 코드의 재사용성을 높이겠다.

    created = models.DateTimeField(auto_now_add=True)
    # auto_now_add가 models가 생성될 때마다 시간을 기록해줌
    updated = models.DateTimeField(auto_now=True)
    # auto_now가 models가 수정될 때마다 시간을 기록해줌

    class Meta:
        abstract = True
        # abstract로 설정된 model은 데이터베이스에 올라가지 않는다 => 확장성을 위해서만 사용
