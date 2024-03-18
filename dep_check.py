Import("env")

# Install missing package
try:
    import pkg_resources
except ImportError:
    # setuptools is not installed in python 3.12, but it's required here:
    # ~/.platformio/platforms/espressif32/builder/frameworks/espidf.py
    env.Execute("$PYTHONEXE -m pip install setuptools==69.2.0")
