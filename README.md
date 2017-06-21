# imagemerge
Program for merging multiple images to one

# theory
This program is based on the phase correlation in the frequency domain.
Steps in the algorithm:
* Apply a window function (Hamming window) to each image
* Calculate the discrete 2D Fourier transformations
* Calculate the cross-power spectrum by taking the complex conjugate of the second result, multiply the fourier transforms to gether using the Hadamard product
* Calculate the inverse Fourier transform
* Obtain the most likely phase shift at the peak of the inverse Fourier transform

# dependencies
* scipy
* numpy

# usage
python3 imavg.py /path/to/images combined.jpg
