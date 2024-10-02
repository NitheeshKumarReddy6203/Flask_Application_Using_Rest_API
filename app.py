from flask import Flask
from Controllers.customer_controller import customer_blueprint
from Controllers.order_controller import order_blueprint
from Controllers.product_controller import product_blueprint

app = Flask(__name__)

app.register_blueprint(customer_blueprint, url_prefix='/api')
app.register_blueprint(order_blueprint, url_prefix='/api')
app.register_blueprint(product_blueprint, url_prefix='/api')

@app.route('/')
def home():
    return "Welcome to the REST API"

if __name__ == "__main__":
    app.run(debug=True)


