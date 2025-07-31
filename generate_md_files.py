import os

output_dir = "_posts"
os.makedirs(output_dir, exist_ok=True)

template = """---
layout: default
modal-id: {modal_id}
date: 2025-07-25
img: {img}.jpg
alt: "{alt}"
project-date: July 2025
category: Oil Painting
description: "Oleo"
---
"""

groups = [
    ("Paisajes", 10),
    ("Rincones", 15),
    ("Collage", 12),
    ("Cartas del tarot", 7),
    ("Nueva York", 10),
    ("Acantilados", 10),
]

modal_id = 1

for group, count in groups:
    for img_num in range(1, count + 1):
        filename = f"2025-07-29-{modal_id}.md"
        filepath = os.path.join(output_dir, filename)
        img_path = f"{group}/{img_num}"
        content = template.format(modal_id=modal_id, img=img_path, alt=group)

        with open(filepath, "w") as f:
            f.write(content)

        print(f"Created {filename} | modal-id: {modal_id}, img: {img_path}.jpg, alt: {group}")
        modal_id += 1

