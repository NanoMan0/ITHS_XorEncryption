```
 __  __              _____  _____  ____  
|  \/  | __ _ _ __  / _ \ \/ / _ \|  _ \ 
| |\/| |/ _` | '_ \| | | \  / | | | |_) |
| |  | | (_| | | | | |_| /  \ |_| |  _ < 
|_|  |_|\__,_|_| |_|\___/_/\_\___/|_| \_\
-----------------------------------------

```

> **Man0 XOR - A Python Tool for Obfuscating / XORing Shellcode**

---

## About

A tool that obfusctates *raw* shellcode as part of payload chain using XOR.

---

## Features

- Input is from raw shellcode file.

- Select your own key for XOR (can be 1 byte or more):

    Supported key formats:
    - HEX: ex. `0xAA`
    - STRING: ex. `google`
    - NUMBER: ex. `123`

    > **NOTE** NUMBER above 255, will yield a key longer than 1 byte.

- Multiple output formats: *raw*, *Python Array*, or *C Array*.

- Output designed for easy copy pasta into ex. a loader. 

- XORed output prints to terminal and saves to selcted file location.

---

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/NanoMan0/ITHS_XorEncryption.git
    ```

2. **Install dependencies**:

    > **NOTE** no external dependecies as of current version

    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

### Command-Line Arguments:

To run the tool, specify the following arguments.

**Required arguments:**

- `--i`: INPUT. Name or path to the raw shellcode file.

- `--o`: OUTPUT. Name or path where the XORed shellcode will be saved.

- `--key`: XOR encryption key as *HEX*, *STRING* or *NUMBER*. 

- `--f`: OUTPUT FORMAT(required). 
    Choose from:
  - `raw`: For *raw* XORed shellcode (in bytes).
  - `py`: For *Python array*.
  - `c`: For *C Array*.

**Optional arguments:**

- `--p`: PRINT. Prints output code to terminal for copy pasta (not available for *raw* output).

### Example Usage:

```bash
python Man0Crypt.py --i raw-shellcode.xyz --o output-file.xyz --key 0xAA --f c
```