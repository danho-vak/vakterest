from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):  # UserCreationFrom을 상속받음
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True  # username field를 disable함