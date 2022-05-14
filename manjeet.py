from os import system
from logging import DEBUG, INFO, basicConfig, getLogger, warning
basicConfig(format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=INFO)
LOGS = getLogger("Helper")
system("git clone https://gitlab.com/loverboyxd/AstroUB && cd AstroUB && python3 astro")
print("lul got error")
