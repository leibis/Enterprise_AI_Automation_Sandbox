import importlib
import inspect
import sys
import traceback

sys.path.insert(0, ".")
try:
    m = importlib.import_module("test_seguridad_ia")
    tests = [
        name
        for name, obj in inspect.getmembers(m)
        if inspect.isfunction(obj) and name.startswith("test_")
    ]
    print("Módulo cargado desde:", getattr(m, "__file__", "<desconocido>"))
    print("Funciones que empiezan con test_:", tests)
except Exception:
    print("ERROR al importar el módulo:")
    traceback.print_exc()
