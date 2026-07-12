import sys
import os

# Add apps/backend to python path so it can import config, auth, main
sys.path.append(os.path.join(os.path.dirname(__file__), "../apps/backend"))

from main import app
