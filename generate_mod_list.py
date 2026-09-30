import os
import re

def clean_mod_name(filename):
    name = filename.replace('.jar', '')
    # simple attempt to strip version numbers like -1.20.1 or -v1.0.0
    name = re.sub(r'(-|_)[\d\.]+(-.*)?', '', name)
    name = name.replace('-', ' ').replace('_', ' ')
    # if the name is too mangled, just use the original without .jar
    if len(name) < 2:
        return filename.replace('.jar', '')
    return name.title()

def main():
    mod_folder = r'c:\Users\AstralSterling\Projects\minecraft_install_guide\full_mod_folder'
    mods = []
    
    if os.path.exists(mod_folder):
        for f in os.listdir(mod_folder):
            if f.endswith('.jar'):
                mods.append((clean_mod_name(f), f))
    
    mods.sort(key=lambda x: x[0].lower())
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homestead - Mod List</title>
    <meta name="description" content="List of all mods running on the Homestead server.">
    <link rel="icon" type="image/jpeg" href="favicon.jpg">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
    <style>
        .mod-list {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1rem;
            margin-top: 2rem;
        }}
        .mod-item {{
            background: rgba(255, 255, 255, 0.05);
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            word-break: break-all;
        }}
        .mod-item strong {{
            display: block;
            margin-bottom: 0.5rem;
            color: #fff;
        }}
        .mod-item span {{
            font-size: 0.85rem;
            color: rgba(255, 255, 255, 0.6);
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Server Mod List</h1>
            <div style="margin-top: 1rem; margin-bottom: 2rem; display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap;">
                <a href="index.html" style="color: #5865F2; text-decoration: none; font-weight: 600;">⬅️ Back to Installation Guide</a>
                <a href="rules.html" style="color: #5865F2; text-decoration: none; font-weight: 600;">📜 View Server Rules</a>
            </div>
            <p>Here are all the {len(mods)} mods currently active on the Homestead server.</p>
        </header>

        <main>
            <div class="mod-list">
"""
    for display_name, original_name in mods:
        html += f"""                <div class="mod-item">
                    <strong>{display_name}</strong>
                    <span>{original_name}</span>
                </div>
"""
        
    html += """            </div>
        </main>
        
        <footer>
            <p>See you on the server! 🚀</p>
        </footer>
    </div>
</body>
</html>"""

    with open(r'c:\Users\AstralSterling\Projects\minecraft_install_guide\mod-list.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    main()
