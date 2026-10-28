"""Defines the HasPaymentState class."""
from vending_machine.state import State

__author__ = "Dong Le Quoc Bao "
__version__ = "1.0.0"


class HasPaymentState(State):
    """The state where the user has made a payment."""
    
    def receive_payment(self, machine: "VendingMachine") -> None:
        """Displays a message that payment was already added.
        
        Args:
            machine (VendingMachine):The vending machine recieving payment.
        """
        
        machine.output_to_display("PAYMENT ALREADY ADDED")
        
    def select_item(self,machine: "VendingMachine") -> None:
        """Dispenses an item and transitions to the nest state.
        
           Args:
               machine (VendingMachine): The vending machine being selected from.
        """
        machine.output_to_display("DISPENDING...", False)
        machine.dispense_product()
        

