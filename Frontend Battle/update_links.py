html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

departments = [
    {"slug": "cse", "title": "Computer Science & Engineering"},
    {"slug": "it", "title": "Information Technology"},
    {"slug": "ee", "title": "Electronics Engineering"},
    {"slug": "elec", "title": "Electrical Engineering"},
    {"slug": "me", "title": "Mechanical Engineering"},
    {"slug": "ce", "title": "Civil Engineering"},
    {"slug": "ai", "title": "Centre for Artificial Intelligence"},
    {"slug": "iot", "title": "Centre for Internet of Things"},
    {"slug": "emc", "title": "Engineering Mathematics & Computing"},
    {"slug": "cst", "title": "Centre for CS & Technology"},
    {"slug": "arch", "title": "Architecture & Planning"},
    {"slug": "applied-science", "title": "Applied Science"},
    {"slug": "chem", "title": "Chemical Engineering"},
    {"slug": "ete", "title": "Electronics & Telecom Engg"},
    {"slug": "hm", "title": "Humanities & Management"}
]

for i in range(len(lines)):
    for dept in departments:
        # If we see the department title on this line
        if f"<h3>{dept['title']}</h3>" in lines[i]:
            # The very next line should be the link
            if '<a href="#"' in lines[i+1]:
                lines[i+1] = lines[i+1].replace('<a href="#"', f'<a href="pages/{dept["slug"]}.html"')

with open(html_file, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Updated links successfully.")
