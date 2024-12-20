class MySQLRouter:
    route_app_labels = {'docker_app'}  # Models from 'docker_app' go to MySQL

    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'mysql_model':  # Explicitly route MySQLModel
            return 'additional'
        return 'default'  # Default to PostgreSQL

    def db_for_write(self, model, **hints):
        if model._meta.db_table == 'mysql_model':  # Explicitly route MySQLModel
            return 'additional'
        return 'default'  # Default to PostgreSQL

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.db_table == 'mysql_model' or
            obj2._meta.db_table == 'mysql_model'
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'mysqlmodel':  # Migrate MySQLModel to MySQL
            return db == 'additional'
        if model_name == 'postgresmodel':  # Migrate PostgresModel to PostgreSQL
            return db == 'default'
        return None
