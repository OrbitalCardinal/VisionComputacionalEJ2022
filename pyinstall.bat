if exist python-env (
    python-env\Scripts\python.exe -m pip install -r requirements.txt
) else (
    python -m venv python-env 
    python-env\Scripts\python.exe -m pip install -r requirements.txt
) 