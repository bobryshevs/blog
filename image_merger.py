from PIL import (
    Image,
    ImageFont,
    ImageDraw
)


class ImageMerger:
    def __init__(self) -> None:
        self.ava_coord = (0, 512)
        self.text_coord = (0, 1050)
        self.font = ImageFont.truetype("data/fonts/Ubuntu-Bold.ttf", 32)
        self.fill = "#ffffff"

    def merge(self, wall_path: str, ava_path: str, nickname: str) -> Image:
        wall = Image.open(wall_path)
        ava = Image.open(ava_path)

        wall.paste(ava, self.ava_coord)
        draw = ImageDraw.Draw(wall)
        draw.text(self.text_coord, nickname, font=self.font, fill=self.fill)
        return wall
