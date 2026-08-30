"""Compatibility entry point for Streamlit Community Cloud.

The deployed cloud app is configured to run app.py, while the real app
entry is sephiriadfm05.py. Importing it here executes the full app.
"""

import sephiriadfm05  # noqa: F401
