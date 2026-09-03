from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/log', methods=['POST'])
def receive_log():
    data = request.json or {}
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = data.get('user_agent', 'Unknown')
    
    print(f"[+] LOG MASUK -> IP: {ip_address} | Device: {user_agent}")
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
