from pathlib import Path
import zipfile, textwrap

root = Path("/storage/emulated/0/Download/noorul_quran_online_academy")
root.mkdir(exist_ok=True)
root.mkdir(exist_ok=True)

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#123b32">
  <meta name="description" content="Noorul Quran Online Academy — online Quran learning, Hifz, Nazra, Tajweed and revision classes.">
  <title>Noorul Quran Online Academy</title>
  <style>
    :root{--green:#123b32;--green2:#1d5a49;--gold:#d9b66f;--cream:#fbf8f0;--ink:#24312c;--muted:#66736c}
    *{box-sizing:border-box} html{scroll-behavior:smooth}
    body{margin:0;font-family:Arial,Helvetica,sans-serif;background:var(--cream);color:var(--ink);line-height:1.65}
    a{color:inherit;text-decoration:none}.top{background:var(--green);color:#fff;padding:12px 6%;display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;font-size:14px}
    header{background:#fff;position:sticky;top:0;z-index:5;box-shadow:0 2px 14px #0000000b}
    nav{max-width:1120px;margin:auto;padding:15px 22px;display:flex;align-items:center;justify-content:space-between;gap:20px}
    .brand{display:flex;align-items:center;gap:11px;font-weight:700;color:var(--green);font-size:18px}
    .logo{width:42px;height:42px;border-radius:50%;background:var(--green);color:var(--gold);display:grid;place-items:center;font-size:22px}
    .links{display:flex;gap:22px;align-items:center;font-size:14px}.links a:hover{color:var(--green2)}
    .btn{display:inline-block;background:var(--gold);color:#20372f;padding:12px 20px;border-radius:8px;font-weight:700;border:0;cursor:pointer}
    .hero{background:linear-gradient(120deg,#10392f 0%,#1b5747 100%);color:white;padding:82px 22px}
    .hero-inner{max-width:1050px;margin:auto;display:grid;grid-template-columns:1.25fr .75fr;gap:45px;align-items:center}
    .eyebrow{color:#f0d99f;text-transform:uppercase;letter-spacing:2px;font-size:12px;font-weight:700}
    h1{font-size:clamp(36px,5vw,58px);line-height:1.12;margin:15px 0}
    .hero p{max-width:600px;color:#e4eee9;font-size:17px}
    .hero-card{border:1px solid #ffffff35;background:#ffffff12;border-radius:20px;padding:28px;text-align:center}
    .crescent{font-size:70px;color:var(--gold);line-height:1.2}.arabic{font-size:29px;color:#f0d99f;margin:10px 0}
    section{padding:68px 22px}.wrap{max-width:1050px;margin:auto}.section-head{text-align:center;max-width:650px;margin:0 auto 35px}
    h2{color:var(--green);font-size:32px;margin:0 0 10px}.section-head p,.muted{color:var(--muted)}
    .cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
    .card{background:white;border:1px solid #e9e5da;border-radius:15px;padding:24px;box-shadow:0 8px 25px #183b3010}
    .card .symbol{font-size:28px}.card h3{color:var(--green);margin:12px 0 7px}
    .about{background:#f1eee4}.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:38px;align-items:center}
    .check{padding:0;list-style:none}.check li{margin:12px 0}.check li:before{content:"✓";color:var(--green2);font-weight:bold;margin-right:10px}
    .steps{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;text-align:center}.step{padding:20px}
    .num{width:42px;height:42px;border-radius:50%;background:var(--green);color:white;display:grid;place-items:center;margin:0 auto 12px;font-weight:bold}
    .contact{background:var(--green);color:white}.contact h2{color:white}.contact .section-head p{color:#d9e6df}
    .contact-box{max-width:650px;margin:auto;background:#ffffff12;border:1px solid #ffffff30;padding:28px;border-radius:16px}
    label{display:block;margin:12px 0 5px;font-size:14px}input,select,textarea{width:100%;padding:13px;border-radius:8px;border:1px solid #d7ddd8;font:inherit;background:white;color:#24312c}
    textarea{min-height:90px;resize:vertical}.contact .btn{width:100%;margin-top:18px;font-size:16px}
    footer{background:#0c2c25;color:#d9e6df;text-align:center;padding:24px;font-size:13px}
    @media(max-width:760px){.hero-inner,.about-grid{grid-template-columns:1fr}.cards,.steps{grid-template-columns:1fr}.links{gap:12px;flex-wrap:wrap;justify-content:flex-end}.links a:not(.btn){display:none}.hero{padding:60px 22px}}
  </style>
</head>
<body>
  <div class="top"><span>Online Quran Learning</span><span>Flexible class timings · Monthly fee</span></div>
  <header>
    <nav>
      <a class="brand" href="#"><span class="logo">☾</span><span>Noorul Quran<br>Online Academy</span></a>
      <div class="links"><a href="#courses">Courses</a><a href="#about">About</a><a href="#how">How to Join</a><a class="btn" href="#contact">Enroll Now</a></div>
    </nav>
  </header>

  <main>
    <section class="hero">
      <div class="hero-inner">
        <div>
          <div class="eyebrow">Learn the Quran from home</div>
          <h1>Begin your Quran journey with confidence.</h1>
          <p>Personal online Quran classes with a focus on correct recitation, Hifz, regular revision and steady progress — one lesson at a time.</p>
          <a class="btn" href="#contact">Ask About Classes</a>
        </div>
        <div class="hero-card">
          <div class="crescent">☾</div>
          <div class="arabic" lang="ar" dir="rtl">وَقُل رَّبِّ زِدْنِي عِلْمًا</div>
          <p>“My Lord, increase me in knowledge.”</p>
          <small>Surah Taha · 20:114</small>
        </div>
      </div>
    </section>

    <section id="courses">
      <div class="wrap">
        <div class="section-head"><h2>Our Quran Classes</h2><p>Lessons are planned according to each student's level and learning pace.</p></div>
        <div class="cards">
          <article class="card"><div class="symbol">📖</div><h3>Hifz-ul-Quran</h3><p class="muted">Memorisation with daily lesson targets, listening practice and regular revision to help strengthen what has been memorised.</p></article>
          <article class="card"><div class="symbol">🌙</div><h3>Nazra & Reading</h3><p class="muted">Learn to read the Holy Quran with guidance, fluency practice and correction of recitation.</p></article>
          <article class="card"><div class="symbol">✨</div><h3>Tajweed & Revision</h3><p class="muted">Practise pronunciation and basic Tajweed rules, or revise previously memorised Surahs and Paras.</p></article>
        </div>
      </div>
    </section>

    <section class="about" id="about">
      <div class="wrap about-grid">
        <div><div class="eyebrow" style="color:#8b713b">About the academy</div><h2>A calm, supportive way to learn.</h2><p class="muted">Noorul Quran Online Academy offers one-to-one online teaching. Lessons are guided with patience, consistency and attention to the student's progress.</p></div>
        <div class="card"><h3>What students can expect</h3><ul class="check"><li>Personal attention from the teacher</li><li>Flexible class timings</li><li>Monthly fee structure</li><li>Regular Hifz and revision practice</li><li>Progress updates for parents</li></ul></div>
      </div>
    </section>

    <section id="how">
      <div class="wrap">
        <div class="section-head"><h2>How to Join</h2><p>Getting started is simple.</p></div>
        <div class="steps">
          <div class="step"><div class="num">1</div><h3>Send an inquiry</h3><p class="muted">Share the student's age, current level and preferred timing.</p></div>
          <div class="step"><div class="num">2</div><h3>Discuss a plan</h3><p class="muted">Choose the suitable course and monthly class schedule.</p></div>
          <div class="step"><div class="num">3</div><h3>Start learning</h3><p class="muted">Begin lessons and follow a steady learning and revision routine.</p></div>
        </div>
      </div>
    </section>

    <section class="contact" id="contact">
      <div class="wrap">
        <div class="section-head"><h2>Start Learning Today</h2><p>Send your details and we will help you choose the right class.</p></div>
        <div class="contact-box">
          <form id="inquiryForm">
            <label for="student">Student name</label><input id="student" required placeholder="Enter student name">
            <label for="age">Student age</label><input id="age" required inputmode="numeric" placeholder="Enter age">
            <label for="course">Interested course</label>
            <select id="course"><option>Hifz-ul-Quran</option><option>Nazra & Reading</option><option>Tajweed</option><option>Revision</option></select>
            <label for="timing">Preferred class timing</label><input id="timing" placeholder="e.g. 5:00 pm">
            <label for="message">Any message (optional)</label><textarea id="message" placeholder="Tell us about the student's current Quran level"></textarea>
            <button class="btn" type="submit">Send Inquiry on WhatsApp</button>
          </form>
          <p style="font-size:12px;color:#d9e6df;margin-bottom:0">Please add your WhatsApp number in the website settings before publishing. See README.txt.</p>
        </div>
      </div>
    </section>
  </main>
  <footer>© <span id="year"></span> Noorul Quran Online Academy · May Allah bless every effort to learn the Quran.</footer>
  <script>
    // IMPORTANT: Replace the digits below with your WhatsApp number, including country code.
    // Pakistan example format: 923001234567 (no + sign, spaces or dashes).
    const WHATSAPP_NUMBER = "92XXXXXXXXXX";
    document.getElementById("year").textContent = new Date().getFullYear();
    document.getElementById("inquiryForm").addEventListener("submit", function(e) {
      e.preventDefault();
      if (WHATSAPP_NUMBER.includes("X")) {
        alert("Please add your WhatsApp number in index.html first. See README.txt.");
        return;
      }
      const details = [
        "Assalamualaikum! I want to ask about online Quran classes.",
        "Student: " + document.getElementById("student").value,
        "Age: " + document.getElementById("age").value,
        "Course: " + document.getElementById("course").value,
        "Preferred timing: " + (document.getElementById("timing").value || "Flexible"),
        "Message: " + (document.getElementById("message").value || "None")
      ].join("\n");
      window.open("https://wa.me/" + WHATSAPP_NUMBER + "?text=" + encodeURIComponent(details), "_blank");
    });
  </script>
</body>
</html>
'''

readme = """NOORUL QURAN ONLINE ACADEMY — WEBSITE FILES

Files:
- index.html: your website

BEFORE PUBLISHING:
1. Open index.html in a text editor.
2. Find: const WHATSAPP_NUMBER = "92XXXXXXXXXX";
3. Replace it with your WhatsApp number in international format, digits only.
   Pakistan example: 923001234567 (do not include +, spaces or dashes).
4. Save the file.

The website includes:
- Hifz-ul-Quran, Nazra, Tajweed and revision course sections
- About the academy and how-to-join sections
- An inquiry form that prepares a WhatsApp message
- Responsive layout for mobile and computer

IMPORTANT:
- This is a front-end information website. It does not collect or store student data online.
- The inquiry form only opens WhatsApp after the WhatsApp number is configured.
- Add your actual monthly fee, teacher details, and class timings before publishing if you want them displayed.
- Do not publish a personal phone number unless you are comfortable using it for student inquiries.
"""
(root / "index.html").write_text(html, encoding="utf-8")
(root / "README.txt").write_text(readme, encoding="utf-8")

zip_path = Path("/storage/emulated/0/Download/noorul_quran_online_academy_website.zip")


with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(root / "index.html", "noorul_quran_online_academy/index.html")
    z.write(root / "README.txt", "noorul_quran_online_academy/README.txt")

print(f"Created: {zip_path}")
print(f"Website preview file: {root / 'index.html'}")
