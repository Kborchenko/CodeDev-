"""Generate the font-independent CD favicon. Requires Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
# Angular CD silhouettes retain their open counters even at 16 px.
C = [(29,16),(19,16),(10,25),(10,39),(19,48),(29,48),(29,40),(23,40),(18,35),(18,29),(23,24),(29,24)]
D = [(35,16),(45,16),(54,25),(54,39),(45,48),(35,48)]
COUNTER = [(43,25),(46,28),(46,36),(43,39)]
BG, LIME, WHITE = '#090A09', '#D9FF28', '#F3F0E7'
def path(points):
    return 'M' + ' L'.join(f'{x} {y}' for x,y in points) + 'Z'
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
<rect width="64" height="64" rx="13" fill="{BG}"/>
<path d="{path(C)}" fill="{LIME}"/>
<path d="{path(D)} {path(COUNTER)}" fill="{WHITE}" fill-rule="evenodd"/>
</svg>\n'''
image = Image.new('RGBA', (1024,1024))
draw = ImageDraw.Draw(image)
draw.rounded_rectangle((0,0,1023,1023), radius=208, fill=BG)
for points,color in [(C,LIME),(D,WHITE),(COUNTER,BG)]:
    draw.polygon([(x*16,y*16) for x,y in points],fill=color)
public = ROOT/'public'
public.mkdir(exist_ok=True)
(public/'favicon.svg').write_text(svg,encoding='utf-8')
for size,name in [(96,'favicon-96.png'),(180,'apple-touch-icon.png')]:
    image.resize((size,size),Image.Resampling.LANCZOS).save(public/name)
image.resize((256,256),Image.Resampling.LANCZOS).save(public/'favicon.ico',sizes=[(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)])
# Keep the old URL working for clients that cached the previous HTML.
for base in [ROOT/'assets',public/'assets']:
    base.mkdir(exist_ok=True)
    image.resize((64,64),Image.Resampling.LANCZOS).save(base/'codedev-favicon.png')
# Root files also support direct static serving, alongside the Astro build.
for name in ['favicon.svg','favicon.ico','favicon-96.png','apple-touch-icon.png']:
    (ROOT/name).write_bytes((public/name).read_bytes())

# Distinct URLs invalidate browsers' separately cached favicon selection.
for size in [32,48]:
    image.resize((size,size),Image.Resampling.LANCZOS).save(public/f'codedev-cd-v2-{size}.png')
for source,dest in [('favicon.ico','codedev-cd-v2.ico'),('favicon.svg','codedev-cd-v2.svg')]:
    (public/dest).write_bytes((public/source).read_bytes())
for name in ['codedev-cd-v2-32.png','codedev-cd-v2-48.png','codedev-cd-v2.ico','codedev-cd-v2.svg']:
    (ROOT/name).write_bytes((public/name).read_bytes())
