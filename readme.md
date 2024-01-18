#Environment setting
## Install or update python.
```
# Current Python Version
python --version

# Install the Latest Python Version
python -m pip install --upgrade python

# Update Python Using Pip
python -m pip install --upgrade pip

# Install Python Launcher (Windows Only):
# This allows you to specify the version of Python you want to use when running scripts
python -m pip install --upgrade launcher

# Verify the Updated Version.
```

## Set requirments(Optional)
```
# Install Dependencies:
pip install -r requirements.txt

# Create requirements file
pip freeze > requirements.txt
```

## Virtual Environment
```
# Create
python -m venv genv

[!TIP]
> 권한 에러 발생 시 : Windows PowerShell 관리자로 실행 후 `Set-ExecutionPolicy RemoteSigned` > Y

# Activate
genv\Scripts\activate

# Listing packages in VE
pip list --local

# Deactivate
deactivate

[!NOTE]
> To create VE and access global package in venv `python -m venv venv --system-site-packages`
```

## Environment variables
```
# Install and import the python-dotenv package
pip install python-dotenv

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Create .env file
API_KEY=your_key
DEBUG=True
```

## Etc
```
# Install OpenAI
pip install --upgrade openai
```