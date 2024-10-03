from skimage.filters import difference_of_gaussians
from skimage.io import imread, imsave
from skimage.util import img_as_uint
import fire
from pathlib import Path


def main(img_path: str, out_path: str, sigma=10):
    img = imread(img_path)
    img = difference_of_gaussians(img, 0, sigma)
    img = img_as_uint(img)
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    imsave(out_path, img)


if __name__ == '__main__':
    fire.Fire(main)