import os

output_dir = "_posts"
os.makedirs(output_dir, exist_ok=True)

template = """---
layout: default
modal-id: {modal_id}
date: 2025-07-25
img: {img}
alt: "Luna"
project-date: July 2025
category: Oil Painting
description: "Oleo"
---
"""

groups = [
    ("collage", 10),
    ("tarot", 7),
    ("naturaleza", 13),
    ("montañas", 11),
]

start_index = 32
current_index = start_index

for group, count in groups:
    for i in range(1, count + 1):
        filename = f"2025-07-29-{current_index}.md"
        filepath = os.path.join(output_dir, filename)
        img_path = f"{group}/{i}.jpeg"
        content = template.format(modal_id=current_index, img=img_path)

        with open(filepath, "w") as f:
            f.write(content)

        print(f"Created file: {filename} with img: {img_path}")
        current_index += 1

