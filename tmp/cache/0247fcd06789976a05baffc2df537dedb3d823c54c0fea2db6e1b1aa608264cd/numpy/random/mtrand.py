# encoding: utf-8
# module numpy.random.mtrand
# from /.venv/lib/python3.8/site-packages/numpy/random/mtrand.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import operator as operator # /usr/local/lib/python3.8/operator.py
import warnings as warnings # /usr/local/lib/python3.8/warnings.py
import numpy as np # /.venv/lib/python3.8/site-packages/numpy/__init__.py
from numpy.random._mt19937 import _MT19937

import collections.abc as __collections_abc


# functions

def beta(a, b, size=None): # real signature unknown; restored from __doc__
    """
    beta(a, b, size=None)
    
            Draw samples from a Beta distribution.
    
            The Beta distribution is a special case of the Dirichlet distribution,
            and is related to the Gamma distribution.  It has the probability
            distribution function
    
            .. math:: f(x; a,b) = \frac{1}{B(\alpha, \beta)} x^{\alpha - 1}
                                                             (1 - x)^{\beta - 1},
    
            where the normalization, B, is the beta function,
    
            .. math:: B(\alpha, \beta) = \int_0^1 t^{\alpha - 1}
                                         (1 - t)^{\beta - 1} dt.
    
            It is often seen in Bayesian inference and order statistics.
    
            .. note::
                New code should use the `~numpy.random.Generator.beta`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
    
            Parameters
            ----------
            a : float or array_like of floats
                Alpha, positive (>0).
            b : float or array_like of floats
                Beta, positive (>0).
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``a`` and ``b`` are both scalars.
                Otherwise, ``np.broadcast(a, b).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized beta distribution.
    
            See Also
            --------
            random.Generator.beta: which should be used for new code.
    """
    pass

def binomial(n, p, size=None): # real signature unknown; restored from __doc__
    """
    binomial(n, p, size=None)
    
            Draw samples from a binomial distribution.
    
            Samples are drawn from a binomial distribution with specified
            parameters, n trials and p probability of success where
            n an integer >= 0 and p is in the interval [0,1]. (n may be
            input as a float, but it is truncated to an integer in use)
    
            .. note::
                New code should use the `~numpy.random.Generator.binomial`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            n : int or array_like of ints
                Parameter of the distribution, >= 0. Floats are also accepted,
                but they will be truncated to integers.
            p : float or array_like of floats
                Parameter of the distribution, >= 0 and <=1.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``n`` and ``p`` are both scalars.
                Otherwise, ``np.broadcast(n, p).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized binomial distribution, where
                each sample is equal to the number of successes over the n trials.
    
            See Also
            --------
            scipy.stats.binom : probability density function, distribution or
                cumulative density function, etc.
            random.Generator.binomial: which should be used for new code.
    
            Notes
            -----
            The probability density for the binomial distribution is
    
            .. math:: P(N) = \binom{n}{N}p^N(1-p)^{n-N},
    
            where :math:`n` is the number of trials, :math:`p` is the probability
            of success, and :math:`N` is the number of successes.
    
            When estimating the standard error of a proportion in a population by
            using a random sample, the normal distribution works well unless the
            product p*n <=5, where p = population proportion estimate, and n =
            number of samples, in which case the binomial distribution is used
            instead. For example, a sample of 15 people shows 4 who are left
            handed, and 11 who are right handed. Then p = 4/15 = 27%. 0.27*15 = 4,
            so the binomial distribution should be used in this case.
    
            References
            ----------
            .. [1] Dalgaard, Peter, "Introductory Statistics with R",
                   Springer-Verlag, 2002.
            .. [2] Glantz, Stanton A. "Primer of Biostatistics.", McGraw-Hill,
                   Fifth Edition, 2002.
            .. [3] Lentner, Marvin, "Elementary Applied Statistics", Bogden
                   and Quigley, 1972.
            .. [4] Weisstein, Eric W. "Binomial Distribution." From MathWorld--A
                   Wolfram Web Resource.
                   http://mathworld.wolfram.com/BinomialDistribution.html
            .. [5] Wikipedia, "Binomial distribution",
                   https://en.wikipedia.org/wiki/Binomial_distribution
    
            Examples
            --------
            Draw samples from the distribution:
    
            >>> n, p = 10, .5  # number of trials, probability of each trial
            >>> s = np.random.binomial(n, p, 1000)
            # result of flipping a coin 10 times, tested 1000 times.
    
            A real world example. A company drills 9 wild-cat oil exploration
            wells, each with an estimated probability of success of 0.1. All nine
            wells fail. What is the probability of that happening?
    
            Let's do 20,000 trials of the model, and count the number that
            generate zero positive results.
    
            >>> sum(np.random.binomial(9, 0.1, 20000) == 0)/20000.
            # answer = 0.38885, or 38%.
    """
    pass

def bytes(length): # real signature unknown; restored from __doc__
    """
    bytes(length)
    
            Return random bytes.
    
            .. note::
                New code should use the `~numpy.random.Generator.bytes`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            length : int
                Number of random bytes.
    
            Returns
            -------
            out : bytes
                String of length `length`.
    
            See Also
            --------
            random.Generator.bytes: which should be used for new code.
    
            Examples
            --------
            >>> np.random.bytes(10)
            b' eh\x85\x022SZ\xbf\xa4' #random
    """
    pass

def chisquare(df, size=None): # real signature unknown; restored from __doc__
    """
    chisquare(df, size=None)
    
            Draw samples from a chi-square distribution.
    
            When `df` independent random variables, each with standard normal
            distributions (mean 0, variance 1), are squared and summed, the
            resulting distribution is chi-square (see Notes).  This distribution
            is often used in hypothesis testing.
    
            .. note::
                New code should use the `~numpy.random.Generator.chisquare`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            df : float or array_like of floats
                 Number of degrees of freedom, must be > 0.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``df`` is a scalar.  Otherwise,
                ``np.array(df).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized chi-square distribution.
    
            Raises
            ------
            ValueError
                When `df` <= 0 or when an inappropriate `size` (e.g. ``size=-1``)
                is given.
    
            See Also
            --------
            random.Generator.chisquare: which should be used for new code.
    
            Notes
            -----
            The variable obtained by summing the squares of `df` independent,
            standard normally distributed random variables:
    
            .. math:: Q = \sum_{i=0}^{\mathtt{df}} X^2_i
    
            is chi-square distributed, denoted
    
            .. math:: Q \sim \chi^2_k.
    
            The probability density function of the chi-squared distribution is
    
            .. math:: p(x) = \frac{(1/2)^{k/2}}{\Gamma(k/2)}
                             x^{k/2 - 1} e^{-x/2},
    
            where :math:`\Gamma` is the gamma function,
    
            .. math:: \Gamma(x) = \int_0^{-\infty} t^{x - 1} e^{-t} dt.
    
            References
            ----------
            .. [1] NIST "Engineering Statistics Handbook"
                   https://www.itl.nist.gov/div898/handbook/eda/section3/eda3666.htm
    
            Examples
            --------
            >>> np.random.chisquare(2,4)
            array([ 1.89920014,  9.00867716,  3.13710533,  5.62318272]) # random
    """
    pass

def choice(a, size=None, replace=True, p=None): # real signature unknown; restored from __doc__
    """
    choice(a, size=None, replace=True, p=None)
    
            Generates a random sample from a given 1-D array
    
            .. versionadded:: 1.7.0
    
            .. note::
                New code should use the `~numpy.random.Generator.choice`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            a : 1-D array-like or int
                If an ndarray, a random sample is generated from its elements.
                If an int, the random sample is generated as if it were ``np.arange(a)``
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  Default is None, in which case a
                single value is returned.
            replace : boolean, optional
                Whether the sample is with or without replacement. Default is True,
                meaning that a value of ``a`` can be selected multiple times.
            p : 1-D array-like, optional
                The probabilities associated with each entry in a.
                If not given, the sample assumes a uniform distribution over all
                entries in ``a``.
    
            Returns
            -------
            samples : single item or ndarray
                The generated random samples
    
            Raises
            ------
            ValueError
                If a is an int and less than zero, if a or p are not 1-dimensional,
                if a is an array-like of size 0, if p is not a vector of
                probabilities, if a and p have different lengths, or if
                replace=False and the sample size is greater than the population
                size
    
            See Also
            --------
            randint, shuffle, permutation
            random.Generator.choice: which should be used in new code
    
            Notes
            -----
            Setting user-specified probabilities through ``p`` uses a more general but less
            efficient sampler than the default. The general sampler produces a different sample
            than the optimized sampler even if each element of ``p`` is 1 / len(a).
    
            Sampling random rows from a 2-D array is not possible with this function,
            but is possible with `Generator.choice` through its ``axis`` keyword.
    
            Examples
            --------
            Generate a uniform random sample from np.arange(5) of size 3:
    
            >>> np.random.choice(5, 3)
            array([0, 3, 4]) # random
            >>> #This is equivalent to np.random.randint(0,5,3)
    
            Generate a non-uniform random sample from np.arange(5) of size 3:
    
            >>> np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0])
            array([3, 3, 0]) # random
    
            Generate a uniform random sample from np.arange(5) of size 3 without
            replacement:
    
            >>> np.random.choice(5, 3, replace=False)
            array([3,1,0]) # random
            >>> #This is equivalent to np.random.permutation(np.arange(5))[:3]
    
            Generate a non-uniform random sample from np.arange(5) of size
            3 without replacement:
    
            >>> np.random.choice(5, 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0])
            array([2, 3, 0]) # random
    
            Any of the above can be repeated with an arbitrary array-like
            instead of just integers. For instance:
    
            >>> aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
            >>> np.random.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3])
            array(['pooh', 'pooh', 'pooh', 'Christopher', 'piglet'], # random
                  dtype='<U11')
    """
    pass

def dirichlet(alpha, size=None): # real signature unknown; restored from __doc__
    """
    dirichlet(alpha, size=None)
    
            Draw samples from the Dirichlet distribution.
    
            Draw `size` samples of dimension k from a Dirichlet distribution. A
            Dirichlet-distributed random variable can be seen as a multivariate
            generalization of a Beta distribution. The Dirichlet distribution
            is a conjugate prior of a multinomial distribution in Bayesian
            inference.
    
            .. note::
                New code should use the `~numpy.random.Generator.dirichlet`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            alpha : sequence of floats, length k
                Parameter of the distribution (length ``k`` for sample of
                length ``k``).
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n)``, then
                ``m * n * k`` samples are drawn.  Default is None, in which case a
                vector of length ``k`` is returned.
    
            Returns
            -------
            samples : ndarray,
                The drawn samples, of shape ``(size, k)``.
    
            Raises
            ------
            ValueError
                If any value in ``alpha`` is less than or equal to zero
    
            See Also
            --------
            random.Generator.dirichlet: which should be used for new code.
    
            Notes
            -----
            The Dirichlet distribution is a distribution over vectors
            :math:`x` that fulfil the conditions :math:`x_i>0` and
            :math:`\sum_{i=1}^k x_i = 1`.
    
            The probability density function :math:`p` of a
            Dirichlet-distributed random vector :math:`X` is
            proportional to
    
            .. math:: p(x) \propto \prod_{i=1}^{k}{x^{\alpha_i-1}_i},
    
            where :math:`\alpha` is a vector containing the positive
            concentration parameters.
    
            The method uses the following property for computation: let :math:`Y`
            be a random vector which has components that follow a standard gamma
            distribution, then :math:`X = \frac{1}{\sum_{i=1}^k{Y_i}} Y`
            is Dirichlet-distributed
    
            References
            ----------
            .. [1] David McKay, "Information Theory, Inference and Learning
                   Algorithms," chapter 23,
                   http://www.inference.org.uk/mackay/itila/
            .. [2] Wikipedia, "Dirichlet distribution",
                   https://en.wikipedia.org/wiki/Dirichlet_distribution
    
            Examples
            --------
            Taking an example cited in Wikipedia, this distribution can be used if
            one wanted to cut strings (each of initial length 1.0) into K pieces
            with different lengths, where each piece had, on average, a designated
            average length, but allowing some variation in the relative sizes of
            the pieces.
    
            >>> s = np.random.dirichlet((10, 5, 3), 20).transpose()
    
            >>> import matplotlib.pyplot as plt
            >>> plt.barh(range(20), s[0])
            >>> plt.barh(range(20), s[1], left=s[0], color='g')
            >>> plt.barh(range(20), s[2], left=s[0]+s[1], color='r')
            >>> plt.title("Lengths of Strings")
    """
    pass

def exponential(scale=1.0, size=None): # real signature unknown; restored from __doc__
    """
    exponential(scale=1.0, size=None)
    
            Draw samples from an exponential distribution.
    
            Its probability density function is
    
            .. math:: f(x; \frac{1}{\beta}) = \frac{1}{\beta} \exp(-\frac{x}{\beta}),
    
            for ``x > 0`` and 0 elsewhere. :math:`\beta` is the scale parameter,
            which is the inverse of the rate parameter :math:`\lambda = 1/\beta`.
            The rate parameter is an alternative, widely used parameterization
            of the exponential distribution [3]_.
    
            The exponential distribution is a continuous analogue of the
            geometric distribution.  It describes many common situations, such as
            the size of raindrops measured over many rainstorms [1]_, or the time
            between page requests to Wikipedia [2]_.
    
            .. note::
                New code should use the `~numpy.random.Generator.exponential`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            scale : float or array_like of floats
                The scale parameter, :math:`\beta = 1/\lambda`. Must be
                non-negative.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``scale`` is a scalar.  Otherwise,
                ``np.array(scale).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized exponential distribution.
    
            See Also
            --------
            random.Generator.exponential: which should be used for new code.
    
            References
            ----------
            .. [1] Peyton Z. Peebles Jr., "Probability, Random Variables and
                   Random Signal Principles", 4th ed, 2001, p. 57.
            .. [2] Wikipedia, "Poisson process",
                   https://en.wikipedia.org/wiki/Poisson_process
            .. [3] Wikipedia, "Exponential distribution",
                   https://en.wikipedia.org/wiki/Exponential_distribution
    """
    pass

def f(dfnum, dfden, size=None): # real signature unknown; restored from __doc__
    """
    f(dfnum, dfden, size=None)
    
            Draw samples from an F distribution.
    
            Samples are drawn from an F distribution with specified parameters,
            `dfnum` (degrees of freedom in numerator) and `dfden` (degrees of
            freedom in denominator), where both parameters must be greater than
            zero.
    
            The random variate of the F distribution (also known as the
            Fisher distribution) is a continuous probability distribution
            that arises in ANOVA tests, and is the ratio of two chi-square
            variates.
    
            .. note::
                New code should use the `~numpy.random.Generator.f`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            dfnum : float or array_like of floats
                Degrees of freedom in numerator, must be > 0.
            dfden : float or array_like of float
                Degrees of freedom in denominator, must be > 0.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``dfnum`` and ``dfden`` are both scalars.
                Otherwise, ``np.broadcast(dfnum, dfden).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized Fisher distribution.
    
            See Also
            --------
            scipy.stats.f : probability density function, distribution or
                cumulative density function, etc.
            random.Generator.f: which should be used for new code.
    
            Notes
            -----
            The F statistic is used to compare in-group variances to between-group
            variances. Calculating the distribution depends on the sampling, and
            so it is a function of the respective degrees of freedom in the
            problem.  The variable `dfnum` is the number of samples minus one, the
            between-groups degrees of freedom, while `dfden` is the within-groups
            degrees of freedom, the sum of the number of samples in each group
            minus the number of groups.
    
            References
            ----------
            .. [1] Glantz, Stanton A. "Primer of Biostatistics.", McGraw-Hill,
                   Fifth Edition, 2002.
            .. [2] Wikipedia, "F-distribution",
                   https://en.wikipedia.org/wiki/F-distribution
    
            Examples
            --------
            An example from Glantz[1], pp 47-40:
    
            Two groups, children of diabetics (25 people) and children from people
            without diabetes (25 controls). Fasting blood glucose was measured,
            case group had a mean value of 86.1, controls had a mean value of
            82.2. Standard deviations were 2.09 and 2.49 respectively. Are these
            data consistent with the null hypothesis that the parents diabetic
            status does not affect their children's blood glucose levels?
            Calculating the F statistic from the data gives a value of 36.01.
    
            Draw samples from the distribution:
    
            >>> dfnum = 1. # between group degrees of freedom
            >>> dfden = 48. # within groups degrees of freedom
            >>> s = np.random.f(dfnum, dfden, 1000)
    
            The lower bound for the top 1% of the samples is :
    
            >>> np.sort(s)[-10]
            7.61988120985 # random
    
            So there is about a 1% chance that the F statistic will exceed 7.62,
            the measured value is 36, so the null hypothesis is rejected at the 1%
            level.
    """
    pass

def gamma(shape, scale=1.0, size=None): # real signature unknown; restored from __doc__
    """
    gamma(shape, scale=1.0, size=None)
    
            Draw samples from a Gamma distribution.
    
            Samples are drawn from a Gamma distribution with specified parameters,
            `shape` (sometimes designated "k") and `scale` (sometimes designated
            "theta"), where both parameters are > 0.
    
            .. note::
                New code should use the `~numpy.random.Generator.gamma`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            shape : float or array_like of floats
                The shape of the gamma distribution. Must be non-negative.
            scale : float or array_like of floats, optional
                The scale of the gamma distribution. Must be non-negative.
                Default is equal to 1.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``shape`` and ``scale`` are both scalars.
                Otherwise, ``np.broadcast(shape, scale).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized gamma distribution.
    
            See Also
            --------
            scipy.stats.gamma : probability density function, distribution or
                cumulative density function, etc.
            random.Generator.gamma: which should be used for new code.
    
            Notes
            -----
            The probability density for the Gamma distribution is
    
            .. math:: p(x) = x^{k-1}\frac{e^{-x/\theta}}{\theta^k\Gamma(k)},
    
            where :math:`k` is the shape and :math:`\theta` the scale,
            and :math:`\Gamma` is the Gamma function.
    
            The Gamma distribution is often used to model the times to failure of
            electronic components, and arises naturally in processes for which the
            waiting times between Poisson distributed events are relevant.
    
            References
            ----------
            .. [1] Weisstein, Eric W. "Gamma Distribution." From MathWorld--A
                   Wolfram Web Resource.
                   http://mathworld.wolfram.com/GammaDistribution.html
            .. [2] Wikipedia, "Gamma distribution",
                   https://en.wikipedia.org/wiki/Gamma_distribution
    
            Examples
            --------
            Draw samples from the distribution:
    
            >>> shape, scale = 2., 2.  # mean=4, std=2*sqrt(2)
            >>> s = np.random.gamma(shape, scale, 1000)
    
            Display the histogram of the samples, along with
            the probability density function:
    
            >>> import matplotlib.pyplot as plt
            >>> import scipy.special as sps  # doctest: +SKIP
            >>> count, bins, ignored = plt.hist(s, 50, density=True)
            >>> y = bins**(shape-1)*(np.exp(-bins/scale) /  # doctest: +SKIP
            ...                      (sps.gamma(shape)*scale**shape))
            >>> plt.plot(bins, y, linewidth=2, color='r')  # doctest: +SKIP
            >>> plt.show()
    """
    pass

def geometric(p, size=None): # real signature unknown; restored from __doc__
    """
    geometric(p, size=None)
    
            Draw samples from the geometric distribution.
    
            Bernoulli trials are experiments with one of two outcomes:
            success or failure (an example of such an experiment is flipping
            a coin).  The geometric distribution models the number of trials
            that must be run in order to achieve success.  It is therefore
            supported on the positive integers, ``k = 1, 2, ...``.
    
            The probability mass function of the geometric distribution is
    
            .. math:: f(k) = (1 - p)^{k - 1} p
    
            where `p` is the probability of success of an individual trial.
    
            .. note::
                New code should use the `~numpy.random.Generator.geometric`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            p : float or array_like of floats
                The probability of success of an individual trial.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``p`` is a scalar.  Otherwise,
                ``np.array(p).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized geometric distribution.
    
            See Also
            --------
            random.Generator.geometric: which should be used for new code.
    
            Examples
            --------
            Draw ten thousand values from the geometric distribution,
            with the probability of an individual success equal to 0.35:
    
            >>> z = np.random.geometric(p=0.35, size=10000)
    
            How many trials succeeded after a single run?
    
            >>> (z == 1).sum() / 10000.
            0.34889999999999999 #random
    """
    pass

def get_bit_generator(*args, **kwargs): # real signature unknown
    """
    Returns the singleton RandomState's bit generator
    
        Returns
        -------
        BitGenerator
            The bit generator that underlies the singleton RandomState instance
    
        Notes
        -----
        The singleton RandomState provides the random variate generators in the
        ``numpy.random`` namespace. This function, and its counterpart set method,
        provides a path to hot-swap the default MT19937 bit generator with a
        user provided alternative. These function are intended to provide
        a continuous path where a single underlying bit generator can be
        used both with an instance of ``Generator`` and with the singleton
        instance of RandomState.
    
        See Also
        --------
        set_bit_generator
        numpy.random.Generator
    """
    pass

def get_state(legacy=True): # real signature unknown; restored from __doc__
    """
    get_state(legacy=True)
    
            Return a tuple representing the internal state of the generator.
    
            For more details, see `set_state`.
    
            Parameters
            ----------
            legacy : bool, optional
                Flag indicating to return a legacy tuple state when the BitGenerator
                is MT19937, instead of a dict. Raises ValueError if the underlying
                bit generator is not an instance of MT19937.
    
            Returns
            -------
            out : {tuple(str, ndarray of 624 uints, int, int, float), dict}
                If legacy is True, the returned tuple has the following items:
    
                1. the string 'MT19937'.
                2. a 1-D array of 624 unsigned integer keys.
                3. an integer ``pos``.
                4. an integer ``has_gauss``.
                5. a float ``cached_gaussian``.
    
                If `legacy` is False, or the BitGenerator is not MT19937, then
                state is returned as a dictionary.
    
            See Also
            --------
            set_state
    
            Notes
            -----
            `set_state` and `get_state` are not needed to work with any of the
            random distributions in NumPy. If the internal state is manually altered,
            the user should know exactly what he/she is doing.
    """
    pass

def gumbel(loc=0.0, scale=1.0, size=None): # real signature unknown; restored from __doc__
    """
    gumbel(loc=0.0, scale=1.0, size=None)
    
            Draw samples from a Gumbel distribution.
    
            Draw samples from a Gumbel distribution with specified location and
            scale.  For more information on the Gumbel distribution, see
            Notes and References below.
    
            .. note::
                New code should use the `~numpy.random.Generator.gumbel`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            loc : float or array_like of floats, optional
                The location of the mode of the distribution. Default is 0.
            scale : float or array_like of floats, optional
                The scale parameter of the distribution. Default is 1. Must be non-
                negative.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``loc`` and ``scale`` are both scalars.
                Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized Gumbel distribution.
    
            See Also
            --------
            scipy.stats.gumbel_l
            scipy.stats.gumbel_r
            scipy.stats.genextreme
            weibull
            random.Generator.gumbel: which should be used for new code.
    
            Notes
            -----
            The Gumbel (or Smallest Extreme Value (SEV) or the Smallest Extreme
            Value Type I) distribution is one of a class of Generalized Extreme
            Value (GEV) distributions used in modeling extreme value problems.
            The Gumbel is a special case of the Extreme Value Type I distribution
            for maximums from distributions with "exponential-like" tails.
    
            The probability density for the Gumbel distribution is
    
            .. math:: p(x) = \frac{e^{-(x - \mu)/ \beta}}{\beta} e^{ -e^{-(x - \mu)/
                      \beta}},
    
            where :math:`\mu` is the mode, a location parameter, and
            :math:`\beta` is the scale parameter.
    
            The Gumbel (named for German mathematician Emil Julius Gumbel) was used
            very early in the hydrology literature, for modeling the occurrence of
            flood events. It is also used for modeling maximum wind speed and
            rainfall rates.  It is a "fat-tailed" distribution - the probability of
            an event in the tail of the distribution is larger than if one used a
            Gaussian, hence the surprisingly frequent occurrence of 100-year
            floods. Floods were initially modeled as a Gaussian process, which
            underestimated the frequency of extreme events.
    
            It is one of a class of extreme value distributions, the Generalized
            Extreme Value (GEV) distributions, which also includes the Weibull and
            Frechet.
    
            The function has a mean of :math:`\mu + 0.57721\beta` and a variance
            of :math:`\frac{\pi^2}{6}\beta^2`.
    
            References
            ----------
            .. [1] Gumbel, E. J., "Statistics of Extremes,"
                   New York: Columbia University Press, 1958.
            .. [2] Reiss, R.-D. and Thomas, M., "Statistical Analysis of Extreme
                   Values from Insurance, Finance, Hydrology and Other Fields,"
                   Basel: Birkhauser Verlag, 2001.
    
            Examples
            --------
            Draw samples from the distribution:
    
            >>> mu, beta = 0, 0.1 # location and scale
            >>> s = np.random.gumbel(mu, beta, 1000)
    
            Display the histogram of the samples, along with
            the probability density function:
    
            >>> import matplotlib.pyplot as plt
            >>> count, bins, ignored = plt.hist(s, 30, density=True)
            >>> plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
            ...          * np.exp( -np.exp( -(bins - mu) /beta) ),
            ...          linewidth=2, color='r')
            >>> plt.show()
    
            Show how an extreme value distribution can arise from a Gaussian process
            and compare to a Gaussian:
    
            >>> means = []
            >>> maxima = []
            >>> for i in range(0,1000) :
            ...    a = np.random.normal(mu, beta, 1000)
            ...    means.append(a.mean())
            ...    maxima.append(a.max())
            >>> count, bins, ignored = plt.hist(maxima, 30, density=True)
            >>> beta = np.std(maxima) * np.sqrt(6) / np.pi
            >>> mu = np.mean(maxima) - 0.57721*beta
            >>> plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
            ...          * np.exp(-np.exp(-(bins - mu)/beta)),
            ...          linewidth=2, color='r')
            >>> plt.plot(bins, 1/(beta * np.sqrt(2 * np.pi))
            ...          * np.exp(-(bins - mu)**2 / (2 * beta**2)),
            ...          linewidth=2, color='g')
            >>> plt.show()
    """
    pass

def hypergeometric(ngood, nbad, nsample, size=None): # real signature unknown; restored from __doc__
    """
    hypergeometric(ngood, nbad, nsample, size=None)
    
            Draw samples from a Hypergeometric distribution.
    
            Samples are drawn from a hypergeometric distribution with specified
            parameters, `ngood` (ways to make a good selection), `nbad` (ways to make
            a bad selection), and `nsample` (number of items sampled, which is less
            than or equal to the sum ``ngood + nbad``).
    
            .. note::
                New code should use the
                `~numpy.random.Generator.hypergeometric`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            ngood : int or array_like of ints
                Number of ways to make a good selection.  Must be nonnegative.
            nbad : int or array_like of ints
                Number of ways to make a bad selection.  Must be nonnegative.
            nsample : int or array_like of ints
                Number of items sampled.  Must be at least 1 and at most
                ``ngood + nbad``.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if `ngood`, `nbad`, and `nsample`
                are all scalars.  Otherwise, ``np.broadcast(ngood, nbad, nsample).size``
                samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized hypergeometric distribution. Each
                sample is the number of good items within a randomly selected subset of
                size `nsample` taken from a set of `ngood` good items and `nbad` bad items.
    
            See Also
            --------
            scipy.stats.hypergeom : probability density function, distribution or
                cumulative density function, etc.
            random.Generator.hypergeometric: which should be used for new code.
    
            Notes
            -----
            The probability density for the Hypergeometric distribution is
    
            .. math:: P(x) = \frac{\binom{g}{x}\binom{b}{n-x}}{\binom{g+b}{n}},
    
            where :math:`0 \le x \le n` and :math:`n-b \le x \le g`
    
            for P(x) the probability of ``x`` good results in the drawn sample,
            g = `ngood`, b = `nbad`, and n = `nsample`.
    
            Consider an urn with black and white marbles in it, `ngood` of them
            are black and `nbad` are white. If you draw `nsample` balls without
            replacement, then the hypergeometric distribution describes the
            distribution of black balls in the drawn sample.
    
            Note that this distribution is very similar to the binomial
            distribution, except that in this case, samples are drawn without
            replacement, whereas in the Binomial case samples are drawn with
            replacement (or the sample space is infinite). As the sample space
            becomes large, this distribution approaches the binomial.
    
            References
            ----------
            .. [1] Lentner, Marvin, "Elementary Applied Statistics", Bogden
                   and Quigley, 1972.
            .. [2] Weisstein, Eric W. "Hypergeometric Distribution." From
                   MathWorld--A Wolfram Web Resource.
                   http://mathworld.wolfram.com/HypergeometricDistribution.html
            .. [3] Wikipedia, "Hypergeometric distribution",
                   https://en.wikipedia.org/wiki/Hypergeometric_distribution
    
            Examples
            --------
            Draw samples from the distribution:
    
            >>> ngood, nbad, nsamp = 100, 2, 10
            # number of good, number of bad, and number of samples
            >>> s = np.random.hypergeometric(ngood, nbad, nsamp, 1000)
            >>> from matplotlib.pyplot import hist
            >>> hist(s)
            #   note that it is very unlikely to grab both bad items
    
            Suppose you have an urn with 15 white and 15 black marbles.
            If you pull 15 marbles at random, how likely is it that
            12 or more of them are one color?
    
            >>> s = np.random.hypergeometric(15, 15, 15, 100000)
            >>> sum(s>=12)/100000. + sum(s<=3)/100000.
            #   answer = 0.003 ... pretty unlikely!
    """
    pass

def laplace(loc=0.0, scale=1.0, size=None): # real signature unknown; restored from __doc__
    """
    laplace(loc=0.0, scale=1.0, size=None)
    
            Draw samples from the Laplace or double exponential distribution with
            specified location (or mean) and scale (decay).
    
            The Laplace distribution is similar to the Gaussian/normal distribution,
            but is sharper at the peak and has fatter tails. It represents the
            difference between two independent, identically distributed exponential
            random variables.
    
            .. note::
                New code should use the `~numpy.random.Generator.laplace`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            loc : float or array_like of floats, optional
                The position, :math:`\mu`, of the distribution peak. Default is 0.
            scale : float or array_like of floats, optional
                :math:`\lambda`, the exponential decay. Default is 1. Must be non-
                negative.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``loc`` and ``scale`` are both scalars.
                Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized Laplace distribution.
    
            See Also
            --------
            random.Generator.laplace: which should be used for new code.
    
            Notes
            -----
            It has the probability density function
    
            .. math:: f(x; \mu, \lambda) = \frac{1}{2\lambda}
                                           \exp\left(-\frac{|x - \mu|}{\lambda}\right).
    
            The first law of Laplace, from 1774, states that the frequency
            of an error can be expressed as an exponential function of the
            absolute magnitude of the error, which leads to the Laplace
            distribution. For many problems in economics and health
            sciences, this distribution seems to model the data better
            than the standard Gaussian distribution.
    
            References
            ----------
            .. [1] Abramowitz, M. and Stegun, I. A. (Eds.). "Handbook of
                   Mathematical Functions with Formulas, Graphs, and Mathematical
                   Tables, 9th printing," New York: Dover, 1972.
            .. [2] Kotz, Samuel, et. al. "The Laplace Distribution and
                   Generalizations, " Birkhauser, 2001.
            .. [3] Weisstein, Eric W. "Laplace Distribution."
                   From MathWorld--A Wolfram Web Resource.
                   http://mathworld.wolfram.com/LaplaceDistribution.html
            .. [4] Wikipedia, "Laplace distribution",
                   https://en.wikipedia.org/wiki/Laplace_distribution
    
            Examples
            --------
            Draw samples from the distribution
    
            >>> loc, scale = 0., 1.
            >>> s = np.random.laplace(loc, scale, 1000)
    
            Display the histogram of the samples, along with
            the probability density function:
    
            >>> import matplotlib.pyplot as plt
            >>> count, bins, ignored = plt.hist(s, 30, density=True)
            >>> x = np.arange(-8., 8., .01)
            >>> pdf = np.exp(-abs(x-loc)/scale)/(2.*scale)
            >>> plt.plot(x, pdf)
    
            Plot Gaussian for comparison:
    
            >>> g = (1/(scale * np.sqrt(2 * np.pi)) *
            ...      np.exp(-(x - loc)**2 / (2 * scale**2)))
            >>> plt.plot(x,g)
    """
    pass

def logistic(loc=0.0, scale=1.0, size=None): # real signature unknown; restored from __doc__
    """
    logistic(loc=0.0, scale=1.0, size=None)
    
            Draw samples from a logistic distribution.
    
            Samples are drawn from a logistic distribution with specified
            parameters, loc (location or mean, also median), and scale (>0).
    
            .. note::
                New code should use the `~numpy.random.Generator.logistic`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            loc : float or array_like of floats, optional
                Parameter of the distribution. Default is 0.
            scale : float or array_like of floats, optional
                Parameter of the distribution. Must be non-negative.
                Default is 1.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``loc`` and ``scale`` are both scalars.
                Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized logistic distribution.
    
            See Also
            --------
            scipy.stats.logistic : probability density function, distribution or
                cumulative density function, etc.
            random.Generator.logistic: which should be used for new code.
    
            Notes
            -----
            The probability density for the Logistic distribution is
    
            .. math:: P(x) = P(x) = \frac{e^{-(x-\mu)/s}}{s(1+e^{-(x-\mu)/s})^2},
    
            where :math:`\mu` = location and :math:`s` = scale.
    
            The Logistic distribution is used in Extreme Value problems where it
            can act as a mixture of Gumbel distributions, in Epidemiology, and by
            the World Chess Federation (FIDE) where it is used in the Elo ranking
            system, assuming the performance of each player is a logistically
            distributed random variable.
    
            References
            ----------
            .. [1] Reiss, R.-D. and Thomas M. (2001), "Statistical Analysis of
                   Extreme Values, from Insurance, Finance, Hydrology and Other
                   Fields," Birkhauser Verlag, Basel, pp 132-133.
            .. [2] Weisstein, Eric W. "Logistic Distribution." From
                   MathWorld--A Wolfram Web Resource.
                   http://mathworld.wolfram.com/LogisticDistribution.html
            .. [3] Wikipedia, "Logistic-distribution",
                   https://en.wikipedia.org/wiki/Logistic_distribution
    
            Examples
            --------
            Draw samples from the distribution:
    
            >>> loc, scale = 10, 1
            >>> s = np.random.logistic(loc, scale, 10000)
            >>> import matplotlib.pyplot as plt
            >>> count, bins, ignored = plt.hist(s, bins=50)
    
            #   plot against distribution
    
            >>> def logist(x, loc, scale):
            ...     return np.exp((loc-x)/scale)/(scale*(1+np.exp((loc-x)/scale))**2)
            >>> lgst_val = logist(bins, loc, scale)
            >>> plt.plot(bins, lgst_val * count.max() / lgst_val.max())
            >>> plt.show()
    """
    pass

def lognormal(mean=0.0, sigma=1.0, size=None): # real signature unknown; restored from __doc__
    """
    lognormal(mean=0.0, sigma=1.0, size=None)
    
            Draw samples from a log-normal distribution.
    
            Draw samples from a log-normal distribution with specified mean,
            standard deviation, and array shape.  Note that the mean and standard
            deviation are not the values for the distribution itself, but of the
            underlying normal distribution it is derived from.
    
            .. note::
                New code should use the `~numpy.random.Generator.lognormal`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            mean : float or array_like of floats, optional
                Mean value of the underlying normal distribution. Default is 0.
            sigma : float or array_like of floats, optional
                Standard deviation of the underlying normal distribution. Must be
                non-negative. Default is 1.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``mean`` and ``sigma`` are both scalars.
                Otherwise, ``np.broadcast(mean, sigma).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized log-normal distribution.
    
            See Also
            --------
            scipy.stats.lognorm : probability density function, distribution,
                cumulative density function, etc.
            random.Generator.lognormal: which should be used for new code.
    
            Notes
            -----
            A variable `x` has a log-normal distribution if `log(x)` is normally
            distributed.  The probability density function for the log-normal
            distribution is:
    
            .. math:: p(x) = \frac{1}{\sigma x \sqrt{2\pi}}
                             e^{(-\frac{(ln(x)-\mu)^2}{2\sigma^2})}
    
            where :math:`\mu` is the mean and :math:`\sigma` is the standard
            deviation of the normally distributed logarithm of the variable.
            A log-normal distribution results if a random variable is the *product*
            of a large number of independent, identically-distributed variables in
            the same way that a normal distribution results if the variable is the
            *sum* of a large number of independent, identically-distributed
            variables.
    
            References
            ----------
            .. [1] Limpert, E., Stahel, W. A., and Abbt, M., "Log-normal
                   Distributions across the Sciences: Keys and Clues,"
                   BioScience, Vol. 51, No. 5, May, 2001.
                   https://stat.ethz.ch/~stahel/lognormal/bioscience.pdf
            .. [2] Reiss, R.D. and Thomas, M., "Statistical Analysis of Extreme
                   Values," Basel: Birkhauser Verlag, 2001, pp. 31-32.
    
            Examples
            --------
            Draw samples from the distribution:
    
            >>> mu, sigma = 3., 1. # mean and standard deviation
            >>> s = np.random.lognormal(mu, sigma, 1000)
    
            Display the histogram of the samples, along with
            the probability density function:
    
            >>> import matplotlib.pyplot as plt
            >>> count, bins, ignored = plt.hist(s, 100, density=True, align='mid')
    
            >>> x = np.linspace(min(bins), max(bins), 10000)
            >>> pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
            ...        / (x * sigma * np.sqrt(2 * np.pi)))
    
            >>> plt.plot(x, pdf, linewidth=2, color='r')
            >>> plt.axis('tight')
            >>> plt.show()
    
            Demonstrate that taking the products of random samples from a uniform
            distribution can be fit well by a log-normal probability density
            function.
    
            >>> # Generate a thousand samples: each is the product of 100 random
            >>> # values, drawn from a normal distribution.
            >>> b = []
            >>> for i in range(1000):
            ...    a = 10. + np.random.standard_normal(100)
            ...    b.append(np.product(a))
    
            >>> b = np.array(b) / np.min(b) # scale values to be positive
            >>> count, bins, ignored = plt.hist(b, 100, density=True, align='mid')
            >>> sigma = np.std(np.log(b))
            >>> mu = np.mean(np.log(b))
    
            >>> x = np.linspace(min(bins), max(bins), 10000)
            >>> pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
            ...        / (x * sigma * np.sqrt(2 * np.pi)))
    
            >>> plt.plot(x, pdf, color='r', linewidth=2)
            >>> plt.show()
    """
    pass

def logseries(p, size=None): # real signature unknown; restored from __doc__
    """
    logseries(p, size=None)
    
            Draw samples from a logarithmic series distribution.
    
            Samples are drawn from a log series distribution with specified
            shape parameter, 0 <= ``p`` < 1.
    
            .. note::
                New code should use the `~numpy.random.Generator.logseries`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            p : float or array_like of floats
                Shape parameter for the distribution.  Must be in the range [0, 1).
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``p`` is a scalar.  Otherwise,
                ``np.array(p).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized logarithmic series distribution.
    
            See Also
            --------
            scipy.stats.logser : probability density function, distribution or
                cumulative density function, etc.
            random.Generator.logseries: which should be used for new code.
    
            Notes
            -----
            The probability density for the Log Series distribution is
    
            .. math:: P(k) = \frac{-p^k}{k \ln(1-p)},
    
            where p = probability.
    
            The log series distribution is frequently used to represent species
            richness and occurrence, first proposed by Fisher, Corbet, and
            Williams in 1943 [2].  It may also be used to model the numbers of
            occupants seen in cars [3].
    
            References
            ----------
            .. [1] Buzas, Martin A.; Culver, Stephen J.,  Understanding regional
                   species diversity through the log series distribution of
                   occurrences: BIODIVERSITY RESEARCH Diversity & Distributions,
                   Volume 5, Number 5, September 1999 , pp. 187-195(9).
            .. [2] Fisher, R.A,, A.S. Corbet, and C.B. Williams. 1943. The
                   relation between the number of species and the number of
                   individuals in a random sample of an animal population.
                   Journal of Animal Ecology, 12:42-58.
            .. [3] D. J. Hand, F. Daly, D. Lunn, E. Ostrowski, A Handbook of Small
                   Data Sets, CRC Press, 1994.
            .. [4] Wikipedia, "Logarithmic distribution",
                   https://en.wikipedia.org/wiki/Logarithmic_distribution
    
            Examples
            --------
            Draw samples from the distribution:
    
            >>> a = .6
            >>> s = np.random.logseries(a, 10000)
            >>> import matplotlib.pyplot as plt
            >>> count, bins, ignored = plt.hist(s)
    
            #   plot against distribution
    
            >>> def logseries(k, p):
            ...     return -p**k/(k*np.log(1-p))
            >>> plt.plot(bins, logseries(bins, a)*count.max()/
            ...          logseries(bins, a).max(), 'r')
            >>> plt.show()
    """
    pass

def multinomial(n, pvals, size=None): # real signature unknown; restored from __doc__
    """
    multinomial(n, pvals, size=None)
    
            Draw samples from a multinomial distribution.
    
            The multinomial distribution is a multivariate generalization of the
            binomial distribution.  Take an experiment with one of ``p``
            possible outcomes.  An example of such an experiment is throwing a dice,
            where the outcome can be 1 through 6.  Each sample drawn from the
            distribution represents `n` such experiments.  Its values,
            ``X_i = [X_0, X_1, ..., X_p]``, represent the number of times the
            outcome was ``i``.
    
            .. note::
                New code should use the `~numpy.random.Generator.multinomial`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            n : int
                Number of experiments.
            pvals : sequence of floats, length p
                Probabilities of each of the ``p`` different outcomes.  These
                must sum to 1 (however, the last element is always assumed to
                account for the remaining probability, as long as
                ``sum(pvals[:-1]) <= 1)``.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  Default is None, in which case a
                single value is returned.
    
            Returns
            -------
            out : ndarray
                The drawn samples, of shape *size*, if that was provided.  If not,
                the shape is ``(N,)``.
    
                In other words, each entry ``out[i,j,...,:]`` is an N-dimensional
                value drawn from the distribution.
    
            See Also
            --------
            random.Generator.multinomial: which should be used for new code.
    
            Examples
            --------
            Throw a dice 20 times:
    
            >>> np.random.multinomial(20, [1/6.]*6, size=1)
            array([[4, 1, 7, 5, 2, 1]]) # random
    
            It landed 4 times on 1, once on 2, etc.
    
            Now, throw the dice 20 times, and 20 times again:
    
            >>> np.random.multinomial(20, [1/6.]*6, size=2)
            array([[3, 4, 3, 3, 4, 3], # random
                   [2, 4, 3, 4, 0, 7]])
    
            For the first run, we threw 3 times 1, 4 times 2, etc.  For the second,
            we threw 2 times 1, 4 times 2, etc.
    
            A loaded die is more likely to land on number 6:
    
            >>> np.random.multinomial(100, [1/7.]*5 + [2/7.])
            array([11, 16, 14, 17, 16, 26]) # random
    
            The probability inputs should be normalized. As an implementation
            detail, the value of the last entry is ignored and assumed to take
            up any leftover probability mass, but this should not be relied on.
            A biased coin which has twice as much weight on one side as on the
            other should be sampled like so:
    
            >>> np.random.multinomial(100, [1.0 / 3, 2.0 / 3])  # RIGHT
            array([38, 62]) # random
    
            not like:
    
            >>> np.random.multinomial(100, [1.0, 2.0])  # WRONG
            Traceback (most recent call last):
            ValueError: pvals < 0, pvals > 1 or pvals contains NaNs
    """
    pass

def multivariate_normal(mean, cov, size=None, check_valid='warn', tol=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    multivariate_normal(mean, cov, size=None, check_valid='warn', tol=1e-8)
    
            Draw random samples from a multivariate normal distribution.
    
            The multivariate normal, multinormal or Gaussian distribution is a
            generalization of the one-dimensional normal distribution to higher
            dimensions.  Such a distribution is specified by its mean and
            covariance matrix.  These parameters are analogous to the mean
            (average or "center") and variance (standard deviation, or "width,"
            squared) of the one-dimensional normal distribution.
    
            .. note::
                New code should use the
                `~numpy.random.Generator.multivariate_normal`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            mean : 1-D array_like, of length N
                Mean of the N-dimensional distribution.
            cov : 2-D array_like, of shape (N, N)
                Covariance matrix of the distribution. It must be symmetric and
                positive-semidefinite for proper sampling.
            size : int or tuple of ints, optional
                Given a shape of, for example, ``(m,n,k)``, ``m*n*k`` samples are
                generated, and packed in an `m`-by-`n`-by-`k` arrangement.  Because
                each sample is `N`-dimensional, the output shape is ``(m,n,k,N)``.
                If no shape is specified, a single (`N`-D) sample is returned.
            check_valid : { 'warn', 'raise', 'ignore' }, optional
                Behavior when the covariance matrix is not positive semidefinite.
            tol : float, optional
                Tolerance when checking the singular values in covariance matrix.
                cov is cast to double before the check.
    
            Returns
            -------
            out : ndarray
                The drawn samples, of shape *size*, if that was provided.  If not,
                the shape is ``(N,)``.
    
                In other words, each entry ``out[i,j,...,:]`` is an N-dimensional
                value drawn from the distribution.
    
            See Also
            --------
            random.Generator.multivariate_normal: which should be used for new code.
    
            Notes
            -----
            The mean is a coordinate in N-dimensional space, which represents the
            location where samples are most likely to be generated.  This is
            analogous to the peak of the bell curve for the one-dimensional or
            univariate normal distribution.
    
            Covariance indicates the level to which two variables vary together.
            From the multivariate normal distribution, we draw N-dimensional
            samples, :math:`X = [x_1, x_2, ... x_N]`.  The covariance matrix
            element :math:`C_{ij}` is the covariance of :math:`x_i` and :math:`x_j`.
            The element :math:`C_{ii}` is the variance of :math:`x_i` (i.e. its
            "spread").
    
            Instead of specifying the full covariance matrix, popular
            approximations include:
    
              - Spherical covariance (`cov` is a multiple of the identity matrix)
              - Diagonal covariance (`cov` has non-negative elements, and only on
                the diagonal)
    
            This geometrical property can be seen in two dimensions by plotting
            generated data-points:
    
            >>> mean = [0, 0]
            >>> cov = [[1, 0], [0, 100]]  # diagonal covariance
    
            Diagonal covariance means that points are oriented along x or y-axis:
    
            >>> import matplotlib.pyplot as plt
            >>> x, y = np.random.multivariate_normal(mean, cov, 5000).T
            >>> plt.plot(x, y, 'x')
            >>> plt.axis('equal')
            >>> plt.show()
    
            Note that the covariance matrix must be positive semidefinite (a.k.a.
            nonnegative-definite). Otherwise, the behavior of this method is
            undefined and backwards compatibility is not guaranteed.
    
            References
            ----------
            .. [1] Papoulis, A., "Probability, Random Variables, and Stochastic
                   Processes," 3rd ed., New York: McGraw-Hill, 1991.
            .. [2] Duda, R. O., Hart, P. E., and Stork, D. G., "Pattern
                   Classification," 2nd ed., New York: Wiley, 2001.
    
            Examples
            --------
            >>> mean = (1, 2)
            >>> cov = [[1, 0], [0, 1]]
            >>> x = np.random.multivariate_normal(mean, cov, (3, 3))
            >>> x.shape
            (3, 3, 2)
    
            Here we generate 800 samples from the bivariate normal distribution
            with mean [0, 0] and covariance matrix [[6, -3], [-3, 3.5]].  The
            expected variances of the first and second components of the sample
            are 6 and 3.5, respectively, and the expected correlation
            coefficient is -3/sqrt(6*3.5) ≈ -0.65465.
    
            >>> cov = np.array([[6, -3], [-3, 3.5]])
            >>> pts = np.random.multivariate_normal([0, 0], cov, size=800)
    
            Check that the mean, covariance, and correlation coefficient of the
            sample are close to the expected values:
    
            >>> pts.mean(axis=0)
            array([ 0.0326911 , -0.01280782])  # may vary
            >>> np.cov(pts.T)
            array([[ 5.96202397, -2.85602287],
                   [-2.85602287,  3.47613949]])  # may vary
            >>> np.corrcoef(pts.T)[0, 1]
            -0.6273591314603949  # may vary
    
            We can visualize this data with a scatter plot.  The orientation
            of the point cloud illustrates the negative correlation of the
            components of this sample.
    
            >>> import matplotlib.pyplot as plt
            >>> plt.plot(pts[:, 0], pts[:, 1], '.', alpha=0.5)
            >>> plt.axis('equal')
            >>> plt.grid()
            >>> plt.show()
    """
    pass

def negative_binomial(n, p, size=None): # real signature unknown; restored from __doc__
    """
    negative_binomial(n, p, size=None)
    
            Draw samples from a negative binomial distribution.
    
            Samples are drawn from a negative binomial distribution with specified
            parameters, `n` successes and `p` probability of success where `n`
            is > 0 and `p` is in the interval [0, 1].
    
            .. note::
                New code should use the
                `~numpy.random.Generator.negative_binomial`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            n : float or array_like of floats
                Parameter of the distribution, > 0.
            p : float or array_like of floats
                Parameter of the distribution, >= 0 and <=1.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``n`` and ``p`` are both scalars.
                Otherwise, ``np.broadcast(n, p).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized negative binomial distribution,
                where each sample is equal to N, the number of failures that
                occurred before a total of n successes was reached.
    
            See Also
            --------
            random.Generator.negative_binomial: which should be used for new code.
    
            Notes
            -----
            The probability mass function of the negative binomial distribution is
    
            .. math:: P(N;n,p) = \frac{\Gamma(N+n)}{N!\Gamma(n)}p^{n}(1-p)^{N},
    
            where :math:`n` is the number of successes, :math:`p` is the
            probability of success, :math:`N+n` is the number of trials, and
            :math:`\Gamma` is the gamma function. When :math:`n` is an integer,
            :math:`\frac{\Gamma(N+n)}{N!\Gamma(n)} = \binom{N+n-1}{N}`, which is
            the more common form of this term in the pmf. The negative
            binomial distribution gives the probability of N failures given n
            successes, with a success on the last trial.
    
            If one throws a die repeatedly until the third time a "1" appears,
            then the probability distribution of the number of non-"1"s that
            appear before the third "1" is a negative binomial distribution.
    
            References
            ----------
            .. [1] Weisstein, Eric W. "Negative Binomial Distribution." From
                   MathWorld--A Wolfram Web Resource.
                   http://mathworld.wolfram.com/NegativeBinomialDistribution.html
            .. [2] Wikipedia, "Negative binomial distribution",
                   https://en.wikipedia.org/wiki/Negative_binomial_distribution
    
            Examples
            --------
            Draw samples from the distribution:
    
            A real world example. A company drills wild-cat oil
            exploration wells, each with an estimated probability of
            success of 0.1.  What is the probability of having one success
            for each successive well, that is what is the probability of a
            single success after drilling 5 wells, after 6 wells, etc.?
    
            >>> s = np.random.negative_binomial(1, 0.1, 100000)
            >>> for i in range(1, 11): # doctest: +SKIP
            ...    probability = sum(s<i) / 100000.
            ...    print(i, "wells drilled, probability of one success =", probability)
    """
    pass

def noncentral_chisquare(df, nonc, size=None): # real signature unknown; restored from __doc__
    """
    noncentral_chisquare(df, nonc, size=None)
    
            Draw samples from a noncentral chi-square distribution.
    
            The noncentral :math:`\chi^2` distribution is a generalization of
            the :math:`\chi^2` distribution.
    
            .. note::
                New code should use the
                `~numpy.random.Generator.noncentral_chisquare`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            df : float or array_like of floats
                Degrees of freedom, must be > 0.
    
                .. versionchanged:: 1.10.0
                   Earlier NumPy versions required dfnum > 1.
            nonc : float or array_like of floats
                Non-centrality, must be non-negative.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``df`` and ``nonc`` are both scalars.
                Otherwise, ``np.broadcast(df, nonc).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized noncentral chi-square distribution.
    
            See Also
            --------
            random.Generator.noncentral_chisquare: which should be used for new code.
    
            Notes
            -----
            The probability density function for the noncentral Chi-square
            distribution is
    
            .. math:: P(x;df,nonc) = \sum^{\infty}_{i=0}
                                   \frac{e^{-nonc/2}(nonc/2)^{i}}{i!}
                                   P_{Y_{df+2i}}(x),
    
            where :math:`Y_{q}` is the Chi-square with q degrees of freedom.
    
            References
            ----------
            .. [1] Wikipedia, "Noncentral chi-squared distribution"
                   https://en.wikipedia.org/wiki/Noncentral_chi-squared_distribution
    
            Examples
            --------
            Draw values from the distribution and plot the histogram
    
            >>> import matplotlib.pyplot as plt
            >>> values = plt.hist(np.random.noncentral_chisquare(3, 20, 100000),
            ...                   bins=200, density=True)
            >>> plt.show()
    
            Draw values from a noncentral chisquare with very small noncentrality,
            and compare to a chisquare.
    
            >>> plt.figure()
            >>> values = plt.hist(np.random.noncentral_chisquare(3, .0000001, 100000),
            ...                   bins=np.arange(0., 25, .1), density=True)
            >>> values2 = plt.hist(np.random.chisquare(3, 100000),
            ...                    bins=np.arange(0., 25, .1), density=True)
            >>> plt.plot(values[1][0:-1], values[0]-values2[0], 'ob')
            >>> plt.show()
    
            Demonstrate how large values of non-centrality lead to a more symmetric
            distribution.
    
            >>> plt.figure()
            >>> values = plt.hist(np.random.noncentral_chisquare(3, 20, 100000),
            ...                   bins=200, density=True)
            >>> plt.show()
    """
    pass

def noncentral_f(dfnum, dfden, nonc, size=None): # real signature unknown; restored from __doc__
    """
    noncentral_f(dfnum, dfden, nonc, size=None)
    
            Draw samples from the noncentral F distribution.
    
            Samples are drawn from an F distribution with specified parameters,
            `dfnum` (degrees of freedom in numerator) and `dfden` (degrees of
            freedom in denominator), where both parameters > 1.
            `nonc` is the non-centrality parameter.
    
            .. note::
                New code should use the
                `~numpy.random.Generator.noncentral_f`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            dfnum : float or array_like of floats
                Numerator degrees of freedom, must be > 0.
    
                .. versionchanged:: 1.14.0
                   Earlier NumPy versions required dfnum > 1.
            dfden : float or array_like of floats
                Denominator degrees of freedom, must be > 0.
            nonc : float or array_like of floats
                Non-centrality parameter, the sum of the squares of the numerator
                means, must be >= 0.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``dfnum``, ``dfden``, and ``nonc``
                are all scalars.  Otherwise, ``np.broadcast(dfnum, dfden, nonc).size``
                samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized noncentral Fisher distribution.
    
            See Also
            --------
            random.Generator.noncentral_f: which should be used for new code.
    
            Notes
            -----
            When calculating the power of an experiment (power = probability of
            rejecting the null hypothesis when a specific alternative is true) the
            non-central F statistic becomes important.  When the null hypothesis is
            true, the F statistic follows a central F distribution. When the null
            hypothesis is not true, then it follows a non-central F statistic.
    
            References
            ----------
            .. [1] Weisstein, Eric W. "Noncentral F-Distribution."
                   From MathWorld--A Wolfram Web Resource.
                   http://mathworld.wolfram.com/NoncentralF-Distribution.html
            .. [2] Wikipedia, "Noncentral F-distribution",
                   https://en.wikipedia.org/wiki/Noncentral_F-distribution
    
            Examples
            --------
            In a study, testing for a specific alternative to the null hypothesis
            requires use of the Noncentral F distribution. We need to calculate the
            area in the tail of the distribution that exceeds the value of the F
            distribution for the null hypothesis.  We'll plot the two probability
            distributions for comparison.
    
            >>> dfnum = 3 # between group deg of freedom
            >>> dfden = 20 # within groups degrees of freedom
            >>> nonc = 3.0
            >>> nc_vals = np.random.noncentral_f(dfnum, dfden, nonc, 1000000)
            >>> NF = np.histogram(nc_vals, bins=50, density=True)
            >>> c_vals = np.random.f(dfnum, dfden, 1000000)
            >>> F = np.histogram(c_vals, bins=50, density=True)
            >>> import matplotlib.pyplot as plt
            >>> plt.plot(F[1][1:], F[0])
            >>> plt.plot(NF[1][1:], NF[0])
            >>> plt.show()
    """
    pass

def normal(loc=0.0, scale=1.0, size=None): # real signature unknown; restored from __doc__
    """
    normal(loc=0.0, scale=1.0, size=None)
    
            Draw random samples from a normal (Gaussian) distribution.
    
            The probability density function of the normal distribution, first
            derived by De Moivre and 200 years later by both Gauss and Laplace
            independently [2]_, is often called the bell curve because of
            its characteristic shape (see the example below).
    
            The normal distributions occurs often in nature.  For example, it
            describes the commonly occurring distribution of samples influenced
            by a large number of tiny, random disturbances, each with its own
            unique distribution [2]_.
    
            .. note::
                New code should use the `~numpy.random.Generator.normal`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            loc : float or array_like of floats
                Mean ("centre") of the distribution.
            scale : float or array_like of floats
                Standard deviation (spread or "width") of the distribution. Must be
                non-negative.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``loc`` and ``scale`` are both scalars.
                Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized normal distribution.
    
            See Also
            --------
            scipy.stats.norm : probability density function, distribution or
                cumulative density function, etc.
            random.Generator.normal: which should be used for new code.
    
            Notes
            -----
            The probability density for the Gaussian distribution is
    
            .. math:: p(x) = \frac{1}{\sqrt{ 2 \pi \sigma^2 }}
                             e^{ - \frac{ (x - \mu)^2 } {2 \sigma^2} },
    
            where :math:`\mu` is the mean and :math:`\sigma` the standard
            deviation. The square of the standard deviation, :math:`\sigma^2`,
            is called the variance.
    
            The function has its peak at the mean, and its "spread" increases with
            the standard deviation (the function reaches 0.607 times its maximum at
            :math:`x + \sigma` and :math:`x - \sigma` [2]_).  This implies that
            normal is more likely to return samples lying close to the mean, rather
            than those far away.
    
            References
            ----------
            .. [1] Wikipedia, "Normal distribution",
                   https://en.wikipedia.org/wiki/Normal_distribution
            .. [2] P. R. Peebles Jr., "Central Limit Theorem" in "Probability,
                   Random Variables and Random Signal Principles", 4th ed., 2001,
                   pp. 51, 51, 125.
    
            Examples
            --------
            Draw samples from the distribution:
    
            >>> mu, sigma = 0, 0.1 # mean and standard deviation
            >>> s = np.random.normal(mu, sigma, 1000)
    
            Verify the mean and the variance:
    
            >>> abs(mu - np.mean(s))
            0.0  # may vary
    
            >>> abs(sigma - np.std(s, ddof=1))
            0.1  # may vary
    
            Display the histogram of the samples, along with
            the probability density function:
    
            >>> import matplotlib.pyplot as plt
            >>> count, bins, ignored = plt.hist(s, 30, density=True)
            >>> plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
            ...                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
            ...          linewidth=2, color='r')
            >>> plt.show()
    
            Two-by-four array of samples from the normal distribution with
            mean 3 and standard deviation 2.5:
    
            >>> np.random.normal(3, 2.5, size=(2, 4))
            array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
                   [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random
    """
    pass

def pareto(a, size=None): # real signature unknown; restored from __doc__
    """
    pareto(a, size=None)
    
            Draw samples from a Pareto II or Lomax distribution with
            specified shape.
    
            The Lomax or Pareto II distribution is a shifted Pareto
            distribution. The classical Pareto distribution can be
            obtained from the Lomax distribution by adding 1 and
            multiplying by the scale parameter ``m`` (see Notes).  The
            smallest value of the Lomax distribution is zero while for the
            classical Pareto distribution it is ``mu``, where the standard
            Pareto distribution has location ``mu = 1``.  Lomax can also
            be considered as a simplified version of the Generalized
            Pareto distribution (available in SciPy), with the scale set
            to one and the location set to zero.
    
            The Pareto distribution must be greater than zero, and is
            unbounded above.  It is also known as the "80-20 rule".  In
            this distribution, 80 percent of the weights are in the lowest
            20 percent of the range, while the other 20 percent fill the
            remaining 80 percent of the range.
    
            .. note::
                New code should use the `~numpy.random.Generator.pareto`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            a : float or array_like of floats
                Shape of the distribution. Must be positive.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``a`` is a scalar.  Otherwise,
                ``np.array(a).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized Pareto distribution.
    
            See Also
            --------
            scipy.stats.lomax : probability density function, distribution or
                cumulative density function, etc.
            scipy.stats.genpareto : probability density function, distribution or
                cumulative density function, etc.
            random.Generator.pareto: which should be used for new code.
    
            Notes
            -----
            The probability density for the Pareto distribution is
    
            .. math:: p(x) = \frac{am^a}{x^{a+1}}
    
            where :math:`a` is the shape and :math:`m` the scale.
    
            The Pareto distribution, named after the Italian economist
            Vilfredo Pareto, is a power law probability distribution
            useful in many real world problems.  Outside the field of
            economics it is generally referred to as the Bradford
            distribution. Pareto developed the distribution to describe
            the distribution of wealth in an economy.  It has also found
            use in insurance, web page access statistics, oil field sizes,
            and many other problems, including the download frequency for
            projects in Sourceforge [1]_.  It is one of the so-called
            "fat-tailed" distributions.
    
            References
            ----------
            .. [1] Francis Hunt and Paul Johnson, On the Pareto Distribution of
                   Sourceforge projects.
            .. [2] Pareto, V. (1896). Course of Political Economy. Lausanne.
            .. [3] Reiss, R.D., Thomas, M.(2001), Statistical Analysis of Extreme
                   Values, Birkhauser Verlag, Basel, pp 23-30.
            .. [4] Wikipedia, "Pareto distribution",
                   https://en.wikipedia.org/wiki/Pareto_distribution
    
            Examples
            --------
            Draw samples from the distribution:
    
            >>> a, m = 3., 2.  # shape and mode
            >>> s = (np.random.pareto(a, 1000) + 1) * m
    
            Display the histogram of the samples, along with the probability
            density function:
    
            >>> import matplotlib.pyplot as plt
            >>> count, bins, _ = plt.hist(s, 100, density=True)
            >>> fit = a*m**a / bins**(a+1)
            >>> plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='r')
            >>> plt.show()
    """
    pass

def permutation(x): # real signature unknown; restored from __doc__
    """
    permutation(x)
    
            Randomly permute a sequence, or return a permuted range.
    
            If `x` is a multi-dimensional array, it is only shuffled along its
            first index.
    
            .. note::
                New code should use the
                `~numpy.random.Generator.permutation`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            x : int or array_like
                If `x` is an integer, randomly permute ``np.arange(x)``.
                If `x` is an array, make a copy and shuffle the elements
                randomly.
    
            Returns
            -------
            out : ndarray
                Permuted sequence or array range.
    
            See Also
            --------
            random.Generator.permutation: which should be used for new code.
    
            Examples
            --------
            >>> np.random.permutation(10)
            array([1, 7, 4, 3, 0, 9, 2, 5, 8, 6]) # random
    
            >>> np.random.permutation([1, 4, 9, 12, 15])
            array([15,  1,  9,  4, 12]) # random
    
            >>> arr = np.arange(9).reshape((3, 3))
            >>> np.random.permutation(arr)
            array([[6, 7, 8], # random
                   [0, 1, 2],
                   [3, 4, 5]])
    """
    pass

def poisson(lam=1.0, size=None): # real signature unknown; restored from __doc__
    """
    poisson(lam=1.0, size=None)
    
            Draw samples from a Poisson distribution.
    
            The Poisson distribution is the limit of the binomial distribution
            for large N.
    
            .. note::
                New code should use the `~numpy.random.Generator.poisson`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            lam : float or array_like of floats
                Expected number of events occurring in a fixed-time interval,
                must be >= 0. A sequence must be broadcastable over the requested
                size.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``lam`` is a scalar. Otherwise,
                ``np.array(lam).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized Poisson distribution.
    
            See Also
            --------
            random.Generator.poisson: which should be used for new code.
    
            Notes
            -----
            The Poisson distribution
    
            .. math:: f(k; \lambda)=\frac{\lambda^k e^{-\lambda}}{k!}
    
            For events with an expected separation :math:`\lambda` the Poisson
            distribution :math:`f(k; \lambda)` describes the probability of
            :math:`k` events occurring within the observed
            interval :math:`\lambda`.
    
            Because the output is limited to the range of the C int64 type, a
            ValueError is raised when `lam` is within 10 sigma of the maximum
            representable value.
    
            References
            ----------
            .. [1] Weisstein, Eric W. "Poisson Distribution."
                   From MathWorld--A Wolfram Web Resource.
                   http://mathworld.wolfram.com/PoissonDistribution.html
            .. [2] Wikipedia, "Poisson distribution",
                   https://en.wikipedia.org/wiki/Poisson_distribution
    
            Examples
            --------
            Draw samples from the distribution:
    
            >>> import numpy as np
            >>> s = np.random.poisson(5, 10000)
    
            Display histogram of the sample:
    
            >>> import matplotlib.pyplot as plt
            >>> count, bins, ignored = plt.hist(s, 14, density=True)
            >>> plt.show()
    
            Draw each 100 values for lambda 100 and 500:
    
            >>> s = np.random.poisson(lam=(100., 500.), size=(100, 2))
    """
    pass

def power(a, size=None): # real signature unknown; restored from __doc__
    """
    power(a, size=None)
    
            Draws samples in [0, 1] from a power distribution with positive
            exponent a - 1.
    
            Also known as the power function distribution.
    
            .. note::
                New code should use the `~numpy.random.Generator.power`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            a : float or array_like of floats
                Parameter of the distribution. Must be non-negative.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``a`` is a scalar.  Otherwise,
                ``np.array(a).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized power distribution.
    
            Raises
            ------
            ValueError
                If a <= 0.
    
            See Also
            --------
            random.Generator.power: which should be used for new code.
    
            Notes
            -----
            The probability density function is
    
            .. math:: P(x; a) = ax^{a-1}, 0 \le x \le 1, a>0.
    
            The power function distribution is just the inverse of the Pareto
            distribution. It may also be seen as a special case of the Beta
            distribution.
    
            It is used, for example, in modeling the over-reporting of insurance
            claims.
    
            References
            ----------
            .. [1] Christian Kleiber, Samuel Kotz, "Statistical size distributions
                   in economics and actuarial sciences", Wiley, 2003.
            .. [2] Heckert, N. A. and Filliben, James J. "NIST Handbook 148:
                   Dataplot Reference Manual, Volume 2: Let Subcommands and Library
                   Functions", National Institute of Standards and Technology
                   Handbook Series, June 2003.
                   https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/powpdf.pdf
    
            Examples
            --------
            Draw samples from the distribution:
    
            >>> a = 5. # shape
            >>> samples = 1000
            >>> s = np.random.power(a, samples)
    
            Display the histogram of the samples, along with
            the probability density function:
    
            >>> import matplotlib.pyplot as plt
            >>> count, bins, ignored = plt.hist(s, bins=30)
            >>> x = np.linspace(0, 1, 100)
            >>> y = a*x**(a-1.)
            >>> normed_y = samples*np.diff(bins)[0]*y
            >>> plt.plot(x, normed_y)
            >>> plt.show()
    
            Compare the power function distribution to the inverse of the Pareto.
    
            >>> from scipy import stats # doctest: +SKIP
            >>> rvs = np.random.power(5, 1000000)
            >>> rvsp = np.random.pareto(5, 1000000)
            >>> xx = np.linspace(0,1,100)
            >>> powpdf = stats.powerlaw.pdf(xx,5)  # doctest: +SKIP
    
            >>> plt.figure()
            >>> plt.hist(rvs, bins=50, density=True)
            >>> plt.plot(xx,powpdf,'r-')  # doctest: +SKIP
            >>> plt.title('np.random.power(5)')
    
            >>> plt.figure()
            >>> plt.hist(1./(1.+rvsp), bins=50, density=True)
            >>> plt.plot(xx,powpdf,'r-')  # doctest: +SKIP
            >>> plt.title('inverse of 1 + np.random.pareto(5)')
    
            >>> plt.figure()
            >>> plt.hist(1./(1.+rvsp), bins=50, density=True)
            >>> plt.plot(xx,powpdf,'r-')  # doctest: +SKIP
            >>> plt.title('inverse of stats.pareto(5)')
    """
    pass

def rand(*dn): # known case of numpy.random.mtrand.rand
    """
    rand(d0, d1, ..., dn)
    
            Random values in a given shape.
    
            .. note::
                This is a convenience function for users porting code from Matlab,
                and wraps `random_sample`. That function takes a
                tuple to specify the size of the output, which is consistent with
                other NumPy functions like `numpy.zeros` and `numpy.ones`.
    
            Create an array of the given shape and populate it with
            random samples from a uniform distribution
            over ``[0, 1)``.
    
            Parameters
            ----------
            d0, d1, ..., dn : int, optional
                The dimensions of the returned array, must be non-negative.
                If no argument is given a single Python float is returned.
    
            Returns
            -------
            out : ndarray, shape ``(d0, d1, ..., dn)``
                Random values.
    
            See Also
            --------
            random
    
            Examples
            --------
            >>> np.random.rand(3,2)
            array([[ 0.14022471,  0.96360618],  #random
                   [ 0.37601032,  0.25528411],  #random
                   [ 0.49313049,  0.94909878]]) #random
    """
    pass

def randint(low, high=None, size=None, dtype=None): # real signature unknown; restored from __doc__
    """
    randint(low, high=None, size=None, dtype=int)
    
            Return random integers from `low` (inclusive) to `high` (exclusive).
    
            Return random integers from the "discrete uniform" distribution of
            the specified dtype in the "half-open" interval [`low`, `high`). If
            `high` is None (the default), then results are from [0, `low`).
    
            .. note::
                New code should use the `~numpy.random.Generator.randint`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            low : int or array-like of ints
                Lowest (signed) integers to be drawn from the distribution (unless
                ``high=None``, in which case this parameter is one above the
                *highest* such integer).
            high : int or array-like of ints, optional
                If provided, one above the largest (signed) integer to be drawn
                from the distribution (see above for behavior if ``high=None``).
                If array-like, must contain integer values
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  Default is None, in which case a
                single value is returned.
            dtype : dtype, optional
                Desired dtype of the result. Byteorder must be native.
                The default value is int.
    
                .. versionadded:: 1.11.0
    
            Returns
            -------
            out : int or ndarray of ints
                `size`-shaped array of random integers from the appropriate
                distribution, or a single such random int if `size` not provided.
    
            See Also
            --------
            random_integers : similar to `randint`, only for the closed
                interval [`low`, `high`], and 1 is the lowest value if `high` is
                omitted.
            random.Generator.integers: which should be used for new code.
    
            Examples
            --------
            >>> np.random.randint(2, size=10)
            array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0]) # random
            >>> np.random.randint(1, size=10)
            array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    
            Generate a 2 x 4 array of ints between 0 and 4, inclusive:
    
            >>> np.random.randint(5, size=(2, 4))
            array([[4, 0, 2, 1], # random
                   [3, 2, 2, 0]])
    
            Generate a 1 x 3 array with 3 different upper bounds
    
            >>> np.random.randint(1, [3, 5, 10])
            array([2, 2, 9]) # random
    
            Generate a 1 by 3 array with 3 different lower bounds
    
            >>> np.random.randint([1, 5, 7], 10)
            array([9, 8, 7]) # random
    
            Generate a 2 by 4 array using broadcasting with dtype of uint8
    
            >>> np.random.randint([1, 3, 5, 7], [[10], [20]], dtype=np.uint8)
            array([[ 8,  6,  9,  7], # random
                   [ 1, 16,  9, 12]], dtype=uint8)
    """
    pass

def randn(*dn): # known case of numpy.random.mtrand.randn
    """
    randn(d0, d1, ..., dn)
    
            Return a sample (or samples) from the "standard normal" distribution.
    
            .. note::
                This is a convenience function for users porting code from Matlab,
                and wraps `standard_normal`. That function takes a
                tuple to specify the size of the output, which is consistent with
                other NumPy functions like `numpy.zeros` and `numpy.ones`.
    
            .. note::
                New code should use the
                `~numpy.random.Generator.standard_normal`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            If positive int_like arguments are provided, `randn` generates an array
            of shape ``(d0, d1, ..., dn)``, filled
            with random floats sampled from a univariate "normal" (Gaussian)
            distribution of mean 0 and variance 1. A single float randomly sampled
            from the distribution is returned if no argument is provided.
    
            Parameters
            ----------
            d0, d1, ..., dn : int, optional
                The dimensions of the returned array, must be non-negative.
                If no argument is given a single Python float is returned.
    
            Returns
            -------
            Z : ndarray or float
                A ``(d0, d1, ..., dn)``-shaped array of floating-point samples from
                the standard normal distribution, or a single such float if
                no parameters were supplied.
    
            See Also
            --------
            standard_normal : Similar, but takes a tuple as its argument.
            normal : Also accepts mu and sigma arguments.
            random.Generator.standard_normal: which should be used for new code.
    
            Notes
            -----
            For random samples from the normal distribution with mean ``mu`` and
            standard deviation ``sigma``, use::
    
                sigma * np.random.randn(...) + mu
    
            Examples
            --------
            >>> np.random.randn()
            2.1923875335537315  # random
    
            Two-by-four array of samples from the normal distribution with
            mean 3 and standard deviation 2.5:
    
            >>> 3 + 2.5 * np.random.randn(2, 4)
            array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
                   [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random
    """
    pass

def random(size=None): # real signature unknown; restored from __doc__
    """
    random(size=None)
    
            Return random floats in the half-open interval [0.0, 1.0). Alias for
            `random_sample` to ease forward-porting to the new random API.
    """
    pass

def random_integers(low, high=None, size=None): # real signature unknown; restored from __doc__
    """
    random_integers(low, high=None, size=None)
    
            Random integers of type `np.int_` between `low` and `high`, inclusive.
    
            Return random integers of type `np.int_` from the "discrete uniform"
            distribution in the closed interval [`low`, `high`].  If `high` is
            None (the default), then results are from [1, `low`]. The `np.int_`
            type translates to the C long integer type and its precision
            is platform dependent.
    
            This function has been deprecated. Use randint instead.
    
            .. deprecated:: 1.11.0
    
            Parameters
            ----------
            low : int
                Lowest (signed) integer to be drawn from the distribution (unless
                ``high=None``, in which case this parameter is the *highest* such
                integer).
            high : int, optional
                If provided, the largest (signed) integer to be drawn from the
                distribution (see above for behavior if ``high=None``).
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  Default is None, in which case a
                single value is returned.
    
            Returns
            -------
            out : int or ndarray of ints
                `size`-shaped array of random integers from the appropriate
                distribution, or a single such random int if `size` not provided.
    
            See Also
            --------
            randint : Similar to `random_integers`, only for the half-open
                interval [`low`, `high`), and 0 is the lowest value if `high` is
                omitted.
    
            Notes
            -----
            To sample from N evenly spaced floating-point numbers between a and b,
            use::
    
              a + (b - a) * (np.random.random_integers(N) - 1) / (N - 1.)
    
            Examples
            --------
            >>> np.random.random_integers(5)
            4 # random
            >>> type(np.random.random_integers(5))
            <class 'numpy.int64'>
            >>> np.random.random_integers(5, size=(3,2))
            array([[5, 4], # random
                   [3, 3],
                   [4, 5]])
    
            Choose five random numbers from the set of five evenly-spaced
            numbers between 0 and 2.5, inclusive (*i.e.*, from the set
            :math:`{0, 5/8, 10/8, 15/8, 20/8}`):
    
            >>> 2.5 * (np.random.random_integers(5, size=(5,)) - 1) / 4.
            array([ 0.625,  1.25 ,  0.625,  0.625,  2.5  ]) # random
    
            Roll two six sided dice 1000 times and sum the results:
    
            >>> d1 = np.random.random_integers(1, 6, 1000)
            >>> d2 = np.random.random_integers(1, 6, 1000)
            >>> dsums = d1 + d2
    
            Display results as a histogram:
    
            >>> import matplotlib.pyplot as plt
            >>> count, bins, ignored = plt.hist(dsums, 11, density=True)
            >>> plt.show()
    """
    pass

def random_sample(size=None): # real signature unknown; restored from __doc__
    """
    random_sample(size=None)
    
            Return random floats in the half-open interval [0.0, 1.0).
    
            Results are from the "continuous uniform" distribution over the
            stated interval.  To sample :math:`Unif[a, b), b > a` multiply
            the output of `random_sample` by `(b-a)` and add `a`::
    
              (b - a) * random_sample() + a
    
            .. note::
                New code should use the `~numpy.random.Generator.random`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  Default is None, in which case a
                single value is returned.
    
            Returns
            -------
            out : float or ndarray of floats
                Array of random floats of shape `size` (unless ``size=None``, in which
                case a single float is returned).
    
            See Also
            --------
            random.Generator.random: which should be used for new code.
    
            Examples
            --------
            >>> np.random.random_sample()
            0.47108547995356098 # random
            >>> type(np.random.random_sample())
            <class 'float'>
            >>> np.random.random_sample((5,))
            array([ 0.30220482,  0.86820401,  0.1654503 ,  0.11659149,  0.54323428]) # random
    
            Three-by-two array of random numbers from [-5, 0):
    
            >>> 5 * np.random.random_sample((3, 2)) - 5
            array([[-3.99149989, -0.52338984], # random
                   [-2.99091858, -0.79479508],
                   [-1.23204345, -1.75224494]])
    """
    pass

def ranf(*args, **kwargs): # real signature unknown
    """
    This is an alias of `random_sample`. See `random_sample`  for the complete
        documentation.
    """
    pass

def rayleigh(scale=1.0, size=None): # real signature unknown; restored from __doc__
    """
    rayleigh(scale=1.0, size=None)
    
            Draw samples from a Rayleigh distribution.
    
            The :math:`\chi` and Weibull distributions are generalizations of the
            Rayleigh.
    
            .. note::
                New code should use the `~numpy.random.Generator.rayleigh`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            scale : float or array_like of floats, optional
                Scale, also equals the mode. Must be non-negative. Default is 1.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``scale`` is a scalar.  Otherwise,
                ``np.array(scale).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized Rayleigh distribution.
    
            See Also
            --------
            random.Generator.rayleigh: which should be used for new code.
    
            Notes
            -----
            The probability density function for the Rayleigh distribution is
    
            .. math:: P(x;scale) = \frac{x}{scale^2}e^{\frac{-x^2}{2 \cdotp scale^2}}
    
            The Rayleigh distribution would arise, for example, if the East
            and North components of the wind velocity had identical zero-mean
            Gaussian distributions.  Then the wind speed would have a Rayleigh
            distribution.
    
            References
            ----------
            .. [1] Brighton Webs Ltd., "Rayleigh Distribution,"
                   https://web.archive.org/web/20090514091424/http://brighton-webs.co.uk:80/distributions/rayleigh.asp
            .. [2] Wikipedia, "Rayleigh distribution"
                   https://en.wikipedia.org/wiki/Rayleigh_distribution
    
            Examples
            --------
            Draw values from the distribution and plot the histogram
    
            >>> from matplotlib.pyplot import hist
            >>> values = hist(np.random.rayleigh(3, 100000), bins=200, density=True)
    
            Wave heights tend to follow a Rayleigh distribution. If the mean wave
            height is 1 meter, what fraction of waves are likely to be larger than 3
            meters?
    
            >>> meanvalue = 1
            >>> modevalue = np.sqrt(2 / np.pi) * meanvalue
            >>> s = np.random.rayleigh(modevalue, 1000000)
    
            The percentage of waves larger than 3 meters is:
    
            >>> 100.*sum(s>3)/1000000.
            0.087300000000000003 # random
    """
    pass

def sample(*args, **kwargs): # real signature unknown
    """
    This is an alias of `random_sample`. See `random_sample`  for the complete
        documentation.
    """
    pass

def seed(seed=None): # real signature unknown; restored from __doc__
    """
    seed(seed=None)
    
        Reseed the singleton RandomState instance.
    
        Notes
        -----
        This is a convenience, legacy function that exists to support
        older code that uses the singleton RandomState. Best practice
        is to use a dedicated ``Generator`` instance rather than
        the random variate generation methods exposed directly in
        the random module.
    
        See Also
        --------
        numpy.random.Generator
    """
    pass

def set_bit_generator(*args, **kwargs): # real signature unknown
    """
    Sets the singleton RandomState's bit generator
    
        Parameters
        ----------
        bitgen
            A bit generator instance
    
        Notes
        -----
        The singleton RandomState provides the random variate generators in the
        ``numpy.random``namespace. This function, and its counterpart get method,
        provides a path to hot-swap the default MT19937 bit generator with a
        user provided alternative. These function are intended to provide
        a continuous path where a single underlying bit generator can be
        used both with an instance of ``Generator`` and with the singleton
        instance of RandomState.
    
        See Also
        --------
        get_bit_generator
        numpy.random.Generator
    """
    pass

def set_state(state): # real signature unknown; restored from __doc__
    """
    set_state(state)
    
            Set the internal state of the generator from a tuple.
    
            For use if one has reason to manually (re-)set the internal state of
            the bit generator used by the RandomState instance. By default,
            RandomState uses the "Mersenne Twister"[1]_ pseudo-random number
            generating algorithm.
    
            Parameters
            ----------
            state : {tuple(str, ndarray of 624 uints, int, int, float), dict}
                The `state` tuple has the following items:
    
                1. the string 'MT19937', specifying the Mersenne Twister algorithm.
                2. a 1-D array of 624 unsigned integers ``keys``.
                3. an integer ``pos``.
                4. an integer ``has_gauss``.
                5. a float ``cached_gaussian``.
    
                If state is a dictionary, it is directly set using the BitGenerators
                `state` property.
    
            Returns
            -------
            out : None
                Returns 'None' on success.
    
            See Also
            --------
            get_state
    
            Notes
            -----
            `set_state` and `get_state` are not needed to work with any of the
            random distributions in NumPy. If the internal state is manually altered,
            the user should know exactly what he/she is doing.
    
            For backwards compatibility, the form (str, array of 624 uints, int) is
            also accepted although it is missing some information about the cached
            Gaussian value: ``state = ('MT19937', keys, pos)``.
    
            References
            ----------
            .. [1] M. Matsumoto and T. Nishimura, "Mersenne Twister: A
               623-dimensionally equidistributed uniform pseudorandom number
               generator," *ACM Trans. on Modeling and Computer Simulation*,
               Vol. 8, No. 1, pp. 3-30, Jan. 1998.
    """
    pass

def shuffle(x): # real signature unknown; restored from __doc__
    """
    shuffle(x)
    
            Modify a sequence in-place by shuffling its contents.
    
            This function only shuffles the array along the first axis of a
            multi-dimensional array. The order of sub-arrays is changed but
            their contents remains the same.
    
            .. note::
                New code should use the `~numpy.random.Generator.shuffle`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            x : ndarray or MutableSequence
                The array, list or mutable sequence to be shuffled.
    
            Returns
            -------
            None
    
            See Also
            --------
            random.Generator.shuffle: which should be used for new code.
    
            Examples
            --------
            >>> arr = np.arange(10)
            >>> np.random.shuffle(arr)
            >>> arr
            [1 7 5 2 9 4 3 6 0 8] # random
    
            Multi-dimensional arrays are only shuffled along the first axis:
    
            >>> arr = np.arange(9).reshape((3, 3))
            >>> np.random.shuffle(arr)
            >>> arr
            array([[3, 4, 5], # random
                   [6, 7, 8],
                   [0, 1, 2]])
    """
    pass

def standard_cauchy(size=None): # real signature unknown; restored from __doc__
    """
    standard_cauchy(size=None)
    
            Draw samples from a standard Cauchy distribution with mode = 0.
    
            Also known as the Lorentz distribution.
    
            .. note::
                New code should use the
                `~numpy.random.Generator.standard_cauchy`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  Default is None, in which case a
                single value is returned.
    
            Returns
            -------
            samples : ndarray or scalar
                The drawn samples.
    
            See Also
            --------
            random.Generator.standard_cauchy: which should be used for new code.
    
            Notes
            -----
            The probability density function for the full Cauchy distribution is
    
            .. math:: P(x; x_0, \gamma) = \frac{1}{\pi \gamma \bigl[ 1+
                      (\frac{x-x_0}{\gamma})^2 \bigr] }
    
            and the Standard Cauchy distribution just sets :math:`x_0=0` and
            :math:`\gamma=1`
    
            The Cauchy distribution arises in the solution to the driven harmonic
            oscillator problem, and also describes spectral line broadening. It
            also describes the distribution of values at which a line tilted at
            a random angle will cut the x axis.
    
            When studying hypothesis tests that assume normality, seeing how the
            tests perform on data from a Cauchy distribution is a good indicator of
            their sensitivity to a heavy-tailed distribution, since the Cauchy looks
            very much like a Gaussian distribution, but with heavier tails.
    
            References
            ----------
            .. [1] NIST/SEMATECH e-Handbook of Statistical Methods, "Cauchy
                  Distribution",
                  https://www.itl.nist.gov/div898/handbook/eda/section3/eda3663.htm
            .. [2] Weisstein, Eric W. "Cauchy Distribution." From MathWorld--A
                  Wolfram Web Resource.
                  http://mathworld.wolfram.com/CauchyDistribution.html
            .. [3] Wikipedia, "Cauchy distribution"
                  https://en.wikipedia.org/wiki/Cauchy_distribution
    
            Examples
            --------
            Draw samples and plot the distribution:
    
            >>> import matplotlib.pyplot as plt
            >>> s = np.random.standard_cauchy(1000000)
            >>> s = s[(s>-25) & (s<25)]  # truncate distribution so it plots well
            >>> plt.hist(s, bins=100)
            >>> plt.show()
    """
    pass

def standard_exponential(size=None): # real signature unknown; restored from __doc__
    """
    standard_exponential(size=None)
    
            Draw samples from the standard exponential distribution.
    
            `standard_exponential` is identical to the exponential distribution
            with a scale parameter of 1.
    
            .. note::
                New code should use the
                `~numpy.random.Generator.standard_exponential`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  Default is None, in which case a
                single value is returned.
    
            Returns
            -------
            out : float or ndarray
                Drawn samples.
    
            See Also
            --------
            random.Generator.standard_exponential: which should be used for new code.
    
            Examples
            --------
            Output a 3x8000 array:
    
            >>> n = np.random.standard_exponential((3, 8000))
    """
    pass

def standard_gamma(shape, size=None): # real signature unknown; restored from __doc__
    """
    standard_gamma(shape, size=None)
    
            Draw samples from a standard Gamma distribution.
    
            Samples are drawn from a Gamma distribution with specified parameters,
            shape (sometimes designated "k") and scale=1.
    
            .. note::
                New code should use the
                `~numpy.random.Generator.standard_gamma`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            shape : float or array_like of floats
                Parameter, must be non-negative.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``shape`` is a scalar.  Otherwise,
                ``np.array(shape).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized standard gamma distribution.
    
            See Also
            --------
            scipy.stats.gamma : probability density function, distribution or
                cumulative density function, etc.
            random.Generator.standard_gamma: which should be used for new code.
    
            Notes
            -----
            The probability density for the Gamma distribution is
    
            .. math:: p(x) = x^{k-1}\frac{e^{-x/\theta}}{\theta^k\Gamma(k)},
    
            where :math:`k` is the shape and :math:`\theta` the scale,
            and :math:`\Gamma` is the Gamma function.
    
            The Gamma distribution is often used to model the times to failure of
            electronic components, and arises naturally in processes for which the
            waiting times between Poisson distributed events are relevant.
    
            References
            ----------
            .. [1] Weisstein, Eric W. "Gamma Distribution." From MathWorld--A
                   Wolfram Web Resource.
                   http://mathworld.wolfram.com/GammaDistribution.html
            .. [2] Wikipedia, "Gamma distribution",
                   https://en.wikipedia.org/wiki/Gamma_distribution
    
            Examples
            --------
            Draw samples from the distribution:
    
            >>> shape, scale = 2., 1. # mean and width
            >>> s = np.random.standard_gamma(shape, 1000000)
    
            Display the histogram of the samples, along with
            the probability density function:
    
            >>> import matplotlib.pyplot as plt
            >>> import scipy.special as sps  # doctest: +SKIP
            >>> count, bins, ignored = plt.hist(s, 50, density=True)
            >>> y = bins**(shape-1) * ((np.exp(-bins/scale))/  # doctest: +SKIP
            ...                       (sps.gamma(shape) * scale**shape))
            >>> plt.plot(bins, y, linewidth=2, color='r')  # doctest: +SKIP
            >>> plt.show()
    """
    pass

def standard_normal(size=None): # real signature unknown; restored from __doc__
    """
    standard_normal(size=None)
    
            Draw samples from a standard Normal distribution (mean=0, stdev=1).
    
            .. note::
                New code should use the
                `~numpy.random.Generator.standard_normal`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  Default is None, in which case a
                single value is returned.
    
            Returns
            -------
            out : float or ndarray
                A floating-point array of shape ``size`` of drawn samples, or a
                single sample if ``size`` was not specified.
    
            See Also
            --------
            normal :
                Equivalent function with additional ``loc`` and ``scale`` arguments
                for setting the mean and standard deviation.
            random.Generator.standard_normal: which should be used for new code.
    
            Notes
            -----
            For random samples from the normal distribution with mean ``mu`` and
            standard deviation ``sigma``, use one of::
    
                mu + sigma * np.random.standard_normal(size=...)
                np.random.normal(mu, sigma, size=...)
    
            Examples
            --------
            >>> np.random.standard_normal()
            2.1923875335537315 #random
    
            >>> s = np.random.standard_normal(8000)
            >>> s
            array([ 0.6888893 ,  0.78096262, -0.89086505, ...,  0.49876311,  # random
                   -0.38672696, -0.4685006 ])                                # random
            >>> s.shape
            (8000,)
            >>> s = np.random.standard_normal(size=(3, 4, 2))
            >>> s.shape
            (3, 4, 2)
    
            Two-by-four array of samples from the normal distribution with
            mean 3 and standard deviation 2.5:
    
            >>> 3 + 2.5 * np.random.standard_normal(size=(2, 4))
            array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
                   [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random
    """
    pass

def standard_t(df, size=None): # real signature unknown; restored from __doc__
    """
    standard_t(df, size=None)
    
            Draw samples from a standard Student's t distribution with `df` degrees
            of freedom.
    
            A special case of the hyperbolic distribution.  As `df` gets
            large, the result resembles that of the standard normal
            distribution (`standard_normal`).
    
            .. note::
                New code should use the `~numpy.random.Generator.standard_t`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            df : float or array_like of floats
                Degrees of freedom, must be > 0.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``df`` is a scalar.  Otherwise,
                ``np.array(df).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized standard Student's t distribution.
    
            See Also
            --------
            random.Generator.standard_t: which should be used for new code.
    
            Notes
            -----
            The probability density function for the t distribution is
    
            .. math:: P(x, df) = \frac{\Gamma(\frac{df+1}{2})}{\sqrt{\pi df}
                      \Gamma(\frac{df}{2})}\Bigl( 1+\frac{x^2}{df} \Bigr)^{-(df+1)/2}
    
            The t test is based on an assumption that the data come from a
            Normal distribution. The t test provides a way to test whether
            the sample mean (that is the mean calculated from the data) is
            a good estimate of the true mean.
    
            The derivation of the t-distribution was first published in
            1908 by William Gosset while working for the Guinness Brewery
            in Dublin. Due to proprietary issues, he had to publish under
            a pseudonym, and so he used the name Student.
    
            References
            ----------
            .. [1] Dalgaard, Peter, "Introductory Statistics With R",
                   Springer, 2002.
            .. [2] Wikipedia, "Student's t-distribution"
                   https://en.wikipedia.org/wiki/Student's_t-distribution
    
            Examples
            --------
            From Dalgaard page 83 [1]_, suppose the daily energy intake for 11
            women in kilojoules (kJ) is:
    
            >>> intake = np.array([5260., 5470, 5640, 6180, 6390, 6515, 6805, 7515, \
            ...                    7515, 8230, 8770])
    
            Does their energy intake deviate systematically from the recommended
            value of 7725 kJ? Our null hypothesis will be the absence of deviation,
            and the alternate hypothesis will be the presence of an effect that could be
            either positive or negative, hence making our test 2-tailed. 
    
            Because we are estimating the mean and we have N=11 values in our sample,
            we have N-1=10 degrees of freedom. We set our significance level to 95% and 
            compute the t statistic using the empirical mean and empirical standard 
            deviation of our intake. We use a ddof of 1 to base the computation of our 
            empirical standard deviation on an unbiased estimate of the variance (note:
            the final estimate is not unbiased due to the concave nature of the square 
            root).
    
            >>> np.mean(intake)
            6753.636363636364
            >>> intake.std(ddof=1)
            1142.1232221373727
            >>> t = (np.mean(intake)-7725)/(intake.std(ddof=1)/np.sqrt(len(intake)))
            >>> t
            -2.8207540608310198
    
            We draw 1000000 samples from Student's t distribution with the adequate
            degrees of freedom.
    
            >>> import matplotlib.pyplot as plt
            >>> s = np.random.standard_t(10, size=1000000)
            >>> h = plt.hist(s, bins=100, density=True)
    
            Does our t statistic land in one of the two critical regions found at 
            both tails of the distribution?
    
            >>> np.sum(np.abs(t) < np.abs(s)) / float(len(s))
            0.018318  #random < 0.05, statistic is in critical region
    
            The probability value for this 2-tailed test is about 1.83%, which is 
            lower than the 5% pre-determined significance threshold. 
    
            Therefore, the probability of observing values as extreme as our intake
            conditionally on the null hypothesis being true is too low, and we reject 
            the null hypothesis of no deviation.
    """
    pass

def triangular(left, mode, right, size=None): # real signature unknown; restored from __doc__
    """
    triangular(left, mode, right, size=None)
    
            Draw samples from the triangular distribution over the
            interval ``[left, right]``.
    
            The triangular distribution is a continuous probability
            distribution with lower limit left, peak at mode, and upper
            limit right. Unlike the other distributions, these parameters
            directly define the shape of the pdf.
    
            .. note::
                New code should use the `~numpy.random.Generator.triangular`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            left : float or array_like of floats
                Lower limit.
            mode : float or array_like of floats
                The value where the peak of the distribution occurs.
                The value must fulfill the condition ``left <= mode <= right``.
            right : float or array_like of floats
                Upper limit, must be larger than `left`.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``left``, ``mode``, and ``right``
                are all scalars.  Otherwise, ``np.broadcast(left, mode, right).size``
                samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized triangular distribution.
    
            See Also
            --------
            random.Generator.triangular: which should be used for new code.
    
            Notes
            -----
            The probability density function for the triangular distribution is
    
            .. math:: P(x;l, m, r) = \begin{cases}
                      \frac{2(x-l)}{(r-l)(m-l)}& \text{for $l \leq x \leq m$},\\
                      \frac{2(r-x)}{(r-l)(r-m)}& \text{for $m \leq x \leq r$},\\
                      0& \text{otherwise}.
                      \end{cases}
    
            The triangular distribution is often used in ill-defined
            problems where the underlying distribution is not known, but
            some knowledge of the limits and mode exists. Often it is used
            in simulations.
    
            References
            ----------
            .. [1] Wikipedia, "Triangular distribution"
                   https://en.wikipedia.org/wiki/Triangular_distribution
    
            Examples
            --------
            Draw values from the distribution and plot the histogram:
    
            >>> import matplotlib.pyplot as plt
            >>> h = plt.hist(np.random.triangular(-3, 0, 8, 100000), bins=200,
            ...              density=True)
            >>> plt.show()
    """
    pass

def uniform(low=0.0, high=1.0, size=None): # real signature unknown; restored from __doc__
    """
    uniform(low=0.0, high=1.0, size=None)
    
            Draw samples from a uniform distribution.
    
            Samples are uniformly distributed over the half-open interval
            ``[low, high)`` (includes low, but excludes high).  In other words,
            any value within the given interval is equally likely to be drawn
            by `uniform`.
    
            .. note::
                New code should use the `~numpy.random.Generator.uniform`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            low : float or array_like of floats, optional
                Lower boundary of the output interval.  All values generated will be
                greater than or equal to low.  The default value is 0.
            high : float or array_like of floats
                Upper boundary of the output interval.  All values generated will be
                less than or equal to high.  The high limit may be included in the 
                returned array of floats due to floating-point rounding in the 
                equation ``low + (high-low) * random_sample()``.  The default value 
                is 1.0.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``low`` and ``high`` are both scalars.
                Otherwise, ``np.broadcast(low, high).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized uniform distribution.
    
            See Also
            --------
            randint : Discrete uniform distribution, yielding integers.
            random_integers : Discrete uniform distribution over the closed
                              interval ``[low, high]``.
            random_sample : Floats uniformly distributed over ``[0, 1)``.
            random : Alias for `random_sample`.
            rand : Convenience function that accepts dimensions as input, e.g.,
                   ``rand(2,2)`` would generate a 2-by-2 array of floats,
                   uniformly distributed over ``[0, 1)``.
            random.Generator.uniform: which should be used for new code.
    
            Notes
            -----
            The probability density function of the uniform distribution is
    
            .. math:: p(x) = \frac{1}{b - a}
    
            anywhere within the interval ``[a, b)``, and zero elsewhere.
    
            When ``high`` == ``low``, values of ``low`` will be returned.
            If ``high`` < ``low``, the results are officially undefined
            and may eventually raise an error, i.e. do not rely on this
            function to behave when passed arguments satisfying that
            inequality condition. The ``high`` limit may be included in the
            returned array of floats due to floating-point rounding in the
            equation ``low + (high-low) * random_sample()``. For example:
    
            >>> x = np.float32(5*0.99999999)
            >>> x
            5.0
    
    
            Examples
            --------
            Draw samples from the distribution:
    
            >>> s = np.random.uniform(-1,0,1000)
    
            All values are within the given interval:
    
            >>> np.all(s >= -1)
            True
            >>> np.all(s < 0)
            True
    
            Display the histogram of the samples, along with the
            probability density function:
    
            >>> import matplotlib.pyplot as plt
            >>> count, bins, ignored = plt.hist(s, 15, density=True)
            >>> plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
            >>> plt.show()
    """
    pass

def vonmises(mu, kappa, size=None): # real signature unknown; restored from __doc__
    """
    vonmises(mu, kappa, size=None)
    
            Draw samples from a von Mises distribution.
    
            Samples are drawn from a von Mises distribution with specified mode
            (mu) and dispersion (kappa), on the interval [-pi, pi].
    
            The von Mises distribution (also known as the circular normal
            distribution) is a continuous probability distribution on the unit
            circle.  It may be thought of as the circular analogue of the normal
            distribution.
    
            .. note::
                New code should use the `~numpy.random.Generator.vonmises`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            mu : float or array_like of floats
                Mode ("center") of the distribution.
            kappa : float or array_like of floats
                Dispersion of the distribution, has to be >=0.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``mu`` and ``kappa`` are both scalars.
                Otherwise, ``np.broadcast(mu, kappa).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized von Mises distribution.
    
            See Also
            --------
            scipy.stats.vonmises : probability density function, distribution, or
                cumulative density function, etc.
            random.Generator.vonmises: which should be used for new code.
    
            Notes
            -----
            The probability density for the von Mises distribution is
    
            .. math:: p(x) = \frac{e^{\kappa cos(x-\mu)}}{2\pi I_0(\kappa)},
    
            where :math:`\mu` is the mode and :math:`\kappa` the dispersion,
            and :math:`I_0(\kappa)` is the modified Bessel function of order 0.
    
            The von Mises is named for Richard Edler von Mises, who was born in
            Austria-Hungary, in what is now the Ukraine.  He fled to the United
            States in 1939 and became a professor at Harvard.  He worked in
            probability theory, aerodynamics, fluid mechanics, and philosophy of
            science.
    
            References
            ----------
            .. [1] Abramowitz, M. and Stegun, I. A. (Eds.). "Handbook of
                   Mathematical Functions with Formulas, Graphs, and Mathematical
                   Tables, 9th printing," New York: Dover, 1972.
            .. [2] von Mises, R., "Mathematical Theory of Probability
                   and Statistics", New York: Academic Press, 1964.
    
            Examples
            --------
            Draw samples from the distribution:
    
            >>> mu, kappa = 0.0, 4.0 # mean and dispersion
            >>> s = np.random.vonmises(mu, kappa, 1000)
    
            Display the histogram of the samples, along with
            the probability density function:
    
            >>> import matplotlib.pyplot as plt
            >>> from scipy.special import i0  # doctest: +SKIP
            >>> plt.hist(s, 50, density=True)
            >>> x = np.linspace(-np.pi, np.pi, num=51)
            >>> y = np.exp(kappa*np.cos(x-mu))/(2*np.pi*i0(kappa))  # doctest: +SKIP
            >>> plt.plot(x, y, linewidth=2, color='r')  # doctest: +SKIP
            >>> plt.show()
    """
    pass

def wald(mean, scale, size=None): # real signature unknown; restored from __doc__
    """
    wald(mean, scale, size=None)
    
            Draw samples from a Wald, or inverse Gaussian, distribution.
    
            As the scale approaches infinity, the distribution becomes more like a
            Gaussian. Some references claim that the Wald is an inverse Gaussian
            with mean equal to 1, but this is by no means universal.
    
            The inverse Gaussian distribution was first studied in relationship to
            Brownian motion. In 1956 M.C.K. Tweedie used the name inverse Gaussian
            because there is an inverse relationship between the time to cover a
            unit distance and distance covered in unit time.
    
            .. note::
                New code should use the `~numpy.random.Generator.wald`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            mean : float or array_like of floats
                Distribution mean, must be > 0.
            scale : float or array_like of floats
                Scale parameter, must be > 0.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``mean`` and ``scale`` are both scalars.
                Otherwise, ``np.broadcast(mean, scale).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized Wald distribution.
    
            See Also
            --------
            random.Generator.wald: which should be used for new code.
    
            Notes
            -----
            The probability density function for the Wald distribution is
    
            .. math:: P(x;mean,scale) = \sqrt{\frac{scale}{2\pi x^3}}e^
                                        \frac{-scale(x-mean)^2}{2\cdotp mean^2x}
    
            As noted above the inverse Gaussian distribution first arise
            from attempts to model Brownian motion. It is also a
            competitor to the Weibull for use in reliability modeling and
            modeling stock returns and interest rate processes.
    
            References
            ----------
            .. [1] Brighton Webs Ltd., Wald Distribution,
                   https://web.archive.org/web/20090423014010/http://www.brighton-webs.co.uk:80/distributions/wald.asp
            .. [2] Chhikara, Raj S., and Folks, J. Leroy, "The Inverse Gaussian
                   Distribution: Theory : Methodology, and Applications", CRC Press,
                   1988.
            .. [3] Wikipedia, "Inverse Gaussian distribution"
                   https://en.wikipedia.org/wiki/Inverse_Gaussian_distribution
    
            Examples
            --------
            Draw values from the distribution and plot the histogram:
    
            >>> import matplotlib.pyplot as plt
            >>> h = plt.hist(np.random.wald(3, 2, 100000), bins=200, density=True)
            >>> plt.show()
    """
    pass

def weibull(a, size=None): # real signature unknown; restored from __doc__
    """
    weibull(a, size=None)
    
            Draw samples from a Weibull distribution.
    
            Draw samples from a 1-parameter Weibull distribution with the given
            shape parameter `a`.
    
            .. math:: X = (-ln(U))^{1/a}
    
            Here, U is drawn from the uniform distribution over (0,1].
    
            The more common 2-parameter Weibull, including a scale parameter
            :math:`\lambda` is just :math:`X = \lambda(-ln(U))^{1/a}`.
    
            .. note::
                New code should use the `~numpy.random.Generator.weibull`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            a : float or array_like of floats
                Shape parameter of the distribution.  Must be nonnegative.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``a`` is a scalar.  Otherwise,
                ``np.array(a).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized Weibull distribution.
    
            See Also
            --------
            scipy.stats.weibull_max
            scipy.stats.weibull_min
            scipy.stats.genextreme
            gumbel
            random.Generator.weibull: which should be used for new code.
    
            Notes
            -----
            The Weibull (or Type III asymptotic extreme value distribution
            for smallest values, SEV Type III, or Rosin-Rammler
            distribution) is one of a class of Generalized Extreme Value
            (GEV) distributions used in modeling extreme value problems.
            This class includes the Gumbel and Frechet distributions.
    
            The probability density for the Weibull distribution is
    
            .. math:: p(x) = \frac{a}
                             {\lambda}(\frac{x}{\lambda})^{a-1}e^{-(x/\lambda)^a},
    
            where :math:`a` is the shape and :math:`\lambda` the scale.
    
            The function has its peak (the mode) at
            :math:`\lambda(\frac{a-1}{a})^{1/a}`.
    
            When ``a = 1``, the Weibull distribution reduces to the exponential
            distribution.
    
            References
            ----------
            .. [1] Waloddi Weibull, Royal Technical University, Stockholm,
                   1939 "A Statistical Theory Of The Strength Of Materials",
                   Ingeniorsvetenskapsakademiens Handlingar Nr 151, 1939,
                   Generalstabens Litografiska Anstalts Forlag, Stockholm.
            .. [2] Waloddi Weibull, "A Statistical Distribution Function of
                   Wide Applicability", Journal Of Applied Mechanics ASME Paper
                   1951.
            .. [3] Wikipedia, "Weibull distribution",
                   https://en.wikipedia.org/wiki/Weibull_distribution
    
            Examples
            --------
            Draw samples from the distribution:
    
            >>> a = 5. # shape
            >>> s = np.random.weibull(a, 1000)
    
            Display the histogram of the samples, along with
            the probability density function:
    
            >>> import matplotlib.pyplot as plt
            >>> x = np.arange(1,100.)/50.
            >>> def weib(x,n,a):
            ...     return (a / n) * (x / n)**(a - 1) * np.exp(-(x / n)**a)
    
            >>> count, bins, ignored = plt.hist(np.random.weibull(5.,1000))
            >>> x = np.arange(1,100.)/50.
            >>> scale = count.max()/weib(x, 1., 5.).max()
            >>> plt.plot(x, weib(x, 1., 5.)*scale)
            >>> plt.show()
    """
    pass

def zipf(a, size=None): # real signature unknown; restored from __doc__
    """
    zipf(a, size=None)
    
            Draw samples from a Zipf distribution.
    
            Samples are drawn from a Zipf distribution with specified parameter
            `a` > 1.
    
            The Zipf distribution (also known as the zeta distribution) is a
            discrete probability distribution that satisfies Zipf's law: the
            frequency of an item is inversely proportional to its rank in a
            frequency table.
    
            .. note::
                New code should use the `~numpy.random.Generator.zipf`
                method of a `~numpy.random.Generator` instance instead;
                please see the :ref:`random-quick-start`.
    
            Parameters
            ----------
            a : float or array_like of floats
                Distribution parameter. Must be greater than 1.
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                a single value is returned if ``a`` is a scalar. Otherwise,
                ``np.array(a).size`` samples are drawn.
    
            Returns
            -------
            out : ndarray or scalar
                Drawn samples from the parameterized Zipf distribution.
    
            See Also
            --------
            scipy.stats.zipf : probability density function, distribution, or
                cumulative density function, etc.
            random.Generator.zipf: which should be used for new code.
    
            Notes
            -----
            The probability density for the Zipf distribution is
    
            .. math:: p(k) = \frac{k^{-a}}{\zeta(a)},
    
            for integers :math:`k \geq 1`, where :math:`\zeta` is the Riemann Zeta
            function.
    
            It is named for the American linguist George Kingsley Zipf, who noted
            that the frequency of any word in a sample of a language is inversely
            proportional to its rank in the frequency table.
    
            References
            ----------
            .. [1] Zipf, G. K., "Selected Studies of the Principle of Relative
                   Frequency in Language," Cambridge, MA: Harvard Univ. Press,
                   1932.
    
            Examples
            --------
            Draw samples from the distribution:
    
            >>> a = 4.0
            >>> n = 20000
            >>> s = np.random.zipf(a, n)
    
            Display the histogram of the samples, along with
            the expected histogram based on the probability
            density function:
    
            >>> import matplotlib.pyplot as plt
            >>> from scipy.special import zeta  # doctest: +SKIP
    
            `bincount` provides a fast histogram for small integers.
    
            >>> count = np.bincount(s)
            >>> k = np.arange(1, s.max() + 1)
    
            >>> plt.bar(k, count[1:], alpha=0.5, label='sample count')
            >>> plt.plot(k, n*(k**-a)/zeta(a), 'k.-', alpha=0.5,
            ...          label='expected count')   # doctest: +SKIP
            >>> plt.semilogy()
            >>> plt.grid(alpha=0.4)
            >>> plt.legend()
            >>> plt.title(f'Zipf sample, a={a}, size={n}')
            >>> plt.show()
    """
    pass

# classes

class RandomState(object):
    """
    RandomState(seed=None)
    
        Container for the slow Mersenne Twister pseudo-random number generator.
        Consider using a different BitGenerator with the Generator container
        instead.
    
        `RandomState` and `Generator` expose a number of methods for generating
        random numbers drawn from a variety of probability distributions. In
        addition to the distribution-specific arguments, each method takes a
        keyword argument `size` that defaults to ``None``. If `size` is ``None``,
        then a single value is generated and returned. If `size` is an integer,
        then a 1-D array filled with generated values is returned. If `size` is a
        tuple, then an array with that shape is filled and returned.
    
        **Compatibility Guarantee**
    
        A fixed bit generator using a fixed seed and a fixed series of calls to
        'RandomState' methods using the same parameters will always produce the
        same results up to roundoff error except when the values were incorrect.
        `RandomState` is effectively frozen and will only receive updates that
        are required by changes in the internals of Numpy. More substantial
        changes, including algorithmic improvements, are reserved for
        `Generator`.
    
        Parameters
        ----------
        seed : {None, int, array_like, BitGenerator}, optional
            Random seed used to initialize the pseudo-random number generator or
            an instantized BitGenerator.  If an integer or array, used as a seed for
            the MT19937 BitGenerator. Values can be any integer between 0 and
            2**32 - 1 inclusive, an array (or other sequence) of such integers,
            or ``None`` (the default).  If `seed` is ``None``, then the `MT19937`
            BitGenerator is initialized by reading data from ``/dev/urandom``
            (or the Windows analogue) if available or seed from the clock
            otherwise.
    
        Notes
        -----
        The Python stdlib module "random" also contains a Mersenne Twister
        pseudo-random number generator with a number of methods that are similar
        to the ones available in `RandomState`. `RandomState`, besides being
        NumPy-aware, has the advantage that it provides a much larger number
        of probability distributions to choose from.
    
        See Also
        --------
        Generator
        MT19937
        numpy.random.BitGenerator
    """
    def beta(self, a, b, size=None): # real signature unknown; restored from __doc__
        """
        beta(a, b, size=None)
        
                Draw samples from a Beta distribution.
        
                The Beta distribution is a special case of the Dirichlet distribution,
                and is related to the Gamma distribution.  It has the probability
                distribution function
        
                .. math:: f(x; a,b) = \frac{1}{B(\alpha, \beta)} x^{\alpha - 1}
                                                                 (1 - x)^{\beta - 1},
        
                where the normalization, B, is the beta function,
        
                .. math:: B(\alpha, \beta) = \int_0^1 t^{\alpha - 1}
                                             (1 - t)^{\beta - 1} dt.
        
                It is often seen in Bayesian inference and order statistics.
        
                .. note::
                    New code should use the `~numpy.random.Generator.beta`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
        
                Parameters
                ----------
                a : float or array_like of floats
                    Alpha, positive (>0).
                b : float or array_like of floats
                    Beta, positive (>0).
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``a`` and ``b`` are both scalars.
                    Otherwise, ``np.broadcast(a, b).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized beta distribution.
        
                See Also
                --------
                random.Generator.beta: which should be used for new code.
        """
        pass

    def binomial(self, n, p, size=None): # real signature unknown; restored from __doc__
        """
        binomial(n, p, size=None)
        
                Draw samples from a binomial distribution.
        
                Samples are drawn from a binomial distribution with specified
                parameters, n trials and p probability of success where
                n an integer >= 0 and p is in the interval [0,1]. (n may be
                input as a float, but it is truncated to an integer in use)
        
                .. note::
                    New code should use the `~numpy.random.Generator.binomial`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                n : int or array_like of ints
                    Parameter of the distribution, >= 0. Floats are also accepted,
                    but they will be truncated to integers.
                p : float or array_like of floats
                    Parameter of the distribution, >= 0 and <=1.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``n`` and ``p`` are both scalars.
                    Otherwise, ``np.broadcast(n, p).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized binomial distribution, where
                    each sample is equal to the number of successes over the n trials.
        
                See Also
                --------
                scipy.stats.binom : probability density function, distribution or
                    cumulative density function, etc.
                random.Generator.binomial: which should be used for new code.
        
                Notes
                -----
                The probability density for the binomial distribution is
        
                .. math:: P(N) = \binom{n}{N}p^N(1-p)^{n-N},
        
                where :math:`n` is the number of trials, :math:`p` is the probability
                of success, and :math:`N` is the number of successes.
        
                When estimating the standard error of a proportion in a population by
                using a random sample, the normal distribution works well unless the
                product p*n <=5, where p = population proportion estimate, and n =
                number of samples, in which case the binomial distribution is used
                instead. For example, a sample of 15 people shows 4 who are left
                handed, and 11 who are right handed. Then p = 4/15 = 27%. 0.27*15 = 4,
                so the binomial distribution should be used in this case.
        
                References
                ----------
                .. [1] Dalgaard, Peter, "Introductory Statistics with R",
                       Springer-Verlag, 2002.
                .. [2] Glantz, Stanton A. "Primer of Biostatistics.", McGraw-Hill,
                       Fifth Edition, 2002.
                .. [3] Lentner, Marvin, "Elementary Applied Statistics", Bogden
                       and Quigley, 1972.
                .. [4] Weisstein, Eric W. "Binomial Distribution." From MathWorld--A
                       Wolfram Web Resource.
                       http://mathworld.wolfram.com/BinomialDistribution.html
                .. [5] Wikipedia, "Binomial distribution",
                       https://en.wikipedia.org/wiki/Binomial_distribution
        
                Examples
                --------
                Draw samples from the distribution:
        
                >>> n, p = 10, .5  # number of trials, probability of each trial
                >>> s = np.random.binomial(n, p, 1000)
                # result of flipping a coin 10 times, tested 1000 times.
        
                A real world example. A company drills 9 wild-cat oil exploration
                wells, each with an estimated probability of success of 0.1. All nine
                wells fail. What is the probability of that happening?
        
                Let's do 20,000 trials of the model, and count the number that
                generate zero positive results.
        
                >>> sum(np.random.binomial(9, 0.1, 20000) == 0)/20000.
                # answer = 0.38885, or 38%.
        """
        pass

    def bytes(self, length): # real signature unknown; restored from __doc__
        """
        bytes(length)
        
                Return random bytes.
        
                .. note::
                    New code should use the `~numpy.random.Generator.bytes`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                length : int
                    Number of random bytes.
        
                Returns
                -------
                out : bytes
                    String of length `length`.
        
                See Also
                --------
                random.Generator.bytes: which should be used for new code.
        
                Examples
                --------
                >>> np.random.bytes(10)
                b' eh\x85\x022SZ\xbf\xa4' #random
        """
        pass

    def chisquare(self, df, size=None): # real signature unknown; restored from __doc__
        """
        chisquare(df, size=None)
        
                Draw samples from a chi-square distribution.
        
                When `df` independent random variables, each with standard normal
                distributions (mean 0, variance 1), are squared and summed, the
                resulting distribution is chi-square (see Notes).  This distribution
                is often used in hypothesis testing.
        
                .. note::
                    New code should use the `~numpy.random.Generator.chisquare`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                df : float or array_like of floats
                     Number of degrees of freedom, must be > 0.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``df`` is a scalar.  Otherwise,
                    ``np.array(df).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized chi-square distribution.
        
                Raises
                ------
                ValueError
                    When `df` <= 0 or when an inappropriate `size` (e.g. ``size=-1``)
                    is given.
        
                See Also
                --------
                random.Generator.chisquare: which should be used for new code.
        
                Notes
                -----
                The variable obtained by summing the squares of `df` independent,
                standard normally distributed random variables:
        
                .. math:: Q = \sum_{i=0}^{\mathtt{df}} X^2_i
        
                is chi-square distributed, denoted
        
                .. math:: Q \sim \chi^2_k.
        
                The probability density function of the chi-squared distribution is
        
                .. math:: p(x) = \frac{(1/2)^{k/2}}{\Gamma(k/2)}
                                 x^{k/2 - 1} e^{-x/2},
        
                where :math:`\Gamma` is the gamma function,
        
                .. math:: \Gamma(x) = \int_0^{-\infty} t^{x - 1} e^{-t} dt.
        
                References
                ----------
                .. [1] NIST "Engineering Statistics Handbook"
                       https://www.itl.nist.gov/div898/handbook/eda/section3/eda3666.htm
        
                Examples
                --------
                >>> np.random.chisquare(2,4)
                array([ 1.89920014,  9.00867716,  3.13710533,  5.62318272]) # random
        """
        pass

    def choice(self, a, size=None, replace=True, p=None): # real signature unknown; restored from __doc__
        """
        choice(a, size=None, replace=True, p=None)
        
                Generates a random sample from a given 1-D array
        
                .. versionadded:: 1.7.0
        
                .. note::
                    New code should use the `~numpy.random.Generator.choice`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                a : 1-D array-like or int
                    If an ndarray, a random sample is generated from its elements.
                    If an int, the random sample is generated as if it were ``np.arange(a)``
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  Default is None, in which case a
                    single value is returned.
                replace : boolean, optional
                    Whether the sample is with or without replacement. Default is True,
                    meaning that a value of ``a`` can be selected multiple times.
                p : 1-D array-like, optional
                    The probabilities associated with each entry in a.
                    If not given, the sample assumes a uniform distribution over all
                    entries in ``a``.
        
                Returns
                -------
                samples : single item or ndarray
                    The generated random samples
        
                Raises
                ------
                ValueError
                    If a is an int and less than zero, if a or p are not 1-dimensional,
                    if a is an array-like of size 0, if p is not a vector of
                    probabilities, if a and p have different lengths, or if
                    replace=False and the sample size is greater than the population
                    size
        
                See Also
                --------
                randint, shuffle, permutation
                random.Generator.choice: which should be used in new code
        
                Notes
                -----
                Setting user-specified probabilities through ``p`` uses a more general but less
                efficient sampler than the default. The general sampler produces a different sample
                than the optimized sampler even if each element of ``p`` is 1 / len(a).
        
                Sampling random rows from a 2-D array is not possible with this function,
                but is possible with `Generator.choice` through its ``axis`` keyword.
        
                Examples
                --------
                Generate a uniform random sample from np.arange(5) of size 3:
        
                >>> np.random.choice(5, 3)
                array([0, 3, 4]) # random
                >>> #This is equivalent to np.random.randint(0,5,3)
        
                Generate a non-uniform random sample from np.arange(5) of size 3:
        
                >>> np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0])
                array([3, 3, 0]) # random
        
                Generate a uniform random sample from np.arange(5) of size 3 without
                replacement:
        
                >>> np.random.choice(5, 3, replace=False)
                array([3,1,0]) # random
                >>> #This is equivalent to np.random.permutation(np.arange(5))[:3]
        
                Generate a non-uniform random sample from np.arange(5) of size
                3 without replacement:
        
                >>> np.random.choice(5, 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0])
                array([2, 3, 0]) # random
        
                Any of the above can be repeated with an arbitrary array-like
                instead of just integers. For instance:
        
                >>> aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
                >>> np.random.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3])
                array(['pooh', 'pooh', 'pooh', 'Christopher', 'piglet'], # random
                      dtype='<U11')
        """
        pass

    def dirichlet(self, alpha, size=None): # real signature unknown; restored from __doc__
        """
        dirichlet(alpha, size=None)
        
                Draw samples from the Dirichlet distribution.
        
                Draw `size` samples of dimension k from a Dirichlet distribution. A
                Dirichlet-distributed random variable can be seen as a multivariate
                generalization of a Beta distribution. The Dirichlet distribution
                is a conjugate prior of a multinomial distribution in Bayesian
                inference.
        
                .. note::
                    New code should use the `~numpy.random.Generator.dirichlet`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                alpha : sequence of floats, length k
                    Parameter of the distribution (length ``k`` for sample of
                    length ``k``).
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n)``, then
                    ``m * n * k`` samples are drawn.  Default is None, in which case a
                    vector of length ``k`` is returned.
        
                Returns
                -------
                samples : ndarray,
                    The drawn samples, of shape ``(size, k)``.
        
                Raises
                ------
                ValueError
                    If any value in ``alpha`` is less than or equal to zero
        
                See Also
                --------
                random.Generator.dirichlet: which should be used for new code.
        
                Notes
                -----
                The Dirichlet distribution is a distribution over vectors
                :math:`x` that fulfil the conditions :math:`x_i>0` and
                :math:`\sum_{i=1}^k x_i = 1`.
        
                The probability density function :math:`p` of a
                Dirichlet-distributed random vector :math:`X` is
                proportional to
        
                .. math:: p(x) \propto \prod_{i=1}^{k}{x^{\alpha_i-1}_i},
        
                where :math:`\alpha` is a vector containing the positive
                concentration parameters.
        
                The method uses the following property for computation: let :math:`Y`
                be a random vector which has components that follow a standard gamma
                distribution, then :math:`X = \frac{1}{\sum_{i=1}^k{Y_i}} Y`
                is Dirichlet-distributed
        
                References
                ----------
                .. [1] David McKay, "Information Theory, Inference and Learning
                       Algorithms," chapter 23,
                       http://www.inference.org.uk/mackay/itila/
                .. [2] Wikipedia, "Dirichlet distribution",
                       https://en.wikipedia.org/wiki/Dirichlet_distribution
        
                Examples
                --------
                Taking an example cited in Wikipedia, this distribution can be used if
                one wanted to cut strings (each of initial length 1.0) into K pieces
                with different lengths, where each piece had, on average, a designated
                average length, but allowing some variation in the relative sizes of
                the pieces.
        
                >>> s = np.random.dirichlet((10, 5, 3), 20).transpose()
        
                >>> import matplotlib.pyplot as plt
                >>> plt.barh(range(20), s[0])
                >>> plt.barh(range(20), s[1], left=s[0], color='g')
                >>> plt.barh(range(20), s[2], left=s[0]+s[1], color='r')
                >>> plt.title("Lengths of Strings")
        """
        pass

    def exponential(self, scale=1.0, size=None): # real signature unknown; restored from __doc__
        """
        exponential(scale=1.0, size=None)
        
                Draw samples from an exponential distribution.
        
                Its probability density function is
        
                .. math:: f(x; \frac{1}{\beta}) = \frac{1}{\beta} \exp(-\frac{x}{\beta}),
        
                for ``x > 0`` and 0 elsewhere. :math:`\beta` is the scale parameter,
                which is the inverse of the rate parameter :math:`\lambda = 1/\beta`.
                The rate parameter is an alternative, widely used parameterization
                of the exponential distribution [3]_.
        
                The exponential distribution is a continuous analogue of the
                geometric distribution.  It describes many common situations, such as
                the size of raindrops measured over many rainstorms [1]_, or the time
                between page requests to Wikipedia [2]_.
        
                .. note::
                    New code should use the `~numpy.random.Generator.exponential`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                scale : float or array_like of floats
                    The scale parameter, :math:`\beta = 1/\lambda`. Must be
                    non-negative.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``scale`` is a scalar.  Otherwise,
                    ``np.array(scale).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized exponential distribution.
        
                See Also
                --------
                random.Generator.exponential: which should be used for new code.
        
                References
                ----------
                .. [1] Peyton Z. Peebles Jr., "Probability, Random Variables and
                       Random Signal Principles", 4th ed, 2001, p. 57.
                .. [2] Wikipedia, "Poisson process",
                       https://en.wikipedia.org/wiki/Poisson_process
                .. [3] Wikipedia, "Exponential distribution",
                       https://en.wikipedia.org/wiki/Exponential_distribution
        """
        pass

    def f(self, dfnum, dfden, size=None): # real signature unknown; restored from __doc__
        """
        f(dfnum, dfden, size=None)
        
                Draw samples from an F distribution.
        
                Samples are drawn from an F distribution with specified parameters,
                `dfnum` (degrees of freedom in numerator) and `dfden` (degrees of
                freedom in denominator), where both parameters must be greater than
                zero.
        
                The random variate of the F distribution (also known as the
                Fisher distribution) is a continuous probability distribution
                that arises in ANOVA tests, and is the ratio of two chi-square
                variates.
        
                .. note::
                    New code should use the `~numpy.random.Generator.f`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                dfnum : float or array_like of floats
                    Degrees of freedom in numerator, must be > 0.
                dfden : float or array_like of float
                    Degrees of freedom in denominator, must be > 0.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``dfnum`` and ``dfden`` are both scalars.
                    Otherwise, ``np.broadcast(dfnum, dfden).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized Fisher distribution.
        
                See Also
                --------
                scipy.stats.f : probability density function, distribution or
                    cumulative density function, etc.
                random.Generator.f: which should be used for new code.
        
                Notes
                -----
                The F statistic is used to compare in-group variances to between-group
                variances. Calculating the distribution depends on the sampling, and
                so it is a function of the respective degrees of freedom in the
                problem.  The variable `dfnum` is the number of samples minus one, the
                between-groups degrees of freedom, while `dfden` is the within-groups
                degrees of freedom, the sum of the number of samples in each group
                minus the number of groups.
        
                References
                ----------
                .. [1] Glantz, Stanton A. "Primer of Biostatistics.", McGraw-Hill,
                       Fifth Edition, 2002.
                .. [2] Wikipedia, "F-distribution",
                       https://en.wikipedia.org/wiki/F-distribution
        
                Examples
                --------
                An example from Glantz[1], pp 47-40:
        
                Two groups, children of diabetics (25 people) and children from people
                without diabetes (25 controls). Fasting blood glucose was measured,
                case group had a mean value of 86.1, controls had a mean value of
                82.2. Standard deviations were 2.09 and 2.49 respectively. Are these
                data consistent with the null hypothesis that the parents diabetic
                status does not affect their children's blood glucose levels?
                Calculating the F statistic from the data gives a value of 36.01.
        
                Draw samples from the distribution:
        
                >>> dfnum = 1. # between group degrees of freedom
                >>> dfden = 48. # within groups degrees of freedom
                >>> s = np.random.f(dfnum, dfden, 1000)
        
                The lower bound for the top 1% of the samples is :
        
                >>> np.sort(s)[-10]
                7.61988120985 # random
        
                So there is about a 1% chance that the F statistic will exceed 7.62,
                the measured value is 36, so the null hypothesis is rejected at the 1%
                level.
        """
        pass

    def gamma(self, shape, scale=1.0, size=None): # real signature unknown; restored from __doc__
        """
        gamma(shape, scale=1.0, size=None)
        
                Draw samples from a Gamma distribution.
        
                Samples are drawn from a Gamma distribution with specified parameters,
                `shape` (sometimes designated "k") and `scale` (sometimes designated
                "theta"), where both parameters are > 0.
        
                .. note::
                    New code should use the `~numpy.random.Generator.gamma`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                shape : float or array_like of floats
                    The shape of the gamma distribution. Must be non-negative.
                scale : float or array_like of floats, optional
                    The scale of the gamma distribution. Must be non-negative.
                    Default is equal to 1.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``shape`` and ``scale`` are both scalars.
                    Otherwise, ``np.broadcast(shape, scale).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized gamma distribution.
        
                See Also
                --------
                scipy.stats.gamma : probability density function, distribution or
                    cumulative density function, etc.
                random.Generator.gamma: which should be used for new code.
        
                Notes
                -----
                The probability density for the Gamma distribution is
        
                .. math:: p(x) = x^{k-1}\frac{e^{-x/\theta}}{\theta^k\Gamma(k)},
        
                where :math:`k` is the shape and :math:`\theta` the scale,
                and :math:`\Gamma` is the Gamma function.
        
                The Gamma distribution is often used to model the times to failure of
                electronic components, and arises naturally in processes for which the
                waiting times between Poisson distributed events are relevant.
        
                References
                ----------
                .. [1] Weisstein, Eric W. "Gamma Distribution." From MathWorld--A
                       Wolfram Web Resource.
                       http://mathworld.wolfram.com/GammaDistribution.html
                .. [2] Wikipedia, "Gamma distribution",
                       https://en.wikipedia.org/wiki/Gamma_distribution
        
                Examples
                --------
                Draw samples from the distribution:
        
                >>> shape, scale = 2., 2.  # mean=4, std=2*sqrt(2)
                >>> s = np.random.gamma(shape, scale, 1000)
        
                Display the histogram of the samples, along with
                the probability density function:
        
                >>> import matplotlib.pyplot as plt
                >>> import scipy.special as sps  # doctest: +SKIP
                >>> count, bins, ignored = plt.hist(s, 50, density=True)
                >>> y = bins**(shape-1)*(np.exp(-bins/scale) /  # doctest: +SKIP
                ...                      (sps.gamma(shape)*scale**shape))
                >>> plt.plot(bins, y, linewidth=2, color='r')  # doctest: +SKIP
                >>> plt.show()
        """
        pass

    def geometric(self, p, size=None): # real signature unknown; restored from __doc__
        """
        geometric(p, size=None)
        
                Draw samples from the geometric distribution.
        
                Bernoulli trials are experiments with one of two outcomes:
                success or failure (an example of such an experiment is flipping
                a coin).  The geometric distribution models the number of trials
                that must be run in order to achieve success.  It is therefore
                supported on the positive integers, ``k = 1, 2, ...``.
        
                The probability mass function of the geometric distribution is
        
                .. math:: f(k) = (1 - p)^{k - 1} p
        
                where `p` is the probability of success of an individual trial.
        
                .. note::
                    New code should use the `~numpy.random.Generator.geometric`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                p : float or array_like of floats
                    The probability of success of an individual trial.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``p`` is a scalar.  Otherwise,
                    ``np.array(p).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized geometric distribution.
        
                See Also
                --------
                random.Generator.geometric: which should be used for new code.
        
                Examples
                --------
                Draw ten thousand values from the geometric distribution,
                with the probability of an individual success equal to 0.35:
        
                >>> z = np.random.geometric(p=0.35, size=10000)
        
                How many trials succeeded after a single run?
        
                >>> (z == 1).sum() / 10000.
                0.34889999999999999 #random
        """
        pass

    def get_state(self, legacy=True): # real signature unknown; restored from __doc__
        """
        get_state(legacy=True)
        
                Return a tuple representing the internal state of the generator.
        
                For more details, see `set_state`.
        
                Parameters
                ----------
                legacy : bool, optional
                    Flag indicating to return a legacy tuple state when the BitGenerator
                    is MT19937, instead of a dict. Raises ValueError if the underlying
                    bit generator is not an instance of MT19937.
        
                Returns
                -------
                out : {tuple(str, ndarray of 624 uints, int, int, float), dict}
                    If legacy is True, the returned tuple has the following items:
        
                    1. the string 'MT19937'.
                    2. a 1-D array of 624 unsigned integer keys.
                    3. an integer ``pos``.
                    4. an integer ``has_gauss``.
                    5. a float ``cached_gaussian``.
        
                    If `legacy` is False, or the BitGenerator is not MT19937, then
                    state is returned as a dictionary.
        
                See Also
                --------
                set_state
        
                Notes
                -----
                `set_state` and `get_state` are not needed to work with any of the
                random distributions in NumPy. If the internal state is manually altered,
                the user should know exactly what he/she is doing.
        """
        pass

    def gumbel(self, loc=0.0, scale=1.0, size=None): # real signature unknown; restored from __doc__
        """
        gumbel(loc=0.0, scale=1.0, size=None)
        
                Draw samples from a Gumbel distribution.
        
                Draw samples from a Gumbel distribution with specified location and
                scale.  For more information on the Gumbel distribution, see
                Notes and References below.
        
                .. note::
                    New code should use the `~numpy.random.Generator.gumbel`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                loc : float or array_like of floats, optional
                    The location of the mode of the distribution. Default is 0.
                scale : float or array_like of floats, optional
                    The scale parameter of the distribution. Default is 1. Must be non-
                    negative.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``loc`` and ``scale`` are both scalars.
                    Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized Gumbel distribution.
        
                See Also
                --------
                scipy.stats.gumbel_l
                scipy.stats.gumbel_r
                scipy.stats.genextreme
                weibull
                random.Generator.gumbel: which should be used for new code.
        
                Notes
                -----
                The Gumbel (or Smallest Extreme Value (SEV) or the Smallest Extreme
                Value Type I) distribution is one of a class of Generalized Extreme
                Value (GEV) distributions used in modeling extreme value problems.
                The Gumbel is a special case of the Extreme Value Type I distribution
                for maximums from distributions with "exponential-like" tails.
        
                The probability density for the Gumbel distribution is
        
                .. math:: p(x) = \frac{e^{-(x - \mu)/ \beta}}{\beta} e^{ -e^{-(x - \mu)/
                          \beta}},
        
                where :math:`\mu` is the mode, a location parameter, and
                :math:`\beta` is the scale parameter.
        
                The Gumbel (named for German mathematician Emil Julius Gumbel) was used
                very early in the hydrology literature, for modeling the occurrence of
                flood events. It is also used for modeling maximum wind speed and
                rainfall rates.  It is a "fat-tailed" distribution - the probability of
                an event in the tail of the distribution is larger than if one used a
                Gaussian, hence the surprisingly frequent occurrence of 100-year
                floods. Floods were initially modeled as a Gaussian process, which
                underestimated the frequency of extreme events.
        
                It is one of a class of extreme value distributions, the Generalized
                Extreme Value (GEV) distributions, which also includes the Weibull and
                Frechet.
        
                The function has a mean of :math:`\mu + 0.57721\beta` and a variance
                of :math:`\frac{\pi^2}{6}\beta^2`.
        
                References
                ----------
                .. [1] Gumbel, E. J., "Statistics of Extremes,"
                       New York: Columbia University Press, 1958.
                .. [2] Reiss, R.-D. and Thomas, M., "Statistical Analysis of Extreme
                       Values from Insurance, Finance, Hydrology and Other Fields,"
                       Basel: Birkhauser Verlag, 2001.
        
                Examples
                --------
                Draw samples from the distribution:
        
                >>> mu, beta = 0, 0.1 # location and scale
                >>> s = np.random.gumbel(mu, beta, 1000)
        
                Display the histogram of the samples, along with
                the probability density function:
        
                >>> import matplotlib.pyplot as plt
                >>> count, bins, ignored = plt.hist(s, 30, density=True)
                >>> plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
                ...          * np.exp( -np.exp( -(bins - mu) /beta) ),
                ...          linewidth=2, color='r')
                >>> plt.show()
        
                Show how an extreme value distribution can arise from a Gaussian process
                and compare to a Gaussian:
        
                >>> means = []
                >>> maxima = []
                >>> for i in range(0,1000) :
                ...    a = np.random.normal(mu, beta, 1000)
                ...    means.append(a.mean())
                ...    maxima.append(a.max())
                >>> count, bins, ignored = plt.hist(maxima, 30, density=True)
                >>> beta = np.std(maxima) * np.sqrt(6) / np.pi
                >>> mu = np.mean(maxima) - 0.57721*beta
                >>> plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
                ...          * np.exp(-np.exp(-(bins - mu)/beta)),
                ...          linewidth=2, color='r')
                >>> plt.plot(bins, 1/(beta * np.sqrt(2 * np.pi))
                ...          * np.exp(-(bins - mu)**2 / (2 * beta**2)),
                ...          linewidth=2, color='g')
                >>> plt.show()
        """
        pass

    def hypergeometric(self, ngood, nbad, nsample, size=None): # real signature unknown; restored from __doc__
        """
        hypergeometric(ngood, nbad, nsample, size=None)
        
                Draw samples from a Hypergeometric distribution.
        
                Samples are drawn from a hypergeometric distribution with specified
                parameters, `ngood` (ways to make a good selection), `nbad` (ways to make
                a bad selection), and `nsample` (number of items sampled, which is less
                than or equal to the sum ``ngood + nbad``).
        
                .. note::
                    New code should use the
                    `~numpy.random.Generator.hypergeometric`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                ngood : int or array_like of ints
                    Number of ways to make a good selection.  Must be nonnegative.
                nbad : int or array_like of ints
                    Number of ways to make a bad selection.  Must be nonnegative.
                nsample : int or array_like of ints
                    Number of items sampled.  Must be at least 1 and at most
                    ``ngood + nbad``.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if `ngood`, `nbad`, and `nsample`
                    are all scalars.  Otherwise, ``np.broadcast(ngood, nbad, nsample).size``
                    samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized hypergeometric distribution. Each
                    sample is the number of good items within a randomly selected subset of
                    size `nsample` taken from a set of `ngood` good items and `nbad` bad items.
        
                See Also
                --------
                scipy.stats.hypergeom : probability density function, distribution or
                    cumulative density function, etc.
                random.Generator.hypergeometric: which should be used for new code.
        
                Notes
                -----
                The probability density for the Hypergeometric distribution is
        
                .. math:: P(x) = \frac{\binom{g}{x}\binom{b}{n-x}}{\binom{g+b}{n}},
        
                where :math:`0 \le x \le n` and :math:`n-b \le x \le g`
        
                for P(x) the probability of ``x`` good results in the drawn sample,
                g = `ngood`, b = `nbad`, and n = `nsample`.
        
                Consider an urn with black and white marbles in it, `ngood` of them
                are black and `nbad` are white. If you draw `nsample` balls without
                replacement, then the hypergeometric distribution describes the
                distribution of black balls in the drawn sample.
        
                Note that this distribution is very similar to the binomial
                distribution, except that in this case, samples are drawn without
                replacement, whereas in the Binomial case samples are drawn with
                replacement (or the sample space is infinite). As the sample space
                becomes large, this distribution approaches the binomial.
        
                References
                ----------
                .. [1] Lentner, Marvin, "Elementary Applied Statistics", Bogden
                       and Quigley, 1972.
                .. [2] Weisstein, Eric W. "Hypergeometric Distribution." From
                       MathWorld--A Wolfram Web Resource.
                       http://mathworld.wolfram.com/HypergeometricDistribution.html
                .. [3] Wikipedia, "Hypergeometric distribution",
                       https://en.wikipedia.org/wiki/Hypergeometric_distribution
        
                Examples
                --------
                Draw samples from the distribution:
        
                >>> ngood, nbad, nsamp = 100, 2, 10
                # number of good, number of bad, and number of samples
                >>> s = np.random.hypergeometric(ngood, nbad, nsamp, 1000)
                >>> from matplotlib.pyplot import hist
                >>> hist(s)
                #   note that it is very unlikely to grab both bad items
        
                Suppose you have an urn with 15 white and 15 black marbles.
                If you pull 15 marbles at random, how likely is it that
                12 or more of them are one color?
        
                >>> s = np.random.hypergeometric(15, 15, 15, 100000)
                >>> sum(s>=12)/100000. + sum(s<=3)/100000.
                #   answer = 0.003 ... pretty unlikely!
        """
        pass

    def laplace(self, loc=0.0, scale=1.0, size=None): # real signature unknown; restored from __doc__
        """
        laplace(loc=0.0, scale=1.0, size=None)
        
                Draw samples from the Laplace or double exponential distribution with
                specified location (or mean) and scale (decay).
        
                The Laplace distribution is similar to the Gaussian/normal distribution,
                but is sharper at the peak and has fatter tails. It represents the
                difference between two independent, identically distributed exponential
                random variables.
        
                .. note::
                    New code should use the `~numpy.random.Generator.laplace`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                loc : float or array_like of floats, optional
                    The position, :math:`\mu`, of the distribution peak. Default is 0.
                scale : float or array_like of floats, optional
                    :math:`\lambda`, the exponential decay. Default is 1. Must be non-
                    negative.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``loc`` and ``scale`` are both scalars.
                    Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized Laplace distribution.
        
                See Also
                --------
                random.Generator.laplace: which should be used for new code.
        
                Notes
                -----
                It has the probability density function
        
                .. math:: f(x; \mu, \lambda) = \frac{1}{2\lambda}
                                               \exp\left(-\frac{|x - \mu|}{\lambda}\right).
        
                The first law of Laplace, from 1774, states that the frequency
                of an error can be expressed as an exponential function of the
                absolute magnitude of the error, which leads to the Laplace
                distribution. For many problems in economics and health
                sciences, this distribution seems to model the data better
                than the standard Gaussian distribution.
        
                References
                ----------
                .. [1] Abramowitz, M. and Stegun, I. A. (Eds.). "Handbook of
                       Mathematical Functions with Formulas, Graphs, and Mathematical
                       Tables, 9th printing," New York: Dover, 1972.
                .. [2] Kotz, Samuel, et. al. "The Laplace Distribution and
                       Generalizations, " Birkhauser, 2001.
                .. [3] Weisstein, Eric W. "Laplace Distribution."
                       From MathWorld--A Wolfram Web Resource.
                       http://mathworld.wolfram.com/LaplaceDistribution.html
                .. [4] Wikipedia, "Laplace distribution",
                       https://en.wikipedia.org/wiki/Laplace_distribution
        
                Examples
                --------
                Draw samples from the distribution
        
                >>> loc, scale = 0., 1.
                >>> s = np.random.laplace(loc, scale, 1000)
        
                Display the histogram of the samples, along with
                the probability density function:
        
                >>> import matplotlib.pyplot as plt
                >>> count, bins, ignored = plt.hist(s, 30, density=True)
                >>> x = np.arange(-8., 8., .01)
                >>> pdf = np.exp(-abs(x-loc)/scale)/(2.*scale)
                >>> plt.plot(x, pdf)
        
                Plot Gaussian for comparison:
        
                >>> g = (1/(scale * np.sqrt(2 * np.pi)) *
                ...      np.exp(-(x - loc)**2 / (2 * scale**2)))
                >>> plt.plot(x,g)
        """
        pass

    def logistic(self, loc=0.0, scale=1.0, size=None): # real signature unknown; restored from __doc__
        """
        logistic(loc=0.0, scale=1.0, size=None)
        
                Draw samples from a logistic distribution.
        
                Samples are drawn from a logistic distribution with specified
                parameters, loc (location or mean, also median), and scale (>0).
        
                .. note::
                    New code should use the `~numpy.random.Generator.logistic`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                loc : float or array_like of floats, optional
                    Parameter of the distribution. Default is 0.
                scale : float or array_like of floats, optional
                    Parameter of the distribution. Must be non-negative.
                    Default is 1.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``loc`` and ``scale`` are both scalars.
                    Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized logistic distribution.
        
                See Also
                --------
                scipy.stats.logistic : probability density function, distribution or
                    cumulative density function, etc.
                random.Generator.logistic: which should be used for new code.
        
                Notes
                -----
                The probability density for the Logistic distribution is
        
                .. math:: P(x) = P(x) = \frac{e^{-(x-\mu)/s}}{s(1+e^{-(x-\mu)/s})^2},
        
                where :math:`\mu` = location and :math:`s` = scale.
        
                The Logistic distribution is used in Extreme Value problems where it
                can act as a mixture of Gumbel distributions, in Epidemiology, and by
                the World Chess Federation (FIDE) where it is used in the Elo ranking
                system, assuming the performance of each player is a logistically
                distributed random variable.
        
                References
                ----------
                .. [1] Reiss, R.-D. and Thomas M. (2001), "Statistical Analysis of
                       Extreme Values, from Insurance, Finance, Hydrology and Other
                       Fields," Birkhauser Verlag, Basel, pp 132-133.
                .. [2] Weisstein, Eric W. "Logistic Distribution." From
                       MathWorld--A Wolfram Web Resource.
                       http://mathworld.wolfram.com/LogisticDistribution.html
                .. [3] Wikipedia, "Logistic-distribution",
                       https://en.wikipedia.org/wiki/Logistic_distribution
        
                Examples
                --------
                Draw samples from the distribution:
        
                >>> loc, scale = 10, 1
                >>> s = np.random.logistic(loc, scale, 10000)
                >>> import matplotlib.pyplot as plt
                >>> count, bins, ignored = plt.hist(s, bins=50)
        
                #   plot against distribution
        
                >>> def logist(x, loc, scale):
                ...     return np.exp((loc-x)/scale)/(scale*(1+np.exp((loc-x)/scale))**2)
                >>> lgst_val = logist(bins, loc, scale)
                >>> plt.plot(bins, lgst_val * count.max() / lgst_val.max())
                >>> plt.show()
        """
        pass

    def lognormal(self, mean=0.0, sigma=1.0, size=None): # real signature unknown; restored from __doc__
        """
        lognormal(mean=0.0, sigma=1.0, size=None)
        
                Draw samples from a log-normal distribution.
        
                Draw samples from a log-normal distribution with specified mean,
                standard deviation, and array shape.  Note that the mean and standard
                deviation are not the values for the distribution itself, but of the
                underlying normal distribution it is derived from.
        
                .. note::
                    New code should use the `~numpy.random.Generator.lognormal`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                mean : float or array_like of floats, optional
                    Mean value of the underlying normal distribution. Default is 0.
                sigma : float or array_like of floats, optional
                    Standard deviation of the underlying normal distribution. Must be
                    non-negative. Default is 1.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``mean`` and ``sigma`` are both scalars.
                    Otherwise, ``np.broadcast(mean, sigma).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized log-normal distribution.
        
                See Also
                --------
                scipy.stats.lognorm : probability density function, distribution,
                    cumulative density function, etc.
                random.Generator.lognormal: which should be used for new code.
        
                Notes
                -----
                A variable `x` has a log-normal distribution if `log(x)` is normally
                distributed.  The probability density function for the log-normal
                distribution is:
        
                .. math:: p(x) = \frac{1}{\sigma x \sqrt{2\pi}}
                                 e^{(-\frac{(ln(x)-\mu)^2}{2\sigma^2})}
        
                where :math:`\mu` is the mean and :math:`\sigma` is the standard
                deviation of the normally distributed logarithm of the variable.
                A log-normal distribution results if a random variable is the *product*
                of a large number of independent, identically-distributed variables in
                the same way that a normal distribution results if the variable is the
                *sum* of a large number of independent, identically-distributed
                variables.
        
                References
                ----------
                .. [1] Limpert, E., Stahel, W. A., and Abbt, M., "Log-normal
                       Distributions across the Sciences: Keys and Clues,"
                       BioScience, Vol. 51, No. 5, May, 2001.
                       https://stat.ethz.ch/~stahel/lognormal/bioscience.pdf
                .. [2] Reiss, R.D. and Thomas, M., "Statistical Analysis of Extreme
                       Values," Basel: Birkhauser Verlag, 2001, pp. 31-32.
        
                Examples
                --------
                Draw samples from the distribution:
        
                >>> mu, sigma = 3., 1. # mean and standard deviation
                >>> s = np.random.lognormal(mu, sigma, 1000)
        
                Display the histogram of the samples, along with
                the probability density function:
        
                >>> import matplotlib.pyplot as plt
                >>> count, bins, ignored = plt.hist(s, 100, density=True, align='mid')
        
                >>> x = np.linspace(min(bins), max(bins), 10000)
                >>> pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
                ...        / (x * sigma * np.sqrt(2 * np.pi)))
        
                >>> plt.plot(x, pdf, linewidth=2, color='r')
                >>> plt.axis('tight')
                >>> plt.show()
        
                Demonstrate that taking the products of random samples from a uniform
                distribution can be fit well by a log-normal probability density
                function.
        
                >>> # Generate a thousand samples: each is the product of 100 random
                >>> # values, drawn from a normal distribution.
                >>> b = []
                >>> for i in range(1000):
                ...    a = 10. + np.random.standard_normal(100)
                ...    b.append(np.product(a))
        
                >>> b = np.array(b) / np.min(b) # scale values to be positive
                >>> count, bins, ignored = plt.hist(b, 100, density=True, align='mid')
                >>> sigma = np.std(np.log(b))
                >>> mu = np.mean(np.log(b))
        
                >>> x = np.linspace(min(bins), max(bins), 10000)
                >>> pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
                ...        / (x * sigma * np.sqrt(2 * np.pi)))
        
                >>> plt.plot(x, pdf, color='r', linewidth=2)
                >>> plt.show()
        """
        pass

    def logseries(self, p, size=None): # real signature unknown; restored from __doc__
        """
        logseries(p, size=None)
        
                Draw samples from a logarithmic series distribution.
        
                Samples are drawn from a log series distribution with specified
                shape parameter, 0 <= ``p`` < 1.
        
                .. note::
                    New code should use the `~numpy.random.Generator.logseries`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                p : float or array_like of floats
                    Shape parameter for the distribution.  Must be in the range [0, 1).
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``p`` is a scalar.  Otherwise,
                    ``np.array(p).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized logarithmic series distribution.
        
                See Also
                --------
                scipy.stats.logser : probability density function, distribution or
                    cumulative density function, etc.
                random.Generator.logseries: which should be used for new code.
        
                Notes
                -----
                The probability density for the Log Series distribution is
        
                .. math:: P(k) = \frac{-p^k}{k \ln(1-p)},
        
                where p = probability.
        
                The log series distribution is frequently used to represent species
                richness and occurrence, first proposed by Fisher, Corbet, and
                Williams in 1943 [2].  It may also be used to model the numbers of
                occupants seen in cars [3].
        
                References
                ----------
                .. [1] Buzas, Martin A.; Culver, Stephen J.,  Understanding regional
                       species diversity through the log series distribution of
                       occurrences: BIODIVERSITY RESEARCH Diversity & Distributions,
                       Volume 5, Number 5, September 1999 , pp. 187-195(9).
                .. [2] Fisher, R.A,, A.S. Corbet, and C.B. Williams. 1943. The
                       relation between the number of species and the number of
                       individuals in a random sample of an animal population.
                       Journal of Animal Ecology, 12:42-58.
                .. [3] D. J. Hand, F. Daly, D. Lunn, E. Ostrowski, A Handbook of Small
                       Data Sets, CRC Press, 1994.
                .. [4] Wikipedia, "Logarithmic distribution",
                       https://en.wikipedia.org/wiki/Logarithmic_distribution
        
                Examples
                --------
                Draw samples from the distribution:
        
                >>> a = .6
                >>> s = np.random.logseries(a, 10000)
                >>> import matplotlib.pyplot as plt
                >>> count, bins, ignored = plt.hist(s)
        
                #   plot against distribution
        
                >>> def logseries(k, p):
                ...     return -p**k/(k*np.log(1-p))
                >>> plt.plot(bins, logseries(bins, a)*count.max()/
                ...          logseries(bins, a).max(), 'r')
                >>> plt.show()
        """
        pass

    def multinomial(self, n, pvals, size=None): # real signature unknown; restored from __doc__
        """
        multinomial(n, pvals, size=None)
        
                Draw samples from a multinomial distribution.
        
                The multinomial distribution is a multivariate generalization of the
                binomial distribution.  Take an experiment with one of ``p``
                possible outcomes.  An example of such an experiment is throwing a dice,
                where the outcome can be 1 through 6.  Each sample drawn from the
                distribution represents `n` such experiments.  Its values,
                ``X_i = [X_0, X_1, ..., X_p]``, represent the number of times the
                outcome was ``i``.
        
                .. note::
                    New code should use the `~numpy.random.Generator.multinomial`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                n : int
                    Number of experiments.
                pvals : sequence of floats, length p
                    Probabilities of each of the ``p`` different outcomes.  These
                    must sum to 1 (however, the last element is always assumed to
                    account for the remaining probability, as long as
                    ``sum(pvals[:-1]) <= 1)``.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  Default is None, in which case a
                    single value is returned.
        
                Returns
                -------
                out : ndarray
                    The drawn samples, of shape *size*, if that was provided.  If not,
                    the shape is ``(N,)``.
        
                    In other words, each entry ``out[i,j,...,:]`` is an N-dimensional
                    value drawn from the distribution.
        
                See Also
                --------
                random.Generator.multinomial: which should be used for new code.
        
                Examples
                --------
                Throw a dice 20 times:
        
                >>> np.random.multinomial(20, [1/6.]*6, size=1)
                array([[4, 1, 7, 5, 2, 1]]) # random
        
                It landed 4 times on 1, once on 2, etc.
        
                Now, throw the dice 20 times, and 20 times again:
        
                >>> np.random.multinomial(20, [1/6.]*6, size=2)
                array([[3, 4, 3, 3, 4, 3], # random
                       [2, 4, 3, 4, 0, 7]])
        
                For the first run, we threw 3 times 1, 4 times 2, etc.  For the second,
                we threw 2 times 1, 4 times 2, etc.
        
                A loaded die is more likely to land on number 6:
        
                >>> np.random.multinomial(100, [1/7.]*5 + [2/7.])
                array([11, 16, 14, 17, 16, 26]) # random
        
                The probability inputs should be normalized. As an implementation
                detail, the value of the last entry is ignored and assumed to take
                up any leftover probability mass, but this should not be relied on.
                A biased coin which has twice as much weight on one side as on the
                other should be sampled like so:
        
                >>> np.random.multinomial(100, [1.0 / 3, 2.0 / 3])  # RIGHT
                array([38, 62]) # random
        
                not like:
        
                >>> np.random.multinomial(100, [1.0, 2.0])  # WRONG
                Traceback (most recent call last):
                ValueError: pvals < 0, pvals > 1 or pvals contains NaNs
        """
        pass

    def multivariate_normal(self, mean, cov, size=None, check_valid='warn', tol=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        multivariate_normal(mean, cov, size=None, check_valid='warn', tol=1e-8)
        
                Draw random samples from a multivariate normal distribution.
        
                The multivariate normal, multinormal or Gaussian distribution is a
                generalization of the one-dimensional normal distribution to higher
                dimensions.  Such a distribution is specified by its mean and
                covariance matrix.  These parameters are analogous to the mean
                (average or "center") and variance (standard deviation, or "width,"
                squared) of the one-dimensional normal distribution.
        
                .. note::
                    New code should use the
                    `~numpy.random.Generator.multivariate_normal`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                mean : 1-D array_like, of length N
                    Mean of the N-dimensional distribution.
                cov : 2-D array_like, of shape (N, N)
                    Covariance matrix of the distribution. It must be symmetric and
                    positive-semidefinite for proper sampling.
                size : int or tuple of ints, optional
                    Given a shape of, for example, ``(m,n,k)``, ``m*n*k`` samples are
                    generated, and packed in an `m`-by-`n`-by-`k` arrangement.  Because
                    each sample is `N`-dimensional, the output shape is ``(m,n,k,N)``.
                    If no shape is specified, a single (`N`-D) sample is returned.
                check_valid : { 'warn', 'raise', 'ignore' }, optional
                    Behavior when the covariance matrix is not positive semidefinite.
                tol : float, optional
                    Tolerance when checking the singular values in covariance matrix.
                    cov is cast to double before the check.
        
                Returns
                -------
                out : ndarray
                    The drawn samples, of shape *size*, if that was provided.  If not,
                    the shape is ``(N,)``.
        
                    In other words, each entry ``out[i,j,...,:]`` is an N-dimensional
                    value drawn from the distribution.
        
                See Also
                --------
                random.Generator.multivariate_normal: which should be used for new code.
        
                Notes
                -----
                The mean is a coordinate in N-dimensional space, which represents the
                location where samples are most likely to be generated.  This is
                analogous to the peak of the bell curve for the one-dimensional or
                univariate normal distribution.
        
                Covariance indicates the level to which two variables vary together.
                From the multivariate normal distribution, we draw N-dimensional
                samples, :math:`X = [x_1, x_2, ... x_N]`.  The covariance matrix
                element :math:`C_{ij}` is the covariance of :math:`x_i` and :math:`x_j`.
                The element :math:`C_{ii}` is the variance of :math:`x_i` (i.e. its
                "spread").
        
                Instead of specifying the full covariance matrix, popular
                approximations include:
        
                  - Spherical covariance (`cov` is a multiple of the identity matrix)
                  - Diagonal covariance (`cov` has non-negative elements, and only on
                    the diagonal)
        
                This geometrical property can be seen in two dimensions by plotting
                generated data-points:
        
                >>> mean = [0, 0]
                >>> cov = [[1, 0], [0, 100]]  # diagonal covariance
        
                Diagonal covariance means that points are oriented along x or y-axis:
        
                >>> import matplotlib.pyplot as plt
                >>> x, y = np.random.multivariate_normal(mean, cov, 5000).T
                >>> plt.plot(x, y, 'x')
                >>> plt.axis('equal')
                >>> plt.show()
        
                Note that the covariance matrix must be positive semidefinite (a.k.a.
                nonnegative-definite). Otherwise, the behavior of this method is
                undefined and backwards compatibility is not guaranteed.
        
                References
                ----------
                .. [1] Papoulis, A., "Probability, Random Variables, and Stochastic
                       Processes," 3rd ed., New York: McGraw-Hill, 1991.
                .. [2] Duda, R. O., Hart, P. E., and Stork, D. G., "Pattern
                       Classification," 2nd ed., New York: Wiley, 2001.
        
                Examples
                --------
                >>> mean = (1, 2)
                >>> cov = [[1, 0], [0, 1]]
                >>> x = np.random.multivariate_normal(mean, cov, (3, 3))
                >>> x.shape
                (3, 3, 2)
        
                Here we generate 800 samples from the bivariate normal distribution
                with mean [0, 0] and covariance matrix [[6, -3], [-3, 3.5]].  The
                expected variances of the first and second components of the sample
                are 6 and 3.5, respectively, and the expected correlation
                coefficient is -3/sqrt(6*3.5) ≈ -0.65465.
        
                >>> cov = np.array([[6, -3], [-3, 3.5]])
                >>> pts = np.random.multivariate_normal([0, 0], cov, size=800)
        
                Check that the mean, covariance, and correlation coefficient of the
                sample are close to the expected values:
        
                >>> pts.mean(axis=0)
                array([ 0.0326911 , -0.01280782])  # may vary
                >>> np.cov(pts.T)
                array([[ 5.96202397, -2.85602287],
                       [-2.85602287,  3.47613949]])  # may vary
                >>> np.corrcoef(pts.T)[0, 1]
                -0.6273591314603949  # may vary
        
                We can visualize this data with a scatter plot.  The orientation
                of the point cloud illustrates the negative correlation of the
                components of this sample.
        
                >>> import matplotlib.pyplot as plt
                >>> plt.plot(pts[:, 0], pts[:, 1], '.', alpha=0.5)
                >>> plt.axis('equal')
                >>> plt.grid()
                >>> plt.show()
        """
        pass

    def negative_binomial(self, n, p, size=None): # real signature unknown; restored from __doc__
        """
        negative_binomial(n, p, size=None)
        
                Draw samples from a negative binomial distribution.
        
                Samples are drawn from a negative binomial distribution with specified
                parameters, `n` successes and `p` probability of success where `n`
                is > 0 and `p` is in the interval [0, 1].
        
                .. note::
                    New code should use the
                    `~numpy.random.Generator.negative_binomial`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                n : float or array_like of floats
                    Parameter of the distribution, > 0.
                p : float or array_like of floats
                    Parameter of the distribution, >= 0 and <=1.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``n`` and ``p`` are both scalars.
                    Otherwise, ``np.broadcast(n, p).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized negative binomial distribution,
                    where each sample is equal to N, the number of failures that
                    occurred before a total of n successes was reached.
        
                See Also
                --------
                random.Generator.negative_binomial: which should be used for new code.
        
                Notes
                -----
                The probability mass function of the negative binomial distribution is
        
                .. math:: P(N;n,p) = \frac{\Gamma(N+n)}{N!\Gamma(n)}p^{n}(1-p)^{N},
        
                where :math:`n` is the number of successes, :math:`p` is the
                probability of success, :math:`N+n` is the number of trials, and
                :math:`\Gamma` is the gamma function. When :math:`n` is an integer,
                :math:`\frac{\Gamma(N+n)}{N!\Gamma(n)} = \binom{N+n-1}{N}`, which is
                the more common form of this term in the pmf. The negative
                binomial distribution gives the probability of N failures given n
                successes, with a success on the last trial.
        
                If one throws a die repeatedly until the third time a "1" appears,
                then the probability distribution of the number of non-"1"s that
                appear before the third "1" is a negative binomial distribution.
        
                References
                ----------
                .. [1] Weisstein, Eric W. "Negative Binomial Distribution." From
                       MathWorld--A Wolfram Web Resource.
                       http://mathworld.wolfram.com/NegativeBinomialDistribution.html
                .. [2] Wikipedia, "Negative binomial distribution",
                       https://en.wikipedia.org/wiki/Negative_binomial_distribution
        
                Examples
                --------
                Draw samples from the distribution:
        
                A real world example. A company drills wild-cat oil
                exploration wells, each with an estimated probability of
                success of 0.1.  What is the probability of having one success
                for each successive well, that is what is the probability of a
                single success after drilling 5 wells, after 6 wells, etc.?
        
                >>> s = np.random.negative_binomial(1, 0.1, 100000)
                >>> for i in range(1, 11): # doctest: +SKIP
                ...    probability = sum(s<i) / 100000.
                ...    print(i, "wells drilled, probability of one success =", probability)
        """
        pass

    def noncentral_chisquare(self, df, nonc, size=None): # real signature unknown; restored from __doc__
        """
        noncentral_chisquare(df, nonc, size=None)
        
                Draw samples from a noncentral chi-square distribution.
        
                The noncentral :math:`\chi^2` distribution is a generalization of
                the :math:`\chi^2` distribution.
        
                .. note::
                    New code should use the
                    `~numpy.random.Generator.noncentral_chisquare`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                df : float or array_like of floats
                    Degrees of freedom, must be > 0.
        
                    .. versionchanged:: 1.10.0
                       Earlier NumPy versions required dfnum > 1.
                nonc : float or array_like of floats
                    Non-centrality, must be non-negative.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``df`` and ``nonc`` are both scalars.
                    Otherwise, ``np.broadcast(df, nonc).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized noncentral chi-square distribution.
        
                See Also
                --------
                random.Generator.noncentral_chisquare: which should be used for new code.
        
                Notes
                -----
                The probability density function for the noncentral Chi-square
                distribution is
        
                .. math:: P(x;df,nonc) = \sum^{\infty}_{i=0}
                                       \frac{e^{-nonc/2}(nonc/2)^{i}}{i!}
                                       P_{Y_{df+2i}}(x),
        
                where :math:`Y_{q}` is the Chi-square with q degrees of freedom.
        
                References
                ----------
                .. [1] Wikipedia, "Noncentral chi-squared distribution"
                       https://en.wikipedia.org/wiki/Noncentral_chi-squared_distribution
        
                Examples
                --------
                Draw values from the distribution and plot the histogram
        
                >>> import matplotlib.pyplot as plt
                >>> values = plt.hist(np.random.noncentral_chisquare(3, 20, 100000),
                ...                   bins=200, density=True)
                >>> plt.show()
        
                Draw values from a noncentral chisquare with very small noncentrality,
                and compare to a chisquare.
        
                >>> plt.figure()
                >>> values = plt.hist(np.random.noncentral_chisquare(3, .0000001, 100000),
                ...                   bins=np.arange(0., 25, .1), density=True)
                >>> values2 = plt.hist(np.random.chisquare(3, 100000),
                ...                    bins=np.arange(0., 25, .1), density=True)
                >>> plt.plot(values[1][0:-1], values[0]-values2[0], 'ob')
                >>> plt.show()
        
                Demonstrate how large values of non-centrality lead to a more symmetric
                distribution.
        
                >>> plt.figure()
                >>> values = plt.hist(np.random.noncentral_chisquare(3, 20, 100000),
                ...                   bins=200, density=True)
                >>> plt.show()
        """
        pass

    def noncentral_f(self, dfnum, dfden, nonc, size=None): # real signature unknown; restored from __doc__
        """
        noncentral_f(dfnum, dfden, nonc, size=None)
        
                Draw samples from the noncentral F distribution.
        
                Samples are drawn from an F distribution with specified parameters,
                `dfnum` (degrees of freedom in numerator) and `dfden` (degrees of
                freedom in denominator), where both parameters > 1.
                `nonc` is the non-centrality parameter.
        
                .. note::
                    New code should use the
                    `~numpy.random.Generator.noncentral_f`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                dfnum : float or array_like of floats
                    Numerator degrees of freedom, must be > 0.
        
                    .. versionchanged:: 1.14.0
                       Earlier NumPy versions required dfnum > 1.
                dfden : float or array_like of floats
                    Denominator degrees of freedom, must be > 0.
                nonc : float or array_like of floats
                    Non-centrality parameter, the sum of the squares of the numerator
                    means, must be >= 0.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``dfnum``, ``dfden``, and ``nonc``
                    are all scalars.  Otherwise, ``np.broadcast(dfnum, dfden, nonc).size``
                    samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized noncentral Fisher distribution.
        
                See Also
                --------
                random.Generator.noncentral_f: which should be used for new code.
        
                Notes
                -----
                When calculating the power of an experiment (power = probability of
                rejecting the null hypothesis when a specific alternative is true) the
                non-central F statistic becomes important.  When the null hypothesis is
                true, the F statistic follows a central F distribution. When the null
                hypothesis is not true, then it follows a non-central F statistic.
        
                References
                ----------
                .. [1] Weisstein, Eric W. "Noncentral F-Distribution."
                       From MathWorld--A Wolfram Web Resource.
                       http://mathworld.wolfram.com/NoncentralF-Distribution.html
                .. [2] Wikipedia, "Noncentral F-distribution",
                       https://en.wikipedia.org/wiki/Noncentral_F-distribution
        
                Examples
                --------
                In a study, testing for a specific alternative to the null hypothesis
                requires use of the Noncentral F distribution. We need to calculate the
                area in the tail of the distribution that exceeds the value of the F
                distribution for the null hypothesis.  We'll plot the two probability
                distributions for comparison.
        
                >>> dfnum = 3 # between group deg of freedom
                >>> dfden = 20 # within groups degrees of freedom
                >>> nonc = 3.0
                >>> nc_vals = np.random.noncentral_f(dfnum, dfden, nonc, 1000000)
                >>> NF = np.histogram(nc_vals, bins=50, density=True)
                >>> c_vals = np.random.f(dfnum, dfden, 1000000)
                >>> F = np.histogram(c_vals, bins=50, density=True)
                >>> import matplotlib.pyplot as plt
                >>> plt.plot(F[1][1:], F[0])
                >>> plt.plot(NF[1][1:], NF[0])
                >>> plt.show()
        """
        pass

    def normal(self, loc=0.0, scale=1.0, size=None): # real signature unknown; restored from __doc__
        """
        normal(loc=0.0, scale=1.0, size=None)
        
                Draw random samples from a normal (Gaussian) distribution.
        
                The probability density function of the normal distribution, first
                derived by De Moivre and 200 years later by both Gauss and Laplace
                independently [2]_, is often called the bell curve because of
                its characteristic shape (see the example below).
        
                The normal distributions occurs often in nature.  For example, it
                describes the commonly occurring distribution of samples influenced
                by a large number of tiny, random disturbances, each with its own
                unique distribution [2]_.
        
                .. note::
                    New code should use the `~numpy.random.Generator.normal`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                loc : float or array_like of floats
                    Mean ("centre") of the distribution.
                scale : float or array_like of floats
                    Standard deviation (spread or "width") of the distribution. Must be
                    non-negative.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``loc`` and ``scale`` are both scalars.
                    Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized normal distribution.
        
                See Also
                --------
                scipy.stats.norm : probability density function, distribution or
                    cumulative density function, etc.
                random.Generator.normal: which should be used for new code.
        
                Notes
                -----
                The probability density for the Gaussian distribution is
        
                .. math:: p(x) = \frac{1}{\sqrt{ 2 \pi \sigma^2 }}
                                 e^{ - \frac{ (x - \mu)^2 } {2 \sigma^2} },
        
                where :math:`\mu` is the mean and :math:`\sigma` the standard
                deviation. The square of the standard deviation, :math:`\sigma^2`,
                is called the variance.
        
                The function has its peak at the mean, and its "spread" increases with
                the standard deviation (the function reaches 0.607 times its maximum at
                :math:`x + \sigma` and :math:`x - \sigma` [2]_).  This implies that
                normal is more likely to return samples lying close to the mean, rather
                than those far away.
        
                References
                ----------
                .. [1] Wikipedia, "Normal distribution",
                       https://en.wikipedia.org/wiki/Normal_distribution
                .. [2] P. R. Peebles Jr., "Central Limit Theorem" in "Probability,
                       Random Variables and Random Signal Principles", 4th ed., 2001,
                       pp. 51, 51, 125.
        
                Examples
                --------
                Draw samples from the distribution:
        
                >>> mu, sigma = 0, 0.1 # mean and standard deviation
                >>> s = np.random.normal(mu, sigma, 1000)
        
                Verify the mean and the variance:
        
                >>> abs(mu - np.mean(s))
                0.0  # may vary
        
                >>> abs(sigma - np.std(s, ddof=1))
                0.1  # may vary
        
                Display the histogram of the samples, along with
                the probability density function:
        
                >>> import matplotlib.pyplot as plt
                >>> count, bins, ignored = plt.hist(s, 30, density=True)
                >>> plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
                ...                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
                ...          linewidth=2, color='r')
                >>> plt.show()
        
                Two-by-four array of samples from the normal distribution with
                mean 3 and standard deviation 2.5:
        
                >>> np.random.normal(3, 2.5, size=(2, 4))
                array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
                       [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random
        """
        pass

    def pareto(self, a, size=None): # real signature unknown; restored from __doc__
        """
        pareto(a, size=None)
        
                Draw samples from a Pareto II or Lomax distribution with
                specified shape.
        
                The Lomax or Pareto II distribution is a shifted Pareto
                distribution. The classical Pareto distribution can be
                obtained from the Lomax distribution by adding 1 and
                multiplying by the scale parameter ``m`` (see Notes).  The
                smallest value of the Lomax distribution is zero while for the
                classical Pareto distribution it is ``mu``, where the standard
                Pareto distribution has location ``mu = 1``.  Lomax can also
                be considered as a simplified version of the Generalized
                Pareto distribution (available in SciPy), with the scale set
                to one and the location set to zero.
        
                The Pareto distribution must be greater than zero, and is
                unbounded above.  It is also known as the "80-20 rule".  In
                this distribution, 80 percent of the weights are in the lowest
                20 percent of the range, while the other 20 percent fill the
                remaining 80 percent of the range.
        
                .. note::
                    New code should use the `~numpy.random.Generator.pareto`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                a : float or array_like of floats
                    Shape of the distribution. Must be positive.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``a`` is a scalar.  Otherwise,
                    ``np.array(a).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized Pareto distribution.
        
                See Also
                --------
                scipy.stats.lomax : probability density function, distribution or
                    cumulative density function, etc.
                scipy.stats.genpareto : probability density function, distribution or
                    cumulative density function, etc.
                random.Generator.pareto: which should be used for new code.
        
                Notes
                -----
                The probability density for the Pareto distribution is
        
                .. math:: p(x) = \frac{am^a}{x^{a+1}}
        
                where :math:`a` is the shape and :math:`m` the scale.
        
                The Pareto distribution, named after the Italian economist
                Vilfredo Pareto, is a power law probability distribution
                useful in many real world problems.  Outside the field of
                economics it is generally referred to as the Bradford
                distribution. Pareto developed the distribution to describe
                the distribution of wealth in an economy.  It has also found
                use in insurance, web page access statistics, oil field sizes,
                and many other problems, including the download frequency for
                projects in Sourceforge [1]_.  It is one of the so-called
                "fat-tailed" distributions.
        
                References
                ----------
                .. [1] Francis Hunt and Paul Johnson, On the Pareto Distribution of
                       Sourceforge projects.
                .. [2] Pareto, V. (1896). Course of Political Economy. Lausanne.
                .. [3] Reiss, R.D., Thomas, M.(2001), Statistical Analysis of Extreme
                       Values, Birkhauser Verlag, Basel, pp 23-30.
                .. [4] Wikipedia, "Pareto distribution",
                       https://en.wikipedia.org/wiki/Pareto_distribution
        
                Examples
                --------
                Draw samples from the distribution:
        
                >>> a, m = 3., 2.  # shape and mode
                >>> s = (np.random.pareto(a, 1000) + 1) * m
        
                Display the histogram of the samples, along with the probability
                density function:
        
                >>> import matplotlib.pyplot as plt
                >>> count, bins, _ = plt.hist(s, 100, density=True)
                >>> fit = a*m**a / bins**(a+1)
                >>> plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='r')
                >>> plt.show()
        """
        pass

    def permutation(self, x): # real signature unknown; restored from __doc__
        """
        permutation(x)
        
                Randomly permute a sequence, or return a permuted range.
        
                If `x` is a multi-dimensional array, it is only shuffled along its
                first index.
        
                .. note::
                    New code should use the
                    `~numpy.random.Generator.permutation`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                x : int or array_like
                    If `x` is an integer, randomly permute ``np.arange(x)``.
                    If `x` is an array, make a copy and shuffle the elements
                    randomly.
        
                Returns
                -------
                out : ndarray
                    Permuted sequence or array range.
        
                See Also
                --------
                random.Generator.permutation: which should be used for new code.
        
                Examples
                --------
                >>> np.random.permutation(10)
                array([1, 7, 4, 3, 0, 9, 2, 5, 8, 6]) # random
        
                >>> np.random.permutation([1, 4, 9, 12, 15])
                array([15,  1,  9,  4, 12]) # random
        
                >>> arr = np.arange(9).reshape((3, 3))
                >>> np.random.permutation(arr)
                array([[6, 7, 8], # random
                       [0, 1, 2],
                       [3, 4, 5]])
        """
        pass

    def poisson(self, lam=1.0, size=None): # real signature unknown; restored from __doc__
        """
        poisson(lam=1.0, size=None)
        
                Draw samples from a Poisson distribution.
        
                The Poisson distribution is the limit of the binomial distribution
                for large N.
        
                .. note::
                    New code should use the `~numpy.random.Generator.poisson`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                lam : float or array_like of floats
                    Expected number of events occurring in a fixed-time interval,
                    must be >= 0. A sequence must be broadcastable over the requested
                    size.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``lam`` is a scalar. Otherwise,
                    ``np.array(lam).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized Poisson distribution.
        
                See Also
                --------
                random.Generator.poisson: which should be used for new code.
        
                Notes
                -----
                The Poisson distribution
        
                .. math:: f(k; \lambda)=\frac{\lambda^k e^{-\lambda}}{k!}
        
                For events with an expected separation :math:`\lambda` the Poisson
                distribution :math:`f(k; \lambda)` describes the probability of
                :math:`k` events occurring within the observed
                interval :math:`\lambda`.
        
                Because the output is limited to the range of the C int64 type, a
                ValueError is raised when `lam` is within 10 sigma of the maximum
                representable value.
        
                References
                ----------
                .. [1] Weisstein, Eric W. "Poisson Distribution."
                       From MathWorld--A Wolfram Web Resource.
                       http://mathworld.wolfram.com/PoissonDistribution.html
                .. [2] Wikipedia, "Poisson distribution",
                       https://en.wikipedia.org/wiki/Poisson_distribution
        
                Examples
                --------
                Draw samples from the distribution:
        
                >>> import numpy as np
                >>> s = np.random.poisson(5, 10000)
        
                Display histogram of the sample:
        
                >>> import matplotlib.pyplot as plt
                >>> count, bins, ignored = plt.hist(s, 14, density=True)
                >>> plt.show()
        
                Draw each 100 values for lambda 100 and 500:
        
                >>> s = np.random.poisson(lam=(100., 500.), size=(100, 2))
        """
        pass

    def power(self, a, size=None): # real signature unknown; restored from __doc__
        """
        power(a, size=None)
        
                Draws samples in [0, 1] from a power distribution with positive
                exponent a - 1.
        
                Also known as the power function distribution.
        
                .. note::
                    New code should use the `~numpy.random.Generator.power`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                a : float or array_like of floats
                    Parameter of the distribution. Must be non-negative.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``a`` is a scalar.  Otherwise,
                    ``np.array(a).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized power distribution.
        
                Raises
                ------
                ValueError
                    If a <= 0.
        
                See Also
                --------
                random.Generator.power: which should be used for new code.
        
                Notes
                -----
                The probability density function is
        
                .. math:: P(x; a) = ax^{a-1}, 0 \le x \le 1, a>0.
        
                The power function distribution is just the inverse of the Pareto
                distribution. It may also be seen as a special case of the Beta
                distribution.
        
                It is used, for example, in modeling the over-reporting of insurance
                claims.
        
                References
                ----------
                .. [1] Christian Kleiber, Samuel Kotz, "Statistical size distributions
                       in economics and actuarial sciences", Wiley, 2003.
                .. [2] Heckert, N. A. and Filliben, James J. "NIST Handbook 148:
                       Dataplot Reference Manual, Volume 2: Let Subcommands and Library
                       Functions", National Institute of Standards and Technology
                       Handbook Series, June 2003.
                       https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/powpdf.pdf
        
                Examples
                --------
                Draw samples from the distribution:
        
                >>> a = 5. # shape
                >>> samples = 1000
                >>> s = np.random.power(a, samples)
        
                Display the histogram of the samples, along with
                the probability density function:
        
                >>> import matplotlib.pyplot as plt
                >>> count, bins, ignored = plt.hist(s, bins=30)
                >>> x = np.linspace(0, 1, 100)
                >>> y = a*x**(a-1.)
                >>> normed_y = samples*np.diff(bins)[0]*y
                >>> plt.plot(x, normed_y)
                >>> plt.show()
        
                Compare the power function distribution to the inverse of the Pareto.
        
                >>> from scipy import stats # doctest: +SKIP
                >>> rvs = np.random.power(5, 1000000)
                >>> rvsp = np.random.pareto(5, 1000000)
                >>> xx = np.linspace(0,1,100)
                >>> powpdf = stats.powerlaw.pdf(xx,5)  # doctest: +SKIP
        
                >>> plt.figure()
                >>> plt.hist(rvs, bins=50, density=True)
                >>> plt.plot(xx,powpdf,'r-')  # doctest: +SKIP
                >>> plt.title('np.random.power(5)')
        
                >>> plt.figure()
                >>> plt.hist(1./(1.+rvsp), bins=50, density=True)
                >>> plt.plot(xx,powpdf,'r-')  # doctest: +SKIP
                >>> plt.title('inverse of 1 + np.random.pareto(5)')
        
                >>> plt.figure()
                >>> plt.hist(1./(1.+rvsp), bins=50, density=True)
                >>> plt.plot(xx,powpdf,'r-')  # doctest: +SKIP
                >>> plt.title('inverse of stats.pareto(5)')
        """
        pass

    def rand(self, d0, d1, *more, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        rand(d0, d1, ..., dn)
        
                Random values in a given shape.
        
                .. note::
                    This is a convenience function for users porting code from Matlab,
                    and wraps `random_sample`. That function takes a
                    tuple to specify the size of the output, which is consistent with
                    other NumPy functions like `numpy.zeros` and `numpy.ones`.
        
                Create an array of the given shape and populate it with
                random samples from a uniform distribution
                over ``[0, 1)``.
        
                Parameters
                ----------
                d0, d1, ..., dn : int, optional
                    The dimensions of the returned array, must be non-negative.
                    If no argument is given a single Python float is returned.
        
                Returns
                -------
                out : ndarray, shape ``(d0, d1, ..., dn)``
                    Random values.
        
                See Also
                --------
                random
        
                Examples
                --------
                >>> np.random.rand(3,2)
                array([[ 0.14022471,  0.96360618],  #random
                       [ 0.37601032,  0.25528411],  #random
                       [ 0.49313049,  0.94909878]]) #random
        """
        pass

    def randint(self, low, high=None, size=None, dtype=None): # real signature unknown; restored from __doc__
        """
        randint(low, high=None, size=None, dtype=int)
        
                Return random integers from `low` (inclusive) to `high` (exclusive).
        
                Return random integers from the "discrete uniform" distribution of
                the specified dtype in the "half-open" interval [`low`, `high`). If
                `high` is None (the default), then results are from [0, `low`).
        
                .. note::
                    New code should use the `~numpy.random.Generator.randint`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                low : int or array-like of ints
                    Lowest (signed) integers to be drawn from the distribution (unless
                    ``high=None``, in which case this parameter is one above the
                    *highest* such integer).
                high : int or array-like of ints, optional
                    If provided, one above the largest (signed) integer to be drawn
                    from the distribution (see above for behavior if ``high=None``).
                    If array-like, must contain integer values
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  Default is None, in which case a
                    single value is returned.
                dtype : dtype, optional
                    Desired dtype of the result. Byteorder must be native.
                    The default value is int.
        
                    .. versionadded:: 1.11.0
        
                Returns
                -------
                out : int or ndarray of ints
                    `size`-shaped array of random integers from the appropriate
                    distribution, or a single such random int if `size` not provided.
        
                See Also
                --------
                random_integers : similar to `randint`, only for the closed
                    interval [`low`, `high`], and 1 is the lowest value if `high` is
                    omitted.
                random.Generator.integers: which should be used for new code.
        
                Examples
                --------
                >>> np.random.randint(2, size=10)
                array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0]) # random
                >>> np.random.randint(1, size=10)
                array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        
                Generate a 2 x 4 array of ints between 0 and 4, inclusive:
        
                >>> np.random.randint(5, size=(2, 4))
                array([[4, 0, 2, 1], # random
                       [3, 2, 2, 0]])
        
                Generate a 1 x 3 array with 3 different upper bounds
        
                >>> np.random.randint(1, [3, 5, 10])
                array([2, 2, 9]) # random
        
                Generate a 1 by 3 array with 3 different lower bounds
        
                >>> np.random.randint([1, 5, 7], 10)
                array([9, 8, 7]) # random
        
                Generate a 2 by 4 array using broadcasting with dtype of uint8
        
                >>> np.random.randint([1, 3, 5, 7], [[10], [20]], dtype=np.uint8)
                array([[ 8,  6,  9,  7], # random
                       [ 1, 16,  9, 12]], dtype=uint8)
        """
        pass

    def randn(self, d0, d1, *more, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        randn(d0, d1, ..., dn)
        
                Return a sample (or samples) from the "standard normal" distribution.
        
                .. note::
                    This is a convenience function for users porting code from Matlab,
                    and wraps `standard_normal`. That function takes a
                    tuple to specify the size of the output, which is consistent with
                    other NumPy functions like `numpy.zeros` and `numpy.ones`.
        
                .. note::
                    New code should use the
                    `~numpy.random.Generator.standard_normal`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                If positive int_like arguments are provided, `randn` generates an array
                of shape ``(d0, d1, ..., dn)``, filled
                with random floats sampled from a univariate "normal" (Gaussian)
                distribution of mean 0 and variance 1. A single float randomly sampled
                from the distribution is returned if no argument is provided.
        
                Parameters
                ----------
                d0, d1, ..., dn : int, optional
                    The dimensions of the returned array, must be non-negative.
                    If no argument is given a single Python float is returned.
        
                Returns
                -------
                Z : ndarray or float
                    A ``(d0, d1, ..., dn)``-shaped array of floating-point samples from
                    the standard normal distribution, or a single such float if
                    no parameters were supplied.
        
                See Also
                --------
                standard_normal : Similar, but takes a tuple as its argument.
                normal : Also accepts mu and sigma arguments.
                random.Generator.standard_normal: which should be used for new code.
        
                Notes
                -----
                For random samples from the normal distribution with mean ``mu`` and
                standard deviation ``sigma``, use::
        
                    sigma * np.random.randn(...) + mu
        
                Examples
                --------
                >>> np.random.randn()
                2.1923875335537315  # random
        
                Two-by-four array of samples from the normal distribution with
                mean 3 and standard deviation 2.5:
        
                >>> 3 + 2.5 * np.random.randn(2, 4)
                array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
                       [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random
        """
        pass

    def random(self, size=None): # real signature unknown; restored from __doc__
        """
        random(size=None)
        
                Return random floats in the half-open interval [0.0, 1.0). Alias for
                `random_sample` to ease forward-porting to the new random API.
        """
        pass

    def random_integers(self, low, high=None, size=None): # real signature unknown; restored from __doc__
        """
        random_integers(low, high=None, size=None)
        
                Random integers of type `np.int_` between `low` and `high`, inclusive.
        
                Return random integers of type `np.int_` from the "discrete uniform"
                distribution in the closed interval [`low`, `high`].  If `high` is
                None (the default), then results are from [1, `low`]. The `np.int_`
                type translates to the C long integer type and its precision
                is platform dependent.
        
                This function has been deprecated. Use randint instead.
        
                .. deprecated:: 1.11.0
        
                Parameters
                ----------
                low : int
                    Lowest (signed) integer to be drawn from the distribution (unless
                    ``high=None``, in which case this parameter is the *highest* such
                    integer).
                high : int, optional
                    If provided, the largest (signed) integer to be drawn from the
                    distribution (see above for behavior if ``high=None``).
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  Default is None, in which case a
                    single value is returned.
        
                Returns
                -------
                out : int or ndarray of ints
                    `size`-shaped array of random integers from the appropriate
                    distribution, or a single such random int if `size` not provided.
        
                See Also
                --------
                randint : Similar to `random_integers`, only for the half-open
                    interval [`low`, `high`), and 0 is the lowest value if `high` is
                    omitted.
        
                Notes
                -----
                To sample from N evenly spaced floating-point numbers between a and b,
                use::
        
                  a + (b - a) * (np.random.random_integers(N) - 1) / (N - 1.)
        
                Examples
                --------
                >>> np.random.random_integers(5)
                4 # random
                >>> type(np.random.random_integers(5))
                <class 'numpy.int64'>
                >>> np.random.random_integers(5, size=(3,2))
                array([[5, 4], # random
                       [3, 3],
                       [4, 5]])
        
                Choose five random numbers from the set of five evenly-spaced
                numbers between 0 and 2.5, inclusive (*i.e.*, from the set
                :math:`{0, 5/8, 10/8, 15/8, 20/8}`):
        
                >>> 2.5 * (np.random.random_integers(5, size=(5,)) - 1) / 4.
                array([ 0.625,  1.25 ,  0.625,  0.625,  2.5  ]) # random
        
                Roll two six sided dice 1000 times and sum the results:
        
                >>> d1 = np.random.random_integers(1, 6, 1000)
                >>> d2 = np.random.random_integers(1, 6, 1000)
                >>> dsums = d1 + d2
        
                Display results as a histogram:
        
                >>> import matplotlib.pyplot as plt
                >>> count, bins, ignored = plt.hist(dsums, 11, density=True)
                >>> plt.show()
        """
        pass

    def random_sample(self, size=None): # real signature unknown; restored from __doc__
        """
        random_sample(size=None)
        
                Return random floats in the half-open interval [0.0, 1.0).
        
                Results are from the "continuous uniform" distribution over the
                stated interval.  To sample :math:`Unif[a, b), b > a` multiply
                the output of `random_sample` by `(b-a)` and add `a`::
        
                  (b - a) * random_sample() + a
        
                .. note::
                    New code should use the `~numpy.random.Generator.random`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  Default is None, in which case a
                    single value is returned.
        
                Returns
                -------
                out : float or ndarray of floats
                    Array of random floats of shape `size` (unless ``size=None``, in which
                    case a single float is returned).
        
                See Also
                --------
                random.Generator.random: which should be used for new code.
        
                Examples
                --------
                >>> np.random.random_sample()
                0.47108547995356098 # random
                >>> type(np.random.random_sample())
                <class 'float'>
                >>> np.random.random_sample((5,))
                array([ 0.30220482,  0.86820401,  0.1654503 ,  0.11659149,  0.54323428]) # random
        
                Three-by-two array of random numbers from [-5, 0):
        
                >>> 5 * np.random.random_sample((3, 2)) - 5
                array([[-3.99149989, -0.52338984], # random
                       [-2.99091858, -0.79479508],
                       [-1.23204345, -1.75224494]])
        """
        pass

    def rayleigh(self, scale=1.0, size=None): # real signature unknown; restored from __doc__
        """
        rayleigh(scale=1.0, size=None)
        
                Draw samples from a Rayleigh distribution.
        
                The :math:`\chi` and Weibull distributions are generalizations of the
                Rayleigh.
        
                .. note::
                    New code should use the `~numpy.random.Generator.rayleigh`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                scale : float or array_like of floats, optional
                    Scale, also equals the mode. Must be non-negative. Default is 1.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``scale`` is a scalar.  Otherwise,
                    ``np.array(scale).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized Rayleigh distribution.
        
                See Also
                --------
                random.Generator.rayleigh: which should be used for new code.
        
                Notes
                -----
                The probability density function for the Rayleigh distribution is
        
                .. math:: P(x;scale) = \frac{x}{scale^2}e^{\frac{-x^2}{2 \cdotp scale^2}}
        
                The Rayleigh distribution would arise, for example, if the East
                and North components of the wind velocity had identical zero-mean
                Gaussian distributions.  Then the wind speed would have a Rayleigh
                distribution.
        
                References
                ----------
                .. [1] Brighton Webs Ltd., "Rayleigh Distribution,"
                       https://web.archive.org/web/20090514091424/http://brighton-webs.co.uk:80/distributions/rayleigh.asp
                .. [2] Wikipedia, "Rayleigh distribution"
                       https://en.wikipedia.org/wiki/Rayleigh_distribution
        
                Examples
                --------
                Draw values from the distribution and plot the histogram
        
                >>> from matplotlib.pyplot import hist
                >>> values = hist(np.random.rayleigh(3, 100000), bins=200, density=True)
        
                Wave heights tend to follow a Rayleigh distribution. If the mean wave
                height is 1 meter, what fraction of waves are likely to be larger than 3
                meters?
        
                >>> meanvalue = 1
                >>> modevalue = np.sqrt(2 / np.pi) * meanvalue
                >>> s = np.random.rayleigh(modevalue, 1000000)
        
                The percentage of waves larger than 3 meters is:
        
                >>> 100.*sum(s>3)/1000000.
                0.087300000000000003 # random
        """
        pass

    def seed(self, seed=None): # real signature unknown; restored from __doc__
        """
        seed(seed=None)
        
                Reseed a legacy MT19937 BitGenerator
        
                Notes
                -----
                This is a convenience, legacy function.
        
                The best practice is to **not** reseed a BitGenerator, rather to
                recreate a new one. This method is here for legacy reasons.
                This example demonstrates best practice.
        
                >>> from numpy.random import MT19937
                >>> from numpy.random import RandomState, SeedSequence
                >>> rs = RandomState(MT19937(SeedSequence(123456789)))
                # Later, you want to restart the stream
                >>> rs = RandomState(MT19937(SeedSequence(987654321)))
        """
        pass

    def set_state(self, state): # real signature unknown; restored from __doc__
        """
        set_state(state)
        
                Set the internal state of the generator from a tuple.
        
                For use if one has reason to manually (re-)set the internal state of
                the bit generator used by the RandomState instance. By default,
                RandomState uses the "Mersenne Twister"[1]_ pseudo-random number
                generating algorithm.
        
                Parameters
                ----------
                state : {tuple(str, ndarray of 624 uints, int, int, float), dict}
                    The `state` tuple has the following items:
        
                    1. the string 'MT19937', specifying the Mersenne Twister algorithm.
                    2. a 1-D array of 624 unsigned integers ``keys``.
                    3. an integer ``pos``.
                    4. an integer ``has_gauss``.
                    5. a float ``cached_gaussian``.
        
                    If state is a dictionary, it is directly set using the BitGenerators
                    `state` property.
        
                Returns
                -------
                out : None
                    Returns 'None' on success.
        
                See Also
                --------
                get_state
        
                Notes
                -----
                `set_state` and `get_state` are not needed to work with any of the
                random distributions in NumPy. If the internal state is manually altered,
                the user should know exactly what he/she is doing.
        
                For backwards compatibility, the form (str, array of 624 uints, int) is
                also accepted although it is missing some information about the cached
                Gaussian value: ``state = ('MT19937', keys, pos)``.
        
                References
                ----------
                .. [1] M. Matsumoto and T. Nishimura, "Mersenne Twister: A
                   623-dimensionally equidistributed uniform pseudorandom number
                   generator," *ACM Trans. on Modeling and Computer Simulation*,
                   Vol. 8, No. 1, pp. 3-30, Jan. 1998.
        """
        pass

    def shuffle(self, x): # real signature unknown; restored from __doc__
        """
        shuffle(x)
        
                Modify a sequence in-place by shuffling its contents.
        
                This function only shuffles the array along the first axis of a
                multi-dimensional array. The order of sub-arrays is changed but
                their contents remains the same.
        
                .. note::
                    New code should use the `~numpy.random.Generator.shuffle`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                x : ndarray or MutableSequence
                    The array, list or mutable sequence to be shuffled.
        
                Returns
                -------
                None
        
                See Also
                --------
                random.Generator.shuffle: which should be used for new code.
        
                Examples
                --------
                >>> arr = np.arange(10)
                >>> np.random.shuffle(arr)
                >>> arr
                [1 7 5 2 9 4 3 6 0 8] # random
        
                Multi-dimensional arrays are only shuffled along the first axis:
        
                >>> arr = np.arange(9).reshape((3, 3))
                >>> np.random.shuffle(arr)
                >>> arr
                array([[3, 4, 5], # random
                       [6, 7, 8],
                       [0, 1, 2]])
        """
        pass

    def standard_cauchy(self, size=None): # real signature unknown; restored from __doc__
        """
        standard_cauchy(size=None)
        
                Draw samples from a standard Cauchy distribution with mode = 0.
        
                Also known as the Lorentz distribution.
        
                .. note::
                    New code should use the
                    `~numpy.random.Generator.standard_cauchy`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  Default is None, in which case a
                    single value is returned.
        
                Returns
                -------
                samples : ndarray or scalar
                    The drawn samples.
        
                See Also
                --------
                random.Generator.standard_cauchy: which should be used for new code.
        
                Notes
                -----
                The probability density function for the full Cauchy distribution is
        
                .. math:: P(x; x_0, \gamma) = \frac{1}{\pi \gamma \bigl[ 1+
                          (\frac{x-x_0}{\gamma})^2 \bigr] }
        
                and the Standard Cauchy distribution just sets :math:`x_0=0` and
                :math:`\gamma=1`
        
                The Cauchy distribution arises in the solution to the driven harmonic
                oscillator problem, and also describes spectral line broadening. It
                also describes the distribution of values at which a line tilted at
                a random angle will cut the x axis.
        
                When studying hypothesis tests that assume normality, seeing how the
                tests perform on data from a Cauchy distribution is a good indicator of
                their sensitivity to a heavy-tailed distribution, since the Cauchy looks
                very much like a Gaussian distribution, but with heavier tails.
        
                References
                ----------
                .. [1] NIST/SEMATECH e-Handbook of Statistical Methods, "Cauchy
                      Distribution",
                      https://www.itl.nist.gov/div898/handbook/eda/section3/eda3663.htm
                .. [2] Weisstein, Eric W. "Cauchy Distribution." From MathWorld--A
                      Wolfram Web Resource.
                      http://mathworld.wolfram.com/CauchyDistribution.html
                .. [3] Wikipedia, "Cauchy distribution"
                      https://en.wikipedia.org/wiki/Cauchy_distribution
        
                Examples
                --------
                Draw samples and plot the distribution:
        
                >>> import matplotlib.pyplot as plt
                >>> s = np.random.standard_cauchy(1000000)
                >>> s = s[(s>-25) & (s<25)]  # truncate distribution so it plots well
                >>> plt.hist(s, bins=100)
                >>> plt.show()
        """
        pass

    def standard_exponential(self, size=None): # real signature unknown; restored from __doc__
        """
        standard_exponential(size=None)
        
                Draw samples from the standard exponential distribution.
        
                `standard_exponential` is identical to the exponential distribution
                with a scale parameter of 1.
        
                .. note::
                    New code should use the
                    `~numpy.random.Generator.standard_exponential`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  Default is None, in which case a
                    single value is returned.
        
                Returns
                -------
                out : float or ndarray
                    Drawn samples.
        
                See Also
                --------
                random.Generator.standard_exponential: which should be used for new code.
        
                Examples
                --------
                Output a 3x8000 array:
        
                >>> n = np.random.standard_exponential((3, 8000))
        """
        pass

    def standard_gamma(self, shape, size=None): # real signature unknown; restored from __doc__
        """
        standard_gamma(shape, size=None)
        
                Draw samples from a standard Gamma distribution.
        
                Samples are drawn from a Gamma distribution with specified parameters,
                shape (sometimes designated "k") and scale=1.
        
                .. note::
                    New code should use the
                    `~numpy.random.Generator.standard_gamma`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                shape : float or array_like of floats
                    Parameter, must be non-negative.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``shape`` is a scalar.  Otherwise,
                    ``np.array(shape).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized standard gamma distribution.
        
                See Also
                --------
                scipy.stats.gamma : probability density function, distribution or
                    cumulative density function, etc.
                random.Generator.standard_gamma: which should be used for new code.
        
                Notes
                -----
                The probability density for the Gamma distribution is
        
                .. math:: p(x) = x^{k-1}\frac{e^{-x/\theta}}{\theta^k\Gamma(k)},
        
                where :math:`k` is the shape and :math:`\theta` the scale,
                and :math:`\Gamma` is the Gamma function.
        
                The Gamma distribution is often used to model the times to failure of
                electronic components, and arises naturally in processes for which the
                waiting times between Poisson distributed events are relevant.
        
                References
                ----------
                .. [1] Weisstein, Eric W. "Gamma Distribution." From MathWorld--A
                       Wolfram Web Resource.
                       http://mathworld.wolfram.com/GammaDistribution.html
                .. [2] Wikipedia, "Gamma distribution",
                       https://en.wikipedia.org/wiki/Gamma_distribution
        
                Examples
                --------
                Draw samples from the distribution:
        
                >>> shape, scale = 2., 1. # mean and width
                >>> s = np.random.standard_gamma(shape, 1000000)
        
                Display the histogram of the samples, along with
                the probability density function:
        
                >>> import matplotlib.pyplot as plt
                >>> import scipy.special as sps  # doctest: +SKIP
                >>> count, bins, ignored = plt.hist(s, 50, density=True)
                >>> y = bins**(shape-1) * ((np.exp(-bins/scale))/  # doctest: +SKIP
                ...                       (sps.gamma(shape) * scale**shape))
                >>> plt.plot(bins, y, linewidth=2, color='r')  # doctest: +SKIP
                >>> plt.show()
        """
        pass

    def standard_normal(self, size=None): # real signature unknown; restored from __doc__
        """
        standard_normal(size=None)
        
                Draw samples from a standard Normal distribution (mean=0, stdev=1).
        
                .. note::
                    New code should use the
                    `~numpy.random.Generator.standard_normal`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  Default is None, in which case a
                    single value is returned.
        
                Returns
                -------
                out : float or ndarray
                    A floating-point array of shape ``size`` of drawn samples, or a
                    single sample if ``size`` was not specified.
        
                See Also
                --------
                normal :
                    Equivalent function with additional ``loc`` and ``scale`` arguments
                    for setting the mean and standard deviation.
                random.Generator.standard_normal: which should be used for new code.
        
                Notes
                -----
                For random samples from the normal distribution with mean ``mu`` and
                standard deviation ``sigma``, use one of::
        
                    mu + sigma * np.random.standard_normal(size=...)
                    np.random.normal(mu, sigma, size=...)
        
                Examples
                --------
                >>> np.random.standard_normal()
                2.1923875335537315 #random
        
                >>> s = np.random.standard_normal(8000)
                >>> s
                array([ 0.6888893 ,  0.78096262, -0.89086505, ...,  0.49876311,  # random
                       -0.38672696, -0.4685006 ])                                # random
                >>> s.shape
                (8000,)
                >>> s = np.random.standard_normal(size=(3, 4, 2))
                >>> s.shape
                (3, 4, 2)
        
                Two-by-four array of samples from the normal distribution with
                mean 3 and standard deviation 2.5:
        
                >>> 3 + 2.5 * np.random.standard_normal(size=(2, 4))
                array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
                       [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random
        """
        pass

    def standard_t(self, df, size=None): # real signature unknown; restored from __doc__
        """
        standard_t(df, size=None)
        
                Draw samples from a standard Student's t distribution with `df` degrees
                of freedom.
        
                A special case of the hyperbolic distribution.  As `df` gets
                large, the result resembles that of the standard normal
                distribution (`standard_normal`).
        
                .. note::
                    New code should use the `~numpy.random.Generator.standard_t`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                df : float or array_like of floats
                    Degrees of freedom, must be > 0.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``df`` is a scalar.  Otherwise,
                    ``np.array(df).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized standard Student's t distribution.
        
                See Also
                --------
                random.Generator.standard_t: which should be used for new code.
        
                Notes
                -----
                The probability density function for the t distribution is
        
                .. math:: P(x, df) = \frac{\Gamma(\frac{df+1}{2})}{\sqrt{\pi df}
                          \Gamma(\frac{df}{2})}\Bigl( 1+\frac{x^2}{df} \Bigr)^{-(df+1)/2}
        
                The t test is based on an assumption that the data come from a
                Normal distribution. The t test provides a way to test whether
                the sample mean (that is the mean calculated from the data) is
                a good estimate of the true mean.
        
                The derivation of the t-distribution was first published in
                1908 by William Gosset while working for the Guinness Brewery
                in Dublin. Due to proprietary issues, he had to publish under
                a pseudonym, and so he used the name Student.
        
                References
                ----------
                .. [1] Dalgaard, Peter, "Introductory Statistics With R",
                       Springer, 2002.
                .. [2] Wikipedia, "Student's t-distribution"
                       https://en.wikipedia.org/wiki/Student's_t-distribution
        
                Examples
                --------
                From Dalgaard page 83 [1]_, suppose the daily energy intake for 11
                women in kilojoules (kJ) is:
        
                >>> intake = np.array([5260., 5470, 5640, 6180, 6390, 6515, 6805, 7515, \
                ...                    7515, 8230, 8770])
        
                Does their energy intake deviate systematically from the recommended
                value of 7725 kJ? Our null hypothesis will be the absence of deviation,
                and the alternate hypothesis will be the presence of an effect that could be
                either positive or negative, hence making our test 2-tailed. 
        
                Because we are estimating the mean and we have N=11 values in our sample,
                we have N-1=10 degrees of freedom. We set our significance level to 95% and 
                compute the t statistic using the empirical mean and empirical standard 
                deviation of our intake. We use a ddof of 1 to base the computation of our 
                empirical standard deviation on an unbiased estimate of the variance (note:
                the final estimate is not unbiased due to the concave nature of the square 
                root).
        
                >>> np.mean(intake)
                6753.636363636364
                >>> intake.std(ddof=1)
                1142.1232221373727
                >>> t = (np.mean(intake)-7725)/(intake.std(ddof=1)/np.sqrt(len(intake)))
                >>> t
                -2.8207540608310198
        
                We draw 1000000 samples from Student's t distribution with the adequate
                degrees of freedom.
        
                >>> import matplotlib.pyplot as plt
                >>> s = np.random.standard_t(10, size=1000000)
                >>> h = plt.hist(s, bins=100, density=True)
        
                Does our t statistic land in one of the two critical regions found at 
                both tails of the distribution?
        
                >>> np.sum(np.abs(t) < np.abs(s)) / float(len(s))
                0.018318  #random < 0.05, statistic is in critical region
        
                The probability value for this 2-tailed test is about 1.83%, which is 
                lower than the 5% pre-determined significance threshold. 
        
                Therefore, the probability of observing values as extreme as our intake
                conditionally on the null hypothesis being true is too low, and we reject 
                the null hypothesis of no deviation.
        """
        pass

    def tomaxint(self, size=None): # real signature unknown; restored from __doc__
        """
        tomaxint(size=None)
        
                Return a sample of uniformly distributed random integers in the interval
                [0, ``np.iinfo(np.int_).max``]. The `np.int_` type translates to the C long
                integer type and its precision is platform dependent.
        
                Parameters
                ----------
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  Default is None, in which case a
                    single value is returned.
        
                Returns
                -------
                out : ndarray
                    Drawn samples, with shape `size`.
        
                See Also
                --------
                randint : Uniform sampling over a given half-open interval of integers.
                random_integers : Uniform sampling over a given closed interval of
                    integers.
        
                Examples
                --------
                >>> rs = np.random.RandomState() # need a RandomState object
                >>> rs.tomaxint((2,2,2))
                array([[[1170048599, 1600360186], # random
                        [ 739731006, 1947757578]],
                       [[1871712945,  752307660],
                        [1601631370, 1479324245]]])
                >>> rs.tomaxint((2,2,2)) < np.iinfo(np.int_).max
                array([[[ True,  True],
                        [ True,  True]],
                       [[ True,  True],
                        [ True,  True]]])
        """
        pass

    def triangular(self, left, mode, right, size=None): # real signature unknown; restored from __doc__
        """
        triangular(left, mode, right, size=None)
        
                Draw samples from the triangular distribution over the
                interval ``[left, right]``.
        
                The triangular distribution is a continuous probability
                distribution with lower limit left, peak at mode, and upper
                limit right. Unlike the other distributions, these parameters
                directly define the shape of the pdf.
        
                .. note::
                    New code should use the `~numpy.random.Generator.triangular`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                left : float or array_like of floats
                    Lower limit.
                mode : float or array_like of floats
                    The value where the peak of the distribution occurs.
                    The value must fulfill the condition ``left <= mode <= right``.
                right : float or array_like of floats
                    Upper limit, must be larger than `left`.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``left``, ``mode``, and ``right``
                    are all scalars.  Otherwise, ``np.broadcast(left, mode, right).size``
                    samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized triangular distribution.
        
                See Also
                --------
                random.Generator.triangular: which should be used for new code.
        
                Notes
                -----
                The probability density function for the triangular distribution is
        
                .. math:: P(x;l, m, r) = \begin{cases}
                          \frac{2(x-l)}{(r-l)(m-l)}& \text{for $l \leq x \leq m$},\\
                          \frac{2(r-x)}{(r-l)(r-m)}& \text{for $m \leq x \leq r$},\\
                          0& \text{otherwise}.
                          \end{cases}
        
                The triangular distribution is often used in ill-defined
                problems where the underlying distribution is not known, but
                some knowledge of the limits and mode exists. Often it is used
                in simulations.
        
                References
                ----------
                .. [1] Wikipedia, "Triangular distribution"
                       https://en.wikipedia.org/wiki/Triangular_distribution
        
                Examples
                --------
                Draw values from the distribution and plot the histogram:
        
                >>> import matplotlib.pyplot as plt
                >>> h = plt.hist(np.random.triangular(-3, 0, 8, 100000), bins=200,
                ...              density=True)
                >>> plt.show()
        """
        pass

    def uniform(self, low=0.0, high=1.0, size=None): # real signature unknown; restored from __doc__
        """
        uniform(low=0.0, high=1.0, size=None)
        
                Draw samples from a uniform distribution.
        
                Samples are uniformly distributed over the half-open interval
                ``[low, high)`` (includes low, but excludes high).  In other words,
                any value within the given interval is equally likely to be drawn
                by `uniform`.
        
                .. note::
                    New code should use the `~numpy.random.Generator.uniform`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                low : float or array_like of floats, optional
                    Lower boundary of the output interval.  All values generated will be
                    greater than or equal to low.  The default value is 0.
                high : float or array_like of floats
                    Upper boundary of the output interval.  All values generated will be
                    less than or equal to high.  The high limit may be included in the 
                    returned array of floats due to floating-point rounding in the 
                    equation ``low + (high-low) * random_sample()``.  The default value 
                    is 1.0.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``low`` and ``high`` are both scalars.
                    Otherwise, ``np.broadcast(low, high).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized uniform distribution.
        
                See Also
                --------
                randint : Discrete uniform distribution, yielding integers.
                random_integers : Discrete uniform distribution over the closed
                                  interval ``[low, high]``.
                random_sample : Floats uniformly distributed over ``[0, 1)``.
                random : Alias for `random_sample`.
                rand : Convenience function that accepts dimensions as input, e.g.,
                       ``rand(2,2)`` would generate a 2-by-2 array of floats,
                       uniformly distributed over ``[0, 1)``.
                random.Generator.uniform: which should be used for new code.
        
                Notes
                -----
                The probability density function of the uniform distribution is
        
                .. math:: p(x) = \frac{1}{b - a}
        
                anywhere within the interval ``[a, b)``, and zero elsewhere.
        
                When ``high`` == ``low``, values of ``low`` will be returned.
                If ``high`` < ``low``, the results are officially undefined
                and may eventually raise an error, i.e. do not rely on this
                function to behave when passed arguments satisfying that
                inequality condition. The ``high`` limit may be included in the
                returned array of floats due to floating-point rounding in the
                equation ``low + (high-low) * random_sample()``. For example:
        
                >>> x = np.float32(5*0.99999999)
                >>> x
                5.0
        
        
                Examples
                --------
                Draw samples from the distribution:
        
                >>> s = np.random.uniform(-1,0,1000)
        
                All values are within the given interval:
        
                >>> np.all(s >= -1)
                True
                >>> np.all(s < 0)
                True
        
                Display the histogram of the samples, along with the
                probability density function:
        
                >>> import matplotlib.pyplot as plt
                >>> count, bins, ignored = plt.hist(s, 15, density=True)
                >>> plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
                >>> plt.show()
        """
        pass

    def vonmises(self, mu, kappa, size=None): # real signature unknown; restored from __doc__
        """
        vonmises(mu, kappa, size=None)
        
                Draw samples from a von Mises distribution.
        
                Samples are drawn from a von Mises distribution with specified mode
                (mu) and dispersion (kappa), on the interval [-pi, pi].
        
                The von Mises distribution (also known as the circular normal
                distribution) is a continuous probability distribution on the unit
                circle.  It may be thought of as the circular analogue of the normal
                distribution.
        
                .. note::
                    New code should use the `~numpy.random.Generator.vonmises`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                mu : float or array_like of floats
                    Mode ("center") of the distribution.
                kappa : float or array_like of floats
                    Dispersion of the distribution, has to be >=0.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``mu`` and ``kappa`` are both scalars.
                    Otherwise, ``np.broadcast(mu, kappa).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized von Mises distribution.
        
                See Also
                --------
                scipy.stats.vonmises : probability density function, distribution, or
                    cumulative density function, etc.
                random.Generator.vonmises: which should be used for new code.
        
                Notes
                -----
                The probability density for the von Mises distribution is
        
                .. math:: p(x) = \frac{e^{\kappa cos(x-\mu)}}{2\pi I_0(\kappa)},
        
                where :math:`\mu` is the mode and :math:`\kappa` the dispersion,
                and :math:`I_0(\kappa)` is the modified Bessel function of order 0.
        
                The von Mises is named for Richard Edler von Mises, who was born in
                Austria-Hungary, in what is now the Ukraine.  He fled to the United
                States in 1939 and became a professor at Harvard.  He worked in
                probability theory, aerodynamics, fluid mechanics, and philosophy of
                science.
        
                References
                ----------
                .. [1] Abramowitz, M. and Stegun, I. A. (Eds.). "Handbook of
                       Mathematical Functions with Formulas, Graphs, and Mathematical
                       Tables, 9th printing," New York: Dover, 1972.
                .. [2] von Mises, R., "Mathematical Theory of Probability
                       and Statistics", New York: Academic Press, 1964.
        
                Examples
                --------
                Draw samples from the distribution:
        
                >>> mu, kappa = 0.0, 4.0 # mean and dispersion
                >>> s = np.random.vonmises(mu, kappa, 1000)
        
                Display the histogram of the samples, along with
                the probability density function:
        
                >>> import matplotlib.pyplot as plt
                >>> from scipy.special import i0  # doctest: +SKIP
                >>> plt.hist(s, 50, density=True)
                >>> x = np.linspace(-np.pi, np.pi, num=51)
                >>> y = np.exp(kappa*np.cos(x-mu))/(2*np.pi*i0(kappa))  # doctest: +SKIP
                >>> plt.plot(x, y, linewidth=2, color='r')  # doctest: +SKIP
                >>> plt.show()
        """
        pass

    def wald(self, mean, scale, size=None): # real signature unknown; restored from __doc__
        """
        wald(mean, scale, size=None)
        
                Draw samples from a Wald, or inverse Gaussian, distribution.
        
                As the scale approaches infinity, the distribution becomes more like a
                Gaussian. Some references claim that the Wald is an inverse Gaussian
                with mean equal to 1, but this is by no means universal.
        
                The inverse Gaussian distribution was first studied in relationship to
                Brownian motion. In 1956 M.C.K. Tweedie used the name inverse Gaussian
                because there is an inverse relationship between the time to cover a
                unit distance and distance covered in unit time.
        
                .. note::
                    New code should use the `~numpy.random.Generator.wald`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                mean : float or array_like of floats
                    Distribution mean, must be > 0.
                scale : float or array_like of floats
                    Scale parameter, must be > 0.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``mean`` and ``scale`` are both scalars.
                    Otherwise, ``np.broadcast(mean, scale).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized Wald distribution.
        
                See Also
                --------
                random.Generator.wald: which should be used for new code.
        
                Notes
                -----
                The probability density function for the Wald distribution is
        
                .. math:: P(x;mean,scale) = \sqrt{\frac{scale}{2\pi x^3}}e^
                                            \frac{-scale(x-mean)^2}{2\cdotp mean^2x}
        
                As noted above the inverse Gaussian distribution first arise
                from attempts to model Brownian motion. It is also a
                competitor to the Weibull for use in reliability modeling and
                modeling stock returns and interest rate processes.
        
                References
                ----------
                .. [1] Brighton Webs Ltd., Wald Distribution,
                       https://web.archive.org/web/20090423014010/http://www.brighton-webs.co.uk:80/distributions/wald.asp
                .. [2] Chhikara, Raj S., and Folks, J. Leroy, "The Inverse Gaussian
                       Distribution: Theory : Methodology, and Applications", CRC Press,
                       1988.
                .. [3] Wikipedia, "Inverse Gaussian distribution"
                       https://en.wikipedia.org/wiki/Inverse_Gaussian_distribution
        
                Examples
                --------
                Draw values from the distribution and plot the histogram:
        
                >>> import matplotlib.pyplot as plt
                >>> h = plt.hist(np.random.wald(3, 2, 100000), bins=200, density=True)
                >>> plt.show()
        """
        pass

    def weibull(self, a, size=None): # real signature unknown; restored from __doc__
        """
        weibull(a, size=None)
        
                Draw samples from a Weibull distribution.
        
                Draw samples from a 1-parameter Weibull distribution with the given
                shape parameter `a`.
        
                .. math:: X = (-ln(U))^{1/a}
        
                Here, U is drawn from the uniform distribution over (0,1].
        
                The more common 2-parameter Weibull, including a scale parameter
                :math:`\lambda` is just :math:`X = \lambda(-ln(U))^{1/a}`.
        
                .. note::
                    New code should use the `~numpy.random.Generator.weibull`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                a : float or array_like of floats
                    Shape parameter of the distribution.  Must be nonnegative.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``a`` is a scalar.  Otherwise,
                    ``np.array(a).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized Weibull distribution.
        
                See Also
                --------
                scipy.stats.weibull_max
                scipy.stats.weibull_min
                scipy.stats.genextreme
                gumbel
                random.Generator.weibull: which should be used for new code.
        
                Notes
                -----
                The Weibull (or Type III asymptotic extreme value distribution
                for smallest values, SEV Type III, or Rosin-Rammler
                distribution) is one of a class of Generalized Extreme Value
                (GEV) distributions used in modeling extreme value problems.
                This class includes the Gumbel and Frechet distributions.
        
                The probability density for the Weibull distribution is
        
                .. math:: p(x) = \frac{a}
                                 {\lambda}(\frac{x}{\lambda})^{a-1}e^{-(x/\lambda)^a},
        
                where :math:`a` is the shape and :math:`\lambda` the scale.
        
                The function has its peak (the mode) at
                :math:`\lambda(\frac{a-1}{a})^{1/a}`.
        
                When ``a = 1``, the Weibull distribution reduces to the exponential
                distribution.
        
                References
                ----------
                .. [1] Waloddi Weibull, Royal Technical University, Stockholm,
                       1939 "A Statistical Theory Of The Strength Of Materials",
                       Ingeniorsvetenskapsakademiens Handlingar Nr 151, 1939,
                       Generalstabens Litografiska Anstalts Forlag, Stockholm.
                .. [2] Waloddi Weibull, "A Statistical Distribution Function of
                       Wide Applicability", Journal Of Applied Mechanics ASME Paper
                       1951.
                .. [3] Wikipedia, "Weibull distribution",
                       https://en.wikipedia.org/wiki/Weibull_distribution
        
                Examples
                --------
                Draw samples from the distribution:
        
                >>> a = 5. # shape
                >>> s = np.random.weibull(a, 1000)
        
                Display the histogram of the samples, along with
                the probability density function:
        
                >>> import matplotlib.pyplot as plt
                >>> x = np.arange(1,100.)/50.
                >>> def weib(x,n,a):
                ...     return (a / n) * (x / n)**(a - 1) * np.exp(-(x / n)**a)
        
                >>> count, bins, ignored = plt.hist(np.random.weibull(5.,1000))
                >>> x = np.arange(1,100.)/50.
                >>> scale = count.max()/weib(x, 1., 5.).max()
                >>> plt.plot(x, weib(x, 1., 5.)*scale)
                >>> plt.show()
        """
        pass

    def zipf(self, a, size=None): # real signature unknown; restored from __doc__
        """
        zipf(a, size=None)
        
                Draw samples from a Zipf distribution.
        
                Samples are drawn from a Zipf distribution with specified parameter
                `a` > 1.
        
                The Zipf distribution (also known as the zeta distribution) is a
                discrete probability distribution that satisfies Zipf's law: the
                frequency of an item is inversely proportional to its rank in a
                frequency table.
        
                .. note::
                    New code should use the `~numpy.random.Generator.zipf`
                    method of a `~numpy.random.Generator` instance instead;
                    please see the :ref:`random-quick-start`.
        
                Parameters
                ----------
                a : float or array_like of floats
                    Distribution parameter. Must be greater than 1.
                size : int or tuple of ints, optional
                    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
                    a single value is returned if ``a`` is a scalar. Otherwise,
                    ``np.array(a).size`` samples are drawn.
        
                Returns
                -------
                out : ndarray or scalar
                    Drawn samples from the parameterized Zipf distribution.
        
                See Also
                --------
                scipy.stats.zipf : probability density function, distribution, or
                    cumulative density function, etc.
                random.Generator.zipf: which should be used for new code.
        
                Notes
                -----
                The probability density for the Zipf distribution is
        
                .. math:: p(k) = \frac{k^{-a}}{\zeta(a)},
        
                for integers :math:`k \geq 1`, where :math:`\zeta` is the Riemann Zeta
                function.
        
                It is named for the American linguist George Kingsley Zipf, who noted
                that the frequency of any word in a sample of a language is inversely
                proportional to its rank in the frequency table.
        
                References
                ----------
                .. [1] Zipf, G. K., "Selected Studies of the Principle of Relative
                       Frequency in Language," Cambridge, MA: Harvard Univ. Press,
                       1932.
        
                Examples
                --------
                Draw samples from the distribution:
        
                >>> a = 4.0
                >>> n = 20000
                >>> s = np.random.zipf(a, n)
        
                Display the histogram of the samples, along with
                the expected histogram based on the probability
                density function:
        
                >>> import matplotlib.pyplot as plt
                >>> from scipy.special import zeta  # doctest: +SKIP
        
                `bincount` provides a fast histogram for small integers.
        
                >>> count = np.bincount(s)
                >>> k = np.arange(1, s.max() + 1)
        
                >>> plt.bar(k, count[1:], alpha=0.5, label='sample count')
                >>> plt.plot(k, n*(k**-a)/zeta(a), 'k.-', alpha=0.5,
                ...          label='expected count')   # doctest: +SKIP
                >>> plt.semilogy()
                >>> plt.grid(alpha=0.4)
                >>> plt.legend()
                >>> plt.title(f'Zipf sample, a={a}, size={n}')
                >>> plt.show()
        """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, seed=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    _bit_generator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _poisson_lam_max = 9.223372006484771e+18
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0xffff9fdbf270>'


class Sequence(__collections_abc.Reversible, __collections_abc.Collection):
    """
    All the operations on a read-only sequence.
    
        Concrete subclasses must override __new__ or __init__,
        __getitem__, and __len__.
    """
    def count(self, value): # reliably restored by inspect
        """ S.count(value) -> integer -- return number of occurrences of value """
        pass

    def index(self, value, start=0, stop=None): # reliably restored by inspect
        """
        S.index(value, [start, [stop]]) -> integer -- return first index of value.
                   Raises ValueError if the value is not present.
        
                   Supporting start and stop arguments is optional, but
                   recommended.
        """
        pass

    def __contains__(self, value): # reliably restored by inspect
        # no doc
        pass

    def __getitem__(self, index): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    def __reversed__(self): # reliably restored by inspect
        # no doc
        pass

    _abc_impl = None # (!) real value is '<_abc_data object at 0xffffacde3660>'
    __abstractmethods__ = frozenset({'__getitem__', '__len__'})
    __slots__ = ()


# variables with complex values

_rand = None # (!) real value is 'RandomState(MT19937) at 0xFFFF9FDAF640'

__all__ = [
    'beta',
    'binomial',
    'bytes',
    'chisquare',
    'choice',
    'dirichlet',
    'exponential',
    'f',
    'gamma',
    'geometric',
    'get_bit_generator',
    'get_state',
    'gumbel',
    'hypergeometric',
    'laplace',
    'logistic',
    'lognormal',
    'logseries',
    'multinomial',
    'multivariate_normal',
    'negative_binomial',
    'noncentral_chisquare',
    'noncentral_f',
    'normal',
    'pareto',
    'permutation',
    'poisson',
    'power',
    'rand',
    'randint',
    'randn',
    'random',
    'random_integers',
    'random_sample',
    'ranf',
    'rayleigh',
    'sample',
    'seed',
    'set_bit_generator',
    'set_state',
    'shuffle',
    'standard_cauchy',
    'standard_exponential',
    'standard_gamma',
    'standard_normal',
    'standard_t',
    'triangular',
    'uniform',
    'vonmises',
    'wald',
    'weibull',
    'zipf',
    'RandomState',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9fdb4c10>'

__spec__ = None # (!) real value is "ModuleSpec(name='numpy.random.mtrand', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9fdb4c10>, origin='/.venv/lib/python3.8/site-packages/numpy/random/mtrand.cpython-38-aarch64-linux-gnu.so')"

__test__ = {
    'RandomState.binomial (line 3336)': '\n        binomial(n, p, size=None)\n\n        Draw samples from a binomial distribution.\n\n        Samples are drawn from a binomial distribution with specified\n        parameters, n trials and p probability of success where\n        n an integer >= 0 and p is in the interval [0,1]. (n may be\n        input as a float, but it is truncated to an integer in use)\n\n        .. note::\n            New code should use the `~numpy.random.Generator.binomial`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        n : int or array_like of ints\n            Parameter of the distribution, >= 0. Floats are also accepted,\n            but they will be truncated to integers.\n        p : float or array_like of floats\n            Parameter of the distribution, >= 0 and <=1.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``n`` and ``p`` are both scalars.\n            Otherwise, ``np.broadcast(n, p).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized binomial distribution, where\n            each sample is equal to the number of successes over the n trials.\n\n        See Also\n        --------\n        scipy.stats.binom : probability density function, distribution or\n            cumulative density function, etc.\n        random.Generator.binomial: which should be used for new code.\n\n        Notes\n        -----\n        The probability density for the binomial distribution is\n\n        .. math:: P(N) = \\binom{n}{N}p^N(1-p)^{n-N},\n\n        where :math:`n` is the number of trials, :math:`p` is the probability\n        of success, and :math:`N` is the number of successes.\n\n        When estimating the standard error of a proportion in a population by\n        using a random sample, the normal distribution works well unless the\n        product p*n <=5, where p = population proportion estimate, and n =\n        number of samples, in which case the binomial distribution is used\n        instead. For example, a sample of 15 people shows 4 who are left\n        handed, and 11 who are right handed. Then p = 4/15 = 27%. 0.27*15 = 4,\n        so the binomial distribution should be used in this case.\n\n        References\n        ----------\n        .. [1] Dalgaard, Peter, "Introductory Statistics with R",\n               Springer-Verlag, 2002.\n        .. [2] Glantz, Stanton A. "Primer of Biostatistics.", McGraw-Hill,\n               Fifth Edition, 2002.\n        .. [3] Lentner, Marvin, "Elementary Applied Statistics", Bogden\n               and Quigley, 1972.\n        .. [4] Weisstein, Eric W. "Binomial Distribution." From MathWorld--A\n               Wolfram Web Resource.\n               http://mathworld.wolfram.com/BinomialDistribution.html\n        .. [5] Wikipedia, "Binomial distribution",\n               https://en.wikipedia.org/wiki/Binomial_distribution\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        >>> n, p = 10, .5  # number of trials, probability of each trial\n        >>> s = np.random.binomial(n, p, 1000)\n        # result of flipping a coin 10 times, tested 1000 times.\n\n        A real world example. A company drills 9 wild-cat oil exploration\n        wells, each with an estimated probability of success of 0.1. All nine\n        wells fail. What is the probability of that happening?\n\n        Let\'s do 20,000 trials of the model, and count the number that\n        generate zero positive results.\n\n        >>> sum(np.random.binomial(9, 0.1, 20000) == 0)/20000.\n        # answer = 0.38885, or 38%.\n\n        ',
    'RandomState.bytes (line 788)': "\n        bytes(length)\n\n        Return random bytes.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.bytes`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        length : int\n            Number of random bytes.\n\n        Returns\n        -------\n        out : bytes\n            String of length `length`.\n\n        See Also\n        --------\n        random.Generator.bytes: which should be used for new code.\n\n        Examples\n        --------\n        >>> np.random.bytes(10)\n        b' eh\\x85\\x022SZ\\xbf\\xa4' #random\n        ",
    'RandomState.chisquare (line 1893)': '\n        chisquare(df, size=None)\n\n        Draw samples from a chi-square distribution.\n\n        When `df` independent random variables, each with standard normal\n        distributions (mean 0, variance 1), are squared and summed, the\n        resulting distribution is chi-square (see Notes).  This distribution\n        is often used in hypothesis testing.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.chisquare`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        df : float or array_like of floats\n             Number of degrees of freedom, must be > 0.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``df`` is a scalar.  Otherwise,\n            ``np.array(df).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized chi-square distribution.\n\n        Raises\n        ------\n        ValueError\n            When `df` <= 0 or when an inappropriate `size` (e.g. ``size=-1``)\n            is given.\n\n        See Also\n        --------\n        random.Generator.chisquare: which should be used for new code.\n\n        Notes\n        -----\n        The variable obtained by summing the squares of `df` independent,\n        standard normally distributed random variables:\n\n        .. math:: Q = \\sum_{i=0}^{\\mathtt{df}} X^2_i\n\n        is chi-square distributed, denoted\n\n        .. math:: Q \\sim \\chi^2_k.\n\n        The probability density function of the chi-squared distribution is\n\n        .. math:: p(x) = \\frac{(1/2)^{k/2}}{\\Gamma(k/2)}\n                         x^{k/2 - 1} e^{-x/2},\n\n        where :math:`\\Gamma` is the gamma function,\n\n        .. math:: \\Gamma(x) = \\int_0^{-\\infty} t^{x - 1} e^{-t} dt.\n\n        References\n        ----------\n        .. [1] NIST "Engineering Statistics Handbook"\n               https://www.itl.nist.gov/div898/handbook/eda/section3/eda3666.htm\n\n        Examples\n        --------\n        >>> np.random.chisquare(2,4)\n        array([ 1.89920014,  9.00867716,  3.13710533,  5.62318272]) # random\n        ',
    'RandomState.choice (line 825)': "\n        choice(a, size=None, replace=True, p=None)\n\n        Generates a random sample from a given 1-D array\n\n        .. versionadded:: 1.7.0\n\n        .. note::\n            New code should use the `~numpy.random.Generator.choice`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        a : 1-D array-like or int\n            If an ndarray, a random sample is generated from its elements.\n            If an int, the random sample is generated as if it were ``np.arange(a)``\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  Default is None, in which case a\n            single value is returned.\n        replace : boolean, optional\n            Whether the sample is with or without replacement. Default is True,\n            meaning that a value of ``a`` can be selected multiple times.\n        p : 1-D array-like, optional\n            The probabilities associated with each entry in a.\n            If not given, the sample assumes a uniform distribution over all\n            entries in ``a``.\n\n        Returns\n        -------\n        samples : single item or ndarray\n            The generated random samples\n\n        Raises\n        ------\n        ValueError\n            If a is an int and less than zero, if a or p are not 1-dimensional,\n            if a is an array-like of size 0, if p is not a vector of\n            probabilities, if a and p have different lengths, or if\n            replace=False and the sample size is greater than the population\n            size\n\n        See Also\n        --------\n        randint, shuffle, permutation\n        random.Generator.choice: which should be used in new code\n\n        Notes\n        -----\n        Setting user-specified probabilities through ``p`` uses a more general but less\n        efficient sampler than the default. The general sampler produces a different sample\n        than the optimized sampler even if each element of ``p`` is 1 / len(a).\n\n        Sampling random rows from a 2-D array is not possible with this function,\n        but is possible with `Generator.choice` through its ``axis`` keyword.\n\n        Examples\n        --------\n        Generate a uniform random sample from np.arange(5) of size 3:\n\n        >>> np.random.choice(5, 3)\n        array([0, 3, 4]) # random\n        >>> #This is equivalent to np.random.randint(0,5,3)\n\n        Generate a non-uniform random sample from np.arange(5) of size 3:\n\n        >>> np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0])\n        array([3, 3, 0]) # random\n\n        Generate a uniform random sample from np.arange(5) of size 3 without\n        replacement:\n\n        >>> np.random.choice(5, 3, replace=False)\n        array([3,1,0]) # random\n        >>> #This is equivalent to np.random.permutation(np.arange(5))[:3]\n\n        Generate a non-uniform random sample from np.arange(5) of size\n        3 without replacement:\n\n        >>> np.random.choice(5, 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0])\n        array([2, 3, 0]) # random\n\n        Any of the above can be repeated with an arbitrary array-like\n        instead of just integers. For instance:\n\n        >>> aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']\n        >>> np.random.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3])\n        array(['pooh', 'pooh', 'pooh', 'Christopher', 'piglet'], # random\n              dtype='<U11')\n\n        ",
    'RandomState.dirichlet (line 4377)': '\n        dirichlet(alpha, size=None)\n\n        Draw samples from the Dirichlet distribution.\n\n        Draw `size` samples of dimension k from a Dirichlet distribution. A\n        Dirichlet-distributed random variable can be seen as a multivariate\n        generalization of a Beta distribution. The Dirichlet distribution\n        is a conjugate prior of a multinomial distribution in Bayesian\n        inference.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.dirichlet`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        alpha : sequence of floats, length k\n            Parameter of the distribution (length ``k`` for sample of\n            length ``k``).\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n)``, then\n            ``m * n * k`` samples are drawn.  Default is None, in which case a\n            vector of length ``k`` is returned.\n\n        Returns\n        -------\n        samples : ndarray,\n            The drawn samples, of shape ``(size, k)``.\n\n        Raises\n        ------\n        ValueError\n            If any value in ``alpha`` is less than or equal to zero\n\n        See Also\n        --------\n        random.Generator.dirichlet: which should be used for new code.\n\n        Notes\n        -----\n        The Dirichlet distribution is a distribution over vectors\n        :math:`x` that fulfil the conditions :math:`x_i>0` and\n        :math:`\\sum_{i=1}^k x_i = 1`.\n\n        The probability density function :math:`p` of a\n        Dirichlet-distributed random vector :math:`X` is\n        proportional to\n\n        .. math:: p(x) \\propto \\prod_{i=1}^{k}{x^{\\alpha_i-1}_i},\n\n        where :math:`\\alpha` is a vector containing the positive\n        concentration parameters.\n\n        The method uses the following property for computation: let :math:`Y`\n        be a random vector which has components that follow a standard gamma\n        distribution, then :math:`X = \\frac{1}{\\sum_{i=1}^k{Y_i}} Y`\n        is Dirichlet-distributed\n\n        References\n        ----------\n        .. [1] David McKay, "Information Theory, Inference and Learning\n               Algorithms," chapter 23,\n               http://www.inference.org.uk/mackay/itila/\n        .. [2] Wikipedia, "Dirichlet distribution",\n               https://en.wikipedia.org/wiki/Dirichlet_distribution\n\n        Examples\n        --------\n        Taking an example cited in Wikipedia, this distribution can be used if\n        one wanted to cut strings (each of initial length 1.0) into K pieces\n        with different lengths, where each piece had, on average, a designated\n        average length, but allowing some variation in the relative sizes of\n        the pieces.\n\n        >>> s = np.random.dirichlet((10, 5, 3), 20).transpose()\n\n        >>> import matplotlib.pyplot as plt\n        >>> plt.barh(range(20), s[0])\n        >>> plt.barh(range(20), s[1], left=s[0], color=\'g\')\n        >>> plt.barh(range(20), s[2], left=s[0]+s[1], color=\'r\')\n        >>> plt.title("Lengths of Strings")\n\n        ',
    'RandomState.f (line 1712)': '\n        f(dfnum, dfden, size=None)\n\n        Draw samples from an F distribution.\n\n        Samples are drawn from an F distribution with specified parameters,\n        `dfnum` (degrees of freedom in numerator) and `dfden` (degrees of\n        freedom in denominator), where both parameters must be greater than\n        zero.\n\n        The random variate of the F distribution (also known as the\n        Fisher distribution) is a continuous probability distribution\n        that arises in ANOVA tests, and is the ratio of two chi-square\n        variates.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.f`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        dfnum : float or array_like of floats\n            Degrees of freedom in numerator, must be > 0.\n        dfden : float or array_like of float\n            Degrees of freedom in denominator, must be > 0.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``dfnum`` and ``dfden`` are both scalars.\n            Otherwise, ``np.broadcast(dfnum, dfden).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized Fisher distribution.\n\n        See Also\n        --------\n        scipy.stats.f : probability density function, distribution or\n            cumulative density function, etc.\n        random.Generator.f: which should be used for new code.\n\n        Notes\n        -----\n        The F statistic is used to compare in-group variances to between-group\n        variances. Calculating the distribution depends on the sampling, and\n        so it is a function of the respective degrees of freedom in the\n        problem.  The variable `dfnum` is the number of samples minus one, the\n        between-groups degrees of freedom, while `dfden` is the within-groups\n        degrees of freedom, the sum of the number of samples in each group\n        minus the number of groups.\n\n        References\n        ----------\n        .. [1] Glantz, Stanton A. "Primer of Biostatistics.", McGraw-Hill,\n               Fifth Edition, 2002.\n        .. [2] Wikipedia, "F-distribution",\n               https://en.wikipedia.org/wiki/F-distribution\n\n        Examples\n        --------\n        An example from Glantz[1], pp 47-40:\n\n        Two groups, children of diabetics (25 people) and children from people\n        without diabetes (25 controls). Fasting blood glucose was measured,\n        case group had a mean value of 86.1, controls had a mean value of\n        82.2. Standard deviations were 2.09 and 2.49 respectively. Are these\n        data consistent with the null hypothesis that the parents diabetic\n        status does not affect their children\'s blood glucose levels?\n        Calculating the F statistic from the data gives a value of 36.01.\n\n        Draw samples from the distribution:\n\n        >>> dfnum = 1. # between group degrees of freedom\n        >>> dfden = 48. # within groups degrees of freedom\n        >>> s = np.random.f(dfnum, dfden, 1000)\n\n        The lower bound for the top 1% of the samples is :\n\n        >>> np.sort(s)[-10]\n        7.61988120985 # random\n\n        So there is about a 1% chance that the F statistic will exceed 7.62,\n        the measured value is 36, so the null hypothesis is rejected at the 1%\n        level.\n\n        ',
    'RandomState.gamma (line 1628)': '\n        gamma(shape, scale=1.0, size=None)\n\n        Draw samples from a Gamma distribution.\n\n        Samples are drawn from a Gamma distribution with specified parameters,\n        `shape` (sometimes designated "k") and `scale` (sometimes designated\n        "theta"), where both parameters are > 0.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.gamma`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        shape : float or array_like of floats\n            The shape of the gamma distribution. Must be non-negative.\n        scale : float or array_like of floats, optional\n            The scale of the gamma distribution. Must be non-negative.\n            Default is equal to 1.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``shape`` and ``scale`` are both scalars.\n            Otherwise, ``np.broadcast(shape, scale).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized gamma distribution.\n\n        See Also\n        --------\n        scipy.stats.gamma : probability density function, distribution or\n            cumulative density function, etc.\n        random.Generator.gamma: which should be used for new code.\n\n        Notes\n        -----\n        The probability density for the Gamma distribution is\n\n        .. math:: p(x) = x^{k-1}\\frac{e^{-x/\\theta}}{\\theta^k\\Gamma(k)},\n\n        where :math:`k` is the shape and :math:`\\theta` the scale,\n        and :math:`\\Gamma` is the Gamma function.\n\n        The Gamma distribution is often used to model the times to failure of\n        electronic components, and arises naturally in processes for which the\n        waiting times between Poisson distributed events are relevant.\n\n        References\n        ----------\n        .. [1] Weisstein, Eric W. "Gamma Distribution." From MathWorld--A\n               Wolfram Web Resource.\n               http://mathworld.wolfram.com/GammaDistribution.html\n        .. [2] Wikipedia, "Gamma distribution",\n               https://en.wikipedia.org/wiki/Gamma_distribution\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        >>> shape, scale = 2., 2.  # mean=4, std=2*sqrt(2)\n        >>> s = np.random.gamma(shape, scale, 1000)\n\n        Display the histogram of the samples, along with\n        the probability density function:\n\n        >>> import matplotlib.pyplot as plt\n        >>> import scipy.special as sps  # doctest: +SKIP\n        >>> count, bins, ignored = plt.hist(s, 50, density=True)\n        >>> y = bins**(shape-1)*(np.exp(-bins/scale) /  # doctest: +SKIP\n        ...                      (sps.gamma(shape)*scale**shape))\n        >>> plt.plot(bins, y, linewidth=2, color=\'r\')  # doctest: +SKIP\n        >>> plt.show()\n\n        ',
    'RandomState.geometric (line 3755)': '\n        geometric(p, size=None)\n\n        Draw samples from the geometric distribution.\n\n        Bernoulli trials are experiments with one of two outcomes:\n        success or failure (an example of such an experiment is flipping\n        a coin).  The geometric distribution models the number of trials\n        that must be run in order to achieve success.  It is therefore\n        supported on the positive integers, ``k = 1, 2, ...``.\n\n        The probability mass function of the geometric distribution is\n\n        .. math:: f(k) = (1 - p)^{k - 1} p\n\n        where `p` is the probability of success of an individual trial.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.geometric`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        p : float or array_like of floats\n            The probability of success of an individual trial.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``p`` is a scalar.  Otherwise,\n            ``np.array(p).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized geometric distribution.\n\n        See Also\n        --------\n        random.Generator.geometric: which should be used for new code.\n\n        Examples\n        --------\n        Draw ten thousand values from the geometric distribution,\n        with the probability of an individual success equal to 0.35:\n\n        >>> z = np.random.geometric(p=0.35, size=10000)\n\n        How many trials succeeded after a single run?\n\n        >>> (z == 1).sum() / 10000.\n        0.34889999999999999 #random\n\n        ',
    'RandomState.gumbel (line 2747)': '\n        gumbel(loc=0.0, scale=1.0, size=None)\n\n        Draw samples from a Gumbel distribution.\n\n        Draw samples from a Gumbel distribution with specified location and\n        scale.  For more information on the Gumbel distribution, see\n        Notes and References below.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.gumbel`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        loc : float or array_like of floats, optional\n            The location of the mode of the distribution. Default is 0.\n        scale : float or array_like of floats, optional\n            The scale parameter of the distribution. Default is 1. Must be non-\n            negative.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``loc`` and ``scale`` are both scalars.\n            Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized Gumbel distribution.\n\n        See Also\n        --------\n        scipy.stats.gumbel_l\n        scipy.stats.gumbel_r\n        scipy.stats.genextreme\n        weibull\n        random.Generator.gumbel: which should be used for new code.\n\n        Notes\n        -----\n        The Gumbel (or Smallest Extreme Value (SEV) or the Smallest Extreme\n        Value Type I) distribution is one of a class of Generalized Extreme\n        Value (GEV) distributions used in modeling extreme value problems.\n        The Gumbel is a special case of the Extreme Value Type I distribution\n        for maximums from distributions with "exponential-like" tails.\n\n        The probability density for the Gumbel distribution is\n\n        .. math:: p(x) = \\frac{e^{-(x - \\mu)/ \\beta}}{\\beta} e^{ -e^{-(x - \\mu)/\n                  \\beta}},\n\n        where :math:`\\mu` is the mode, a location parameter, and\n        :math:`\\beta` is the scale parameter.\n\n        The Gumbel (named for German mathematician Emil Julius Gumbel) was used\n        very early in the hydrology literature, for modeling the occurrence of\n        flood events. It is also used for modeling maximum wind speed and\n        rainfall rates.  It is a "fat-tailed" distribution - the probability of\n        an event in the tail of the distribution is larger than if one used a\n        Gaussian, hence the surprisingly frequent occurrence of 100-year\n        floods. Floods were initially modeled as a Gaussian process, which\n        underestimated the frequency of extreme events.\n\n        It is one of a class of extreme value distributions, the Generalized\n        Extreme Value (GEV) distributions, which also includes the Weibull and\n        Frechet.\n\n        The function has a mean of :math:`\\mu + 0.57721\\beta` and a variance\n        of :math:`\\frac{\\pi^2}{6}\\beta^2`.\n\n        References\n        ----------\n        .. [1] Gumbel, E. J., "Statistics of Extremes,"\n               New York: Columbia University Press, 1958.\n        .. [2] Reiss, R.-D. and Thomas, M., "Statistical Analysis of Extreme\n               Values from Insurance, Finance, Hydrology and Other Fields,"\n               Basel: Birkhauser Verlag, 2001.\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        >>> mu, beta = 0, 0.1 # location and scale\n        >>> s = np.random.gumbel(mu, beta, 1000)\n\n        Display the histogram of the samples, along with\n        the probability density function:\n\n        >>> import matplotlib.pyplot as plt\n        >>> count, bins, ignored = plt.hist(s, 30, density=True)\n        >>> plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)\n        ...          * np.exp( -np.exp( -(bins - mu) /beta) ),\n        ...          linewidth=2, color=\'r\')\n        >>> plt.show()\n\n        Show how an extreme value distribution can arise from a Gaussian process\n        and compare to a Gaussian:\n\n        >>> means = []\n        >>> maxima = []\n        >>> for i in range(0,1000) :\n        ...    a = np.random.normal(mu, beta, 1000)\n        ...    means.append(a.mean())\n        ...    maxima.append(a.max())\n        >>> count, bins, ignored = plt.hist(maxima, 30, density=True)\n        >>> beta = np.std(maxima) * np.sqrt(6) / np.pi\n        >>> mu = np.mean(maxima) - 0.57721*beta\n        >>> plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)\n        ...          * np.exp(-np.exp(-(bins - mu)/beta)),\n        ...          linewidth=2, color=\'r\')\n        >>> plt.plot(bins, 1/(beta * np.sqrt(2 * np.pi))\n        ...          * np.exp(-(bins - mu)**2 / (2 * beta**2)),\n        ...          linewidth=2, color=\'g\')\n        >>> plt.show()\n\n        ',
    'RandomState.hypergeometric (line 3817)': '\n        hypergeometric(ngood, nbad, nsample, size=None)\n\n        Draw samples from a Hypergeometric distribution.\n\n        Samples are drawn from a hypergeometric distribution with specified\n        parameters, `ngood` (ways to make a good selection), `nbad` (ways to make\n        a bad selection), and `nsample` (number of items sampled, which is less\n        than or equal to the sum ``ngood + nbad``).\n\n        .. note::\n            New code should use the\n            `~numpy.random.Generator.hypergeometric`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        ngood : int or array_like of ints\n            Number of ways to make a good selection.  Must be nonnegative.\n        nbad : int or array_like of ints\n            Number of ways to make a bad selection.  Must be nonnegative.\n        nsample : int or array_like of ints\n            Number of items sampled.  Must be at least 1 and at most\n            ``ngood + nbad``.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if `ngood`, `nbad`, and `nsample`\n            are all scalars.  Otherwise, ``np.broadcast(ngood, nbad, nsample).size``\n            samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized hypergeometric distribution. Each\n            sample is the number of good items within a randomly selected subset of\n            size `nsample` taken from a set of `ngood` good items and `nbad` bad items.\n\n        See Also\n        --------\n        scipy.stats.hypergeom : probability density function, distribution or\n            cumulative density function, etc.\n        random.Generator.hypergeometric: which should be used for new code.\n\n        Notes\n        -----\n        The probability density for the Hypergeometric distribution is\n\n        .. math:: P(x) = \\frac{\\binom{g}{x}\\binom{b}{n-x}}{\\binom{g+b}{n}},\n\n        where :math:`0 \\le x \\le n` and :math:`n-b \\le x \\le g`\n\n        for P(x) the probability of ``x`` good results in the drawn sample,\n        g = `ngood`, b = `nbad`, and n = `nsample`.\n\n        Consider an urn with black and white marbles in it, `ngood` of them\n        are black and `nbad` are white. If you draw `nsample` balls without\n        replacement, then the hypergeometric distribution describes the\n        distribution of black balls in the drawn sample.\n\n        Note that this distribution is very similar to the binomial\n        distribution, except that in this case, samples are drawn without\n        replacement, whereas in the Binomial case samples are drawn with\n        replacement (or the sample space is infinite). As the sample space\n        becomes large, this distribution approaches the binomial.\n\n        References\n        ----------\n        .. [1] Lentner, Marvin, "Elementary Applied Statistics", Bogden\n               and Quigley, 1972.\n        .. [2] Weisstein, Eric W. "Hypergeometric Distribution." From\n               MathWorld--A Wolfram Web Resource.\n               http://mathworld.wolfram.com/HypergeometricDistribution.html\n        .. [3] Wikipedia, "Hypergeometric distribution",\n               https://en.wikipedia.org/wiki/Hypergeometric_distribution\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        >>> ngood, nbad, nsamp = 100, 2, 10\n        # number of good, number of bad, and number of samples\n        >>> s = np.random.hypergeometric(ngood, nbad, nsamp, 1000)\n        >>> from matplotlib.pyplot import hist\n        >>> hist(s)\n        #   note that it is very unlikely to grab both bad items\n\n        Suppose you have an urn with 15 white and 15 black marbles.\n        If you pull 15 marbles at random, how likely is it that\n        12 or more of them are one color?\n\n        >>> s = np.random.hypergeometric(15, 15, 15, 100000)\n        >>> sum(s>=12)/100000. + sum(s<=3)/100000.\n        #   answer = 0.003 ... pretty unlikely!\n\n        ',
    'RandomState.laplace (line 2653)': '\n        laplace(loc=0.0, scale=1.0, size=None)\n\n        Draw samples from the Laplace or double exponential distribution with\n        specified location (or mean) and scale (decay).\n\n        The Laplace distribution is similar to the Gaussian/normal distribution,\n        but is sharper at the peak and has fatter tails. It represents the\n        difference between two independent, identically distributed exponential\n        random variables.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.laplace`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        loc : float or array_like of floats, optional\n            The position, :math:`\\mu`, of the distribution peak. Default is 0.\n        scale : float or array_like of floats, optional\n            :math:`\\lambda`, the exponential decay. Default is 1. Must be non-\n            negative.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``loc`` and ``scale`` are both scalars.\n            Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized Laplace distribution.\n\n        See Also\n        --------\n        random.Generator.laplace: which should be used for new code.\n\n        Notes\n        -----\n        It has the probability density function\n\n        .. math:: f(x; \\mu, \\lambda) = \\frac{1}{2\\lambda}\n                                       \\exp\\left(-\\frac{|x - \\mu|}{\\lambda}\\right).\n\n        The first law of Laplace, from 1774, states that the frequency\n        of an error can be expressed as an exponential function of the\n        absolute magnitude of the error, which leads to the Laplace\n        distribution. For many problems in economics and health\n        sciences, this distribution seems to model the data better\n        than the standard Gaussian distribution.\n\n        References\n        ----------\n        .. [1] Abramowitz, M. and Stegun, I. A. (Eds.). "Handbook of\n               Mathematical Functions with Formulas, Graphs, and Mathematical\n               Tables, 9th printing," New York: Dover, 1972.\n        .. [2] Kotz, Samuel, et. al. "The Laplace Distribution and\n               Generalizations, " Birkhauser, 2001.\n        .. [3] Weisstein, Eric W. "Laplace Distribution."\n               From MathWorld--A Wolfram Web Resource.\n               http://mathworld.wolfram.com/LaplaceDistribution.html\n        .. [4] Wikipedia, "Laplace distribution",\n               https://en.wikipedia.org/wiki/Laplace_distribution\n\n        Examples\n        --------\n        Draw samples from the distribution\n\n        >>> loc, scale = 0., 1.\n        >>> s = np.random.laplace(loc, scale, 1000)\n\n        Display the histogram of the samples, along with\n        the probability density function:\n\n        >>> import matplotlib.pyplot as plt\n        >>> count, bins, ignored = plt.hist(s, 30, density=True)\n        >>> x = np.arange(-8., 8., .01)\n        >>> pdf = np.exp(-abs(x-loc)/scale)/(2.*scale)\n        >>> plt.plot(x, pdf)\n\n        Plot Gaussian for comparison:\n\n        >>> g = (1/(scale * np.sqrt(2 * np.pi)) *\n        ...      np.exp(-(x - loc)**2 / (2 * scale**2)))\n        >>> plt.plot(x,g)\n\n        ',
    'RandomState.logistic (line 2871)': '\n        logistic(loc=0.0, scale=1.0, size=None)\n\n        Draw samples from a logistic distribution.\n\n        Samples are drawn from a logistic distribution with specified\n        parameters, loc (location or mean, also median), and scale (>0).\n\n        .. note::\n            New code should use the `~numpy.random.Generator.logistic`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        loc : float or array_like of floats, optional\n            Parameter of the distribution. Default is 0.\n        scale : float or array_like of floats, optional\n            Parameter of the distribution. Must be non-negative.\n            Default is 1.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``loc`` and ``scale`` are both scalars.\n            Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized logistic distribution.\n\n        See Also\n        --------\n        scipy.stats.logistic : probability density function, distribution or\n            cumulative density function, etc.\n        random.Generator.logistic: which should be used for new code.\n\n        Notes\n        -----\n        The probability density for the Logistic distribution is\n\n        .. math:: P(x) = P(x) = \\frac{e^{-(x-\\mu)/s}}{s(1+e^{-(x-\\mu)/s})^2},\n\n        where :math:`\\mu` = location and :math:`s` = scale.\n\n        The Logistic distribution is used in Extreme Value problems where it\n        can act as a mixture of Gumbel distributions, in Epidemiology, and by\n        the World Chess Federation (FIDE) where it is used in the Elo ranking\n        system, assuming the performance of each player is a logistically\n        distributed random variable.\n\n        References\n        ----------\n        .. [1] Reiss, R.-D. and Thomas M. (2001), "Statistical Analysis of\n               Extreme Values, from Insurance, Finance, Hydrology and Other\n               Fields," Birkhauser Verlag, Basel, pp 132-133.\n        .. [2] Weisstein, Eric W. "Logistic Distribution." From\n               MathWorld--A Wolfram Web Resource.\n               http://mathworld.wolfram.com/LogisticDistribution.html\n        .. [3] Wikipedia, "Logistic-distribution",\n               https://en.wikipedia.org/wiki/Logistic_distribution\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        >>> loc, scale = 10, 1\n        >>> s = np.random.logistic(loc, scale, 10000)\n        >>> import matplotlib.pyplot as plt\n        >>> count, bins, ignored = plt.hist(s, bins=50)\n\n        #   plot against distribution\n\n        >>> def logist(x, loc, scale):\n        ...     return np.exp((loc-x)/scale)/(scale*(1+np.exp((loc-x)/scale))**2)\n        >>> lgst_val = logist(bins, loc, scale)\n        >>> plt.plot(bins, lgst_val * count.max() / lgst_val.max())\n        >>> plt.show()\n\n        ',
    'RandomState.lognormal (line 2957)': '\n        lognormal(mean=0.0, sigma=1.0, size=None)\n\n        Draw samples from a log-normal distribution.\n\n        Draw samples from a log-normal distribution with specified mean,\n        standard deviation, and array shape.  Note that the mean and standard\n        deviation are not the values for the distribution itself, but of the\n        underlying normal distribution it is derived from.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.lognormal`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        mean : float or array_like of floats, optional\n            Mean value of the underlying normal distribution. Default is 0.\n        sigma : float or array_like of floats, optional\n            Standard deviation of the underlying normal distribution. Must be\n            non-negative. Default is 1.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``mean`` and ``sigma`` are both scalars.\n            Otherwise, ``np.broadcast(mean, sigma).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized log-normal distribution.\n\n        See Also\n        --------\n        scipy.stats.lognorm : probability density function, distribution,\n            cumulative density function, etc.\n        random.Generator.lognormal: which should be used for new code.\n\n        Notes\n        -----\n        A variable `x` has a log-normal distribution if `log(x)` is normally\n        distributed.  The probability density function for the log-normal\n        distribution is:\n\n        .. math:: p(x) = \\frac{1}{\\sigma x \\sqrt{2\\pi}}\n                         e^{(-\\frac{(ln(x)-\\mu)^2}{2\\sigma^2})}\n\n        where :math:`\\mu` is the mean and :math:`\\sigma` is the standard\n        deviation of the normally distributed logarithm of the variable.\n        A log-normal distribution results if a random variable is the *product*\n        of a large number of independent, identically-distributed variables in\n        the same way that a normal distribution results if the variable is the\n        *sum* of a large number of independent, identically-distributed\n        variables.\n\n        References\n        ----------\n        .. [1] Limpert, E., Stahel, W. A., and Abbt, M., "Log-normal\n               Distributions across the Sciences: Keys and Clues,"\n               BioScience, Vol. 51, No. 5, May, 2001.\n               https://stat.ethz.ch/~stahel/lognormal/bioscience.pdf\n        .. [2] Reiss, R.D. and Thomas, M., "Statistical Analysis of Extreme\n               Values," Basel: Birkhauser Verlag, 2001, pp. 31-32.\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        >>> mu, sigma = 3., 1. # mean and standard deviation\n        >>> s = np.random.lognormal(mu, sigma, 1000)\n\n        Display the histogram of the samples, along with\n        the probability density function:\n\n        >>> import matplotlib.pyplot as plt\n        >>> count, bins, ignored = plt.hist(s, 100, density=True, align=\'mid\')\n\n        >>> x = np.linspace(min(bins), max(bins), 10000)\n        >>> pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))\n        ...        / (x * sigma * np.sqrt(2 * np.pi)))\n\n        >>> plt.plot(x, pdf, linewidth=2, color=\'r\')\n        >>> plt.axis(\'tight\')\n        >>> plt.show()\n\n        Demonstrate that taking the products of random samples from a uniform\n        distribution can be fit well by a log-normal probability density\n        function.\n\n        >>> # Generate a thousand samples: each is the product of 100 random\n        >>> # values, drawn from a normal distribution.\n        >>> b = []\n        >>> for i in range(1000):\n        ...    a = 10. + np.random.standard_normal(100)\n        ...    b.append(np.product(a))\n\n        >>> b = np.array(b) / np.min(b) # scale values to be positive\n        >>> count, bins, ignored = plt.hist(b, 100, density=True, align=\'mid\')\n        >>> sigma = np.std(np.log(b))\n        >>> mu = np.mean(np.log(b))\n\n        >>> x = np.linspace(min(bins), max(bins), 10000)\n        >>> pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))\n        ...        / (x * sigma * np.sqrt(2 * np.pi)))\n\n        >>> plt.plot(x, pdf, color=\'r\', linewidth=2)\n        >>> plt.show()\n\n        ',
    'RandomState.logseries (line 3952)': '\n        logseries(p, size=None)\n\n        Draw samples from a logarithmic series distribution.\n\n        Samples are drawn from a log series distribution with specified\n        shape parameter, 0 <= ``p`` < 1.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.logseries`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        p : float or array_like of floats\n            Shape parameter for the distribution.  Must be in the range [0, 1).\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``p`` is a scalar.  Otherwise,\n            ``np.array(p).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized logarithmic series distribution.\n\n        See Also\n        --------\n        scipy.stats.logser : probability density function, distribution or\n            cumulative density function, etc.\n        random.Generator.logseries: which should be used for new code.\n\n        Notes\n        -----\n        The probability density for the Log Series distribution is\n\n        .. math:: P(k) = \\frac{-p^k}{k \\ln(1-p)},\n\n        where p = probability.\n\n        The log series distribution is frequently used to represent species\n        richness and occurrence, first proposed by Fisher, Corbet, and\n        Williams in 1943 [2].  It may also be used to model the numbers of\n        occupants seen in cars [3].\n\n        References\n        ----------\n        .. [1] Buzas, Martin A.; Culver, Stephen J.,  Understanding regional\n               species diversity through the log series distribution of\n               occurrences: BIODIVERSITY RESEARCH Diversity & Distributions,\n               Volume 5, Number 5, September 1999 , pp. 187-195(9).\n        .. [2] Fisher, R.A,, A.S. Corbet, and C.B. Williams. 1943. The\n               relation between the number of species and the number of\n               individuals in a random sample of an animal population.\n               Journal of Animal Ecology, 12:42-58.\n        .. [3] D. J. Hand, F. Daly, D. Lunn, E. Ostrowski, A Handbook of Small\n               Data Sets, CRC Press, 1994.\n        .. [4] Wikipedia, "Logarithmic distribution",\n               https://en.wikipedia.org/wiki/Logarithmic_distribution\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        >>> a = .6\n        >>> s = np.random.logseries(a, 10000)\n        >>> import matplotlib.pyplot as plt\n        >>> count, bins, ignored = plt.hist(s)\n\n        #   plot against distribution\n\n        >>> def logseries(k, p):\n        ...     return -p**k/(k*np.log(1-p))\n        >>> plt.plot(bins, logseries(bins, a)*count.max()/\n        ...          logseries(bins, a).max(), \'r\')\n        >>> plt.show()\n\n        ',
    'RandomState.multinomial (line 4240)': '\n        multinomial(n, pvals, size=None)\n\n        Draw samples from a multinomial distribution.\n\n        The multinomial distribution is a multivariate generalization of the\n        binomial distribution.  Take an experiment with one of ``p``\n        possible outcomes.  An example of such an experiment is throwing a dice,\n        where the outcome can be 1 through 6.  Each sample drawn from the\n        distribution represents `n` such experiments.  Its values,\n        ``X_i = [X_0, X_1, ..., X_p]``, represent the number of times the\n        outcome was ``i``.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.multinomial`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        n : int\n            Number of experiments.\n        pvals : sequence of floats, length p\n            Probabilities of each of the ``p`` different outcomes.  These\n            must sum to 1 (however, the last element is always assumed to\n            account for the remaining probability, as long as\n            ``sum(pvals[:-1]) <= 1)``.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  Default is None, in which case a\n            single value is returned.\n\n        Returns\n        -------\n        out : ndarray\n            The drawn samples, of shape *size*, if that was provided.  If not,\n            the shape is ``(N,)``.\n\n            In other words, each entry ``out[i,j,...,:]`` is an N-dimensional\n            value drawn from the distribution.\n\n        See Also\n        --------\n        random.Generator.multinomial: which should be used for new code.\n\n        Examples\n        --------\n        Throw a dice 20 times:\n\n        >>> np.random.multinomial(20, [1/6.]*6, size=1)\n        array([[4, 1, 7, 5, 2, 1]]) # random\n\n        It landed 4 times on 1, once on 2, etc.\n\n        Now, throw the dice 20 times, and 20 times again:\n\n        >>> np.random.multinomial(20, [1/6.]*6, size=2)\n        array([[3, 4, 3, 3, 4, 3], # random\n               [2, 4, 3, 4, 0, 7]])\n\n        For the first run, we threw 3 times 1, 4 times 2, etc.  For the second,\n        we threw 2 times 1, 4 times 2, etc.\n\n        A loaded die is more likely to land on number 6:\n\n        >>> np.random.multinomial(100, [1/7.]*5 + [2/7.])\n        array([11, 16, 14, 17, 16, 26]) # random\n\n        The probability inputs should be normalized. As an implementation\n        detail, the value of the last entry is ignored and assumed to take\n        up any leftover probability mass, but this should not be relied on.\n        A biased coin which has twice as much weight on one side as on the\n        other should be sampled like so:\n\n        >>> np.random.multinomial(100, [1.0 / 3, 2.0 / 3])  # RIGHT\n        array([38, 62]) # random\n\n        not like:\n\n        >>> np.random.multinomial(100, [1.0, 2.0])  # WRONG\n        Traceback (most recent call last):\n        ValueError: pvals < 0, pvals > 1 or pvals contains NaNs\n\n        ',
    'RandomState.multivariate_normal (line 4041)': '\n        multivariate_normal(mean, cov, size=None, check_valid=\'warn\', tol=1e-8)\n\n        Draw random samples from a multivariate normal distribution.\n\n        The multivariate normal, multinormal or Gaussian distribution is a\n        generalization of the one-dimensional normal distribution to higher\n        dimensions.  Such a distribution is specified by its mean and\n        covariance matrix.  These parameters are analogous to the mean\n        (average or "center") and variance (standard deviation, or "width,"\n        squared) of the one-dimensional normal distribution.\n\n        .. note::\n            New code should use the\n            `~numpy.random.Generator.multivariate_normal`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        mean : 1-D array_like, of length N\n            Mean of the N-dimensional distribution.\n        cov : 2-D array_like, of shape (N, N)\n            Covariance matrix of the distribution. It must be symmetric and\n            positive-semidefinite for proper sampling.\n        size : int or tuple of ints, optional\n            Given a shape of, for example, ``(m,n,k)``, ``m*n*k`` samples are\n            generated, and packed in an `m`-by-`n`-by-`k` arrangement.  Because\n            each sample is `N`-dimensional, the output shape is ``(m,n,k,N)``.\n            If no shape is specified, a single (`N`-D) sample is returned.\n        check_valid : { \'warn\', \'raise\', \'ignore\' }, optional\n            Behavior when the covariance matrix is not positive semidefinite.\n        tol : float, optional\n            Tolerance when checking the singular values in covariance matrix.\n            cov is cast to double before the check.\n\n        Returns\n        -------\n        out : ndarray\n            The drawn samples, of shape *size*, if that was provided.  If not,\n            the shape is ``(N,)``.\n\n            In other words, each entry ``out[i,j,...,:]`` is an N-dimensional\n            value drawn from the distribution.\n\n        See Also\n        --------\n        random.Generator.multivariate_normal: which should be used for new code.\n\n        Notes\n        -----\n        The mean is a coordinate in N-dimensional space, which represents the\n        location where samples are most likely to be generated.  This is\n        analogous to the peak of the bell curve for the one-dimensional or\n        univariate normal distribution.\n\n        Covariance indicates the level to which two variables vary together.\n        From the multivariate normal distribution, we draw N-dimensional\n        samples, :math:`X = [x_1, x_2, ... x_N]`.  The covariance matrix\n        element :math:`C_{ij}` is the covariance of :math:`x_i` and :math:`x_j`.\n        The element :math:`C_{ii}` is the variance of :math:`x_i` (i.e. its\n        "spread").\n\n        Instead of specifying the full covariance matrix, popular\n        approximations include:\n\n          - Spherical covariance (`cov` is a multiple of the identity matrix)\n          - Diagonal covariance (`cov` has non-negative elements, and only on\n            the diagonal)\n\n        This geometrical property can be seen in two dimensions by plotting\n        generated data-points:\n\n        >>> mean = [0, 0]\n        >>> cov = [[1, 0], [0, 100]]  # diagonal covariance\n\n        Diagonal covariance means that points are oriented along x or y-axis:\n\n        >>> import matplotlib.pyplot as plt\n        >>> x, y = np.random.multivariate_normal(mean, cov, 5000).T\n        >>> plt.plot(x, y, \'x\')\n        >>> plt.axis(\'equal\')\n        >>> plt.show()\n\n        Note that the covariance matrix must be positive semidefinite (a.k.a.\n        nonnegative-definite). Otherwise, the behavior of this method is\n        undefined and backwards compatibility is not guaranteed.\n\n        References\n        ----------\n        .. [1] Papoulis, A., "Probability, Random Variables, and Stochastic\n               Processes," 3rd ed., New York: McGraw-Hill, 1991.\n        .. [2] Duda, R. O., Hart, P. E., and Stork, D. G., "Pattern\n               Classification," 2nd ed., New York: Wiley, 2001.\n\n        Examples\n        --------\n        >>> mean = (1, 2)\n        >>> cov = [[1, 0], [0, 1]]\n        >>> x = np.random.multivariate_normal(mean, cov, (3, 3))\n        >>> x.shape\n        (3, 3, 2)\n\n        Here we generate 800 samples from the bivariate normal distribution\n        with mean [0, 0] and covariance matrix [[6, -3], [-3, 3.5]].  The\n        expected variances of the first and second components of the sample\n        are 6 and 3.5, respectively, and the expected correlation\n        coefficient is -3/sqrt(6*3.5) ≈ -0.65465.\n\n        >>> cov = np.array([[6, -3], [-3, 3.5]])\n        >>> pts = np.random.multivariate_normal([0, 0], cov, size=800)\n\n        Check that the mean, covariance, and correlation coefficient of the\n        sample are close to the expected values:\n\n        >>> pts.mean(axis=0)\n        array([ 0.0326911 , -0.01280782])  # may vary\n        >>> np.cov(pts.T)\n        array([[ 5.96202397, -2.85602287],\n               [-2.85602287,  3.47613949]])  # may vary\n        >>> np.corrcoef(pts.T)[0, 1]\n        -0.6273591314603949  # may vary\n\n        We can visualize this data with a scatter plot.  The orientation\n        of the point cloud illustrates the negative correlation of the\n        components of this sample.\n\n        >>> import matplotlib.pyplot as plt\n        >>> plt.plot(pts[:, 0], pts[:, 1], \'.\', alpha=0.5)\n        >>> plt.axis(\'equal\')\n        >>> plt.grid()\n        >>> plt.show()\n        ',
    'RandomState.negative_binomial (line 3488)': '\n        negative_binomial(n, p, size=None)\n\n        Draw samples from a negative binomial distribution.\n\n        Samples are drawn from a negative binomial distribution with specified\n        parameters, `n` successes and `p` probability of success where `n`\n        is > 0 and `p` is in the interval [0, 1].\n\n        .. note::\n            New code should use the\n            `~numpy.random.Generator.negative_binomial`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        n : float or array_like of floats\n            Parameter of the distribution, > 0.\n        p : float or array_like of floats\n            Parameter of the distribution, >= 0 and <=1.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``n`` and ``p`` are both scalars.\n            Otherwise, ``np.broadcast(n, p).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized negative binomial distribution,\n            where each sample is equal to N, the number of failures that\n            occurred before a total of n successes was reached.\n\n        See Also\n        --------\n        random.Generator.negative_binomial: which should be used for new code.\n\n        Notes\n        -----\n        The probability mass function of the negative binomial distribution is\n\n        .. math:: P(N;n,p) = \\frac{\\Gamma(N+n)}{N!\\Gamma(n)}p^{n}(1-p)^{N},\n\n        where :math:`n` is the number of successes, :math:`p` is the\n        probability of success, :math:`N+n` is the number of trials, and\n        :math:`\\Gamma` is the gamma function. When :math:`n` is an integer,\n        :math:`\\frac{\\Gamma(N+n)}{N!\\Gamma(n)} = \\binom{N+n-1}{N}`, which is\n        the more common form of this term in the pmf. The negative\n        binomial distribution gives the probability of N failures given n\n        successes, with a success on the last trial.\n\n        If one throws a die repeatedly until the third time a "1" appears,\n        then the probability distribution of the number of non-"1"s that\n        appear before the third "1" is a negative binomial distribution.\n\n        References\n        ----------\n        .. [1] Weisstein, Eric W. "Negative Binomial Distribution." From\n               MathWorld--A Wolfram Web Resource.\n               http://mathworld.wolfram.com/NegativeBinomialDistribution.html\n        .. [2] Wikipedia, "Negative binomial distribution",\n               https://en.wikipedia.org/wiki/Negative_binomial_distribution\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        A real world example. A company drills wild-cat oil\n        exploration wells, each with an estimated probability of\n        success of 0.1.  What is the probability of having one success\n        for each successive well, that is what is the probability of a\n        single success after drilling 5 wells, after 6 wells, etc.?\n\n        >>> s = np.random.negative_binomial(1, 0.1, 100000)\n        >>> for i in range(1, 11): # doctest: +SKIP\n        ...    probability = sum(s<i) / 100000.\n        ...    print(i, "wells drilled, probability of one success =", probability)\n\n        ',
    'RandomState.noncentral_chisquare (line 1969)': '\n        noncentral_chisquare(df, nonc, size=None)\n\n        Draw samples from a noncentral chi-square distribution.\n\n        The noncentral :math:`\\chi^2` distribution is a generalization of\n        the :math:`\\chi^2` distribution.\n\n        .. note::\n            New code should use the\n            `~numpy.random.Generator.noncentral_chisquare`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        df : float or array_like of floats\n            Degrees of freedom, must be > 0.\n\n            .. versionchanged:: 1.10.0\n               Earlier NumPy versions required dfnum > 1.\n        nonc : float or array_like of floats\n            Non-centrality, must be non-negative.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``df`` and ``nonc`` are both scalars.\n            Otherwise, ``np.broadcast(df, nonc).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized noncentral chi-square distribution.\n\n        See Also\n        --------\n        random.Generator.noncentral_chisquare: which should be used for new code.\n\n        Notes\n        -----\n        The probability density function for the noncentral Chi-square\n        distribution is\n\n        .. math:: P(x;df,nonc) = \\sum^{\\infty}_{i=0}\n                               \\frac{e^{-nonc/2}(nonc/2)^{i}}{i!}\n                               P_{Y_{df+2i}}(x),\n\n        where :math:`Y_{q}` is the Chi-square with q degrees of freedom.\n\n        References\n        ----------\n        .. [1] Wikipedia, "Noncentral chi-squared distribution"\n               https://en.wikipedia.org/wiki/Noncentral_chi-squared_distribution\n\n        Examples\n        --------\n        Draw values from the distribution and plot the histogram\n\n        >>> import matplotlib.pyplot as plt\n        >>> values = plt.hist(np.random.noncentral_chisquare(3, 20, 100000),\n        ...                   bins=200, density=True)\n        >>> plt.show()\n\n        Draw values from a noncentral chisquare with very small noncentrality,\n        and compare to a chisquare.\n\n        >>> plt.figure()\n        >>> values = plt.hist(np.random.noncentral_chisquare(3, .0000001, 100000),\n        ...                   bins=np.arange(0., 25, .1), density=True)\n        >>> values2 = plt.hist(np.random.chisquare(3, 100000),\n        ...                    bins=np.arange(0., 25, .1), density=True)\n        >>> plt.plot(values[1][0:-1], values[0]-values2[0], \'ob\')\n        >>> plt.show()\n\n        Demonstrate how large values of non-centrality lead to a more symmetric\n        distribution.\n\n        >>> plt.figure()\n        >>> values = plt.hist(np.random.noncentral_chisquare(3, 20, 100000),\n        ...                   bins=200, density=True)\n        >>> plt.show()\n\n        ',
    'RandomState.noncentral_f (line 1806)': '\n        noncentral_f(dfnum, dfden, nonc, size=None)\n\n        Draw samples from the noncentral F distribution.\n\n        Samples are drawn from an F distribution with specified parameters,\n        `dfnum` (degrees of freedom in numerator) and `dfden` (degrees of\n        freedom in denominator), where both parameters > 1.\n        `nonc` is the non-centrality parameter.\n\n        .. note::\n            New code should use the\n            `~numpy.random.Generator.noncentral_f`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        dfnum : float or array_like of floats\n            Numerator degrees of freedom, must be > 0.\n\n            .. versionchanged:: 1.14.0\n               Earlier NumPy versions required dfnum > 1.\n        dfden : float or array_like of floats\n            Denominator degrees of freedom, must be > 0.\n        nonc : float or array_like of floats\n            Non-centrality parameter, the sum of the squares of the numerator\n            means, must be >= 0.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``dfnum``, ``dfden``, and ``nonc``\n            are all scalars.  Otherwise, ``np.broadcast(dfnum, dfden, nonc).size``\n            samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized noncentral Fisher distribution.\n\n        See Also\n        --------\n        random.Generator.noncentral_f: which should be used for new code.\n\n        Notes\n        -----\n        When calculating the power of an experiment (power = probability of\n        rejecting the null hypothesis when a specific alternative is true) the\n        non-central F statistic becomes important.  When the null hypothesis is\n        true, the F statistic follows a central F distribution. When the null\n        hypothesis is not true, then it follows a non-central F statistic.\n\n        References\n        ----------\n        .. [1] Weisstein, Eric W. "Noncentral F-Distribution."\n               From MathWorld--A Wolfram Web Resource.\n               http://mathworld.wolfram.com/NoncentralF-Distribution.html\n        .. [2] Wikipedia, "Noncentral F-distribution",\n               https://en.wikipedia.org/wiki/Noncentral_F-distribution\n\n        Examples\n        --------\n        In a study, testing for a specific alternative to the null hypothesis\n        requires use of the Noncentral F distribution. We need to calculate the\n        area in the tail of the distribution that exceeds the value of the F\n        distribution for the null hypothesis.  We\'ll plot the two probability\n        distributions for comparison.\n\n        >>> dfnum = 3 # between group deg of freedom\n        >>> dfden = 20 # within groups degrees of freedom\n        >>> nonc = 3.0\n        >>> nc_vals = np.random.noncentral_f(dfnum, dfden, nonc, 1000000)\n        >>> NF = np.histogram(nc_vals, bins=50, density=True)\n        >>> c_vals = np.random.f(dfnum, dfden, 1000000)\n        >>> F = np.histogram(c_vals, bins=50, density=True)\n        >>> import matplotlib.pyplot as plt\n        >>> plt.plot(F[1][1:], F[0])\n        >>> plt.plot(NF[1][1:], NF[0])\n        >>> plt.show()\n\n        ',
    'RandomState.normal (line 1437)': '\n        normal(loc=0.0, scale=1.0, size=None)\n\n        Draw random samples from a normal (Gaussian) distribution.\n\n        The probability density function of the normal distribution, first\n        derived by De Moivre and 200 years later by both Gauss and Laplace\n        independently [2]_, is often called the bell curve because of\n        its characteristic shape (see the example below).\n\n        The normal distributions occurs often in nature.  For example, it\n        describes the commonly occurring distribution of samples influenced\n        by a large number of tiny, random disturbances, each with its own\n        unique distribution [2]_.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.normal`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        loc : float or array_like of floats\n            Mean ("centre") of the distribution.\n        scale : float or array_like of floats\n            Standard deviation (spread or "width") of the distribution. Must be\n            non-negative.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``loc`` and ``scale`` are both scalars.\n            Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized normal distribution.\n\n        See Also\n        --------\n        scipy.stats.norm : probability density function, distribution or\n            cumulative density function, etc.\n        random.Generator.normal: which should be used for new code.\n\n        Notes\n        -----\n        The probability density for the Gaussian distribution is\n\n        .. math:: p(x) = \\frac{1}{\\sqrt{ 2 \\pi \\sigma^2 }}\n                         e^{ - \\frac{ (x - \\mu)^2 } {2 \\sigma^2} },\n\n        where :math:`\\mu` is the mean and :math:`\\sigma` the standard\n        deviation. The square of the standard deviation, :math:`\\sigma^2`,\n        is called the variance.\n\n        The function has its peak at the mean, and its "spread" increases with\n        the standard deviation (the function reaches 0.607 times its maximum at\n        :math:`x + \\sigma` and :math:`x - \\sigma` [2]_).  This implies that\n        normal is more likely to return samples lying close to the mean, rather\n        than those far away.\n\n        References\n        ----------\n        .. [1] Wikipedia, "Normal distribution",\n               https://en.wikipedia.org/wiki/Normal_distribution\n        .. [2] P. R. Peebles Jr., "Central Limit Theorem" in "Probability,\n               Random Variables and Random Signal Principles", 4th ed., 2001,\n               pp. 51, 51, 125.\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        >>> mu, sigma = 0, 0.1 # mean and standard deviation\n        >>> s = np.random.normal(mu, sigma, 1000)\n\n        Verify the mean and the variance:\n\n        >>> abs(mu - np.mean(s))\n        0.0  # may vary\n\n        >>> abs(sigma - np.std(s, ddof=1))\n        0.1  # may vary\n\n        Display the histogram of the samples, along with\n        the probability density function:\n\n        >>> import matplotlib.pyplot as plt\n        >>> count, bins, ignored = plt.hist(s, 30, density=True)\n        >>> plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *\n        ...                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),\n        ...          linewidth=2, color=\'r\')\n        >>> plt.show()\n\n        Two-by-four array of samples from the normal distribution with\n        mean 3 and standard deviation 2.5:\n\n        >>> np.random.normal(3, 2.5, size=(2, 4))\n        array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random\n               [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random\n\n        ',
    'RandomState.pareto (line 2337)': '\n        pareto(a, size=None)\n\n        Draw samples from a Pareto II or Lomax distribution with\n        specified shape.\n\n        The Lomax or Pareto II distribution is a shifted Pareto\n        distribution. The classical Pareto distribution can be\n        obtained from the Lomax distribution by adding 1 and\n        multiplying by the scale parameter ``m`` (see Notes).  The\n        smallest value of the Lomax distribution is zero while for the\n        classical Pareto distribution it is ``mu``, where the standard\n        Pareto distribution has location ``mu = 1``.  Lomax can also\n        be considered as a simplified version of the Generalized\n        Pareto distribution (available in SciPy), with the scale set\n        to one and the location set to zero.\n\n        The Pareto distribution must be greater than zero, and is\n        unbounded above.  It is also known as the "80-20 rule".  In\n        this distribution, 80 percent of the weights are in the lowest\n        20 percent of the range, while the other 20 percent fill the\n        remaining 80 percent of the range.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.pareto`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        a : float or array_like of floats\n            Shape of the distribution. Must be positive.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``a`` is a scalar.  Otherwise,\n            ``np.array(a).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized Pareto distribution.\n\n        See Also\n        --------\n        scipy.stats.lomax : probability density function, distribution or\n            cumulative density function, etc.\n        scipy.stats.genpareto : probability density function, distribution or\n            cumulative density function, etc.\n        random.Generator.pareto: which should be used for new code.\n\n        Notes\n        -----\n        The probability density for the Pareto distribution is\n\n        .. math:: p(x) = \\frac{am^a}{x^{a+1}}\n\n        where :math:`a` is the shape and :math:`m` the scale.\n\n        The Pareto distribution, named after the Italian economist\n        Vilfredo Pareto, is a power law probability distribution\n        useful in many real world problems.  Outside the field of\n        economics it is generally referred to as the Bradford\n        distribution. Pareto developed the distribution to describe\n        the distribution of wealth in an economy.  It has also found\n        use in insurance, web page access statistics, oil field sizes,\n        and many other problems, including the download frequency for\n        projects in Sourceforge [1]_.  It is one of the so-called\n        "fat-tailed" distributions.\n\n        References\n        ----------\n        .. [1] Francis Hunt and Paul Johnson, On the Pareto Distribution of\n               Sourceforge projects.\n        .. [2] Pareto, V. (1896). Course of Political Economy. Lausanne.\n        .. [3] Reiss, R.D., Thomas, M.(2001), Statistical Analysis of Extreme\n               Values, Birkhauser Verlag, Basel, pp 23-30.\n        .. [4] Wikipedia, "Pareto distribution",\n               https://en.wikipedia.org/wiki/Pareto_distribution\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        >>> a, m = 3., 2.  # shape and mode\n        >>> s = (np.random.pareto(a, 1000) + 1) * m\n\n        Display the histogram of the samples, along with the probability\n        density function:\n\n        >>> import matplotlib.pyplot as plt\n        >>> count, bins, _ = plt.hist(s, 100, density=True)\n        >>> fit = a*m**a / bins**(a+1)\n        >>> plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color=\'r\')\n        >>> plt.show()\n\n        ',
    'RandomState.permutation (line 4651)': '\n        permutation(x)\n\n        Randomly permute a sequence, or return a permuted range.\n\n        If `x` is a multi-dimensional array, it is only shuffled along its\n        first index.\n\n        .. note::\n            New code should use the\n            `~numpy.random.Generator.permutation`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        x : int or array_like\n            If `x` is an integer, randomly permute ``np.arange(x)``.\n            If `x` is an array, make a copy and shuffle the elements\n            randomly.\n\n        Returns\n        -------\n        out : ndarray\n            Permuted sequence or array range.\n\n        See Also\n        --------\n        random.Generator.permutation: which should be used for new code.\n\n        Examples\n        --------\n        >>> np.random.permutation(10)\n        array([1, 7, 4, 3, 0, 9, 2, 5, 8, 6]) # random\n\n        >>> np.random.permutation([1, 4, 9, 12, 15])\n        array([15,  1,  9,  4, 12]) # random\n\n        >>> arr = np.arange(9).reshape((3, 3))\n        >>> np.random.permutation(arr)\n        array([[6, 7, 8], # random\n               [0, 1, 2],\n               [3, 4, 5]])\n\n        ',
    'RandomState.poisson (line 3576)': '\n        poisson(lam=1.0, size=None)\n\n        Draw samples from a Poisson distribution.\n\n        The Poisson distribution is the limit of the binomial distribution\n        for large N.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.poisson`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        lam : float or array_like of floats\n            Expected number of events occurring in a fixed-time interval,\n            must be >= 0. A sequence must be broadcastable over the requested\n            size.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``lam`` is a scalar. Otherwise,\n            ``np.array(lam).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized Poisson distribution.\n\n        See Also\n        --------\n        random.Generator.poisson: which should be used for new code.\n\n        Notes\n        -----\n        The Poisson distribution\n\n        .. math:: f(k; \\lambda)=\\frac{\\lambda^k e^{-\\lambda}}{k!}\n\n        For events with an expected separation :math:`\\lambda` the Poisson\n        distribution :math:`f(k; \\lambda)` describes the probability of\n        :math:`k` events occurring within the observed\n        interval :math:`\\lambda`.\n\n        Because the output is limited to the range of the C int64 type, a\n        ValueError is raised when `lam` is within 10 sigma of the maximum\n        representable value.\n\n        References\n        ----------\n        .. [1] Weisstein, Eric W. "Poisson Distribution."\n               From MathWorld--A Wolfram Web Resource.\n               http://mathworld.wolfram.com/PoissonDistribution.html\n        .. [2] Wikipedia, "Poisson distribution",\n               https://en.wikipedia.org/wiki/Poisson_distribution\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        >>> import numpy as np\n        >>> s = np.random.poisson(5, 10000)\n\n        Display histogram of the sample:\n\n        >>> import matplotlib.pyplot as plt\n        >>> count, bins, ignored = plt.hist(s, 14, density=True)\n        >>> plt.show()\n\n        Draw each 100 values for lambda 100 and 500:\n\n        >>> s = np.random.poisson(lam=(100., 500.), size=(100, 2))\n\n        ',
    'RandomState.power (line 2544)': '\n        power(a, size=None)\n\n        Draws samples in [0, 1] from a power distribution with positive\n        exponent a - 1.\n\n        Also known as the power function distribution.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.power`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        a : float or array_like of floats\n            Parameter of the distribution. Must be non-negative.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``a`` is a scalar.  Otherwise,\n            ``np.array(a).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized power distribution.\n\n        Raises\n        ------\n        ValueError\n            If a <= 0.\n\n        See Also\n        --------\n        random.Generator.power: which should be used for new code.\n\n        Notes\n        -----\n        The probability density function is\n\n        .. math:: P(x; a) = ax^{a-1}, 0 \\le x \\le 1, a>0.\n\n        The power function distribution is just the inverse of the Pareto\n        distribution. It may also be seen as a special case of the Beta\n        distribution.\n\n        It is used, for example, in modeling the over-reporting of insurance\n        claims.\n\n        References\n        ----------\n        .. [1] Christian Kleiber, Samuel Kotz, "Statistical size distributions\n               in economics and actuarial sciences", Wiley, 2003.\n        .. [2] Heckert, N. A. and Filliben, James J. "NIST Handbook 148:\n               Dataplot Reference Manual, Volume 2: Let Subcommands and Library\n               Functions", National Institute of Standards and Technology\n               Handbook Series, June 2003.\n               https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/powpdf.pdf\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        >>> a = 5. # shape\n        >>> samples = 1000\n        >>> s = np.random.power(a, samples)\n\n        Display the histogram of the samples, along with\n        the probability density function:\n\n        >>> import matplotlib.pyplot as plt\n        >>> count, bins, ignored = plt.hist(s, bins=30)\n        >>> x = np.linspace(0, 1, 100)\n        >>> y = a*x**(a-1.)\n        >>> normed_y = samples*np.diff(bins)[0]*y\n        >>> plt.plot(x, normed_y)\n        >>> plt.show()\n\n        Compare the power function distribution to the inverse of the Pareto.\n\n        >>> from scipy import stats # doctest: +SKIP\n        >>> rvs = np.random.power(5, 1000000)\n        >>> rvsp = np.random.pareto(5, 1000000)\n        >>> xx = np.linspace(0,1,100)\n        >>> powpdf = stats.powerlaw.pdf(xx,5)  # doctest: +SKIP\n\n        >>> plt.figure()\n        >>> plt.hist(rvs, bins=50, density=True)\n        >>> plt.plot(xx,powpdf,\'r-\')  # doctest: +SKIP\n        >>> plt.title(\'np.random.power(5)\')\n\n        >>> plt.figure()\n        >>> plt.hist(1./(1.+rvsp), bins=50, density=True)\n        >>> plt.plot(xx,powpdf,\'r-\')  # doctest: +SKIP\n        >>> plt.title(\'inverse of 1 + np.random.pareto(5)\')\n\n        >>> plt.figure()\n        >>> plt.hist(1./(1.+rvsp), bins=50, density=True)\n        >>> plt.plot(xx,powpdf,\'r-\')  # doctest: +SKIP\n        >>> plt.title(\'inverse of stats.pareto(5)\')\n\n        ',
    'RandomState.rand (line 1160)': '\n        rand(d0, d1, ..., dn)\n\n        Random values in a given shape.\n\n        .. note::\n            This is a convenience function for users porting code from Matlab,\n            and wraps `random_sample`. That function takes a\n            tuple to specify the size of the output, which is consistent with\n            other NumPy functions like `numpy.zeros` and `numpy.ones`.\n\n        Create an array of the given shape and populate it with\n        random samples from a uniform distribution\n        over ``[0, 1)``.\n\n        Parameters\n        ----------\n        d0, d1, ..., dn : int, optional\n            The dimensions of the returned array, must be non-negative.\n            If no argument is given a single Python float is returned.\n\n        Returns\n        -------\n        out : ndarray, shape ``(d0, d1, ..., dn)``\n            Random values.\n\n        See Also\n        --------\n        random\n\n        Examples\n        --------\n        >>> np.random.rand(3,2)\n        array([[ 0.14022471,  0.96360618],  #random\n               [ 0.37601032,  0.25528411],  #random\n               [ 0.49313049,  0.94909878]]) #random\n\n        ',
    'RandomState.randint (line 662)': '\n        randint(low, high=None, size=None, dtype=int)\n\n        Return random integers from `low` (inclusive) to `high` (exclusive).\n\n        Return random integers from the "discrete uniform" distribution of\n        the specified dtype in the "half-open" interval [`low`, `high`). If\n        `high` is None (the default), then results are from [0, `low`).\n\n        .. note::\n            New code should use the `~numpy.random.Generator.randint`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        low : int or array-like of ints\n            Lowest (signed) integers to be drawn from the distribution (unless\n            ``high=None``, in which case this parameter is one above the\n            *highest* such integer).\n        high : int or array-like of ints, optional\n            If provided, one above the largest (signed) integer to be drawn\n            from the distribution (see above for behavior if ``high=None``).\n            If array-like, must contain integer values\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  Default is None, in which case a\n            single value is returned.\n        dtype : dtype, optional\n            Desired dtype of the result. Byteorder must be native.\n            The default value is int.\n\n            .. versionadded:: 1.11.0\n\n        Returns\n        -------\n        out : int or ndarray of ints\n            `size`-shaped array of random integers from the appropriate\n            distribution, or a single such random int if `size` not provided.\n\n        See Also\n        --------\n        random_integers : similar to `randint`, only for the closed\n            interval [`low`, `high`], and 1 is the lowest value if `high` is\n            omitted.\n        random.Generator.integers: which should be used for new code.\n\n        Examples\n        --------\n        >>> np.random.randint(2, size=10)\n        array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0]) # random\n        >>> np.random.randint(1, size=10)\n        array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])\n\n        Generate a 2 x 4 array of ints between 0 and 4, inclusive:\n\n        >>> np.random.randint(5, size=(2, 4))\n        array([[4, 0, 2, 1], # random\n               [3, 2, 2, 0]])\n\n        Generate a 1 x 3 array with 3 different upper bounds\n\n        >>> np.random.randint(1, [3, 5, 10])\n        array([2, 2, 9]) # random\n\n        Generate a 1 by 3 array with 3 different lower bounds\n\n        >>> np.random.randint([1, 5, 7], 10)\n        array([9, 8, 7]) # random\n\n        Generate a 2 by 4 array using broadcasting with dtype of uint8\n\n        >>> np.random.randint([1, 3, 5, 7], [[10], [20]], dtype=np.uint8)\n        array([[ 8,  6,  9,  7], # random\n               [ 1, 16,  9, 12]], dtype=uint8)\n        ',
    'RandomState.randn (line 1204)': '\n        randn(d0, d1, ..., dn)\n\n        Return a sample (or samples) from the "standard normal" distribution.\n\n        .. note::\n            This is a convenience function for users porting code from Matlab,\n            and wraps `standard_normal`. That function takes a\n            tuple to specify the size of the output, which is consistent with\n            other NumPy functions like `numpy.zeros` and `numpy.ones`.\n\n        .. note::\n            New code should use the\n            `~numpy.random.Generator.standard_normal`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        If positive int_like arguments are provided, `randn` generates an array\n        of shape ``(d0, d1, ..., dn)``, filled\n        with random floats sampled from a univariate "normal" (Gaussian)\n        distribution of mean 0 and variance 1. A single float randomly sampled\n        from the distribution is returned if no argument is provided.\n\n        Parameters\n        ----------\n        d0, d1, ..., dn : int, optional\n            The dimensions of the returned array, must be non-negative.\n            If no argument is given a single Python float is returned.\n\n        Returns\n        -------\n        Z : ndarray or float\n            A ``(d0, d1, ..., dn)``-shaped array of floating-point samples from\n            the standard normal distribution, or a single such float if\n            no parameters were supplied.\n\n        See Also\n        --------\n        standard_normal : Similar, but takes a tuple as its argument.\n        normal : Also accepts mu and sigma arguments.\n        random.Generator.standard_normal: which should be used for new code.\n\n        Notes\n        -----\n        For random samples from the normal distribution with mean ``mu`` and\n        standard deviation ``sigma``, use::\n\n            sigma * np.random.randn(...) + mu\n\n        Examples\n        --------\n        >>> np.random.randn()\n        2.1923875335537315  # random\n\n        Two-by-four array of samples from the normal distribution with\n        mean 3 and standard deviation 2.5:\n\n        >>> 3 + 2.5 * np.random.randn(2, 4)\n        array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random\n               [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random\n\n        ',
    'RandomState.random_integers (line 1272)': '\n        random_integers(low, high=None, size=None)\n\n        Random integers of type `np.int_` between `low` and `high`, inclusive.\n\n        Return random integers of type `np.int_` from the "discrete uniform"\n        distribution in the closed interval [`low`, `high`].  If `high` is\n        None (the default), then results are from [1, `low`]. The `np.int_`\n        type translates to the C long integer type and its precision\n        is platform dependent.\n\n        This function has been deprecated. Use randint instead.\n\n        .. deprecated:: 1.11.0\n\n        Parameters\n        ----------\n        low : int\n            Lowest (signed) integer to be drawn from the distribution (unless\n            ``high=None``, in which case this parameter is the *highest* such\n            integer).\n        high : int, optional\n            If provided, the largest (signed) integer to be drawn from the\n            distribution (see above for behavior if ``high=None``).\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  Default is None, in which case a\n            single value is returned.\n\n        Returns\n        -------\n        out : int or ndarray of ints\n            `size`-shaped array of random integers from the appropriate\n            distribution, or a single such random int if `size` not provided.\n\n        See Also\n        --------\n        randint : Similar to `random_integers`, only for the half-open\n            interval [`low`, `high`), and 0 is the lowest value if `high` is\n            omitted.\n\n        Notes\n        -----\n        To sample from N evenly spaced floating-point numbers between a and b,\n        use::\n\n          a + (b - a) * (np.random.random_integers(N) - 1) / (N - 1.)\n\n        Examples\n        --------\n        >>> np.random.random_integers(5)\n        4 # random\n        >>> type(np.random.random_integers(5))\n        <class \'numpy.int64\'>\n        >>> np.random.random_integers(5, size=(3,2))\n        array([[5, 4], # random\n               [3, 3],\n               [4, 5]])\n\n        Choose five random numbers from the set of five evenly-spaced\n        numbers between 0 and 2.5, inclusive (*i.e.*, from the set\n        :math:`{0, 5/8, 10/8, 15/8, 20/8}`):\n\n        >>> 2.5 * (np.random.random_integers(5, size=(5,)) - 1) / 4.\n        array([ 0.625,  1.25 ,  0.625,  0.625,  2.5  ]) # random\n\n        Roll two six sided dice 1000 times and sum the results:\n\n        >>> d1 = np.random.random_integers(1, 6, 1000)\n        >>> d2 = np.random.random_integers(1, 6, 1000)\n        >>> dsums = d1 + d2\n\n        Display results as a histogram:\n\n        >>> import matplotlib.pyplot as plt\n        >>> count, bins, ignored = plt.hist(dsums, 11, density=True)\n        >>> plt.show()\n\n        ',
    'RandomState.random_sample (line 384)': '\n        random_sample(size=None)\n\n        Return random floats in the half-open interval [0.0, 1.0).\n\n        Results are from the "continuous uniform" distribution over the\n        stated interval.  To sample :math:`Unif[a, b), b > a` multiply\n        the output of `random_sample` by `(b-a)` and add `a`::\n\n          (b - a) * random_sample() + a\n\n        .. note::\n            New code should use the `~numpy.random.Generator.random`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  Default is None, in which case a\n            single value is returned.\n\n        Returns\n        -------\n        out : float or ndarray of floats\n            Array of random floats of shape `size` (unless ``size=None``, in which\n            case a single float is returned).\n\n        See Also\n        --------\n        random.Generator.random: which should be used for new code.\n\n        Examples\n        --------\n        >>> np.random.random_sample()\n        0.47108547995356098 # random\n        >>> type(np.random.random_sample())\n        <class \'float\'>\n        >>> np.random.random_sample((5,))\n        array([ 0.30220482,  0.86820401,  0.1654503 ,  0.11659149,  0.54323428]) # random\n\n        Three-by-two array of random numbers from [-5, 0):\n\n        >>> 5 * np.random.random_sample((3, 2)) - 5\n        array([[-3.99149989, -0.52338984], # random\n               [-2.99091858, -0.79479508],\n               [-1.23204345, -1.75224494]])\n\n        ',
    'RandomState.rayleigh (line 3073)': '\n        rayleigh(scale=1.0, size=None)\n\n        Draw samples from a Rayleigh distribution.\n\n        The :math:`\\chi` and Weibull distributions are generalizations of the\n        Rayleigh.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.rayleigh`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        scale : float or array_like of floats, optional\n            Scale, also equals the mode. Must be non-negative. Default is 1.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``scale`` is a scalar.  Otherwise,\n            ``np.array(scale).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized Rayleigh distribution.\n\n        See Also\n        --------\n        random.Generator.rayleigh: which should be used for new code.\n\n        Notes\n        -----\n        The probability density function for the Rayleigh distribution is\n\n        .. math:: P(x;scale) = \\frac{x}{scale^2}e^{\\frac{-x^2}{2 \\cdotp scale^2}}\n\n        The Rayleigh distribution would arise, for example, if the East\n        and North components of the wind velocity had identical zero-mean\n        Gaussian distributions.  Then the wind speed would have a Rayleigh\n        distribution.\n\n        References\n        ----------\n        .. [1] Brighton Webs Ltd., "Rayleigh Distribution,"\n               https://web.archive.org/web/20090514091424/http://brighton-webs.co.uk:80/distributions/rayleigh.asp\n        .. [2] Wikipedia, "Rayleigh distribution"\n               https://en.wikipedia.org/wiki/Rayleigh_distribution\n\n        Examples\n        --------\n        Draw values from the distribution and plot the histogram\n\n        >>> from matplotlib.pyplot import hist\n        >>> values = hist(np.random.rayleigh(3, 100000), bins=200, density=True)\n\n        Wave heights tend to follow a Rayleigh distribution. If the mean wave\n        height is 1 meter, what fraction of waves are likely to be larger than 3\n        meters?\n\n        >>> meanvalue = 1\n        >>> modevalue = np.sqrt(2 / np.pi) * meanvalue\n        >>> s = np.random.rayleigh(modevalue, 1000000)\n\n        The percentage of waves larger than 3 meters is:\n\n        >>> 100.*sum(s>3)/1000000.\n        0.087300000000000003 # random\n\n        ',
    'RandomState.seed (line 228)': '\n        seed(seed=None)\n\n        Reseed a legacy MT19937 BitGenerator\n\n        Notes\n        -----\n        This is a convenience, legacy function.\n\n        The best practice is to **not** reseed a BitGenerator, rather to\n        recreate a new one. This method is here for legacy reasons.\n        This example demonstrates best practice.\n\n        >>> from numpy.random import MT19937\n        >>> from numpy.random import RandomState, SeedSequence\n        >>> rs = RandomState(MT19937(SeedSequence(123456789)))\n        # Later, you want to restart the stream\n        >>> rs = RandomState(MT19937(SeedSequence(987654321)))\n        ',
    'RandomState.shuffle (line 4526)': '\n        shuffle(x)\n\n        Modify a sequence in-place by shuffling its contents.\n\n        This function only shuffles the array along the first axis of a\n        multi-dimensional array. The order of sub-arrays is changed but\n        their contents remains the same.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.shuffle`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        x : ndarray or MutableSequence\n            The array, list or mutable sequence to be shuffled.\n\n        Returns\n        -------\n        None\n\n        See Also\n        --------\n        random.Generator.shuffle: which should be used for new code.\n\n        Examples\n        --------\n        >>> arr = np.arange(10)\n        >>> np.random.shuffle(arr)\n        >>> arr\n        [1 7 5 2 9 4 3 6 0 8] # random\n\n        Multi-dimensional arrays are only shuffled along the first axis:\n\n        >>> arr = np.arange(9).reshape((3, 3))\n        >>> np.random.shuffle(arr)\n        >>> arr\n        array([[3, 4, 5], # random\n               [6, 7, 8],\n               [0, 1, 2]])\n\n        ',
    'RandomState.standard_cauchy (line 2058)': '\n        standard_cauchy(size=None)\n\n        Draw samples from a standard Cauchy distribution with mode = 0.\n\n        Also known as the Lorentz distribution.\n\n        .. note::\n            New code should use the\n            `~numpy.random.Generator.standard_cauchy`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  Default is None, in which case a\n            single value is returned.\n\n        Returns\n        -------\n        samples : ndarray or scalar\n            The drawn samples.\n\n        See Also\n        --------\n        random.Generator.standard_cauchy: which should be used for new code.\n\n        Notes\n        -----\n        The probability density function for the full Cauchy distribution is\n\n        .. math:: P(x; x_0, \\gamma) = \\frac{1}{\\pi \\gamma \\bigl[ 1+\n                  (\\frac{x-x_0}{\\gamma})^2 \\bigr] }\n\n        and the Standard Cauchy distribution just sets :math:`x_0=0` and\n        :math:`\\gamma=1`\n\n        The Cauchy distribution arises in the solution to the driven harmonic\n        oscillator problem, and also describes spectral line broadening. It\n        also describes the distribution of values at which a line tilted at\n        a random angle will cut the x axis.\n\n        When studying hypothesis tests that assume normality, seeing how the\n        tests perform on data from a Cauchy distribution is a good indicator of\n        their sensitivity to a heavy-tailed distribution, since the Cauchy looks\n        very much like a Gaussian distribution, but with heavier tails.\n\n        References\n        ----------\n        .. [1] NIST/SEMATECH e-Handbook of Statistical Methods, "Cauchy\n              Distribution",\n              https://www.itl.nist.gov/div898/handbook/eda/section3/eda3663.htm\n        .. [2] Weisstein, Eric W. "Cauchy Distribution." From MathWorld--A\n              Wolfram Web Resource.\n              http://mathworld.wolfram.com/CauchyDistribution.html\n        .. [3] Wikipedia, "Cauchy distribution"\n              https://en.wikipedia.org/wiki/Cauchy_distribution\n\n        Examples\n        --------\n        Draw samples and plot the distribution:\n\n        >>> import matplotlib.pyplot as plt\n        >>> s = np.random.standard_cauchy(1000000)\n        >>> s = s[(s>-25) & (s<25)]  # truncate distribution so it plots well\n        >>> plt.hist(s, bins=100)\n        >>> plt.show()\n\n        ',
    'RandomState.standard_exponential (line 560)': '\n        standard_exponential(size=None)\n\n        Draw samples from the standard exponential distribution.\n\n        `standard_exponential` is identical to the exponential distribution\n        with a scale parameter of 1.\n\n        .. note::\n            New code should use the\n            `~numpy.random.Generator.standard_exponential`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  Default is None, in which case a\n            single value is returned.\n\n        Returns\n        -------\n        out : float or ndarray\n            Drawn samples.\n\n        See Also\n        --------\n        random.Generator.standard_exponential: which should be used for new code.\n\n        Examples\n        --------\n        Output a 3x8000 array:\n\n        >>> n = np.random.standard_exponential((3, 8000))\n\n        ',
    'RandomState.standard_gamma (line 1546)': '\n        standard_gamma(shape, size=None)\n\n        Draw samples from a standard Gamma distribution.\n\n        Samples are drawn from a Gamma distribution with specified parameters,\n        shape (sometimes designated "k") and scale=1.\n\n        .. note::\n            New code should use the\n            `~numpy.random.Generator.standard_gamma`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        shape : float or array_like of floats\n            Parameter, must be non-negative.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``shape`` is a scalar.  Otherwise,\n            ``np.array(shape).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized standard gamma distribution.\n\n        See Also\n        --------\n        scipy.stats.gamma : probability density function, distribution or\n            cumulative density function, etc.\n        random.Generator.standard_gamma: which should be used for new code.\n\n        Notes\n        -----\n        The probability density for the Gamma distribution is\n\n        .. math:: p(x) = x^{k-1}\\frac{e^{-x/\\theta}}{\\theta^k\\Gamma(k)},\n\n        where :math:`k` is the shape and :math:`\\theta` the scale,\n        and :math:`\\Gamma` is the Gamma function.\n\n        The Gamma distribution is often used to model the times to failure of\n        electronic components, and arises naturally in processes for which the\n        waiting times between Poisson distributed events are relevant.\n\n        References\n        ----------\n        .. [1] Weisstein, Eric W. "Gamma Distribution." From MathWorld--A\n               Wolfram Web Resource.\n               http://mathworld.wolfram.com/GammaDistribution.html\n        .. [2] Wikipedia, "Gamma distribution",\n               https://en.wikipedia.org/wiki/Gamma_distribution\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        >>> shape, scale = 2., 1. # mean and width\n        >>> s = np.random.standard_gamma(shape, 1000000)\n\n        Display the histogram of the samples, along with\n        the probability density function:\n\n        >>> import matplotlib.pyplot as plt\n        >>> import scipy.special as sps  # doctest: +SKIP\n        >>> count, bins, ignored = plt.hist(s, 50, density=True)\n        >>> y = bins**(shape-1) * ((np.exp(-bins/scale))/  # doctest: +SKIP\n        ...                       (sps.gamma(shape) * scale**shape))\n        >>> plt.plot(bins, y, linewidth=2, color=\'r\')  # doctest: +SKIP\n        >>> plt.show()\n\n        ',
    'RandomState.standard_normal (line 1368)': '\n        standard_normal(size=None)\n\n        Draw samples from a standard Normal distribution (mean=0, stdev=1).\n\n        .. note::\n            New code should use the\n            `~numpy.random.Generator.standard_normal`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  Default is None, in which case a\n            single value is returned.\n\n        Returns\n        -------\n        out : float or ndarray\n            A floating-point array of shape ``size`` of drawn samples, or a\n            single sample if ``size`` was not specified.\n\n        See Also\n        --------\n        normal :\n            Equivalent function with additional ``loc`` and ``scale`` arguments\n            for setting the mean and standard deviation.\n        random.Generator.standard_normal: which should be used for new code.\n\n        Notes\n        -----\n        For random samples from the normal distribution with mean ``mu`` and\n        standard deviation ``sigma``, use one of::\n\n            mu + sigma * np.random.standard_normal(size=...)\n            np.random.normal(mu, sigma, size=...)\n\n        Examples\n        --------\n        >>> np.random.standard_normal()\n        2.1923875335537315 #random\n\n        >>> s = np.random.standard_normal(8000)\n        >>> s\n        array([ 0.6888893 ,  0.78096262, -0.89086505, ...,  0.49876311,  # random\n               -0.38672696, -0.4685006 ])                                # random\n        >>> s.shape\n        (8000,)\n        >>> s = np.random.standard_normal(size=(3, 4, 2))\n        >>> s.shape\n        (3, 4, 2)\n\n        Two-by-four array of samples from the normal distribution with\n        mean 3 and standard deviation 2.5:\n\n        >>> 3 + 2.5 * np.random.standard_normal(size=(2, 4))\n        array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random\n               [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random\n\n        ',
    'RandomState.standard_t (line 2133)': '\n        standard_t(df, size=None)\n\n        Draw samples from a standard Student\'s t distribution with `df` degrees\n        of freedom.\n\n        A special case of the hyperbolic distribution.  As `df` gets\n        large, the result resembles that of the standard normal\n        distribution (`standard_normal`).\n\n        .. note::\n            New code should use the `~numpy.random.Generator.standard_t`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        df : float or array_like of floats\n            Degrees of freedom, must be > 0.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``df`` is a scalar.  Otherwise,\n            ``np.array(df).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized standard Student\'s t distribution.\n\n        See Also\n        --------\n        random.Generator.standard_t: which should be used for new code.\n\n        Notes\n        -----\n        The probability density function for the t distribution is\n\n        .. math:: P(x, df) = \\frac{\\Gamma(\\frac{df+1}{2})}{\\sqrt{\\pi df}\n                  \\Gamma(\\frac{df}{2})}\\Bigl( 1+\\frac{x^2}{df} \\Bigr)^{-(df+1)/2}\n\n        The t test is based on an assumption that the data come from a\n        Normal distribution. The t test provides a way to test whether\n        the sample mean (that is the mean calculated from the data) is\n        a good estimate of the true mean.\n\n        The derivation of the t-distribution was first published in\n        1908 by William Gosset while working for the Guinness Brewery\n        in Dublin. Due to proprietary issues, he had to publish under\n        a pseudonym, and so he used the name Student.\n\n        References\n        ----------\n        .. [1] Dalgaard, Peter, "Introductory Statistics With R",\n               Springer, 2002.\n        .. [2] Wikipedia, "Student\'s t-distribution"\n               https://en.wikipedia.org/wiki/Student\'s_t-distribution\n\n        Examples\n        --------\n        From Dalgaard page 83 [1]_, suppose the daily energy intake for 11\n        women in kilojoules (kJ) is:\n\n        >>> intake = np.array([5260., 5470, 5640, 6180, 6390, 6515, 6805, 7515, \\\n        ...                    7515, 8230, 8770])\n\n        Does their energy intake deviate systematically from the recommended\n        value of 7725 kJ? Our null hypothesis will be the absence of deviation,\n        and the alternate hypothesis will be the presence of an effect that could be\n        either positive or negative, hence making our test 2-tailed. \n\n        Because we are estimating the mean and we have N=11 values in our sample,\n        we have N-1=10 degrees of freedom. We set our significance level to 95% and \n        compute the t statistic using the empirical mean and empirical standard \n        deviation of our intake. We use a ddof of 1 to base the computation of our \n        empirical standard deviation on an unbiased estimate of the variance (note:\n        the final estimate is not unbiased due to the concave nature of the square \n        root).\n\n        >>> np.mean(intake)\n        6753.636363636364\n        >>> intake.std(ddof=1)\n        1142.1232221373727\n        >>> t = (np.mean(intake)-7725)/(intake.std(ddof=1)/np.sqrt(len(intake)))\n        >>> t\n        -2.8207540608310198\n\n        We draw 1000000 samples from Student\'s t distribution with the adequate\n        degrees of freedom.\n\n        >>> import matplotlib.pyplot as plt\n        >>> s = np.random.standard_t(10, size=1000000)\n        >>> h = plt.hist(s, bins=100, density=True)\n\n        Does our t statistic land in one of the two critical regions found at \n        both tails of the distribution?\n\n        >>> np.sum(np.abs(t) < np.abs(s)) / float(len(s))\n        0.018318  #random < 0.05, statistic is in critical region\n\n        The probability value for this 2-tailed test is about 1.83%, which is \n        lower than the 5% pre-determined significance threshold. \n\n        Therefore, the probability of observing values as extreme as our intake\n        conditionally on the null hypothesis being true is too low, and we reject \n        the null hypothesis of no deviation. \n\n        ',
    'RandomState.tomaxint (line 604)': '\n        tomaxint(size=None)\n\n        Return a sample of uniformly distributed random integers in the interval\n        [0, ``np.iinfo(np.int_).max``]. The `np.int_` type translates to the C long\n        integer type and its precision is platform dependent.\n\n        Parameters\n        ----------\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  Default is None, in which case a\n            single value is returned.\n\n        Returns\n        -------\n        out : ndarray\n            Drawn samples, with shape `size`.\n\n        See Also\n        --------\n        randint : Uniform sampling over a given half-open interval of integers.\n        random_integers : Uniform sampling over a given closed interval of\n            integers.\n\n        Examples\n        --------\n        >>> rs = np.random.RandomState() # need a RandomState object\n        >>> rs.tomaxint((2,2,2))\n        array([[[1170048599, 1600360186], # random\n                [ 739731006, 1947757578]],\n               [[1871712945,  752307660],\n                [1601631370, 1479324245]]])\n        >>> rs.tomaxint((2,2,2)) < np.iinfo(np.int_).max\n        array([[[ True,  True],\n                [ True,  True]],\n               [[ True,  True],\n                [ True,  True]]])\n\n        ',
    'RandomState.triangular (line 3227)': '\n        triangular(left, mode, right, size=None)\n\n        Draw samples from the triangular distribution over the\n        interval ``[left, right]``.\n\n        The triangular distribution is a continuous probability\n        distribution with lower limit left, peak at mode, and upper\n        limit right. Unlike the other distributions, these parameters\n        directly define the shape of the pdf.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.triangular`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        left : float or array_like of floats\n            Lower limit.\n        mode : float or array_like of floats\n            The value where the peak of the distribution occurs.\n            The value must fulfill the condition ``left <= mode <= right``.\n        right : float or array_like of floats\n            Upper limit, must be larger than `left`.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``left``, ``mode``, and ``right``\n            are all scalars.  Otherwise, ``np.broadcast(left, mode, right).size``\n            samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized triangular distribution.\n\n        See Also\n        --------\n        random.Generator.triangular: which should be used for new code.\n\n        Notes\n        -----\n        The probability density function for the triangular distribution is\n\n        .. math:: P(x;l, m, r) = \\begin{cases}\n                  \\frac{2(x-l)}{(r-l)(m-l)}& \\text{for $l \\leq x \\leq m$},\\\\\n                  \\frac{2(r-x)}{(r-l)(r-m)}& \\text{for $m \\leq x \\leq r$},\\\\\n                  0& \\text{otherwise}.\n                  \\end{cases}\n\n        The triangular distribution is often used in ill-defined\n        problems where the underlying distribution is not known, but\n        some knowledge of the limits and mode exists. Often it is used\n        in simulations.\n\n        References\n        ----------\n        .. [1] Wikipedia, "Triangular distribution"\n               https://en.wikipedia.org/wiki/Triangular_distribution\n\n        Examples\n        --------\n        Draw values from the distribution and plot the histogram:\n\n        >>> import matplotlib.pyplot as plt\n        >>> h = plt.hist(np.random.triangular(-3, 0, 8, 100000), bins=200,\n        ...              density=True)\n        >>> plt.show()\n\n        ',
    'RandomState.uniform (line 1033)': "\n        uniform(low=0.0, high=1.0, size=None)\n\n        Draw samples from a uniform distribution.\n\n        Samples are uniformly distributed over the half-open interval\n        ``[low, high)`` (includes low, but excludes high).  In other words,\n        any value within the given interval is equally likely to be drawn\n        by `uniform`.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.uniform`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        low : float or array_like of floats, optional\n            Lower boundary of the output interval.  All values generated will be\n            greater than or equal to low.  The default value is 0.\n        high : float or array_like of floats\n            Upper boundary of the output interval.  All values generated will be\n            less than or equal to high.  The high limit may be included in the \n            returned array of floats due to floating-point rounding in the \n            equation ``low + (high-low) * random_sample()``.  The default value \n            is 1.0.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``low`` and ``high`` are both scalars.\n            Otherwise, ``np.broadcast(low, high).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized uniform distribution.\n\n        See Also\n        --------\n        randint : Discrete uniform distribution, yielding integers.\n        random_integers : Discrete uniform distribution over the closed\n                          interval ``[low, high]``.\n        random_sample : Floats uniformly distributed over ``[0, 1)``.\n        random : Alias for `random_sample`.\n        rand : Convenience function that accepts dimensions as input, e.g.,\n               ``rand(2,2)`` would generate a 2-by-2 array of floats,\n               uniformly distributed over ``[0, 1)``.\n        random.Generator.uniform: which should be used for new code.\n\n        Notes\n        -----\n        The probability density function of the uniform distribution is\n\n        .. math:: p(x) = \\frac{1}{b - a}\n\n        anywhere within the interval ``[a, b)``, and zero elsewhere.\n\n        When ``high`` == ``low``, values of ``low`` will be returned.\n        If ``high`` < ``low``, the results are officially undefined\n        and may eventually raise an error, i.e. do not rely on this\n        function to behave when passed arguments satisfying that\n        inequality condition. The ``high`` limit may be included in the\n        returned array of floats due to floating-point rounding in the\n        equation ``low + (high-low) * random_sample()``. For example:\n\n        >>> x = np.float32(5*0.99999999)\n        >>> x\n        5.0\n\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        >>> s = np.random.uniform(-1,0,1000)\n\n        All values are within the given interval:\n\n        >>> np.all(s >= -1)\n        True\n        >>> np.all(s < 0)\n        True\n\n        Display the histogram of the samples, along with the\n        probability density function:\n\n        >>> import matplotlib.pyplot as plt\n        >>> count, bins, ignored = plt.hist(s, 15, density=True)\n        >>> plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')\n        >>> plt.show()\n\n        ",
    'RandomState.vonmises (line 2248)': '\n        vonmises(mu, kappa, size=None)\n\n        Draw samples from a von Mises distribution.\n\n        Samples are drawn from a von Mises distribution with specified mode\n        (mu) and dispersion (kappa), on the interval [-pi, pi].\n\n        The von Mises distribution (also known as the circular normal\n        distribution) is a continuous probability distribution on the unit\n        circle.  It may be thought of as the circular analogue of the normal\n        distribution.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.vonmises`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        mu : float or array_like of floats\n            Mode ("center") of the distribution.\n        kappa : float or array_like of floats\n            Dispersion of the distribution, has to be >=0.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``mu`` and ``kappa`` are both scalars.\n            Otherwise, ``np.broadcast(mu, kappa).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized von Mises distribution.\n\n        See Also\n        --------\n        scipy.stats.vonmises : probability density function, distribution, or\n            cumulative density function, etc.\n        random.Generator.vonmises: which should be used for new code.\n\n        Notes\n        -----\n        The probability density for the von Mises distribution is\n\n        .. math:: p(x) = \\frac{e^{\\kappa cos(x-\\mu)}}{2\\pi I_0(\\kappa)},\n\n        where :math:`\\mu` is the mode and :math:`\\kappa` the dispersion,\n        and :math:`I_0(\\kappa)` is the modified Bessel function of order 0.\n\n        The von Mises is named for Richard Edler von Mises, who was born in\n        Austria-Hungary, in what is now the Ukraine.  He fled to the United\n        States in 1939 and became a professor at Harvard.  He worked in\n        probability theory, aerodynamics, fluid mechanics, and philosophy of\n        science.\n\n        References\n        ----------\n        .. [1] Abramowitz, M. and Stegun, I. A. (Eds.). "Handbook of\n               Mathematical Functions with Formulas, Graphs, and Mathematical\n               Tables, 9th printing," New York: Dover, 1972.\n        .. [2] von Mises, R., "Mathematical Theory of Probability\n               and Statistics", New York: Academic Press, 1964.\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        >>> mu, kappa = 0.0, 4.0 # mean and dispersion\n        >>> s = np.random.vonmises(mu, kappa, 1000)\n\n        Display the histogram of the samples, along with\n        the probability density function:\n\n        >>> import matplotlib.pyplot as plt\n        >>> from scipy.special import i0  # doctest: +SKIP\n        >>> plt.hist(s, 50, density=True)\n        >>> x = np.linspace(-np.pi, np.pi, num=51)\n        >>> y = np.exp(kappa*np.cos(x-mu))/(2*np.pi*i0(kappa))  # doctest: +SKIP\n        >>> plt.plot(x, y, linewidth=2, color=\'r\')  # doctest: +SKIP\n        >>> plt.show()\n\n        ',
    'RandomState.wald (line 3150)': '\n        wald(mean, scale, size=None)\n\n        Draw samples from a Wald, or inverse Gaussian, distribution.\n\n        As the scale approaches infinity, the distribution becomes more like a\n        Gaussian. Some references claim that the Wald is an inverse Gaussian\n        with mean equal to 1, but this is by no means universal.\n\n        The inverse Gaussian distribution was first studied in relationship to\n        Brownian motion. In 1956 M.C.K. Tweedie used the name inverse Gaussian\n        because there is an inverse relationship between the time to cover a\n        unit distance and distance covered in unit time.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.wald`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        mean : float or array_like of floats\n            Distribution mean, must be > 0.\n        scale : float or array_like of floats\n            Scale parameter, must be > 0.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``mean`` and ``scale`` are both scalars.\n            Otherwise, ``np.broadcast(mean, scale).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized Wald distribution.\n\n        See Also\n        --------\n        random.Generator.wald: which should be used for new code.\n\n        Notes\n        -----\n        The probability density function for the Wald distribution is\n\n        .. math:: P(x;mean,scale) = \\sqrt{\\frac{scale}{2\\pi x^3}}e^\n                                    \\frac{-scale(x-mean)^2}{2\\cdotp mean^2x}\n\n        As noted above the inverse Gaussian distribution first arise\n        from attempts to model Brownian motion. It is also a\n        competitor to the Weibull for use in reliability modeling and\n        modeling stock returns and interest rate processes.\n\n        References\n        ----------\n        .. [1] Brighton Webs Ltd., Wald Distribution,\n               https://web.archive.org/web/20090423014010/http://www.brighton-webs.co.uk:80/distributions/wald.asp\n        .. [2] Chhikara, Raj S., and Folks, J. Leroy, "The Inverse Gaussian\n               Distribution: Theory : Methodology, and Applications", CRC Press,\n               1988.\n        .. [3] Wikipedia, "Inverse Gaussian distribution"\n               https://en.wikipedia.org/wiki/Inverse_Gaussian_distribution\n\n        Examples\n        --------\n        Draw values from the distribution and plot the histogram:\n\n        >>> import matplotlib.pyplot as plt\n        >>> h = plt.hist(np.random.wald(3, 2, 100000), bins=200, density=True)\n        >>> plt.show()\n\n        ',
    'RandomState.weibull (line 2440)': '\n        weibull(a, size=None)\n\n        Draw samples from a Weibull distribution.\n\n        Draw samples from a 1-parameter Weibull distribution with the given\n        shape parameter `a`.\n\n        .. math:: X = (-ln(U))^{1/a}\n\n        Here, U is drawn from the uniform distribution over (0,1].\n\n        The more common 2-parameter Weibull, including a scale parameter\n        :math:`\\lambda` is just :math:`X = \\lambda(-ln(U))^{1/a}`.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.weibull`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        a : float or array_like of floats\n            Shape parameter of the distribution.  Must be nonnegative.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``a`` is a scalar.  Otherwise,\n            ``np.array(a).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized Weibull distribution.\n\n        See Also\n        --------\n        scipy.stats.weibull_max\n        scipy.stats.weibull_min\n        scipy.stats.genextreme\n        gumbel\n        random.Generator.weibull: which should be used for new code.\n\n        Notes\n        -----\n        The Weibull (or Type III asymptotic extreme value distribution\n        for smallest values, SEV Type III, or Rosin-Rammler\n        distribution) is one of a class of Generalized Extreme Value\n        (GEV) distributions used in modeling extreme value problems.\n        This class includes the Gumbel and Frechet distributions.\n\n        The probability density for the Weibull distribution is\n\n        .. math:: p(x) = \\frac{a}\n                         {\\lambda}(\\frac{x}{\\lambda})^{a-1}e^{-(x/\\lambda)^a},\n\n        where :math:`a` is the shape and :math:`\\lambda` the scale.\n\n        The function has its peak (the mode) at\n        :math:`\\lambda(\\frac{a-1}{a})^{1/a}`.\n\n        When ``a = 1``, the Weibull distribution reduces to the exponential\n        distribution.\n\n        References\n        ----------\n        .. [1] Waloddi Weibull, Royal Technical University, Stockholm,\n               1939 "A Statistical Theory Of The Strength Of Materials",\n               Ingeniorsvetenskapsakademiens Handlingar Nr 151, 1939,\n               Generalstabens Litografiska Anstalts Forlag, Stockholm.\n        .. [2] Waloddi Weibull, "A Statistical Distribution Function of\n               Wide Applicability", Journal Of Applied Mechanics ASME Paper\n               1951.\n        .. [3] Wikipedia, "Weibull distribution",\n               https://en.wikipedia.org/wiki/Weibull_distribution\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        >>> a = 5. # shape\n        >>> s = np.random.weibull(a, 1000)\n\n        Display the histogram of the samples, along with\n        the probability density function:\n\n        >>> import matplotlib.pyplot as plt\n        >>> x = np.arange(1,100.)/50.\n        >>> def weib(x,n,a):\n        ...     return (a / n) * (x / n)**(a - 1) * np.exp(-(x / n)**a)\n\n        >>> count, bins, ignored = plt.hist(np.random.weibull(5.,1000))\n        >>> x = np.arange(1,100.)/50.\n        >>> scale = count.max()/weib(x, 1., 5.).max()\n        >>> plt.plot(x, weib(x, 1., 5.)*scale)\n        >>> plt.show()\n\n        ',
    'RandomState.zipf (line 3659)': '\n        zipf(a, size=None)\n\n        Draw samples from a Zipf distribution.\n\n        Samples are drawn from a Zipf distribution with specified parameter\n        `a` > 1.\n\n        The Zipf distribution (also known as the zeta distribution) is a\n        discrete probability distribution that satisfies Zipf\'s law: the\n        frequency of an item is inversely proportional to its rank in a\n        frequency table.\n\n        .. note::\n            New code should use the `~numpy.random.Generator.zipf`\n            method of a `~numpy.random.Generator` instance instead;\n            please see the :ref:`random-quick-start`.\n\n        Parameters\n        ----------\n        a : float or array_like of floats\n            Distribution parameter. Must be greater than 1.\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  If size is ``None`` (default),\n            a single value is returned if ``a`` is a scalar. Otherwise,\n            ``np.array(a).size`` samples are drawn.\n\n        Returns\n        -------\n        out : ndarray or scalar\n            Drawn samples from the parameterized Zipf distribution.\n\n        See Also\n        --------\n        scipy.stats.zipf : probability density function, distribution, or\n            cumulative density function, etc.\n        random.Generator.zipf: which should be used for new code.\n\n        Notes\n        -----\n        The probability density for the Zipf distribution is\n\n        .. math:: p(k) = \\frac{k^{-a}}{\\zeta(a)},\n\n        for integers :math:`k \\geq 1`, where :math:`\\zeta` is the Riemann Zeta\n        function.\n\n        It is named for the American linguist George Kingsley Zipf, who noted\n        that the frequency of any word in a sample of a language is inversely\n        proportional to its rank in the frequency table.\n\n        References\n        ----------\n        .. [1] Zipf, G. K., "Selected Studies of the Principle of Relative\n               Frequency in Language," Cambridge, MA: Harvard Univ. Press,\n               1932.\n\n        Examples\n        --------\n        Draw samples from the distribution:\n\n        >>> a = 4.0\n        >>> n = 20000\n        >>> s = np.random.zipf(a, n)\n\n        Display the histogram of the samples, along with\n        the expected histogram based on the probability\n        density function:\n\n        >>> import matplotlib.pyplot as plt\n        >>> from scipy.special import zeta  # doctest: +SKIP\n\n        `bincount` provides a fast histogram for small integers.\n\n        >>> count = np.bincount(s)\n        >>> k = np.arange(1, s.max() + 1)\n\n        >>> plt.bar(k, count[1:], alpha=0.5, label=\'sample count\')\n        >>> plt.plot(k, n*(k**-a)/zeta(a), \'k.-\', alpha=0.5,\n        ...          label=\'expected count\')   # doctest: +SKIP\n        >>> plt.semilogy()\n        >>> plt.grid(alpha=0.4)\n        >>> plt.legend()\n        >>> plt.title(f\'Zipf sample, a={a}, size={n}\')\n        >>> plt.show()\n\n        ',
}

