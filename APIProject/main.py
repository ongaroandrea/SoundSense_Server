from src.routes.routes import app

# Init app
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")  # host='0.0.0.0', port=105,
