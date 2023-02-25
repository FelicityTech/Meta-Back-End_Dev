from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class PayPal(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} dollars via PayPal.")


class Stripe(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} dollars via stripe.")


paypal = PayPal()
stripe = Stripe()

print(paypal.process_payment(100))
print(stripe.process_payment(50))