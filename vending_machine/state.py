"""Defines the State interface.

A common interface for all vending machine states.
"""
from abc import ABC, abstractmethod

from vending_machine.vending_machine import VendingMachine

__author__ = "Dong Le Quoc Bao"    
__version__ = "1.0.0"   

class State(ABC):
    """Represents the state of a vending machine."""

    @abstractmethod
    def receive_payment(self, machine: "VendingMachine") -> None:
        """Handle a payment being received.
        
        Args:
            machine (VendingMachine): The vending machine receiving payment.
        
        """

    @abstractmethod
    def select_item(self, machine: "VendingMachine") -> None:
        """Customer selects the product to dispense.
        
        Args:
            machine (VendingMachine): The vending machine being selectedd from.
        
        """
    