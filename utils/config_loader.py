import yaml
import os


class Config:
    def __init__(self, env="dev"):
        config_path = os.path.join("config", f"{env}.yaml")
        with open(config_path, "r") as file:
            self.data = yaml.safe_load(file)

    @property
    def base_url(self):
        return self.data["base_url"]

    @property
    def browser(self):
        return self.data["browser"]

    @property
    def headless(self):
        return self.data["headless"]

    @property
    def timeout(self):
        return self.data["timeout"]
