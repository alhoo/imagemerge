from scipy import misc
from scipy.fftpack import fftn, ifftn
from scipy.ndimage.interpolation import shift
from numpy import unravel_index
import numpy as np

def rgb2gray(rgb: "rgb image to convert") -> "gray scale image":
  """Convert rgb to gray scale image

  Arguments:
  rgb -- the rgb image
  """
  r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
  gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
  return gray

def phase(im: "base image",
          im2: "image to compare",
          window: "window function") -> "the phase difference between the given images":
  """Calculate the phase differnce between two images

  Arguments:
  im -- base image to compare with
  im2 -- image to compare to
  window -- a window function
  """
  cps = np.fft.fft2(rgb2gray(im)*window)*np.conj(np.fft.fft2(rgb2gray(im2)*window))
  cps /= np.linalg.norm(cps)
  r = np.fft.ifft2(cps)
  r = unravel_index(r.argmax(), r.shape)
  r = np.array((0-r[0], im.shape[1] - r[1]))%im.shape[:2]
  return r

def combine(images: "images to combine") -> "combined image":
  """Combine a list of images to a single image

  Arguments:
  images -- a list of images
  """
  ima = misc.imread(images[0])
  imavg = ima.astype(np.uint64)*0
  window = np.sqrt(np.outer(np.hamming(ima.shape[0]), np.hamming(ima.shape[1])))
  n = 1

  for imname in images:
    imb = misc.imread(imname)
    r = phase(ima, imb, window)
    if np.linalg.norm(r) > 20:
      continue
    imavg = imavg + shift(imb, np.negative(np.append(r, 0)), cval=0)
    n = n + 1

  return (imavg/n).astype(np.uint8)

if __name__ == '__main__':
  import sys
  from glob import glob
  directory = "."
  if len(sys.argv) > 1:
    directory = sys.argv[1]
  images = sorted(glob(directory+"/*.jpg"))
  im = combine(images)
  if len(sys.argv) > 2:
    misc.imsave(sys.argv[2], im)
  else:
    misc.imshow(im)
