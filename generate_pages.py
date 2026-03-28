import os

departments = [
    {"slug": "cse", "title": "Computer Science & Engineering", "icon": "💻", "desc": "Leading the digital revolution with cutting-edge computing education."},
    {"slug": "it", "title": "Information Technology", "icon": "🌐", "desc": "Bridging businesses and systems perfectly using reliable technology."},
    {"slug": "ee", "title": "Electronics Engineering", "icon": "📡", "desc": "Explore core electronics systems and embedded architecture."},
    {"slug": "elec", "title": "Electrical Engineering", "icon": "⚡", "desc": "Powering the globe by mastering highly efficient electrical systems."},
    {"slug": "me", "title": "Mechanical Engineering", "icon": "⚙️", "desc": "Designing tomorrow's physical machinery and sustainable robotics."},
    {"slug": "ce", "title": "Civil Engineering", "icon": "🏗️", "desc": "Constructing enduring infrastructures for resilient, smart cities."},
    {"slug": "ai", "title": "Centre for Artificial Intelligence", "icon": "🤖", "desc": "Pioneering state-of-the-art machine learning algorithms and neural networks."},
    {"slug": "iot", "title": "Centre for Internet of Things", "icon": "🌐", "desc": "Connecting billions of smart devices into one global network ecosystem."},
    {"slug": "emc", "title": "Engineering Mathematics & Computing", "icon": "🧮", "desc": "Applying deep mathematical logic to abstract theoretical computing."},
    {"slug": "cst", "title": "Centre for CS & Technology", "icon": "🖥️", "desc": "A unified hub for emerging software frameworks and digital interfaces."},
    {"slug": "arch", "title": "Architecture & Planning", "icon": "🏛️", "desc": "Blending gorgeous aesthetic design with structural and civic stability."},
    {"slug": "applied-science", "title": "Applied Science", "icon": "🔬", "desc": "Investigating fundamental physical and chemical scientific laws."},
    {"slug": "chem", "title": "Chemical Engineering", "icon": "🧪", "desc": "Synthesizing safe advanced materials and biochemical therapeutics."},
    {"slug": "ete", "title": "Electronics & Telecom Engg", "icon": "📶", "desc": "Designing high-speed communication hardware and 6G infrastructures."},
    {"slug": "hm", "title": "Humanities & Management", "icon": "📖", "desc": "Fostering well-rounded leadership, communication, and business intelligence."}
]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — MITS Gwalior</title>
  <meta name="theme-color" content="#060D1F">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@600,700&display=swap" rel="stylesheet">
  <link href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="../css/style.css">
</head>
<body>

  <!-- ================= OVERRIDDEN NAVBAR (Rel Paths) ================= -->
  <header class="navbar navbar--scrolled" id="navbar" style="background: rgba(6,13,31,0.98);">
    <div class="navbar__container">
      <a class="navbar__logo" href="../index.html">
        <img src="../assets/images/mits-logo.png" alt="MITS Logo" class="navbar__logo-img">
        <div class="navbar__logo-text-wrap">
          <span class="navbar__logo-text">MITS</span>
          <span class="navbar__logo-sub">Deemed University</span>
        </div>
      </a>
      <nav class="navbar__links" id="navbar-links">
        <a href="../index.html#about" class="nav-link">About</a>
        <a href="../index.html#academics" class="nav-link">Academics</a>
        <a href="../index.html#departments" class="nav-link active">Departments</a>
        <a href="../index.html#contact" class="nav-link">Contact</a>
      </nav>
      <a href="../index.html#contact" class="btn btn--primary navbar__cta">Apply Now</a>
    </div>
  </header>

  <main style="padding-top: var(--space-12);">
    <div class="container" style="padding-bottom: var(--space-9);">
      
      <!-- Dept Hero -->
      <div style="background: var(--bg-secondary); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: var(--space-8) var(--space-6); text-align: center; margin-bottom: var(--space-8);">
        <div style="font-size: 4rem; margin-bottom: var(--space-3);">{icon}</div>
        <h1 class="section-title" style="margin-bottom: var(--space-2);">{title}</h1>
        <p class="section-subtitle" style="max-width: 600px; margin: 0 auto; line-height: 1.6;">{desc} Exploring new horizons in learning, equipped with ultra-modern smart classrooms and industry-collaboration projects.</p>
        <div style="margin-top: var(--space-5);">
            <a href="#curriculum" class="btn btn--primary">View Curriculum</a>
            <a href="../index.html#departments" class="btn btn--outline" style="margin-left: var(--space-3);">Back to Departments</a>
        </div>
      </div>

      <!-- Dept Content Grid -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: var(--space-6);">
        
        <div style="background: var(--bg-secondary); border: 1px solid var(--border); border-radius: var(--radius-md); padding: var(--space-5);">
          <h3 style="color: var(--accent-gold); margin-bottom: var(--space-3);">Head of Department's Message</h3>
          <p style="color: var(--text-secondary); line-height: 1.7;">
            "Welcome to the {title} department. Our primary vision is to empower our students with solid theoretical foundations mixed with highly practical, project-based applications that solve global industry challenges."
          </p>
        </div>
        
        <div style="background: var(--bg-secondary); border: 1px solid var(--border); border-radius: var(--radius-md); padding: var(--space-5);">
          <h3 style="color: var(--accent-gold); margin-bottom: var(--space-3);">Key Laboratories</h3>
          <ul style="color: var(--text-secondary); list-style: none; display: flex; flex-direction: column; gap: 10px;">
            <li>✓ Advanced Simulator Lab</li>
            <li>✓ Computing & Prototyping Workshop</li>
            <li>✓ Data Analysis & Sensing Studio</li>
            <li>✓ AR/VR Innovation Bay</li>
          </ul>
        </div>

        <div id="curriculum" style="background: var(--bg-secondary); border: 1px solid var(--border); border-radius: var(--radius-md); padding: var(--space-5); grid-column: 1 / -1;">
          <h3 style="color: var(--accent-gold); margin-bottom: var(--space-3);">Curriculum & Research</h3>
          <p style="color: var(--text-secondary); line-height: 1.7; margin-bottom: var(--space-3);">
            Aligned directly with NEP 2020 frameworks, the {title} course is extremely flexible, offering major and minor specialization tracks. Students here participate in deep academic internships with leading MNCs and heavily lean into the Novel Engaging Courses (NEC).
          </p>
          <div style="display: flex; gap: var(--space-3); flex-wrap: wrap;">
             <span style="background: var(--bg-tertiary); padding: var(--space-1) var(--space-3); border-radius: var(--radius-full); font-size: var(--text-small);">Machine Learning Basics</span>
             <span style="background: var(--bg-tertiary); padding: var(--space-1) var(--space-3); border-radius: var(--radius-full); font-size: var(--text-small);">Advanced Embedded Principles</span>
             <span style="background: var(--bg-tertiary); padding: var(--space-1) var(--space-3); border-radius: var(--radius-full); font-size: var(--text-small);">Global Project Ethics</span>
             <span style="background: var(--bg-tertiary); padding: var(--space-1) var(--space-3); border-radius: var(--radius-full); font-size: var(--text-small);">Quantum Data Math</span>
          </div>
        </div>

      </div>

    </div>
  </main>
</body>
</html>"""

os.makedirs('pages', exist_ok=True)

for dept in departments:
    filename = f"pages/{dept['slug']}.html"
    content = html_template.format(**dept)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {filename}")

print("Done generating pages.")
