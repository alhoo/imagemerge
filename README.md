# imagemerge
Program for merging multiple images to one

# theory
This program is based on the [phase correlation](https://en.wikipedia.org/wiki/Phase_correlation) in the frequency domain.
Steps in the algorithm:
* Apply a window function ([Hamming window](https://en.wikipedia.org/wiki/hamming_window)) to each image
* Calculate the discrete 2D Fourier transformations
* Calculate the cross-power spectrum by taking the complex conjugate of the second result, multiply the fourier transforms together using the [Hadamard product](https://en.wikipedia.org/wiki/Hadamard_product_(matrices))
* Calculate the inverse Fourier transform
* Obtain the most likely phase shift at the peak of the inverse Fourier transform

# dependencies
* scipy
* numpy

# usage
python3 imavg.py /path/to/images combined.jpg
