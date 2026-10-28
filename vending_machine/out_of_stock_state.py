"""Defines the OutOfStockState class."""

from vending_machine.state import State
__author__ = "Dong Le Quoc Bao"
__version__ = "1.0.0"

class OutOfStockState(State):
    """The state where the vending machine has no product left."""
    def receive_payment(self, machine: "VendingMachine") -> None:
        """Displays an out-of-stock message.
        Args:
            machine (VendingMachine): The vending machine receiving payment.
        
        """
        
        machine.output_to_display("OUT_OF_STOCK")
        
        
    def select_item(self, machine: "VendingMachine") -> None:
        """Does nothing since the machine is out of stock
        Args:
            machine (VendingMachine): The vending machine being selected from.
        """
        
        machine.output_to_display("")