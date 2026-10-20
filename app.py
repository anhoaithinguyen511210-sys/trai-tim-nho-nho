from flask import Flask, render_template_string

app = Flask(__name__)

# Khi bạn có bài thơ, hãy gửi cho ChatGPT để thêm vào biến POEM bên dưới.
# Tạm thời để trống như bạn yêu cầu.
PAGE_TITLE = "Những vần thơ của tôi"
POEM = ""

HTML = """
<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#ffe5ee">
  <title>{{ title }}</title>
  <style>
    * { box-sizing: border-box; }
    body {
      margin: 0; min-height: 100vh; overflow-x: hidden;
      display: grid; place-items: center; padding: 24px 14px;
      font-family: Georgia, "Times New Roman", serif; color: #702944;
      background: radial-gradient(circle at top, #fff8fb, #ffe2ec 52%, #f6c6d9);
    }
    .card {
      width: min(720px, 100%); padding: 34px 22px; text-align: center;
      border: 1px solid rgba(255,255,255,.9); border-radius: 28px;
      background: rgba(255,255,255,.78);
      box-shadow: 0 18px 55px rgba(179,79,120,.22);
      position: relative; z-index: 2;
    }
    .heart {
      font-size: 78px; line-height: 1.2; display: inline-block; color: #ff477e;
      filter: drop-shadow(0 8px 12px rgba(255,71,126,.35));
      animation: beat 1.1s infinite;
    }
    @keyframes beat {
      0%,100% { transform: scale(1); }
      15% { transform: scale(1.16); }
      30% { transform: scale(1); }
      45% { transform: scale(1.1); }
    }
    h1 { margin: 12px 0 8px; font-size: clamp(27px, 6vw, 43px); }
    .subtitle {
      color: #a65a78; margin: 0 0 25px;
      font: 14px/1.6 Arial, sans-serif;
    }
    .poem {
      white-space: pre-wrap; overflow-wrap: anywhere; line-height: 1.95;
      font-size: 19px; padding: 24px 16px; border-radius: 18px;
      background: #fff8fb; min-height: 110px;
    }
    .empty { color: #b77b91; font-style: italic; }
    .signature { margin-top: 22px; font-style: italic; color: #a65a78; }
    .floating {
      position: fixed; bottom: -40px; opacity: .55;
      animation: floatUp linear infinite; z-index: 1; pointer-events: none;
    }
    @keyframes floatUp {
      to { transform: translateY(-115vh) rotate(25deg); opacity: 0; }
    }
    @media (prefers-reduced-motion: reduce) {
      .heart, .floating { animation: none; }
    }
.message {
    margin: 20px auto;
    max-width: 500px;
    padding: 16px;
    color: #c2185b;
    font-size: 20px;
    line-height: 1.7;
    text-align: center;
    font-family: cursive;
    background: rgba(255, 255, 255, 0.65);
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(255, 105, 180, 0.2);
}

.music-player {
    margin: 20px auto;
    max-width: 500px;
    text-align: center;
    color: #c2185b;
}
  </style>
</head>
<body>
  <main class="card">
    <div class="heart" aria-label="Trái tim">♥</div>
    <h1>{{ title }}</h1>
    <p class="subtitle">Một góc nhỏ dành riêng cho những vần thơ của tôi</p>
    <div class="poem">{% if poem %}{{ poem }}{% else %}<span class="empty">Bài thơ sẽ được thêm vào đây sau…</span>{% endif %}</div>
  <div class="signature">♡ viết bằng cả trái tim ♡</div>
<div class="message">
  Ngày Phụ nữ Việt Nam, con xin chúc mẹ
  luôn khỏe mạnh, bớt cáu kỉnh và mắng con!! 💗💗💗
</div>
<div class="music-player">
  <p>🎵 Một giai điệu dành riêng cho mẹ 💗</p>
  <iframe
    width="100%"
    height="200"
    src="https://www.youtube.com/embed/sICoUsvVAok"
    title="Bài hát dành cho mẹ"
    allow="encrypted-media; picture-in-picture"
    allowfullscreen>
  </iframe>
</div>
  </main>
  <script>
    for (let i = 0; i < 18; i++) {
      const heart = document.createElement("div");
      heart.className = "floating";
      heart.textContent = Math.random() > 0.5 ? "♥" : "♡";
      heart.style.left = (Math.random() * 100) + "vw";
      heart.style.animationDuration = (8 + Math.random() * 9) + "s";
      heart.style.animationDelay = (-Math.random() * 15) + "s";
      heart.style.fontSize = (14 + Math.random() * 22) + "px";
      heart.style.color = ["#ff477e", "#d96a9a", "#f18bb1"][i % 3];
      document.body.appendChild(heart);
    }
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, title=PAGE_TITLE, poem=POEM)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
