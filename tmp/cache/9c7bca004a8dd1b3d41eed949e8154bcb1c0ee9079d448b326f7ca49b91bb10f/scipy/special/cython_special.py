# encoding: utf-8
# module scipy.special.cython_special
# from /.venv/lib/python3.8/site-packages/scipy/special/cython_special.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
.. highlight:: cython

Cython API for special functions
================================

Scalar, typed versions of many of the functions in ``scipy.special``
can be accessed directly from Cython; the complete list is given
below. Functions are overloaded using Cython fused types so their
names match their Python counterpart. The module follows the following
conventions:

- If a function's Python counterpart returns multiple values, then the
  function returns its outputs via pointers in the final arguments.
- If a function's Python counterpart returns a single value, then the
  function's output is returned directly.

The module is usable from Cython via::

    cimport scipy.special.cython_special

Error handling
--------------

Functions can indicate an error by returning ``nan``; however they
cannot emit warnings like their counterparts in ``scipy.special``.

Available functions
-------------------

- :py:func:`~scipy.special.voigt_profile`::

        double voigt_profile(double, double, double)

- :py:func:`~scipy.special.agm`::

        double agm(double, double)

- :py:func:`~scipy.special.airy`::

        void airy(double, double *, double *, double *, double *)
        void airy(double complex, double complex *, double complex *, double complex *, double complex *)

- :py:func:`~scipy.special.airye`::

        void airye(double complex, double complex *, double complex *, double complex *, double complex *)
        void airye(double, double *, double *, double *, double *)

- :py:func:`~scipy.special.bdtr`::

        double bdtr(double, double, double)
        double bdtr(double, long, double)

- :py:func:`~scipy.special.bdtrc`::

        double bdtrc(double, double, double)
        double bdtrc(double, long, double)

- :py:func:`~scipy.special.bdtri`::

        double bdtri(double, double, double)
        double bdtri(double, long, double)

- :py:func:`~scipy.special.bdtrik`::

        double bdtrik(double, double, double)

- :py:func:`~scipy.special.bdtrin`::

        double bdtrin(double, double, double)

- :py:func:`~scipy.special.bei`::

        double bei(double)

- :py:func:`~scipy.special.beip`::

        double beip(double)

- :py:func:`~scipy.special.ber`::

        double ber(double)

- :py:func:`~scipy.special.berp`::

        double berp(double)

- :py:func:`~scipy.special.besselpoly`::

        double besselpoly(double, double, double)

- :py:func:`~scipy.special.beta`::

        double beta(double, double)

- :py:func:`~scipy.special.betainc`::

        double betainc(double, double, double)

- :py:func:`~scipy.special.betaincinv`::

        double betaincinv(double, double, double)

- :py:func:`~scipy.special.betaln`::

        double betaln(double, double)

- :py:func:`~scipy.special.binom`::

        double binom(double, double)

- :py:func:`~scipy.special.boxcox`::

        double boxcox(double, double)

- :py:func:`~scipy.special.boxcox1p`::

        double boxcox1p(double, double)

- :py:func:`~scipy.special.btdtr`::

        double btdtr(double, double, double)

- :py:func:`~scipy.special.btdtri`::

        double btdtri(double, double, double)

- :py:func:`~scipy.special.btdtria`::

        double btdtria(double, double, double)

- :py:func:`~scipy.special.btdtrib`::

        double btdtrib(double, double, double)

- :py:func:`~scipy.special.cbrt`::

        double cbrt(double)

- :py:func:`~scipy.special.chdtr`::

        double chdtr(double, double)

- :py:func:`~scipy.special.chdtrc`::

        double chdtrc(double, double)

- :py:func:`~scipy.special.chdtri`::

        double chdtri(double, double)

- :py:func:`~scipy.special.chdtriv`::

        double chdtriv(double, double)

- :py:func:`~scipy.special.chndtr`::

        double chndtr(double, double, double)

- :py:func:`~scipy.special.chndtridf`::

        double chndtridf(double, double, double)

- :py:func:`~scipy.special.chndtrinc`::

        double chndtrinc(double, double, double)

- :py:func:`~scipy.special.chndtrix`::

        double chndtrix(double, double, double)

- :py:func:`~scipy.special.cosdg`::

        double cosdg(double)

- :py:func:`~scipy.special.cosm1`::

        double cosm1(double)

- :py:func:`~scipy.special.cotdg`::

        double cotdg(double)

- :py:func:`~scipy.special.dawsn`::

        double dawsn(double)
        double complex dawsn(double complex)

- :py:func:`~scipy.special.ellipe`::

        double ellipe(double)

- :py:func:`~scipy.special.ellipeinc`::

        double ellipeinc(double, double)

- :py:func:`~scipy.special.ellipj`::

        void ellipj(double, double, double *, double *, double *, double *)

- :py:func:`~scipy.special.ellipkinc`::

        double ellipkinc(double, double)

- :py:func:`~scipy.special.ellipkm1`::

        double ellipkm1(double)

- :py:func:`~scipy.special.ellipk`::

        double ellipk(double)

- :py:func:`~scipy.special.elliprc`::

        double elliprc(double, double)
        double complex elliprc(double complex, double complex)

- :py:func:`~scipy.special.elliprd`::

        double elliprd(double, double, double)
        double complex elliprd(double complex, double complex, double complex)

- :py:func:`~scipy.special.elliprf`::

        double elliprf(double, double, double)
        double complex elliprf(double complex, double complex, double complex)

- :py:func:`~scipy.special.elliprg`::

        double elliprg(double, double, double)
        double complex elliprg(double complex, double complex, double complex)

- :py:func:`~scipy.special.elliprj`::

        double elliprj(double, double, double, double)
        double complex elliprj(double complex, double complex, double complex, double complex)

- :py:func:`~scipy.special.entr`::

        double entr(double)

- :py:func:`~scipy.special.erf`::

        double complex erf(double complex)
        double erf(double)

- :py:func:`~scipy.special.erfc`::

        double complex erfc(double complex)
        double erfc(double)

- :py:func:`~scipy.special.erfcx`::

        double erfcx(double)
        double complex erfcx(double complex)

- :py:func:`~scipy.special.erfi`::

        double erfi(double)
        double complex erfi(double complex)

- :py:func:`~scipy.special.erfinv`::

        float erfinv(float)
        double erfinv(double)

- :py:func:`~scipy.special.erfcinv`::

        double erfcinv(double)

- :py:func:`~scipy.special.eval_chebyc`::

        double complex eval_chebyc(double, double complex)
        double eval_chebyc(double, double)
        double eval_chebyc(long, double)

- :py:func:`~scipy.special.eval_chebys`::

        double complex eval_chebys(double, double complex)
        double eval_chebys(double, double)
        double eval_chebys(long, double)

- :py:func:`~scipy.special.eval_chebyt`::

        double complex eval_chebyt(double, double complex)
        double eval_chebyt(double, double)
        double eval_chebyt(long, double)

- :py:func:`~scipy.special.eval_chebyu`::

        double complex eval_chebyu(double, double complex)
        double eval_chebyu(double, double)
        double eval_chebyu(long, double)

- :py:func:`~scipy.special.eval_gegenbauer`::

        double complex eval_gegenbauer(double, double, double complex)
        double eval_gegenbauer(double, double, double)
        double eval_gegenbauer(long, double, double)

- :py:func:`~scipy.special.eval_genlaguerre`::

        double complex eval_genlaguerre(double, double, double complex)
        double eval_genlaguerre(double, double, double)
        double eval_genlaguerre(long, double, double)

- :py:func:`~scipy.special.eval_hermite`::

        double eval_hermite(long, double)

- :py:func:`~scipy.special.eval_hermitenorm`::

        double eval_hermitenorm(long, double)

- :py:func:`~scipy.special.eval_jacobi`::

        double complex eval_jacobi(double, double, double, double complex)
        double eval_jacobi(double, double, double, double)
        double eval_jacobi(long, double, double, double)

- :py:func:`~scipy.special.eval_laguerre`::

        double complex eval_laguerre(double, double complex)
        double eval_laguerre(double, double)
        double eval_laguerre(long, double)

- :py:func:`~scipy.special.eval_legendre`::

        double complex eval_legendre(double, double complex)
        double eval_legendre(double, double)
        double eval_legendre(long, double)

- :py:func:`~scipy.special.eval_sh_chebyt`::

        double complex eval_sh_chebyt(double, double complex)
        double eval_sh_chebyt(double, double)
        double eval_sh_chebyt(long, double)

- :py:func:`~scipy.special.eval_sh_chebyu`::

        double complex eval_sh_chebyu(double, double complex)
        double eval_sh_chebyu(double, double)
        double eval_sh_chebyu(long, double)

- :py:func:`~scipy.special.eval_sh_jacobi`::

        double complex eval_sh_jacobi(double, double, double, double complex)
        double eval_sh_jacobi(double, double, double, double)
        double eval_sh_jacobi(long, double, double, double)

- :py:func:`~scipy.special.eval_sh_legendre`::

        double complex eval_sh_legendre(double, double complex)
        double eval_sh_legendre(double, double)
        double eval_sh_legendre(long, double)

- :py:func:`~scipy.special.exp1`::

        double complex exp1(double complex)
        double exp1(double)

- :py:func:`~scipy.special.exp10`::

        double exp10(double)

- :py:func:`~scipy.special.exp2`::

        double exp2(double)

- :py:func:`~scipy.special.expi`::

        double complex expi(double complex)
        double expi(double)

- :py:func:`~scipy.special.expit`::

        double expit(double)
        float expit(float)
        long double expit(long double)

- :py:func:`~scipy.special.expm1`::

        double complex expm1(double complex)
        double expm1(double)

- :py:func:`~scipy.special.expn`::

        double expn(double, double)
        double expn(long, double)

- :py:func:`~scipy.special.exprel`::

        double exprel(double)

- :py:func:`~scipy.special.fdtr`::

        double fdtr(double, double, double)

- :py:func:`~scipy.special.fdtrc`::

        double fdtrc(double, double, double)

- :py:func:`~scipy.special.fdtri`::

        double fdtri(double, double, double)

- :py:func:`~scipy.special.fdtridfd`::

        double fdtridfd(double, double, double)

- :py:func:`~scipy.special.fresnel`::

        void fresnel(double, double *, double *)
        void fresnel(double complex, double complex *, double complex *)

- :py:func:`~scipy.special.gamma`::

        double complex gamma(double complex)
        double gamma(double)

- :py:func:`~scipy.special.gammainc`::

        double gammainc(double, double)

- :py:func:`~scipy.special.gammaincc`::

        double gammaincc(double, double)

- :py:func:`~scipy.special.gammainccinv`::

        double gammainccinv(double, double)

- :py:func:`~scipy.special.gammaincinv`::

        double gammaincinv(double, double)

- :py:func:`~scipy.special.gammaln`::

        double gammaln(double)

- :py:func:`~scipy.special.gammasgn`::

        double gammasgn(double)

- :py:func:`~scipy.special.gdtr`::

        double gdtr(double, double, double)

- :py:func:`~scipy.special.gdtrc`::

        double gdtrc(double, double, double)

- :py:func:`~scipy.special.gdtria`::

        double gdtria(double, double, double)

- :py:func:`~scipy.special.gdtrib`::

        double gdtrib(double, double, double)

- :py:func:`~scipy.special.gdtrix`::

        double gdtrix(double, double, double)

- :py:func:`~scipy.special.hankel1`::

        double complex hankel1(double, double complex)

- :py:func:`~scipy.special.hankel1e`::

        double complex hankel1e(double, double complex)

- :py:func:`~scipy.special.hankel2`::

        double complex hankel2(double, double complex)

- :py:func:`~scipy.special.hankel2e`::

        double complex hankel2e(double, double complex)

- :py:func:`~scipy.special.huber`::

        double huber(double, double)

- :py:func:`~scipy.special.hyp0f1`::

        double complex hyp0f1(double, double complex)
        double hyp0f1(double, double)

- :py:func:`~scipy.special.hyp1f1`::

        double hyp1f1(double, double, double)
        double complex hyp1f1(double, double, double complex)

- :py:func:`~scipy.special.hyp2f1`::

        double hyp2f1(double, double, double, double)
        double complex hyp2f1(double, double, double, double complex)

- :py:func:`~scipy.special.hyperu`::

        double hyperu(double, double, double)

- :py:func:`~scipy.special.i0`::

        double i0(double)

- :py:func:`~scipy.special.i0e`::

        double i0e(double)

- :py:func:`~scipy.special.i1`::

        double i1(double)

- :py:func:`~scipy.special.i1e`::

        double i1e(double)

- :py:func:`~scipy.special.inv_boxcox`::

        double inv_boxcox(double, double)

- :py:func:`~scipy.special.inv_boxcox1p`::

        double inv_boxcox1p(double, double)

- :py:func:`~scipy.special.it2i0k0`::

        void it2i0k0(double, double *, double *)

- :py:func:`~scipy.special.it2j0y0`::

        void it2j0y0(double, double *, double *)

- :py:func:`~scipy.special.it2struve0`::

        double it2struve0(double)

- :py:func:`~scipy.special.itairy`::

        void itairy(double, double *, double *, double *, double *)

- :py:func:`~scipy.special.iti0k0`::

        void iti0k0(double, double *, double *)

- :py:func:`~scipy.special.itj0y0`::

        void itj0y0(double, double *, double *)

- :py:func:`~scipy.special.itmodstruve0`::

        double itmodstruve0(double)

- :py:func:`~scipy.special.itstruve0`::

        double itstruve0(double)

- :py:func:`~scipy.special.iv`::

        double complex iv(double, double complex)
        double iv(double, double)

- :py:func:`~scipy.special.ive`::

        double complex ive(double, double complex)
        double ive(double, double)

- :py:func:`~scipy.special.j0`::

        double j0(double)

- :py:func:`~scipy.special.j1`::

        double j1(double)

- :py:func:`~scipy.special.jv`::

        double complex jv(double, double complex)
        double jv(double, double)

- :py:func:`~scipy.special.jve`::

        double complex jve(double, double complex)
        double jve(double, double)

- :py:func:`~scipy.special.k0`::

        double k0(double)

- :py:func:`~scipy.special.k0e`::

        double k0e(double)

- :py:func:`~scipy.special.k1`::

        double k1(double)

- :py:func:`~scipy.special.k1e`::

        double k1e(double)

- :py:func:`~scipy.special.kei`::

        double kei(double)

- :py:func:`~scipy.special.keip`::

        double keip(double)

- :py:func:`~scipy.special.kelvin`::

        void kelvin(double, double complex *, double complex *, double complex *, double complex *)

- :py:func:`~scipy.special.ker`::

        double ker(double)

- :py:func:`~scipy.special.kerp`::

        double kerp(double)

- :py:func:`~scipy.special.kl_div`::

        double kl_div(double, double)

- :py:func:`~scipy.special.kn`::

        double kn(double, double)
        double kn(long, double)

- :py:func:`~scipy.special.kolmogi`::

        double kolmogi(double)

- :py:func:`~scipy.special.kolmogorov`::

        double kolmogorov(double)

- :py:func:`~scipy.special.kv`::

        double complex kv(double, double complex)
        double kv(double, double)

- :py:func:`~scipy.special.kve`::

        double complex kve(double, double complex)
        double kve(double, double)

- :py:func:`~scipy.special.log1p`::

        double complex log1p(double complex)
        double log1p(double)

- :py:func:`~scipy.special.log_expit`::

        double log_expit(double)
        float log_expit(float)
        long double log_expit(long double)

- :py:func:`~scipy.special.log_ndtr`::

        double log_ndtr(double)
        double complex log_ndtr(double complex)

- :py:func:`~scipy.special.loggamma`::

        double loggamma(double)
        double complex loggamma(double complex)

- :py:func:`~scipy.special.logit`::

        double logit(double)
        float logit(float)
        long double logit(long double)

- :py:func:`~scipy.special.lpmv`::

        double lpmv(double, double, double)

- :py:func:`~scipy.special.mathieu_a`::

        double mathieu_a(double, double)

- :py:func:`~scipy.special.mathieu_b`::

        double mathieu_b(double, double)

- :py:func:`~scipy.special.mathieu_cem`::

        void mathieu_cem(double, double, double, double *, double *)

- :py:func:`~scipy.special.mathieu_modcem1`::

        void mathieu_modcem1(double, double, double, double *, double *)

- :py:func:`~scipy.special.mathieu_modcem2`::

        void mathieu_modcem2(double, double, double, double *, double *)

- :py:func:`~scipy.special.mathieu_modsem1`::

        void mathieu_modsem1(double, double, double, double *, double *)

- :py:func:`~scipy.special.mathieu_modsem2`::

        void mathieu_modsem2(double, double, double, double *, double *)

- :py:func:`~scipy.special.mathieu_sem`::

        void mathieu_sem(double, double, double, double *, double *)

- :py:func:`~scipy.special.modfresnelm`::

        void modfresnelm(double, double complex *, double complex *)

- :py:func:`~scipy.special.modfresnelp`::

        void modfresnelp(double, double complex *, double complex *)

- :py:func:`~scipy.special.modstruve`::

        double modstruve(double, double)

- :py:func:`~scipy.special.nbdtr`::

        double nbdtr(double, double, double)
        double nbdtr(long, long, double)

- :py:func:`~scipy.special.nbdtrc`::

        double nbdtrc(double, double, double)
        double nbdtrc(long, long, double)

- :py:func:`~scipy.special.nbdtri`::

        double nbdtri(double, double, double)
        double nbdtri(long, long, double)

- :py:func:`~scipy.special.nbdtrik`::

        double nbdtrik(double, double, double)

- :py:func:`~scipy.special.nbdtrin`::

        double nbdtrin(double, double, double)

- :py:func:`~scipy.special.ncfdtr`::

        double ncfdtr(double, double, double, double)

- :py:func:`~scipy.special.ncfdtri`::

        double ncfdtri(double, double, double, double)

- :py:func:`~scipy.special.ncfdtridfd`::

        double ncfdtridfd(double, double, double, double)

- :py:func:`~scipy.special.ncfdtridfn`::

        double ncfdtridfn(double, double, double, double)

- :py:func:`~scipy.special.ncfdtrinc`::

        double ncfdtrinc(double, double, double, double)

- :py:func:`~scipy.special.nctdtr`::

        double nctdtr(double, double, double)

- :py:func:`~scipy.special.nctdtridf`::

        double nctdtridf(double, double, double)

- :py:func:`~scipy.special.nctdtrinc`::

        double nctdtrinc(double, double, double)

- :py:func:`~scipy.special.nctdtrit`::

        double nctdtrit(double, double, double)

- :py:func:`~scipy.special.ndtr`::

        double complex ndtr(double complex)
        double ndtr(double)

- :py:func:`~scipy.special.ndtri`::

        double ndtri(double)

- :py:func:`~scipy.special.nrdtrimn`::

        double nrdtrimn(double, double, double)

- :py:func:`~scipy.special.nrdtrisd`::

        double nrdtrisd(double, double, double)

- :py:func:`~scipy.special.obl_ang1`::

        void obl_ang1(double, double, double, double, double *, double *)

- :py:func:`~scipy.special.obl_ang1_cv`::

        void obl_ang1_cv(double, double, double, double, double, double *, double *)

- :py:func:`~scipy.special.obl_cv`::

        double obl_cv(double, double, double)

- :py:func:`~scipy.special.obl_rad1`::

        void obl_rad1(double, double, double, double, double *, double *)

- :py:func:`~scipy.special.obl_rad1_cv`::

        void obl_rad1_cv(double, double, double, double, double, double *, double *)

- :py:func:`~scipy.special.obl_rad2`::

        void obl_rad2(double, double, double, double, double *, double *)

- :py:func:`~scipy.special.obl_rad2_cv`::

        void obl_rad2_cv(double, double, double, double, double, double *, double *)

- :py:func:`~scipy.special.owens_t`::

        double owens_t(double, double)

- :py:func:`~scipy.special.pbdv`::

        void pbdv(double, double, double *, double *)

- :py:func:`~scipy.special.pbvv`::

        void pbvv(double, double, double *, double *)

- :py:func:`~scipy.special.pbwa`::

        void pbwa(double, double, double *, double *)

- :py:func:`~scipy.special.pdtr`::

        double pdtr(double, double)

- :py:func:`~scipy.special.pdtrc`::

        double pdtrc(double, double)

- :py:func:`~scipy.special.pdtri`::

        double pdtri(double, double)
        double pdtri(long, double)

- :py:func:`~scipy.special.pdtrik`::

        double pdtrik(double, double)

- :py:func:`~scipy.special.poch`::

        double poch(double, double)

- :py:func:`~scipy.special.powm1`::

        float powm1(float, float)
        double powm1(double, double)

- :py:func:`~scipy.special.pro_ang1`::

        void pro_ang1(double, double, double, double, double *, double *)

- :py:func:`~scipy.special.pro_ang1_cv`::

        void pro_ang1_cv(double, double, double, double, double, double *, double *)

- :py:func:`~scipy.special.pro_cv`::

        double pro_cv(double, double, double)

- :py:func:`~scipy.special.pro_rad1`::

        void pro_rad1(double, double, double, double, double *, double *)

- :py:func:`~scipy.special.pro_rad1_cv`::

        void pro_rad1_cv(double, double, double, double, double, double *, double *)

- :py:func:`~scipy.special.pro_rad2`::

        void pro_rad2(double, double, double, double, double *, double *)

- :py:func:`~scipy.special.pro_rad2_cv`::

        void pro_rad2_cv(double, double, double, double, double, double *, double *)

- :py:func:`~scipy.special.pseudo_huber`::

        double pseudo_huber(double, double)

- :py:func:`~scipy.special.psi`::

        double complex psi(double complex)
        double psi(double)

- :py:func:`~scipy.special.radian`::

        double radian(double, double, double)

- :py:func:`~scipy.special.rel_entr`::

        double rel_entr(double, double)

- :py:func:`~scipy.special.rgamma`::

        double complex rgamma(double complex)
        double rgamma(double)

- :py:func:`~scipy.special.round`::

        double round(double)

- :py:func:`~scipy.special.shichi`::

        void shichi(double complex, double complex *, double complex *)
        void shichi(double, double *, double *)

- :py:func:`~scipy.special.sici`::

        void sici(double complex, double complex *, double complex *)
        void sici(double, double *, double *)

- :py:func:`~scipy.special.sindg`::

        double sindg(double)

- :py:func:`~scipy.special.smirnov`::

        double smirnov(double, double)
        double smirnov(long, double)

- :py:func:`~scipy.special.smirnovi`::

        double smirnovi(double, double)
        double smirnovi(long, double)

- :py:func:`~scipy.special.spence`::

        double complex spence(double complex)
        double spence(double)

- :py:func:`~scipy.special.sph_harm`::

        double complex sph_harm(double, double, double, double)
        double complex sph_harm(long, long, double, double)

- :py:func:`~scipy.special.stdtr`::

        double stdtr(double, double)

- :py:func:`~scipy.special.stdtridf`::

        double stdtridf(double, double)

- :py:func:`~scipy.special.stdtrit`::

        double stdtrit(double, double)

- :py:func:`~scipy.special.struve`::

        double struve(double, double)

- :py:func:`~scipy.special.tandg`::

        double tandg(double)

- :py:func:`~scipy.special.tklmbda`::

        double tklmbda(double, double)

- :py:func:`~scipy.special.wofz`::

        double complex wofz(double complex)

- :py:func:`~scipy.special.wrightomega`::

        double complex wrightomega(double complex)
        double wrightomega(double)

- :py:func:`~scipy.special.xlog1py`::

        double xlog1py(double, double)
        double complex xlog1py(double complex, double complex)

- :py:func:`~scipy.special.xlogy`::

        double xlogy(double, double)
        double complex xlogy(double complex, double complex)

- :py:func:`~scipy.special.y0`::

        double y0(double)

- :py:func:`~scipy.special.y1`::

        double y1(double)

- :py:func:`~scipy.special.yn`::

        double yn(double, double)
        double yn(long, double)

- :py:func:`~scipy.special.yv`::

        double complex yv(double, double complex)
        double yv(double, double)

- :py:func:`~scipy.special.yve`::

        double complex yve(double, double complex)
        double yve(double, double)

- :py:func:`~scipy.special.zetac`::

        double zetac(double)

- :py:func:`~scipy.special.wright_bessel`::

        double wright_bessel(double, double, double)

- :py:func:`~scipy.special.ndtri_exp`::

        double ndtri_exp(double)


Custom functions
----------------

Some functions in ``scipy.special`` which are not ufuncs have custom
Cython wrappers.

Spherical Bessel functions
~~~~~~~~~~~~~~~~~~~~~~~~~~

The optional ``derivative`` boolean argument is replaced with an
optional Cython ``bint``, leading to the following signatures.

- :py:func:`~scipy.special.spherical_jn`::

        double complex spherical_jn(long, double complex)
        double complex spherical_jn(long, double complex, bint)
        double spherical_jn(long, double)
        double spherical_jn(long, double, bint)

- :py:func:`~scipy.special.spherical_yn`::

        double complex spherical_yn(long, double complex)
        double complex spherical_yn(long, double complex, bint)
        double spherical_yn(long, double)
        double spherical_yn(long, double, bint)

- :py:func:`~scipy.special.spherical_in`::

        double complex spherical_in(long, double complex)
        double complex spherical_in(long, double complex, bint)
        double spherical_in(long, double)
        double spherical_in(long, double, bint)

- :py:func:`~scipy.special.spherical_kn`::

        double complex spherical_kn(long, double complex)
        double complex spherical_kn(long, double complex, bint)
        double spherical_kn(long, double)
        double spherical_kn(long, double, bint)
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import scipy.special._ufuncs as _ufuncs # /.venv/lib/python3.8/site-packages/scipy/special/_ufuncs.cpython-38-aarch64-linux-gnu.so

# functions

def agm(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.agm """
    pass

def bdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.bdtr """
    pass

def bdtrc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.bdtrc """
    pass

def bdtri(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.bdtri """
    pass

def bdtrik(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.bdtrik """
    pass

def bdtrin(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.bdtrin """
    pass

def bei(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.bei """
    pass

def beip(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.beip """
    pass

def ber(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ber """
    pass

def berp(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.berp """
    pass

def besselpoly(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.besselpoly """
    pass

def beta(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.beta """
    pass

def betainc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.betainc """
    pass

def betaincinv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.betaincinv """
    pass

def betaln(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.betaln """
    pass

def binom(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.binom """
    pass

def boxcox(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.boxcox """
    pass

def boxcox1p(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.boxcox1p """
    pass

def btdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.btdtr """
    pass

def btdtri(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.btdtri """
    pass

def btdtria(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.btdtria """
    pass

def btdtrib(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.btdtrib """
    pass

def cbrt(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.cbrt """
    pass

def chdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.chdtr """
    pass

def chdtrc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.chdtrc """
    pass

def chdtri(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.chdtri """
    pass

def chdtriv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.chdtriv """
    pass

def chndtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.chndtr """
    pass

def chndtridf(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.chndtridf """
    pass

def chndtrinc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.chndtrinc """
    pass

def chndtrix(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.chndtrix """
    pass

def cosdg(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.cosdg """
    pass

def cosm1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.cosm1 """
    pass

def cotdg(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.cotdg """
    pass

def dawsn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.dawsn """
    pass

def ellipe(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ellipe """
    pass

def ellipeinc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ellipeinc """
    pass

def ellipk(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ellipk """
    pass

def ellipkinc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ellipkinc """
    pass

def ellipkm1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ellipkm1 """
    pass

def elliprc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.elliprc """
    pass

def elliprd(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.elliprd """
    pass

def elliprf(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.elliprf """
    pass

def elliprg(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.elliprg """
    pass

def elliprj(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.elliprj """
    pass

def entr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.entr """
    pass

def erf(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.erf """
    pass

def erfc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.erfc """
    pass

def erfcinv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.erfcinv """
    pass

def erfcx(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.erfcx """
    pass

def erfi(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.erfi """
    pass

def erfinv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.erfinv """
    pass

def eval_chebyc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_chebyc """
    pass

def eval_chebys(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_chebys """
    pass

def eval_chebyt(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_chebyt """
    pass

def eval_chebyu(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_chebyu """
    pass

def eval_gegenbauer(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_gegenbauer """
    pass

def eval_genlaguerre(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_genlaguerre """
    pass

def eval_hermite(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_hermite """
    pass

def eval_hermitenorm(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_hermitenorm """
    pass

def eval_jacobi(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_jacobi """
    pass

def eval_laguerre(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_laguerre """
    pass

def eval_legendre(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_legendre """
    pass

def eval_sh_chebyt(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_sh_chebyt """
    pass

def eval_sh_chebyu(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_sh_chebyu """
    pass

def eval_sh_jacobi(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_sh_jacobi """
    pass

def eval_sh_legendre(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.eval_sh_legendre """
    pass

def exp1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.exp1 """
    pass

def exp10(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.exp10 """
    pass

def exp2(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.exp2 """
    pass

def expi(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.expi """
    pass

def expit(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.expit """
    pass

def expm1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.expm1 """
    pass

def expn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.expn """
    pass

def exprel(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.exprel """
    pass

def fdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.fdtr """
    pass

def fdtrc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.fdtrc """
    pass

def fdtri(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.fdtri """
    pass

def fdtridfd(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.fdtridfd """
    pass

def gamma(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gamma """
    pass

def gammainc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gammainc """
    pass

def gammaincc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gammaincc """
    pass

def gammainccinv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gammainccinv """
    pass

def gammaincinv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gammaincinv """
    pass

def gammaln(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gammaln """
    pass

def gammasgn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gammasgn """
    pass

def gdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gdtr """
    pass

def gdtrc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gdtrc """
    pass

def gdtria(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gdtria """
    pass

def gdtrib(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gdtrib """
    pass

def gdtrix(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.gdtrix """
    pass

def hankel1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.hankel1 """
    pass

def hankel1e(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.hankel1e """
    pass

def hankel2(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.hankel2 """
    pass

def hankel2e(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.hankel2e """
    pass

def huber(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.huber """
    pass

def hyp0f1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.hyp0f1 """
    pass

def hyp1f1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.hyp1f1 """
    pass

def hyp2f1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.hyp2f1 """
    pass

def hyperu(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.hyperu """
    pass

def i0(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.i0 """
    pass

def i0e(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.i0e """
    pass

def i1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.i1 """
    pass

def i1e(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.i1e """
    pass

def inv_boxcox(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.inv_boxcox """
    pass

def inv_boxcox1p(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.inv_boxcox1p """
    pass

def it2struve0(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.it2struve0 """
    pass

def itmodstruve0(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.itmodstruve0 """
    pass

def itstruve0(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.itstruve0 """
    pass

def iv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.iv """
    pass

def ive(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ive """
    pass

def j0(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.j0 """
    pass

def j1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.j1 """
    pass

def jv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.jv """
    pass

def jve(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.jve """
    pass

def k0(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.k0 """
    pass

def k0e(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.k0e """
    pass

def k1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.k1 """
    pass

def k1e(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.k1e """
    pass

def kei(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.kei """
    pass

def keip(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.keip """
    pass

def ker(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ker """
    pass

def kerp(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.kerp """
    pass

def kl_div(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.kl_div """
    pass

def kn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.kn """
    pass

def kolmogi(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.kolmogi """
    pass

def kolmogorov(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.kolmogorov """
    pass

def kv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.kv """
    pass

def kve(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.kve """
    pass

def log1p(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.log1p """
    pass

def loggamma(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.loggamma """
    pass

def logit(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.logit """
    pass

def log_expit(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.log_expit """
    pass

def log_ndtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.log_ndtr """
    pass

def lpmv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.lpmv """
    pass

def mathieu_a(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.mathieu_a """
    pass

def mathieu_b(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.mathieu_b """
    pass

def modstruve(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.modstruve """
    pass

def nbdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nbdtr """
    pass

def nbdtrc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nbdtrc """
    pass

def nbdtri(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nbdtri """
    pass

def nbdtrik(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nbdtrik """
    pass

def nbdtrin(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nbdtrin """
    pass

def ncfdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ncfdtr """
    pass

def ncfdtri(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ncfdtri """
    pass

def ncfdtridfd(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ncfdtridfd """
    pass

def ncfdtridfn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ncfdtridfn """
    pass

def ncfdtrinc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ncfdtrinc """
    pass

def nctdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nctdtr """
    pass

def nctdtridf(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nctdtridf """
    pass

def nctdtrinc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nctdtrinc """
    pass

def nctdtrit(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nctdtrit """
    pass

def ndtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ndtr """
    pass

def ndtri(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ndtri """
    pass

def ndtri_exp(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.ndtri_exp """
    pass

def nrdtrimn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nrdtrimn """
    pass

def nrdtrisd(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.nrdtrisd """
    pass

def obl_cv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.obl_cv """
    pass

def owens_t(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.owens_t """
    pass

def pdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.pdtr """
    pass

def pdtrc(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.pdtrc """
    pass

def pdtri(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.pdtri """
    pass

def pdtrik(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.pdtrik """
    pass

def poch(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.poch """
    pass

def powm1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.powm1 """
    pass

def pro_cv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.pro_cv """
    pass

def pseudo_huber(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.pseudo_huber """
    pass

def psi(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.psi """
    pass

def radian(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.radian """
    pass

def rel_entr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.rel_entr """
    pass

def rgamma(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.rgamma """
    pass

def round(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.round """
    pass

def sindg(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.sindg """
    pass

def smirnov(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.smirnov """
    pass

def smirnovi(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.smirnovi """
    pass

def spence(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.spence """
    pass

def spherical_in(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.spherical_in """
    pass

def spherical_jn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.spherical_jn """
    pass

def spherical_kn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.spherical_kn """
    pass

def spherical_yn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.spherical_yn """
    pass

def sph_harm(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.sph_harm """
    pass

def stdtr(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.stdtr """
    pass

def stdtridf(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.stdtridf """
    pass

def stdtrit(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.stdtrit """
    pass

def struve(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.struve """
    pass

def tandg(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.tandg """
    pass

def tklmbda(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.tklmbda """
    pass

def voigt_profile(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.voigt_profile """
    pass

def wofz(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.wofz """
    pass

def wrightomega(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.wrightomega """
    pass

def wright_bessel(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.wright_bessel """
    pass

def xlog1py(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.xlog1py """
    pass

def xlogy(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.xlogy """
    pass

def y0(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.y0 """
    pass

def y1(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.y1 """
    pass

def yn(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.yn """
    pass

def yv(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.yv """
    pass

def yve(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.yve """
    pass

def zetac(*args, **kwargs): # real signature unknown
    """ See the documentation for scipy.special.zetac """
    pass

def _airye_pywrap(*args, **kwargs): # real signature unknown
    pass

def _airy_pywrap(*args, **kwargs): # real signature unknown
    pass

def _bench_airy_d_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_airy_D_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_airy_d_py(*args, **kwargs): # real signature unknown
    pass

def _bench_airy_D_py(*args, **kwargs): # real signature unknown
    pass

def _bench_beta_dd_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_beta_dd_py(*args, **kwargs): # real signature unknown
    pass

def _bench_erf_d_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_erf_D_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_erf_d_py(*args, **kwargs): # real signature unknown
    pass

def _bench_erf_D_py(*args, **kwargs): # real signature unknown
    pass

def _bench_exprel_d_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_exprel_d_py(*args, **kwargs): # real signature unknown
    pass

def _bench_gamma_d_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_gamma_D_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_gamma_d_py(*args, **kwargs): # real signature unknown
    pass

def _bench_gamma_D_py(*args, **kwargs): # real signature unknown
    pass

def _bench_jv_dd_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_jv_dD_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_jv_dd_py(*args, **kwargs): # real signature unknown
    pass

def _bench_jv_dD_py(*args, **kwargs): # real signature unknown
    pass

def _bench_loggamma_D_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_loggamma_D_py(*args, **kwargs): # real signature unknown
    pass

def _bench_logit_d_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_logit_d_py(*args, **kwargs): # real signature unknown
    pass

def _bench_psi_d_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_psi_D_cy(*args, **kwargs): # real signature unknown
    pass

def _bench_psi_d_py(*args, **kwargs): # real signature unknown
    pass

def _bench_psi_D_py(*args, **kwargs): # real signature unknown
    pass

def _ellipj_pywrap(*args, **kwargs): # real signature unknown
    pass

def _fresnel_pywrap(*args, **kwargs): # real signature unknown
    pass

def _it2i0k0_pywrap(*args, **kwargs): # real signature unknown
    pass

def _it2j0y0_pywrap(*args, **kwargs): # real signature unknown
    pass

def _itairy_pywrap(*args, **kwargs): # real signature unknown
    pass

def _iti0k0_pywrap(*args, **kwargs): # real signature unknown
    pass

def _itj0y0_pywrap(*args, **kwargs): # real signature unknown
    pass

def _kelvin_pywrap(*args, **kwargs): # real signature unknown
    pass

def _mathieu_cem_pywrap(*args, **kwargs): # real signature unknown
    pass

def _mathieu_modcem1_pywrap(*args, **kwargs): # real signature unknown
    pass

def _mathieu_modcem2_pywrap(*args, **kwargs): # real signature unknown
    pass

def _mathieu_modsem1_pywrap(*args, **kwargs): # real signature unknown
    pass

def _mathieu_modsem2_pywrap(*args, **kwargs): # real signature unknown
    pass

def _mathieu_sem_pywrap(*args, **kwargs): # real signature unknown
    pass

def _modfresnelm_pywrap(*args, **kwargs): # real signature unknown
    pass

def _modfresnelp_pywrap(*args, **kwargs): # real signature unknown
    pass

def _obl_ang1_cv_pywrap(*args, **kwargs): # real signature unknown
    pass

def _obl_ang1_pywrap(*args, **kwargs): # real signature unknown
    pass

def _obl_rad1_cv_pywrap(*args, **kwargs): # real signature unknown
    pass

def _obl_rad1_pywrap(*args, **kwargs): # real signature unknown
    pass

def _obl_rad2_cv_pywrap(*args, **kwargs): # real signature unknown
    pass

def _obl_rad2_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pbdv_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pbvv_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pbwa_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pro_ang1_cv_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pro_ang1_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pro_rad1_cv_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pro_rad1_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pro_rad2_cv_pywrap(*args, **kwargs): # real signature unknown
    pass

def _pro_rad2_pywrap(*args, **kwargs): # real signature unknown
    pass

def _shichi_pywrap(*args, **kwargs): # real signature unknown
    pass

def _sici_pywrap(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924eb0>'

__pyx_capi__ = {
    '__pyx_fuse_0_0eval_chebyc': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3a810>'
    '__pyx_fuse_0_0eval_chebys': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3a8d0>'
    '__pyx_fuse_0_0eval_chebyt': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3a990>'
    '__pyx_fuse_0_0eval_chebyu': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3aa50>'
    '__pyx_fuse_0_0eval_gegenbauer': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3ab10>'
    '__pyx_fuse_0_0eval_genlaguerre': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3abd0>'
    '__pyx_fuse_0_0eval_jacobi': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, double, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3ac90>'
    '__pyx_fuse_0_0eval_laguerre': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3ad50>'
    '__pyx_fuse_0_0eval_legendre': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3ae10>'
    '__pyx_fuse_0_0eval_sh_chebyt': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3aed0>'
    '__pyx_fuse_0_0eval_sh_chebyu': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3af90>'
    '__pyx_fuse_0_0eval_sh_jacobi': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, double, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b090>'
    '__pyx_fuse_0_0eval_sh_legendre': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b150>'
    '__pyx_fuse_0_1eval_chebyc': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3a840>'
    '__pyx_fuse_0_1eval_chebys': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3a900>'
    '__pyx_fuse_0_1eval_chebyt': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3a9c0>'
    '__pyx_fuse_0_1eval_chebyu': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3aa80>'
    '__pyx_fuse_0_1eval_gegenbauer': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3ab40>'
    '__pyx_fuse_0_1eval_genlaguerre': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3ac00>'
    '__pyx_fuse_0_1eval_jacobi': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3acc0>'
    '__pyx_fuse_0_1eval_laguerre': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3ad80>'
    '__pyx_fuse_0_1eval_legendre': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3ae40>'
    '__pyx_fuse_0_1eval_sh_chebyt': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3af00>'
    '__pyx_fuse_0_1eval_sh_chebyu': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3afc0>'
    '__pyx_fuse_0_1eval_sh_jacobi': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3b0c0>'
    '__pyx_fuse_0_1eval_sh_legendre': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3b180>'
    '__pyx_fuse_0airy': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0xffff92e3a210>'
    '__pyx_fuse_0airye': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0xffff92e3a270>'
    '__pyx_fuse_0bdtr': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3a2d0>'
    '__pyx_fuse_0bdtrc': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3a330>'
    '__pyx_fuse_0bdtri': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3a390>'
    '__pyx_fuse_0dawsn': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3a3f0>'
    '__pyx_fuse_0elliprc': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3a450>'
    '__pyx_fuse_0elliprd': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, __pyx_t_double_complex, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3a4b0>'
    '__pyx_fuse_0elliprf': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, __pyx_t_double_complex, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3a510>'
    '__pyx_fuse_0elliprg': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, __pyx_t_double_complex, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3a570>'
    '__pyx_fuse_0elliprj': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, __pyx_t_double_complex, __pyx_t_double_complex, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3a5d0>'
    '__pyx_fuse_0erf': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3a630>'
    '__pyx_fuse_0erfc': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3a690>'
    '__pyx_fuse_0erfcx': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3a6f0>'
    '__pyx_fuse_0erfi': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3a750>'
    '__pyx_fuse_0erfinv': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3a7b0>'
    '__pyx_fuse_0exp1': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b210>'
    '__pyx_fuse_0expi': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b270>'
    '__pyx_fuse_0expit': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3b2d0>'
    '__pyx_fuse_0expm1': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b360>'
    '__pyx_fuse_0expn': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3b3c0>'
    '__pyx_fuse_0fresnel': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0xffff92e3b420>'
    '__pyx_fuse_0gamma': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b480>'
    '__pyx_fuse_0hyp0f1': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b4e0>'
    '__pyx_fuse_0hyp1f1': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b540>'
    '__pyx_fuse_0hyp2f1': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, double, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b5a0>'
    '__pyx_fuse_0iv': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b600>'
    '__pyx_fuse_0ive': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b660>'
    '__pyx_fuse_0jv': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b6c0>'
    '__pyx_fuse_0jve': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b720>'
    '__pyx_fuse_0kn': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3b780>'
    '__pyx_fuse_0kv': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b7e0>'
    '__pyx_fuse_0kve': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b840>'
    '__pyx_fuse_0log1p': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b8a0>'
    '__pyx_fuse_0log_expit': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3b900>'
    '__pyx_fuse_0log_ndtr': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b990>'
    '__pyx_fuse_0loggamma': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b9f0>'
    '__pyx_fuse_0logit': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3ba50>'
    '__pyx_fuse_0nbdtr': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3bae0>'
    '__pyx_fuse_0nbdtrc': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3bb40>'
    '__pyx_fuse_0nbdtri': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3bba0>'
    '__pyx_fuse_0ndtr': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3bc00>'
    '__pyx_fuse_0pdtri': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3bc60>'
    '__pyx_fuse_0powm1': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3bcc0>'
    '__pyx_fuse_0psi': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3bd20>'
    '__pyx_fuse_0rgamma': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3bd80>'
    '__pyx_fuse_0shichi': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0xffff92e3bde0>'
    '__pyx_fuse_0sici': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0xffff92e3be40>'
    '__pyx_fuse_0smirnov': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3bea0>'
    '__pyx_fuse_0smirnovi': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3bf00>'
    '__pyx_fuse_0spence': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3bf60>'
    '__pyx_fuse_0sph_harm': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3bfc0>'
    '__pyx_fuse_0spherical_in': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch, struct __pyx_fuse_0__pyx_opt_args_5scipy_7special_14cython_special_spherical_in *__pyx_optional_args)" at 0xffff92e3a150>'
    '__pyx_fuse_0spherical_jn': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch, struct __pyx_fuse_0__pyx_opt_args_5scipy_7special_14cython_special_spherical_jn *__pyx_optional_args)" at 0xffff92e3a090>'
    '__pyx_fuse_0spherical_kn': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch, struct __pyx_fuse_0__pyx_opt_args_5scipy_7special_14cython_special_spherical_kn *__pyx_optional_args)" at 0xffff92e3a1b0>'
    '__pyx_fuse_0spherical_yn': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch, struct __pyx_fuse_0__pyx_opt_args_5scipy_7special_14cython_special_spherical_yn *__pyx_optional_args)" at 0xffff92e3a0f0>'
    '__pyx_fuse_0wrightomega': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3c060>'
    '__pyx_fuse_0xlog1py': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3c0c0>'
    '__pyx_fuse_0xlogy': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3c120>'
    '__pyx_fuse_0yn': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3c180>'
    '__pyx_fuse_0yv': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3c1e0>'
    '__pyx_fuse_0yve': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3c240>'
    '__pyx_fuse_1_0eval_chebyc': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3a870>'
    '__pyx_fuse_1_0eval_chebys': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3a930>'
    '__pyx_fuse_1_0eval_chebyt': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3a9f0>'
    '__pyx_fuse_1_0eval_chebyu': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3aab0>'
    '__pyx_fuse_1_0eval_gegenbauer': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3ab70>'
    '__pyx_fuse_1_0eval_genlaguerre': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3ac30>'
    '__pyx_fuse_1_0eval_jacobi': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, double, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3acf0>'
    '__pyx_fuse_1_0eval_laguerre': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3adb0>'
    '__pyx_fuse_1_0eval_legendre': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3ae70>'
    '__pyx_fuse_1_0eval_sh_chebyt': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3af30>'
    '__pyx_fuse_1_0eval_sh_chebyu': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b030>'
    '__pyx_fuse_1_0eval_sh_jacobi': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, double, double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b0f0>'
    '__pyx_fuse_1_0eval_sh_legendre': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e3b1b0>'
    '__pyx_fuse_1_1eval_chebyc': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e3a8a0>'
    '__pyx_fuse_1_1eval_chebys': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e3a960>'
    '__pyx_fuse_1_1eval_chebyt': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e3aa20>'
    '__pyx_fuse_1_1eval_chebyu': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e3aae0>'
    '__pyx_fuse_1_1eval_gegenbauer': None, # (!) real value is '<capsule object "double (long, double, double, int __pyx_skip_dispatch)" at 0xffff92e3aba0>'
    '__pyx_fuse_1_1eval_genlaguerre': None, # (!) real value is '<capsule object "double (long, double, double, int __pyx_skip_dispatch)" at 0xffff92e3ac60>'
    '__pyx_fuse_1_1eval_jacobi': None, # (!) real value is '<capsule object "double (long, double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3ad20>'
    '__pyx_fuse_1_1eval_laguerre': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e3ade0>'
    '__pyx_fuse_1_1eval_legendre': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e3aea0>'
    '__pyx_fuse_1_1eval_sh_chebyt': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e3af60>'
    '__pyx_fuse_1_1eval_sh_chebyu': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e3b060>'
    '__pyx_fuse_1_1eval_sh_jacobi': None, # (!) real value is '<capsule object "double (long, double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3b120>'
    '__pyx_fuse_1_1eval_sh_legendre': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e3b1e0>'
    '__pyx_fuse_1airy': None, # (!) real value is '<capsule object "void (double, double *, double *, double *, double *)" at 0xffff92e3a240>'
    '__pyx_fuse_1airye': None, # (!) real value is '<capsule object "void (double, double *, double *, double *, double *)" at 0xffff92e3a2a0>'
    '__pyx_fuse_1bdtr': None, # (!) real value is '<capsule object "double (double, long, double, int __pyx_skip_dispatch)" at 0xffff92e3a300>'
    '__pyx_fuse_1bdtrc': None, # (!) real value is '<capsule object "double (double, long, double, int __pyx_skip_dispatch)" at 0xffff92e3a360>'
    '__pyx_fuse_1bdtri': None, # (!) real value is '<capsule object "double (double, long, double, int __pyx_skip_dispatch)" at 0xffff92e3a3c0>'
    '__pyx_fuse_1dawsn': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3a420>'
    '__pyx_fuse_1elliprc': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3a480>'
    '__pyx_fuse_1elliprd': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3a4e0>'
    '__pyx_fuse_1elliprf': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3a540>'
    '__pyx_fuse_1elliprg': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3a5a0>'
    '__pyx_fuse_1elliprj': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3a600>'
    '__pyx_fuse_1erf': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3a660>'
    '__pyx_fuse_1erfc': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3a6c0>'
    '__pyx_fuse_1erfcx': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3a720>'
    '__pyx_fuse_1erfi': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3a780>'
    '__pyx_fuse_1erfinv': None, # (!) real value is '<capsule object "float (float, int __pyx_skip_dispatch)" at 0xffff92e3a7e0>'
    '__pyx_fuse_1exp1': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3b240>'
    '__pyx_fuse_1expi': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3b2a0>'
    '__pyx_fuse_1expit': None, # (!) real value is '<capsule object "float (float, int __pyx_skip_dispatch)" at 0xffff92e3b300>'
    '__pyx_fuse_1expm1': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3b390>'
    '__pyx_fuse_1expn': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e3b3f0>'
    '__pyx_fuse_1fresnel': None, # (!) real value is '<capsule object "void (double, double *, double *)" at 0xffff92e3b450>'
    '__pyx_fuse_1gamma': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3b4b0>'
    '__pyx_fuse_1hyp0f1': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3b510>'
    '__pyx_fuse_1hyp1f1': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3b570>'
    '__pyx_fuse_1hyp2f1': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3b5d0>'
    '__pyx_fuse_1iv': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3b630>'
    '__pyx_fuse_1ive': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3b690>'
    '__pyx_fuse_1jv': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3b6f0>'
    '__pyx_fuse_1jve': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3b750>'
    '__pyx_fuse_1kn': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e3b7b0>'
    '__pyx_fuse_1kv': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3b810>'
    '__pyx_fuse_1kve': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3b870>'
    '__pyx_fuse_1log1p': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3b8d0>'
    '__pyx_fuse_1log_expit': None, # (!) real value is '<capsule object "float (float, int __pyx_skip_dispatch)" at 0xffff92e3b930>'
    '__pyx_fuse_1log_ndtr': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3b9c0>'
    '__pyx_fuse_1loggamma': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3ba20>'
    '__pyx_fuse_1logit': None, # (!) real value is '<capsule object "float (float, int __pyx_skip_dispatch)" at 0xffff92e3ba80>'
    '__pyx_fuse_1nbdtr': None, # (!) real value is '<capsule object "double (long, long, double, int __pyx_skip_dispatch)" at 0xffff92e3bb10>'
    '__pyx_fuse_1nbdtrc': None, # (!) real value is '<capsule object "double (long, long, double, int __pyx_skip_dispatch)" at 0xffff92e3bb70>'
    '__pyx_fuse_1nbdtri': None, # (!) real value is '<capsule object "double (long, long, double, int __pyx_skip_dispatch)" at 0xffff92e3bbd0>'
    '__pyx_fuse_1ndtr': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3bc30>'
    '__pyx_fuse_1pdtri': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e3bc90>'
    '__pyx_fuse_1powm1': None, # (!) real value is '<capsule object "float (float, float, int __pyx_skip_dispatch)" at 0xffff92e3bcf0>'
    '__pyx_fuse_1psi': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3bd50>'
    '__pyx_fuse_1rgamma': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3bdb0>'
    '__pyx_fuse_1shichi': None, # (!) real value is '<capsule object "void (double, double *, double *)" at 0xffff92e3be10>'
    '__pyx_fuse_1sici': None, # (!) real value is '<capsule object "void (double, double *, double *)" at 0xffff92e3be70>'
    '__pyx_fuse_1smirnov': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e3bed0>'
    '__pyx_fuse_1smirnovi': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e3bf30>'
    '__pyx_fuse_1spence': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3bf90>'
    '__pyx_fuse_1sph_harm': None, # (!) real value is '<capsule object "__pyx_t_double_complex (long, long, double, double, int __pyx_skip_dispatch)" at 0xffff92e3c030>'
    '__pyx_fuse_1spherical_in': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch, struct __pyx_fuse_1__pyx_opt_args_5scipy_7special_14cython_special_spherical_in *__pyx_optional_args)" at 0xffff92e3a180>'
    '__pyx_fuse_1spherical_jn': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch, struct __pyx_fuse_1__pyx_opt_args_5scipy_7special_14cython_special_spherical_jn *__pyx_optional_args)" at 0xffff92e3a0c0>'
    '__pyx_fuse_1spherical_kn': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch, struct __pyx_fuse_1__pyx_opt_args_5scipy_7special_14cython_special_spherical_kn *__pyx_optional_args)" at 0xffff92e3a1e0>'
    '__pyx_fuse_1spherical_yn': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch, struct __pyx_fuse_1__pyx_opt_args_5scipy_7special_14cython_special_spherical_yn *__pyx_optional_args)" at 0xffff92e3a120>'
    '__pyx_fuse_1wrightomega': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3c090>'
    '__pyx_fuse_1xlog1py': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3c0f0>'
    '__pyx_fuse_1xlogy': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3c150>'
    '__pyx_fuse_1yn': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e3c1b0>'
    '__pyx_fuse_1yv': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3c210>'
    '__pyx_fuse_1yve': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e3c270>'
    '__pyx_fuse_2expit': None, # (!) real value is '<capsule object "long double (long double, int __pyx_skip_dispatch)" at 0xffff92e3b330>'
    '__pyx_fuse_2log_expit': None, # (!) real value is '<capsule object "long double (long double, int __pyx_skip_dispatch)" at 0xffff92e3b960>'
    '__pyx_fuse_2logit': None, # (!) real value is '<capsule object "long double (long double, int __pyx_skip_dispatch)" at 0xffff92e3bab0>'
    'agm': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e1d750>'
    'bdtrik': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffffac924c90>'
    'bdtrin': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffffac924b40>'
    'bei': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffffac924f90>'
    'beip': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffffac924ab0>'
    'ber': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e272d0>'
    'berp': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27390>'
    'besselpoly': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e273c0>'
    'beta': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e273f0>'
    'betainc': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27420>'
    'betaincinv': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27450>'
    'betaln': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e27480>'
    'binom': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e274b0>'
    'boxcox': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e274e0>'
    'boxcox1p': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e27510>'
    'btdtr': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27540>'
    'btdtri': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27570>'
    'btdtria': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e275a0>'
    'btdtrib': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e275d0>'
    'cbrt': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27600>'
    'chdtr': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e27630>'
    'chdtrc': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e27660>'
    'chdtri': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e27690>'
    'chdtriv': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e276c0>'
    'chndtr': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e276f0>'
    'chndtridf': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27720>'
    'chndtrinc': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27750>'
    'chndtrix': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27780>'
    'cosdg': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e277b0>'
    'cosm1': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e277e0>'
    'cotdg': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27810>'
    'ellipe': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27840>'
    'ellipeinc': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e27870>'
    'ellipj': None, # (!) real value is '<capsule object "void (double, double, double *, double *, double *, double *)" at 0xffff92e278a0>'
    'ellipk': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27930>'
    'ellipkinc': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e278d0>'
    'ellipkm1': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27900>'
    'entr': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27960>'
    'erfcinv': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27990>'
    'eval_hermite': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e279c0>'
    'eval_hermitenorm': None, # (!) real value is '<capsule object "double (long, double, int __pyx_skip_dispatch)" at 0xffff92e279f0>'
    'exp10': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27a20>'
    'exp2': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27a50>'
    'exprel': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27a80>'
    'fdtr': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27ab0>'
    'fdtrc': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27ae0>'
    'fdtri': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27b10>'
    'fdtridfd': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27b40>'
    'gammainc': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e27b70>'
    'gammaincc': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e27ba0>'
    'gammainccinv': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e27bd0>'
    'gammaincinv': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e27c00>'
    'gammaln': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27c30>'
    'gammasgn': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27c60>'
    'gdtr': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27c90>'
    'gdtrc': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27cc0>'
    'gdtria': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27cf0>'
    'gdtrib': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27d20>'
    'gdtrix': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27d50>'
    'hankel1': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e27d80>'
    'hankel1e': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e27db0>'
    'hankel2': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e27de0>'
    'hankel2e': None, # (!) real value is '<capsule object "__pyx_t_double_complex (double, __pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e27e10>'
    'huber': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e27e40>'
    'hyperu': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e27e70>'
    'i0': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27ea0>'
    'i0e': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27ed0>'
    'i1': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27f00>'
    'i1e': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e27f30>'
    'inv_boxcox': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e27f60>'
    'inv_boxcox1p': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e27f90>'
    'it2i0k0': None, # (!) real value is '<capsule object "void (double, double *, double *)" at 0xffff92e27fc0>'
    'it2j0y0': None, # (!) real value is '<capsule object "void (double, double *, double *)" at 0xffff92e39030>'
    'it2struve0': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e39060>'
    'itairy': None, # (!) real value is '<capsule object "void (double, double *, double *, double *, double *)" at 0xffff92e39090>'
    'iti0k0': None, # (!) real value is '<capsule object "void (double, double *, double *)" at 0xffff92e390c0>'
    'itj0y0': None, # (!) real value is '<capsule object "void (double, double *, double *)" at 0xffff92e390f0>'
    'itmodstruve0': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e39120>'
    'itstruve0': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e39150>'
    'j0': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e39180>'
    'j1': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e391b0>'
    'k0': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e391e0>'
    'k0e': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e39210>'
    'k1': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e39240>'
    'k1e': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e39270>'
    'kei': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e392a0>'
    'keip': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e392d0>'
    'kelvin': None, # (!) real value is '<capsule object "void (double, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0xffff92e39300>'
    'ker': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e39330>'
    'kerp': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e39360>'
    'kl_div': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e39390>'
    'kolmogi': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e393c0>'
    'kolmogorov': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e393f0>'
    'lpmv': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e39420>'
    'mathieu_a': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e39450>'
    'mathieu_b': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e39480>'
    'mathieu_cem': None, # (!) real value is '<capsule object "void (double, double, double, double *, double *)" at 0xffff92e394b0>'
    'mathieu_modcem1': None, # (!) real value is '<capsule object "void (double, double, double, double *, double *)" at 0xffff92e394e0>'
    'mathieu_modcem2': None, # (!) real value is '<capsule object "void (double, double, double, double *, double *)" at 0xffff92e39510>'
    'mathieu_modsem1': None, # (!) real value is '<capsule object "void (double, double, double, double *, double *)" at 0xffff92e39540>'
    'mathieu_modsem2': None, # (!) real value is '<capsule object "void (double, double, double, double *, double *)" at 0xffff92e39570>'
    'mathieu_sem': None, # (!) real value is '<capsule object "void (double, double, double, double *, double *)" at 0xffff92e395a0>'
    'modfresnelm': None, # (!) real value is '<capsule object "void (double, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0xffff92e395d0>'
    'modfresnelp': None, # (!) real value is '<capsule object "void (double, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0xffff92e39600>'
    'modstruve': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e39630>'
    'nbdtrik': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e39660>'
    'nbdtrin': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e39690>'
    'ncfdtr': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0xffff92e396c0>'
    'ncfdtri': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0xffff92e396f0>'
    'ncfdtridfd': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0xffff92e39720>'
    'ncfdtridfn': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0xffff92e39750>'
    'ncfdtrinc': None, # (!) real value is '<capsule object "double (double, double, double, double, int __pyx_skip_dispatch)" at 0xffff92e39780>'
    'nctdtr': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e397b0>'
    'nctdtridf': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e397e0>'
    'nctdtrinc': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e39810>'
    'nctdtrit': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e39840>'
    'ndtri': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e39870>'
    'ndtri_exp': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e3a060>'
    'nrdtrimn': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e398a0>'
    'nrdtrisd': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e398d0>'
    'obl_ang1': None, # (!) real value is '<capsule object "void (double, double, double, double, double *, double *)" at 0xffff92e39900>'
    'obl_ang1_cv': None, # (!) real value is '<capsule object "void (double, double, double, double, double, double *, double *)" at 0xffff92e39930>'
    'obl_cv': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e39960>'
    'obl_rad1': None, # (!) real value is '<capsule object "void (double, double, double, double, double *, double *)" at 0xffff92e39990>'
    'obl_rad1_cv': None, # (!) real value is '<capsule object "void (double, double, double, double, double, double *, double *)" at 0xffff92e399c0>'
    'obl_rad2': None, # (!) real value is '<capsule object "void (double, double, double, double, double *, double *)" at 0xffff92e399f0>'
    'obl_rad2_cv': None, # (!) real value is '<capsule object "void (double, double, double, double, double, double *, double *)" at 0xffff92e39a20>'
    'owens_t': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e39a50>'
    'pbdv': None, # (!) real value is '<capsule object "void (double, double, double *, double *)" at 0xffff92e39a80>'
    'pbvv': None, # (!) real value is '<capsule object "void (double, double, double *, double *)" at 0xffff92e39ab0>'
    'pbwa': None, # (!) real value is '<capsule object "void (double, double, double *, double *)" at 0xffff92e39ae0>'
    'pdtr': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e39b10>'
    'pdtrc': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e39b40>'
    'pdtrik': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e39b70>'
    'poch': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e39ba0>'
    'pro_ang1': None, # (!) real value is '<capsule object "void (double, double, double, double, double *, double *)" at 0xffff92e39bd0>'
    'pro_ang1_cv': None, # (!) real value is '<capsule object "void (double, double, double, double, double, double *, double *)" at 0xffff92e39c00>'
    'pro_cv': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e39c30>'
    'pro_rad1': None, # (!) real value is '<capsule object "void (double, double, double, double, double *, double *)" at 0xffff92e39c60>'
    'pro_rad1_cv': None, # (!) real value is '<capsule object "void (double, double, double, double, double, double *, double *)" at 0xffff92e39c90>'
    'pro_rad2': None, # (!) real value is '<capsule object "void (double, double, double, double, double *, double *)" at 0xffff92e39cc0>'
    'pro_rad2_cv': None, # (!) real value is '<capsule object "void (double, double, double, double, double, double *, double *)" at 0xffff92e39cf0>'
    'pseudo_huber': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e39d20>'
    'radian': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e39d50>'
    'rel_entr': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e39d80>'
    'round': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e39db0>'
    'sindg': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e39de0>'
    'stdtr': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e39e10>'
    'stdtridf': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e39e40>'
    'stdtrit': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e39e70>'
    'struve': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e39ea0>'
    'tandg': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e39ed0>'
    'tklmbda': None, # (!) real value is '<capsule object "double (double, double, int __pyx_skip_dispatch)" at 0xffff92e39f00>'
    'voigt_profile': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff9beeae40>'
    'wofz': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex, int __pyx_skip_dispatch)" at 0xffff92e39f30>'
    'wright_bessel': None, # (!) real value is '<capsule object "double (double, double, double, int __pyx_skip_dispatch)" at 0xffff92e3a030>'
    'y0': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e39f60>'
    'y1': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e39f90>'
    'zetac': None, # (!) real value is '<capsule object "double (double, int __pyx_skip_dispatch)" at 0xffff92e39fc0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.special.cython_special', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924eb0>, origin='/.venv/lib/python3.8/site-packages/scipy/special/cython_special.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

