from openwisp_radius.apps import OpenwispRadiusConfig
from openwisp_radius.receivers import send_email_on_new_accounting_handler
from openwisp_radius.signals import radius_accounting_success


class GmtispRadiusConfig(OpenwispRadiusConfig):
    name = 'gmtisp.gmtisp_radius'
    label = 'gmtisp_radius'
    verbose_name = 'GMTISP Radius'

    def connect_signals(self):
        from .api.views import AccountingView

        radius_accounting_success.connect(
            send_email_on_new_accounting_handler,
            sender=AccountingView,
            dispatch_uid='send_email_on_new_accounting',
        )
        return super().connect_signals()


del OpenwispRadiusConfig
