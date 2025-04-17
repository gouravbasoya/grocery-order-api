from flask import Flask
from routes.products import bp as products_bp
from routes.orders import bp as orders_bp

# Initialize Flask application
app = Flask(__name__)

# Register blueprints with URL prefixes
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(orders_bp, url_prefix='/orders')

if __name__ == '__main__':
    # Run in debug mode for development
    app.run(debug=True)