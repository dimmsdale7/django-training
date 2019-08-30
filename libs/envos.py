from pathlib import Path

env_file = '.env'
env_path = Path(env_file)
if env_path.is_file():
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=env_file, verbose=True)
import os
env_os = os