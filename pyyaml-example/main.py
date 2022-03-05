# Import pyyaml package
import yaml
from yaml.loader import SafeLoader

# Open the file and load the contents
with open('user-details.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)
