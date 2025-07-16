# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Programming in Python
# ## Exam: July 15, 2025
#
#
# You can solve the exercises below by using standard Python 3.12 libraries, NumPy, Matplotlib, Pandas, PyMC.
# You can browse the documentation: [Python](https://docs.python.org/3.12/), [NumPy](https://numpy.org/doc/1.26/index.html), [Matplotlib](https://matplotlib.org/3.10.0/users/index.html), [Pandas](https://pandas.pydata.org/pandas-docs/version/2.2/index.html), [PyMC](https://www.pymc.io/projects/docs/en/stable/api.html).
# You can also look at the [slides](https://homes.di.unimi.it/monga/lucidi2425/pyqb00.pdf) or your code on [GitHub](https://github.com).
#
#
# **The exam is "open book", but it is strictly forbidden to communicate with others or "ask questions" online (i.e., stackoverflow is ok if the answer is already there, but you cannot ask a new question or use ChatGPT and similar products). Suspicious canned answers or plagiarism among student solutions will cause the invalidation of the exam for all the people involved.**
#
# To test examples in docstrings use
#
# ```python
# import doctest
# doctest.testmod()
# ```

# **SOLVE EACH EXERCISE IN ONE OR MORE NOTEBOOK CELLS AFTER THE QUESTION.**

import numpy as np
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pymc as pm   # type: ignore
import arviz as az  # type: ignore

# ### Exercise 1 (max 3 points)
#
# The file [brown_bear_blood.csv](./brown_bear_blood.csv) (Shimozuru, Michito, Nakamura, Shiori, Yamazaki, Jumpei, Matsumoto, Naoya, Inoue-Murayama, Miho, Qi, Huiyuan, Yamanaka, Masami, Nakanishi, Masanao, Yanagawa, Yojiro, Sashika, Mariko, Tsubota, Toshio, & Ito, Hideyuki. *Age estimation based on blood DNA methylation levels in brown bears* https://doi.org/10.5061/dryad.9w0vt4bm0) contains
#
#  - Bear ID
#  - Birth date. It was assumed that all bears were born on February 1.
#  - Date of the blood sampling.
#  - Ages were determined at the time of blood sampling
#  - Sex, F: female, M: male.
#  - Growth environment (i.e., captive or wild).
#  - Values of the methylation levels of the samples. As PCR for each sample was conducted in duplicate, the average  value was taken as the methylation level for each sample. 
#
# Load the data in a Pandas dataframe. Be sure the columns with dates have the correct dtype (`datetime64[ns]`) and the dates are parsed correctly (the birth date is always on February 1).

pass

# ### Exercise 2 (max 2 points)
#
# Add a column `age_days` with the exact number of days between `birth` and `sampling_date`. The column should have dtype `int64`.
#

pass

# ### Exercise 3 (max 5 points)
#
# Define a function `date_from_sample_id` that takes a string beginning with six digits and returns three numbers: the year after 2000 correspondig to the first two digits, the month corresponding to the next two digits, and the day corresponding to the last two digits. For example, if the string is "201101 Daichi" the result should be three numbers 2020, 11, 01. 
#
# To get the full marks, you should declare correctly the type hints and add a test within a doctest string.

pass

# +
# You can test your docstrings by uncommenting the following two lines

# import doctest
# doctest.testmod()
# -

# ### Exercise 4 (max 3 points)
#
# Use the function defined in Exercise 3 to check the value in the `sampling_date` function.

pass

# ### Exercise 5 (max 6 points)
#
# Write a function `twentynines` that takes two dates as strings "yyyy-mm-dd" (the first date is always before the second) and computes how many February 29 days (leap days) are within the interval between the two dates. Remember that a year has a February 29 if its number is divisible by 4, with the exception of secular years, that are leap only when divisible by 400. For example, within the dates "2002-02-01" and "2005-12-31" there is only one leap day.  

pass

# ### Exercise 6 (max 5 points)
#
# Plot two histograms, one for males and one for females, with the number of bears sampled in each month of year.

pass

# ### Exercise 7 (max 5 points)
#
# Make a figure with 4 columns and 4 rows with the scatter plots of all the pairs of the four methylation levels `SLC12A5`,`POU4F2`,`VGF`,`SCGN` (i.e., `VGF` vs. `SCGN`, ecc.). Color the points of the scatterplot according to the `environment`.

pass

# ### Exercise 8 (max 4 points)
#
# Consider this statistical model:
#
# - a parameter $\alpha$ is normally distributed with $\mu = 0$ and $\sigma = 2$ 
# - a parameter $\beta$ is normally distributed with $\mu = 1$ and $\sigma = 2$ 
# - a parameter $\gamma$ is exponentially distributed with $\lambda = 1$
# - the observed `VGF` is normally distributed with standard deviation $\gamma$ and a mean given by $\alpha + \beta \cdot M$ (where $M$ is the correspondig value of `age_days`).
#
# Code this model with pymc, sample the model, and plot the summary of the resulting estimation by using `az.plot_posterior`. 
#
#
#

pass
