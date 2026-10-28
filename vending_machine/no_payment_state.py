"""Defines the NoPaymentState class."""
from vending_machine.state import State

__author__ = "Dong Le Quoc Bao"
__version__ = "1.0.0"

class NoPaymentState(State):
    """The state where the user has not made a payment."""
    
    def receive_payment(self, machine: "VendingMachine") -> None:
        """ Accepts payment and transitions to HasPaymentState.
        
        Arg:
           machine (VendingMachine): The vending machine receiving payment.
        """   
        machine.output_to_display("Payment ADDED")
        machine.state = machine.has_payment_state
        
    def select_item(self, machine: "VendingMachine") -> None:
        """Displays an insufficient-funds message.
        
        Args:
            machine (VendingMachine): The vending machine being selected from.
        """
        
        machine.output_to_display("INSUFFICIENT FUNDS - PLEASE ADD PAYMENT")
        