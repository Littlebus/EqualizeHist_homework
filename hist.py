import cv2
import numpy as np


def histest(fp):
    img = cv2.imdecode(np.fromfile(fp, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    # img = cv2.imread(fp, cv2.IMREAD_UNCHANGED)
    # 灰度图
    if len(img.shape) == 2:
        cv2.imwrite('temp_grey.jpg', hist(img))
        return ['temp_grey.jpg']

    elif len(img.shape) == 3 and img.shape[2] == 3:
        print(img.shape)
        print(cv2.split(img))
        hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
        cv2.imwrite('temp_rgb.jpg', rgbhist(img))
        h, l, s = cv2.split(hls)
        l = hist(l)
        cv2.imwrite('temp_hsi.jpg', cv2.cvtColor(cv2.merge((h, l, s)), cv2.COLOR_HLS2BGR))
        return ('temp_rgb.jpg', 'temp_hsi.jpg')


def rgbhist(img):
    B, G, R = map(lambda x: hist(x), cv2.split(img))
    return cv2.merge((B, G, R))


def hist(array, nk=256):
    density = np.histogram(array, bins=range(nk + 1), density=True)[0]
    for i in range(1, len(density)):
        density[i] += density[i - 1]
    hash_table = {i: int(val * (nk - 1)) for i, val in enumerate(density)}
    return np.vectorize(hash_table.get)(array).astype(np.uint8)
