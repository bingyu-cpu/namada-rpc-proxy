# Solution For namadac shielded-sync Issue

This script is intended to fix the issue in namadac shielded-sync process: "error sending request for url (http://127.0.0.1:26657/): connection closed before message completed."

## Installation

1. Download the Python script - `rpc_proxy.py`.

2. Install necessary Python libraries by running the following commands:
    pip install requests
    pip install flask

## Steps to Use the Script

1. Run `rpc_proxy.py` with Python3. Tools like `tmux` can be used to keep the script running even after the shell is closed.
    python3 rpc_proxy.py
   
2. Follow the instruction given by the script and enter your RPC URL accordingly.

3. Execute the sync operation with:
    namadac shielded-sync --node http://127.0.0.1:5000

4. Wait till the synchronization gets successfully completed. Have patience!
