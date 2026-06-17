import os
import json

MUSIC_FOLDER = "music"
OUTPUT_FILE = "songs.json"

supported = (".mp3", ".wav", ".ogg", ".m4a", ".flac")

songs = []

if not os.path.exists(MUSIC_FOLDER):
    os.makedirs(MUSIC_FOLDER)
    print("Đã tạo thư mục music/")
else:
    for file in os.listdir(MUSIC_FOLDER):
        if file.lower().endswith(supported):
            name = os.path.splitext(file)[0]

            songs.append({
                "name": name,
                "file": f"music/{file}"
            })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(songs, f, ensure_ascii=False, indent=2)

print(f"Đã tạo {OUTPUT_FILE} với {len(songs)} bài nhạc.")