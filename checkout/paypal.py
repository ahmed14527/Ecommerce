import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "Aaqhh9RBE2HL8GEnS6rKXwMUHaToA6Ei-MUKLP__Na6x5pHj9RB6_1u-CNkn1F4u6NXFBYq3hYCHzls9"
        self.client_secret = "EOvHFUy42uXgRfQ08IzfiTgFEob1pYNilyEGtCKpLlYiLLkTL9dbtZEjmuRMH92ZFvV2ha7pgVSSq9gL	"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)