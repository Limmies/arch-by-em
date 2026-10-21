"""Curated crops from PDFKit renders in /private/tmp; run after rendering sources."""
from pathlib import Path
from PIL import Image
out = Path(__file__).resolve().parents[1] / 'dist/assets'
def crop(source, target, box):
    image = Image.open(source)
    width, height = image.size
    image = image.crop(tuple(round(value * size) for value, size in zip(box, (width, height, width, height))))
    image.save(out / target, quality=92, optimize=True)
for page in [43,44,45,46,47,48,49,50,51,52]:
    crop(f'/private/tmp/house-{page}.jpg', f'house-{page}.jpg', (0,.102,1,.898))
for page, box in {25:(.102,.184,.897,.817),18:(.105,.166,.895,.806),27:(.102,.183,.898,.817)}.items():
    crop(f'/private/tmp/theatre-{page}.jpg', f'theatre-{page}.jpg', box)
for page, box in {13:(.279,.225,.965,.775),15:(.04,.075,.96,.663),16:(.543,.107,.966,.89),18:(.275,.205,.97,.79),26:(.267,.227,.951,.772),28:(.267,.227,.956,.772),30:(.268,.205,.966,.79)}.items():
    crop(f'/private/tmp/portfolio-{page}.jpg', f'cover-{page}.jpg', box)
# Use the clearer source render for the civic project's cover.
Image.open(out/'theatre-25.jpg').save(out/'cover-8.jpg', quality=92)
Image.open(out/'house-43.jpg').save(out/'cover-7.jpg', quality=92)
