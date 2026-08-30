"""Compatibility entry point for Streamlit Community Cloud.

The deployed cloud app is configured to run app.py, while the real app
entry is sephiriadfm05.py. Execute it the same way `streamlit run
sephiriadfm05.py` does — as a plain script via runpy — so the whole app
is NOT imported as a module. Importing it as a module makes the module
import window span the entire app run, which trips CPython 3.14's
import finalization (KeyError from sys.modules.pop) under concurrent
sessions on Streamlit Cloud.
"""

import runpy

runpy.run_path("sephiriadfm05.py", run_name="__main__")
