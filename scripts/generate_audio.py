"""Generate real Google Translate US English MP3 files before deployment."""
import json
from pathlib import Path
from gtts import gTTS

root = Path(__file__).resolve().parents[1]
out = root / 'audio'
out.mkdir(exist_ok=True)
items = json.loads((root / 'scripts/voice-texts.json').read_text())
for item in items:
    for kind in ('verb', 'phrase', 'sentence'):
        path = out / f"{item['id']}-{kind}.mp3"
        if not path.exists():
            gTTS(text=item[kind], lang='en', tld='us', slow=False, timeout=30).save(str(path))
        if path.stat().st_size < 500:
            raise RuntimeError(f'Invalid audio: {path.name}')
print(f'Validated {len(items) * 3} MP3 files')
