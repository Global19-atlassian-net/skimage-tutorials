# Check skimage along with major dependencies: numpy, scipy, PyQt
import skimage
test_failed = bool(skimage.test_verbose())
doctest_failed = bool(skimage.doctest_verbose())
if test_failed or doctest_failed:
    print("There were errors running scikit-image tests. "
          "See test output for more details.")
skimver = int(skimage.__version__.split('.')[1].rstrip('dev'))
if skimver < 10:
    print("ERROR: skimage version 0.10 or higher required. You have 0.%i." %
          skimver)

# check matplotlib
import matplotlib as mpl
mplver_str = mpl.__version__
mplver = mplver_str.split('.')
major, minor = map(int, mplver[:2])
if major < 1 or (major >= 1 and minor < 2):
    print("ERROR: matplotlib version 1.2 or higher required. You have %s." %
          mplver_str)
