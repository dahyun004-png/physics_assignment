# make_hiseo_image.py
# 실행:  python make_hiseo_image.py
from PIL import Image, ImageDraw, ImageFont
import math, os

W, H = 1280, 720

# 👉 여기를 본인 환경에 맞게 수정
FONT_CANDIDATES = [
    r"C:/Windows/Fonts/malgun.ttf",                       # Windows (맑은 고딕)
    r"C:/Windows/Fonts/malgunbd.ttf",
    "/System/Library/Fonts/AppleSDGothicNeo.ttc",         # macOS
    "/Library/Fonts/AppleGothic.ttf",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",   # Linux (Noto CJK)
    "/usr/share/fonts/truetype/noto/NotoSansCJKkr-Regular.otf",
    "/usr/share/fonts/truetype/unfonts-core/UnDotum.ttf",
]

def find_font(size=120):
    for p in FONT_CANDIDATES:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size=size)
            except Exception:
                pass
    raise RuntimeError("한글 폰트를 찾지 못했어요. FONT_CANDIDATES를 본인 PC 폰트 경로로 바꿔주세요!")

def draw_vertical_gradient(draw, w, h, top_rgb, bot_rgb):
    for y in range(h):
        t = y / (h - 1)
        r = int(top_rgb[0]*(1-t) + bot_rgb[0]*t)
        g = int(top_rgb[1]*(1-t) + bot_rgb[1]*t)
        b = int(top_rgb[2]*(1-t) + bot_rgb[2]*t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

def heart_points(cx, cy, scale=12, samples=400):
    # 유명한 하트 곡선 (파라메트릭)
    pts = []
    for i in range(samples+1):
        t = math.pi*2*i/samples
        x = 16*math.sin(t)**3
        y = 13*math.cos(t) - 5*math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t)
        pts.append((cx + scale*x, cy - scale*y))
    return pts

def make_image(text="희서야 화이팅 하트", out_path="hiseo_fighting_heart.png"):
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)

    # 1) 배경 그라디언트
    draw_vertical_gradient(draw, W, H, (255, 230, 240), (230, 240, 255))

    # 2) 큰 하트 + 안쪽 하트(테두리 효과)
    outer = heart_points(W//2, H//2 + 40, scale=14)
    inner = heart_points(W//2, H//2 + 40, scale=12)
    draw.polygon(outer, fill=(255,110,130), outline=(255, 80, 110))
    draw.polygon(inner, fill=(255,255,255))

    # 3) 제목 텍스트
    title_font = find_font(size=120)
    tw, th = draw.textbbox((0,0), text, font=title_font)[2:]
    tx = (W - tw)//2
    ty = H//2 - th//2 - 20
    # 그림자
    draw.text((tx+3, ty+3), text, font=title_font, fill=(0,0,0,128))
    # 본문
    draw.text((tx, ty), text, font=title_font, fill=(255, 80, 110))

    # 4) 캡션
    cap_font = find_font(size=40)
    caption = "오늘도 파이썬으로 전해요 💖"
    cw, ch = draw.textbbox((0,0), caption, font=cap_font)[2:]
    draw.text(((W-cw)//2, H - ch - 40), caption, font=cap_font, fill=(120,120,140))

    img.save(out_path, "PNG")
    print("Saved:", out_path)

if __name__ == "__main__":
    make_image()
