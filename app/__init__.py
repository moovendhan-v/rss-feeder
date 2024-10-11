from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load config, secret keys, etc.
    app.config.from_mapping(
        DATABASE='rss_sent.db',
        SECRET_KEY='your-secret-key',
    )

    with app.app_context():
        # Initialize database
        from . import db
        db.initialize_db()

    # Import and register the webhook routes
    from . import webhook
    app.register_blueprint(webhook.bp)

    return app
