#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""


import importlib
import models.engine.db_storage
import models.engine.file_storage
import os
import pkgutil


classes = pkgutil.iter_modules(__path__)
classes = (module[1] for module in classes if not module[2])
classes = ((name.title().replace('_', ''), name) for name in classes)
classes = (
    (cls, importlib.import_module('models.' + mod))
    for cls, mod in classes
)
classes = {cls: getattr(mod, cls) for cls, mod in classes}


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = models.engine.db_storage.DBStorage()
else:
    storage = models.engine.file_storage.FileStorage()
storage.reload()
