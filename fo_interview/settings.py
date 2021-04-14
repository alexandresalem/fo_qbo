import os

from intuitlib.enums import Scopes

CLIENT_ID = os.environ.get("QBO_CLIENT_ID", "ABb3No67iNl5r55HaF4TxOEbjnKmRBNNQwllWfod1Qi4hI3FXm")
CLIENT_SECRET = os.environ.get("QBO_CLIENT_SECRET", "TgS14MVrZW3EQoQLqDTCnkMUJ6zprsabrQSaGzwJ")
REDIRECT_URI = "https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl"
SCOPES = [Scopes.ACCOUNTING]
ENVIRONMENT = os.environ.get("QBO_ENVIRONMENT", "sandbox")

OAUTH2_URL = "https://appcenter.intuit.com/connect/oauth2"
PRODUCTION_URL = "https://quickbooks.api.intuit.com"
