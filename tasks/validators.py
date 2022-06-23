from django.core.validators import ValidationError


class DisallowedWordsPassworValidator(object):
    """
        This class ensures that users passwords are not in the list of disallowed words.
    """
    disallowed_words = ['tod', 'task', 'list']

    def __init__(self, min_length):
        self.min_length = min_length
    
    def validate(self, password, user=None):
        if any(word in password for word in self.disallowed_words):
            raise ValidationError(f'Password may not contain words:{", ".join(self.disallowed_words)}')
    
    def get_help_text(self):
        return ""
