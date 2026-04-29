# SKILL.md — Instagram Operations

## Purpose

This skill defines how Friday operates the Instagram of Fluxia — from content creation to publishing to comment management.

---

## 1. Context

**Account:** `fluxia.oficial4`
**Instagram Business ID:** `17841438988720012`
**Repository:** `Alex9Sales/fluxia-Inteligencia` (public)
**Images folder:** `/images/` in repo

**Credentials stored at:**
- `/home/node/.openclaw/secrets/instagram.env` — Instagram token
- `/home/node/.openclaw/secrets/groq.env` — Groq (transcription)
- `/home/node/.openclaw/secrets/levelapse.env` — ElevenLabs (TTS voice)

---

## 2. Content Pillars

All content follows 4 pillars:

1. **Prova viva** — Show how Fluxia operates with AI
2. **Liberação** — AI frees the entrepreneur from manual work
3. **Resultado real** — Measurable business results
4. **Educação** — Why the old model is failing

**Target audience:** Small and medium entrepreneurs, freelancers, service providers who do everything alone.

**Positioning:** "AI that frees the entrepreneur, not replaces them. Lighter, smarter, more profitable operations."

---

## 3. Posting Schedule

**3 posts per week:**
- **Monday** — Thesis/positioning carousel
- **Wednesday** — Applied content, framework, educational
- **Friday** — Behind-the-scenes, proof of concept, vision

**Rule:** Quality beats volume. If the piece is weak, don't publish.

---

## 4. Post Creation Workflow

### Step 1. Generate images with DALL-E or GPT Image 2.0

Use `image_generate` tool with `model: openai/gpt-image-2`.

**Image specs:**
- Size: 1080x1080 (1:1)
- Style: dark tech-noir, premium corporate
- Colors: black background, white text, orange/gold accents
- Font: clean sans-serif, bold, compressed
- Visual elements: circuit patterns, lens flare, particle effects, glowing horizon line
- No emojis, no clutter

**Prompt structure for carousel:**

```
Instagram carousel, dark tech-noir aesthetic. Fundo preto profundo. 

Slide 1 (capa): "TEXT HERE" em branco grande centralizado. Linha laranja horizontal com lens flare. Partículas douradas.

Slide 2: Título "O PROBLEMA" em branco. Lista com destaque laranja: item1 / item2 / item3. Fundo escuro com grades tecnológicas sutis.

Slide 3: Texto final em branco: "TEXT" e embaixo "TEXT" em laranja. Partículas de luz. Premium tech-noir.

Style: sophisticated, clean, authoritative, modern premium corporate. NO generic agency look.
```

### Step 2. Upload images to GitHub

```bash
cd /tmp/fluxia
git add images/
git commit -m "Add [post name] slides"
git push origin main
```

**Image URLs after push:**
```
https://raw.githubusercontent.com/Alex9Sales/fluxia-Inteligencia/main/images/[filename]
```

### Step 3. Create caption

Caption structure:
- Hook (problem or provocation)
- Explanation (why it matters)
- Transformation (what changes)
- CTA (DM or link in bio)
- Hashtags (5-8 relevant)

### Step 4. Publish via Meta Graph API

**Python script for carousel:**

```python
import urllib.request
import urllib.parse
import json

TOKEN = "TOKEN_FROM_instagram.env"
BUSINESS_ID = "17841438988720012"
IMAGES = ["url1", "url2", "url3"]
CAPTION = "Caption text here"

media_url = f"https://graph.facebook.com/v25.0/{BUSINESS_ID}/media"

# Step 1: Upload each image
image_ids = []
for url in IMAGES:
    data = urllib.parse.urlencode({
        "media_type": "IMAGE",
        "image_url": url,
        "access_token": TOKEN
    }).encode()
    req = urllib.request.Request(media_url, data=data, method='POST')
    with urllib.request.urlopen(req) as resp:
        image_ids.append(json.loads(resp.read().decode())['id'])

# Step 2: Create carousel container
children = ",".join(image_ids)
data = urllib.parse.urlencode({
    "media_type": "CAROUSEL",
    "caption": CAPTION,
    "children": children,
    "access_token": TOKEN
}).encode()
req = urllib.request.Request(media_url, data=data, method='POST')
with urllib.request.urlopen(req) as resp:
    container_id = json.loads(resp.read().decode())['id']

# Step 3: Publish
publish_url = f"https://graph.facebook.com/v25.0/{BUSINESS_ID}/media_publish"
data = urllib.parse.urlencode({
    "creation_id": container_id,
    "access_token": TOKEN
}).encode()
req = urllib.request.Request(publish_url, data=data, method='POST')
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read().decode())
    print(f"Published! ID: {result['id']}")
```

---

## 5. Comment Management

**Comment types and responses:**

| Type | Signal | Response style |
|------|--------|----------------|
| Social | Quick reaction | Light, human, elegant |
| Curiosity | How does it work? | Clear, short, useful |
| Commercial | Pain point, need | Intelligent, open DM |
| Recurring | Repeated interaction | Acknowledge context |

**Response rules:**
- Coherent with Fluxia voice
- Never generic agency tone
- Never force commercial
- Escalate to Friday if sensitive

---

## 6. Voice Response (TTS)

**Voice used:** Keren (young Brazilian female, voice_id: `33B4UnXyTNbgLmdEDh5P`)

**Setup:**
```bash
# ElevenLabs API key stored at:
/home/node/.openclaw/secrets/levelapse.env

# Generate voice response:
curl -s -X POST "https://api.elevenlabs.io/v1/text-to-speech/33B4UnXyTNbgLmdEDh5P" \
  -H "xi-api-key: KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Response text here",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {"stability": 0.4, "similarity_boost": 0.85}
  }' \
  --output /data/.openclaw/media/tool-tts/response.mp3
```

**Sending audio to Slack:**
```python
message(action="send", channel="slack", filePath="/data/.openclaw/media/tool-tts/response.mp3", target="user:U0B06JKG02Y")
```

---

## 7. Audio Transcription

**Groq Whisper for audio transcription:**

```bash
GROQ_KEY=$(cat /home/node/.openclaw/secrets/groq.env | cut -d= -f2)
curl -s -X POST "https://api.groq.com/openai/v1/audio/transcriptions" \
  -H "Authorization: Bearer ${GROQ_KEY}" \
  -F "file=@/path/to/audio.m4a" \
  -F "model=whisper-large-v3" \
  -F "language=pt"
```

---

## 8. Token Management

**Instagram tokens expire — they need renewal:**
- User tokens: ~60 days
- Token debug: `GET /debug_token?input_token=TOKEN&access_token=TOKEN`

**When token expires:**
1. Alex generates new token via Meta Developer Explorer
2. Update `/home/node/.openclaw/secrets/instagram.env`
3. Test with: `GET /me?fields=id,username&access_token=TOKEN`

---

## 9. Repository Structure for Instagram

```
fluxia-Inteligencia/
├── images/
│   ├── post1-slide1.png
│   ├── post1-slide2.png
│   ├── post1-slide3.png
│   └── ...
├── cerebro/
│   ├── areas/
│   │   └── instagram-*.md (operational docs)
│   └── skills/
│       └── instagram-operations.md (this skill)
```

---

## 10. Quick Command Reference

**Test Instagram token:**
```bash
curl -s "https://graph.facebook.com/v25.0/17841438988720012?fields=username&access_token=$(cat /home/node/.openclaw/secrets/instagram.env | cut -d= -f2)"
```

**Transcribe audio:**
```bash
GROQ_KEY=$(cat /home/node/.openclaw/secrets/groq.env | cut -d= -f2)
curl -s -X POST "https://api.groq.com/openai/v1/audio/transcriptions" \
  -H "Authorization: Bearer ${GROQ_KEY}" \
  -F "file=@audio.m4a" -F "model=whisper-large-v3" -F "language=pt"
```

**Generate voice response:**
```bash
curl -s -X POST "https://api.elevenlabs.io/v1/text-to-speech/33B4UnXyTNbgLmdEDh5P" \
  -H "xi-api-key: $(cat /home/node/.openclaw/secrets/levelapse.env | cut -d= -f2)" \
  -H "Content-Type: application/json" \
  -d '{"text": "Text", "model_id": "eleven_multilingual_v2", "voice_settings": {"stability": 0.4, "similarity_boost": 0.85}}' \
  --output response.mp3
```

---

## 11. Skill Triggers

This skill activates when:
- Alex asks to create, publish, or manage Instagram content
- Audio message received about Instagram operations
- Request to generate post images or captions
- Comment needs response
- Posting schedule needs to be executed

---

Created: 2026-04-29
Updated from: real Instagram API operations, Meta Graph API integration, content creation, voice TTS pipeline