
def wrap_text(
    text: str,
    font_size: int,
    cont_width: int,
    cont_x: int
    )-> int:
    return ((cont_width - (font_size * len(text)/2.5)) / 2) + cont_x
    