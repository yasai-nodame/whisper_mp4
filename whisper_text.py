import whisper 

import deepl 
import env

model = whisper.load_model('large')
result = model.transcribe('8K9co4OYRlP5APKk.mp4')
print(f"英文: {result['text']}")

deepl.deepl_text(env.os.environ.get('DEEPL_API'), result['text'])