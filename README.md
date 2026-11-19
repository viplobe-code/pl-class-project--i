## Calculator Web Service (Python + Flask)

A simple web calculator built with Python and Flask. It works in two ways:
1. **As a Web Page (UI):** Humans can open it in a browser, type in two numbers, pick an operation, and get an answer.
2. **As an API:** Other programs can send a URL request to it and get the answer back in JSON format.

Instead of crashing when someone makes a mistake (like typing letters or dividing by zero), the app politely replies with a clear error message.

---

## Folder Structure

Make sure your project folder looks like this:

```text
calculator/
├── app.py               # The main Flask server and calculation engine
├── test_client.py       # A script to automatically test the API
└── templates/
    └── index.html       # The web page form for human users
```

*(Note: Flask requires HTML files to be inside a folder named `templates` right next to `app.py`.)*

---

## Setup & Installation

Open your terminal (or VS Code Terminal) and follow these steps:

### 1. Create and enter the project folder
```bash
mkdir calculator
cd calculator
```

### 2. Set up a Virtual Environment (`venv`)
This keeps the project's tools separate from the rest of your computer.
```bash
python -m venv venv
```

Activate it:
* **Windows:**
  ```bash
  venv\Scripts\activate
  ```
* **Mac / Linux:**
  ```bash
  source venv/bin/activate
  ```
*(You should now see `(venv)` at the start of your terminal line.)*

### 3. Install required packages
```bash
pip install flask requests
```

---

## How to Run the App

1. Start the server in your terminal:
   ```bash
   python app.py
   ```
2. Open your browser and go to:
   `http://127.0.0.1:5000`
3. To stop the server, press `Ctrl + C` in the terminal.

---

## How to Use the API

Other programs (or your browser's address bar) can call the calculator directly using this URL pattern:
`http://127.0.0.1:5000/api/<operation>?a=<number1>&b=<number2>`

**Supported Operations:** `add`, `subtract`, `multiply`, `divide`

### Examples

* **Addition (Success - Status `200`):**
  * **Request:** `http://127.0.0.1:5000/api/add?a=5&b=3`
  * **Response:**
    ```json
    {
      "operation": "add",
      "result": 8.0
    }
    ```

* **Divide by Zero (Client Error - Status `400`):**
  * **Request:** `http://127.0.0.1:5000/api/divide?a=9&b=0`
  * **Response:**
    ```json
    {
      "error": "Cannot divide by zero"
    }
    ```

* **Invalid Input (Client Error - Status `400`):**
  * **Request:** `http://127.0.0.1:5000/api/add?a=hello&b=2`
  * **Response:**
    ```json
    {
      "error": "Please enter two valid numbers"
    }
    ```

---

## Running Automated Tests

With your server running in one terminal, open a **second terminal** (with `venv` activated) and run:
```bash
python test_client.py
```
This script acts like another program calling your API to verify that both valid math and intentional errors return the expected status codes (`200` and `400`).

---

## Ideas to Take It Further
* Add `power` ($a^b$) and `modulus` ($a \bmod b$) operations.
* Create a `/api/gst` endpoint that takes a `price` and tax `rate` and returns the final price.
* Show a history table of the last 5 calculations on the home page.d storing the project taught by Prof. Shaunak Pal to store notes, those stuffs are taught over the first two session. [ Thank you ]
