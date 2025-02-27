import os
import json
from pathlib import Path

CONFIG_FILE = Path(os.path.expanduser("~")) / ".easychat_config.json"

def load_api_key():
    """Load API key from configuration file"""
    try:
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
                return config.get("api_key")
    except Exception as e:
        print(f"Warning: Could not read configuration: {e}")
    return None

def save_api_key(api_key):
    """Save API key to configuration file"""
    try:
        config = {}
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, "r") as f:
                try:
                    config = json.load(f)
                except:
                    pass
        
        config["api_key"] = api_key
        
        # Ensure directory exists
        CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
        
        # Write configuration with user-only read/write permissions
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f)
        
        # Set file permissions to user read/write only (0600)
        os.chmod(CONFIG_FILE, 0o600)
        return True
    except Exception as e:
        print(f"Warning: Could not save configuration: {e}")
        return False
