from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
        <form action="/submit" method="POST">
            <input name="username" placeholder="Enter username">
            <input type="submit">
        </form>
    """)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    if not username or len(username) > 20:
        return jsonify({'error': 'Invalid username'}), 400
    return jsonify({'message': f'Welcome, {username}!'}), 200

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
