import os
from importlib.util import spec_from_file_location, module_from_spec
from src.views.base import View
from src.logger import logger
from src.constants import migrations_path
from src.repositories.migration import MigrationRepo
from src.entities.migration import Migration


class MigrationsView(View):
    repo = MigrationRepo()

    @property
    def migrations(self):
        return [
            migration_name
            for migration_name in os.listdir(migrations_path)
            if migration_name.endswith(".py")
        ]

    def find_executed_migrations(self):
        tables_names = [table.name for table in self.repo.client.tables.all()]
        if self.repo.table_name not in tables_names:
            return []

        return [migration.name for migration in self.repo.find_all()]

    def find_migrations_to_execute(self):
        return [
            migration_name
            for migration_name in self.migrations
            if migration_name not in self.find_executed_migrations()
        ]

    @staticmethod
    def import_migration_module(migration_name: str):
        module_name = migration_name.split(".")[0]
        module_path = os.path.join(migrations_path, migration_name)

        spec = spec_from_file_location(module_name, module_path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)

        return module

    def migrate(self, migration: str):
        migration_module = self.import_migration_module(migration)

        logger.debug(f"Running {migration} migration...")
        migration_module.migrate()
        self.repo.create(Migration(name=migration))
        logger.debug(f"{migration} ran successfully!")

    def get(self):
        executed_migrations = []

        try:
            executed_migrations = self.find_executed_migrations()
            logger.debug(f"Executed migrations: {executed_migrations}")

            migrations_to_execute = self.find_migrations_to_execute()
            logger.debug(f"Migrations to execute: {migrations_to_execute}")

            for migration in migrations_to_execute:
                self.migrate(migration)

                executed_migrations.append(migration)

            return self.format_response(
                {
                    "Executed migrations": executed_migrations,
                }
            )

        except Exception as e:
            logger.error(f"Error running migration {migration}: {e}")

            return self.format_response(
                {"Executed migrations": executed_migrations, "error": str(e)},
                status_code=500,
            )


def migrate():
    from flask import Flask

    with Flask(__name__).app_context():
        MigrationsView().get()


if __name__ == "__main__":
    migrate()
