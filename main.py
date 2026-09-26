from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)
CORRECT_PASSWORD = "050"  # pick your own 3-digit password

LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
  <h2>Login</h2>
  <input type="text" id="pwd" placeholder="Enter 3-digit password" maxlength="3">
  <button onclick="submitLogin()">Login</button>
  <p id="result"></p>

  <script>
    async function submitLogin() {
      const pwd = document.getElementById('pwd').value;
      const res = await fetch('/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({password: pwd})
      });
      const data = await res.json();
      document.getElementById('result').innerText = data.status;
    }
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(LOGIN_PAGE)

@app.route("/login", methods=["POST"])
def login():
    pwd = request.json.get("password", "")
    if pwd == CORRECT_PASSWORD:
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "fail"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)