import os
import site

# read environment variable set in maya_stubgen.__main__
# to ensure that maya-stubgen is available when running with mayapy
if os.getenv("MAYASTUB_VENV"):
    for path in os.getenv("MAYASTUB_VENV").split(":"):
        site.addsitedir(path)
