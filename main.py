"""A program to simulate a vending machine."""

from vending_machine.vending_machine import VendingMachine

__author__ = "COMP-2327 Faculty"
__version__ = "1.0.0"

def main() -> None:
    """The main entry point of the program."""

    vending_machine: VendingMachine = VendingMachine(2)

    vending_machine.select_item()
    vending_machine.receive_payment()
    vending_machine.receive_payment()
    vending_machine.select_item()
    vending_machine.receive_payment()
    vending_machine.select_item()
    vending_machine.receive_payment()
    vending_machine.select_item()

if __name__ == "__main__":
    main()
