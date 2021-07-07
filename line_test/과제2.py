'''
문제 설명
10장의 img가 list 형태로 들어옴.
각 img를 augmentation하라.
aug1 = translate x -30
aug2 = translate y 30
aug3 = rotate 137
aug4 = scale up 1.7
augmentation관련 library 사용하지 말 것.
'''

def translate_x(imgs):
    new_imgs = []
    for img in imgs:
        new_img = []
        for line in img:
            new_line = []
            for idx, pixel in enumerate(line):
                if idx < 30:
                    new_pixel = [0, 0, 0]
                else:
                    new_pixel = pixel
                new_line.append(new_pixel)
            new_img.append(new_line)
        new_imgs.append(new_img)
    return new_imgs

def translate_y(imgs):
    new_imgs = []
    for img in imgs:
        new_img = []
        for idx, line in enumerate(img):
            new_line = []
            for pixel in line:
                if idx < 30:
                    new_pixel = [0, 0, 0]
                else:
                    new_pixel = pixel
                new_line.append(new_pixel)
            new_img.append(new_line)
        new_imgs.append(new_img)
    return new_imgs

def rotate(imgs):
    pass

def scale_up(imgs):
    pass

def augmentation(imgs):
    imgs = translate_x(imgs)
    imgs = translate_y(imgs)
    imgs = rotate(imgs)
    imgs = scale_up(imgs)
    return imgs

imgs_array = []
augmented_imgs = augmentation(imgs_array)