from PIL import Image
im = Image.open(r'C:\Users\kt101\OneDrive\デスクトップ\mejinaai\オナガメジナ\1.jpg')

# 上下左右に似にの幅の余白を追加する

def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

im_new = add_margin(im, 50, 10, 0, 100, (128, 0, 64))
im_new.save(r'C:\Users\kt101\OneDrive\デスクトップ\mejinaai\オナガメジナ_add_margin\1_add_margin.jpg', quality=95)

# 長方形に余白を追加し正方形にする

def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

im_new = expand2square(im, (0, 0, 0)).resize((100, 100))
im_new.save(r'C:\Users\kt101\OneDrive\デスクトップ\mejinaai\オナガメジナ_square\1_square.jpg', quality=95)
