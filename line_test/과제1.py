'''
문제 설명
10장의 img가 list 형태로 들어옴.
각 img를 normalize하라.
단, numpy 등 외장 library는 사용하지 말 것.
'''

def normalize(imgs): 
    new_imgs = []
    means = [0, 0, 0]
    stds = [0, 0, 0]
    for img in imgs:
        new_img = []
        for line in img:
            new_line = []
            for pixel in line:
                new_pixel = []
                for channel_value, channel_mean, channel_std in zip(pixel, means, stds):
                    new_value = (channel_value - channel_mean) / (channel_std * 255)
                    new_pixel.append(new_value)
                new_line.append(new_pixel)
            new_img.append(new_line)
        new_imgs.append(new_img)
    return new_imgs

imgs_array = []
normalized_imgs = normalize(imgs_array)