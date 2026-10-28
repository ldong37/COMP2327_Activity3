"""Defines the VendingMachine class."""

from vending_machine.vending_machine_state import VendingMachineState

__author__ = "Dong Le Quoc Bao"
__version__ = "1.0.0"

class VendingMachine:
    """Represents a vending machine."""

    def __init__(self, product_count: int) -> None:
        """Initializes a new instance of the VendingMachine class."""

        self.__product_count: int = product_count
        self.state = VendingMachineState.NO_PAYMENT

    @property
    def state(self) -> VendingMachineState:
        """Returns the current state of the vending machine."""

        return self.__state

    @state.setter
    def state(self, state: VendingMachineState) -> None:
        """Sets the state of the vending machine."""

        self.__state = state

    def receive_payment(self) -> None:
        """Accepts pay payment from the customer."""

        match(self.state):
            case VendingMachineState.NO_PAYMENT:
                self.output_to_display("PAYMENT ADDED")

                self.state = VendingMachineState.HAS_PAYMENT

            case VendingMachineState.HAS_PAYMENT:
                self.output_to_display("PAYMENT ALREADY ADDED")

            case VendingMachineState.OUT_OF_STOCK:
                self.output_to_display("OUT OF STOCK")

    def select_item(self) -> None:
        """Customer selects the product to dispense."""

        match(self.state):
            case VendingMachineState.NO_PAYMENT:
                self.output_to_display("INSUFFICIENT FUNDS - PLEASE ADD PAYMENT")

            case VendingMachineState.HAS_PAYMENT:
                self.output_to_display("DISPENSING...", False)
                self.dispense_product()

                self.__state = VendingMachineState.OUT_OF_STOCK \
                    if self.__product_count <= 0 else \
                    VendingMachineState.NO_PAYMENT

            case VendingMachineState.OUT_OF_STOCK:
                self.output_to_display("")

            case _:
                self.output_to_display("ERROR OCCURRED")

    def dispense_product(self) -> None:
        """Dispenses the product to the customer."""

        if self.__product_count == 0:
            self.output_to_display("ERROR: OUT OF STOCK")
            self.state = VendingMachineState.OUT_OF_STOCK
        else:
            self.__product_count -= 1
            self.output_to_display("ENJOY YOUR ITEM")

            self.state = VendingMachineState.OUT_OF_STOCK \
                    if self.__product_count <= 0 else \
                    VendingMachineState.NO_PAYMENT

    def output_to_display(self, message: str,
                          include_line_break: bool=True) -> None:
        """Outputs message to the machines display.

        If the message is blank, nothing is output to the display.

        Args:
            message (str): The message to display on the screen.
            include_line_break (bool): When True, includes a new line
                character at the end of message; otherwise a blank
                string.
        """

        if message.strip() != "":
            print(f"{message}{"\n" if include_line_break else ""}", end="")
