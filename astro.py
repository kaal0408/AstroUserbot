from os import system
from logging import DEBUG, INFO, basicConfig, getLogger, warning
basicConfig(format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=INFO)
LOGS = getLogger("Helper")
ART = """ 
π­β’Starting Service of Astroβ’π°οΈπΈ
      Β© A S T R O Β©

βββββ¦ββββ¦βββββ¦ββββ¦ββββ
ββββββββββββββββββββββ
βββββββββ¬βββββ£ββββββββ
βββββ βββββββββββββ£ββββ
ββββββββββββββββββ£ββββ
βββββ©βββββββββββββ©ββββ

"""
try:
    system("git clone https://gitlab.com/loverboyxd/AstroUB && cd AstroUB && python3 astro")
    print(ART)
except:
  print("Hey My User You Have Got Error while Deploying Astro")
  print("Please Visit to Support for Help @Astro_helpchat")
