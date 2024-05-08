import os
import sys
from datetime import datetime
from src.constants import migrations_path


if __name__ == "__main__":
    name = sys.argv[2]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    migration_name = f"{now}-{name}.py"
    migration_path = os.path.join(migrations_path, migration_name)
    migration_template = """from src.db import get_client


def migrate():
    client = get_client()
"""

    with open(migration_path, "w") as file:
        file.write(migration_template)

    print(f"Migration template created: {migration_name}")
