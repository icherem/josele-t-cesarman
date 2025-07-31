
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
    ("paisajes", 21),
    ("rincones", 9),
    ("collage", 12),
    ("tarot", 7),
    ("ny", 10),
    ("montañas", 11),
]

modal_id = 1

for group, count in groups:
    for img_num in range(1, count + 1):
        filename = f"2025-07-29-{modal_id}.md"
        filepath = os.path.join(output_dir, filename)
        content = template.format(modal_id=modal_id, img=img_num, alt=group)

        with open(filepath, "w") as f:
            f.write(content)

        print(f"Created {filename} | modal-id: {modal_id}, img: {img_num}.jpg, alt: {group}")
        modal_id += 1

