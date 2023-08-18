from django.apps import AppConfig


class StockConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "stock"
    def ready(self):
        from stock import receivers
