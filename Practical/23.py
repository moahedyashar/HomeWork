import json

class Config:
    def __init__(self, filename):
        """Initialize the Config class by loading settings from a JSON file."""
        self.settings = self._load_config(filename)
    
    def _load_config(self, filename):
        """Load the configuration settings from a file."""
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Configuration file '{filename}' not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the configuration file '{filename}'.")
            return {}
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return {}

    def get(self, key, default=None):
        """Get a setting by key, return default if key does not exist."""
        return self.settings.get(key, default)

    def get_all_settings(self):
        """Return all the settings as a dictionary."""
        return self.settings

    def has_key(self, key):
        """Check if a key exists in the settings."""
        return key in self.settings
