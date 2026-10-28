"""Defines the VendingMachineState enumeration."""

from enum import Enum

__author__ = "Dong Le Quoc Bao"
__version__ = "1.0.0"

class VendingMachineState(Enum):
    """Represents the states of a vending machine."""

    NO_PAYMENT = 0
    """User has not made a payment."""

    HAS_PAYMENT = 1
    """User has made a payment."""

    OUT_OF_STOCK = 2
    """The vending machine no longer has any of the product."""
