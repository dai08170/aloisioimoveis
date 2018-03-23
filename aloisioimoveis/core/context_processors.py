from django.conf import settings


def settings_config(request):
    """Context processor to expose selected site settings to all templates"""

    return {
        'SETTINGS': {
            'GOOGLE_ANALYTICS_CODE': settings.GOOGLE_ANALYTICS_CODE,
            'GOOGLE_RECAPTCHA_SITE_KEY': settings.GOOGLE_RECAPTCHA_SITE_KEY
        }
    }
