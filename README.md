# Simple Currency Converter (Python) 💰

A straightforward command-line utility for converting an amount from one currency to another using pre-defined exchange rates.

## ✨ Features

* **Currency Support:** Converts between **USD**, **EUR**, and **CAD**.
* **Input Validation:** Ensures the user enters a valid positive amount and one of the supported currency codes.
* **Simple Conversion:** Calculates the target amount based on a hardcoded set of exchange rates.

---

## 🚀 How to Run

### Prerequisites

You need **Python 3.x** installed on your system.

### Running the Script

1.  **Save the file:** Save the code as `currency_convertor.py`.
2.  **Open your terminal/command prompt.**
3.  **Execute the script** using Python:

    ```bash
    python currency_convertor.py
    ```

### Example Usage

The program will prompt you for input:

Enter the amount: 100 

Source currency (USD/EUR/CAD): usd

Target currency (USD/EUR/CAD): eur

100.0 usd is equal to eur.

---

## 🛠️ Code Overview

The script is structured into four main functions:

| Function | Description |
| :--- | :--- |
| `get_amount()` | Prompts the user for the amount to convert and handles **ValueError** exceptions for invalid (non-numeric or non-positive) input. |
| `get_currency(label)` | Prompts the user for a currency code (Source or Target) and validates the input against the supported list (`usd`, `eur`, `cad`). |
| `convert(amount, source_currency, target_currency)` | Contains the fixed `exchange_rates` and performs the conversion calculation. |
| `main()` | The main execution function that calls the input functions and prints the final result. |

---

## 🔧 Exchange Rates

The current exchange rates are hardcoded within the `convert` function:

| From | To EUR | To CAD |
| :--- | :--- | :--- |
| **USD** | 0.85 | 1.25 |
| **EUR** | 1.18 (to USD) | 1.47 |
| **CAD** | 0.80 (to USD) | 0.68 (to EUR) |

*Note: These rates are fixed and do not update in real-time.*

---
