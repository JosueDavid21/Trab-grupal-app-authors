from flask import Flask
from flask_cors import CORS
from database.db_config import get_connection
from yoyo import read_migrations

from config import config

# Routes
from routes import AuthorRest

app = Flask(__name__)

# CORS(app, resources={"*": {"origins": "http://localhost:9300"}})


def page_not_found(error):
    return "<h1>Pagina no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Migraciones
    # backend = get_connection()
    # migrations = read_migrations('/migrations')
    # with backend.lock():
    #     backend.apply_migrations(backend.to_apply(migrations))
    
    # Blueprints
    app.register_blueprint(AuthorRest.main, url_prefix='/authors')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(debug=True, host='0.0.0.0')