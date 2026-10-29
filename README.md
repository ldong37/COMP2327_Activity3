# Intermediate Software Development Activity 3

This activity will help to reinforce learning of the Module 3 concepts of:

- OOP Design Patterns

## Author

Dong Le Quoc Bao

## Additional Information

This project implements the "State Design Pattern" to simulate a vending machine. 
- The `State` interface defines the common behavior.
- `NoPaymentState`, `HasPaymentState`, and `OutOfStockState` implement the specific behaviors.
- The `VendingMachine` class maintains a reference to the current state and delegates payment and item selection requests to it.
