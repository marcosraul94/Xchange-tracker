import os
from importlib.util import spec_from_file_location, module_from_spec
from .base import View
from src.constants import migrations_path


class RunMigrations(View):
    @property
    def migrations(self):
        return [
            migration_name
            for migration_name in os.listdir(migrations_path)
            if migration_name.endswith(".py")
        ]

    @property
    def executed_migrations(self):
        return []

    @property
    def migrations_to_execute(self):
        return [
            migration_name
            for migration_name in self.migrations
            if migration_name not in self.executed_migrations
        ]

    @staticmethod
    def import_migration_module(migration_name: str):
        module_name = migration_name.split(".")[0]
        module_path = os.path.join(migrations_path, migration_name)

        spec = spec_from_file_location(module_name, module_path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)

        return module

    def render(self):
        executed_migrations = []

        try:
            for migration in self.migrations_to_execute:
                migration_module = self.import_migration_module(migration)

                print(f"Running {migration} migration...")
                migration_module.migrate()
                print(f"{migration} ran successfully!")

                executed_migrations.append(migration)

            return self.format_response({"Executed migrations": executed_migrations})

        except Exception as e:
            print(f"Error running migration {migration}: {e}")

            return self.format_response(
                {"Executed migrations": executed_migrations, "error": str(e)},
                status=500,
            )
