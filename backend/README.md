# Backend Setup
Follow the instructions below to properly setup the backend. Ensure you are on the proper directory.

```bash

> python -m venv .venv # this creates a virtual environment

> .\.venv\Script\activate # activate the virtual environment

> pip install -r .\requirements.txt # install the requirements needed in the backend

```

# Backend Activation
After the following steps above, continue to follow the steps if you wish to activate the backend.

```bash
uvicorn main:app --reload --port 8000
```
To deactivate, simply do `CTRL + C` on the terminal.