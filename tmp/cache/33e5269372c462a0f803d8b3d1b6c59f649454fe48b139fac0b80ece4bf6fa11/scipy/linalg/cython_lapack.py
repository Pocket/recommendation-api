# encoding: utf-8
# module scipy.linalg.cython_lapack
# from /.venv/lib/python3.8/site-packages/scipy/linalg/cython_lapack.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
LAPACK functions for Cython
===========================

Usable from Cython via::

    cimport scipy.linalg.cython_lapack

This module provides Cython-level wrappers for all primary routines included
in LAPACK 3.4.0 except for ``zcgesv`` since its interface is not consistent
from LAPACK 3.4.0 to 3.6.0. It also provides some of the
fixed-api auxiliary routines.

These wrappers do not check for alignment of arrays.
Alignment should be checked before these wrappers are used.

Raw function pointers (Fortran-style pointer arguments):

- cbbcsd
- cbdsqr
- cgbbrd
- cgbcon
- cgbequ
- cgbequb
- cgbrfs
- cgbsv
- cgbsvx
- cgbtf2
- cgbtrf
- cgbtrs
- cgebak
- cgebal
- cgebd2
- cgebrd
- cgecon
- cgeequ
- cgeequb
- cgees
- cgeesx
- cgeev
- cgeevx
- cgehd2
- cgehrd
- cgelq2
- cgelqf
- cgels
- cgelsd
- cgelss
- cgelsy
- cgemqrt
- cgeql2
- cgeqlf
- cgeqp3
- cgeqr2
- cgeqr2p
- cgeqrf
- cgeqrfp
- cgeqrt
- cgeqrt2
- cgeqrt3
- cgerfs
- cgerq2
- cgerqf
- cgesc2
- cgesdd
- cgesv
- cgesvd
- cgesvx
- cgetc2
- cgetf2
- cgetrf
- cgetri
- cgetrs
- cggbak
- cggbal
- cgges
- cggesx
- cggev
- cggevx
- cggglm
- cgghrd
- cgglse
- cggqrf
- cggrqf
- cgtcon
- cgtrfs
- cgtsv
- cgtsvx
- cgttrf
- cgttrs
- cgtts2
- chbev
- chbevd
- chbevx
- chbgst
- chbgv
- chbgvd
- chbgvx
- chbtrd
- checon
- cheequb
- cheev
- cheevd
- cheevr
- cheevx
- chegs2
- chegst
- chegv
- chegvd
- chegvx
- cherfs
- chesv
- chesvx
- cheswapr
- chetd2
- chetf2
- chetrd
- chetrf
- chetri
- chetri2
- chetri2x
- chetrs
- chetrs2
- chfrk
- chgeqz
- chla_transtype
- chpcon
- chpev
- chpevd
- chpevx
- chpgst
- chpgv
- chpgvd
- chpgvx
- chprfs
- chpsv
- chpsvx
- chptrd
- chptrf
- chptri
- chptrs
- chsein
- chseqr
- clabrd
- clacgv
- clacn2
- clacon
- clacp2
- clacpy
- clacrm
- clacrt
- cladiv
- claed0
- claed7
- claed8
- claein
- claesy
- claev2
- clag2z
- clags2
- clagtm
- clahef
- clahqr
- clahr2
- claic1
- clals0
- clalsa
- clalsd
- clangb
- clange
- clangt
- clanhb
- clanhe
- clanhf
- clanhp
- clanhs
- clanht
- clansb
- clansp
- clansy
- clantb
- clantp
- clantr
- clapll
- clapmr
- clapmt
- claqgb
- claqge
- claqhb
- claqhe
- claqhp
- claqp2
- claqps
- claqr0
- claqr1
- claqr2
- claqr3
- claqr4
- claqr5
- claqsb
- claqsp
- claqsy
- clar1v
- clar2v
- clarcm
- clarf
- clarfb
- clarfg
- clarfgp
- clarft
- clarfx
- clargv
- clarnv
- clarrv
- clartg
- clartv
- clarz
- clarzb
- clarzt
- clascl
- claset
- clasr
- classq
- claswp
- clasyf
- clatbs
- clatdf
- clatps
- clatrd
- clatrs
- clatrz
- clauu2
- clauum
- cpbcon
- cpbequ
- cpbrfs
- cpbstf
- cpbsv
- cpbsvx
- cpbtf2
- cpbtrf
- cpbtrs
- cpftrf
- cpftri
- cpftrs
- cpocon
- cpoequ
- cpoequb
- cporfs
- cposv
- cposvx
- cpotf2
- cpotrf
- cpotri
- cpotrs
- cppcon
- cppequ
- cpprfs
- cppsv
- cppsvx
- cpptrf
- cpptri
- cpptrs
- cpstf2
- cpstrf
- cptcon
- cpteqr
- cptrfs
- cptsv
- cptsvx
- cpttrf
- cpttrs
- cptts2
- crot
- cspcon
- cspmv
- cspr
- csprfs
- cspsv
- cspsvx
- csptrf
- csptri
- csptrs
- csrscl
- cstedc
- cstegr
- cstein
- cstemr
- csteqr
- csycon
- csyconv
- csyequb
- csymv
- csyr
- csyrfs
- csysv
- csysvx
- csyswapr
- csytf2
- csytrf
- csytri
- csytri2
- csytri2x
- csytrs
- csytrs2
- ctbcon
- ctbrfs
- ctbtrs
- ctfsm
- ctftri
- ctfttp
- ctfttr
- ctgevc
- ctgex2
- ctgexc
- ctgsen
- ctgsja
- ctgsna
- ctgsy2
- ctgsyl
- ctpcon
- ctpmqrt
- ctpqrt
- ctpqrt2
- ctprfb
- ctprfs
- ctptri
- ctptrs
- ctpttf
- ctpttr
- ctrcon
- ctrevc
- ctrexc
- ctrrfs
- ctrsen
- ctrsna
- ctrsyl
- ctrti2
- ctrtri
- ctrtrs
- ctrttf
- ctrttp
- ctzrzf
- cunbdb
- cuncsd
- cung2l
- cung2r
- cungbr
- cunghr
- cungl2
- cunglq
- cungql
- cungqr
- cungr2
- cungrq
- cungtr
- cunm2l
- cunm2r
- cunmbr
- cunmhr
- cunml2
- cunmlq
- cunmql
- cunmqr
- cunmr2
- cunmr3
- cunmrq
- cunmrz
- cunmtr
- cupgtr
- cupmtr
- dbbcsd
- dbdsdc
- dbdsqr
- ddisna
- dgbbrd
- dgbcon
- dgbequ
- dgbequb
- dgbrfs
- dgbsv
- dgbsvx
- dgbtf2
- dgbtrf
- dgbtrs
- dgebak
- dgebal
- dgebd2
- dgebrd
- dgecon
- dgeequ
- dgeequb
- dgees
- dgeesx
- dgeev
- dgeevx
- dgehd2
- dgehrd
- dgejsv
- dgelq2
- dgelqf
- dgels
- dgelsd
- dgelss
- dgelsy
- dgemqrt
- dgeql2
- dgeqlf
- dgeqp3
- dgeqr2
- dgeqr2p
- dgeqrf
- dgeqrfp
- dgeqrt
- dgeqrt2
- dgeqrt3
- dgerfs
- dgerq2
- dgerqf
- dgesc2
- dgesdd
- dgesv
- dgesvd
- dgesvj
- dgesvx
- dgetc2
- dgetf2
- dgetrf
- dgetri
- dgetrs
- dggbak
- dggbal
- dgges
- dggesx
- dggev
- dggevx
- dggglm
- dgghrd
- dgglse
- dggqrf
- dggrqf
- dgsvj0
- dgsvj1
- dgtcon
- dgtrfs
- dgtsv
- dgtsvx
- dgttrf
- dgttrs
- dgtts2
- dhgeqz
- dhsein
- dhseqr
- disnan
- dlabad
- dlabrd
- dlacn2
- dlacon
- dlacpy
- dladiv
- dlae2
- dlaebz
- dlaed0
- dlaed1
- dlaed2
- dlaed3
- dlaed4
- dlaed5
- dlaed6
- dlaed7
- dlaed8
- dlaed9
- dlaeda
- dlaein
- dlaev2
- dlaexc
- dlag2
- dlag2s
- dlags2
- dlagtf
- dlagtm
- dlagts
- dlagv2
- dlahqr
- dlahr2
- dlaic1
- dlaln2
- dlals0
- dlalsa
- dlalsd
- dlamch
- dlamrg
- dlaneg
- dlangb
- dlange
- dlangt
- dlanhs
- dlansb
- dlansf
- dlansp
- dlanst
- dlansy
- dlantb
- dlantp
- dlantr
- dlanv2
- dlapll
- dlapmr
- dlapmt
- dlapy2
- dlapy3
- dlaqgb
- dlaqge
- dlaqp2
- dlaqps
- dlaqr0
- dlaqr1
- dlaqr2
- dlaqr3
- dlaqr4
- dlaqr5
- dlaqsb
- dlaqsp
- dlaqsy
- dlaqtr
- dlar1v
- dlar2v
- dlarf
- dlarfb
- dlarfg
- dlarfgp
- dlarft
- dlarfx
- dlargv
- dlarnv
- dlarra
- dlarrb
- dlarrc
- dlarrd
- dlarre
- dlarrf
- dlarrj
- dlarrk
- dlarrr
- dlarrv
- dlartg
- dlartgp
- dlartgs
- dlartv
- dlaruv
- dlarz
- dlarzb
- dlarzt
- dlas2
- dlascl
- dlasd0
- dlasd1
- dlasd2
- dlasd3
- dlasd4
- dlasd5
- dlasd6
- dlasd7
- dlasd8
- dlasda
- dlasdq
- dlasdt
- dlaset
- dlasq1
- dlasq2
- dlasq3
- dlasq4
- dlasq6
- dlasr
- dlasrt
- dlassq
- dlasv2
- dlaswp
- dlasy2
- dlasyf
- dlat2s
- dlatbs
- dlatdf
- dlatps
- dlatrd
- dlatrs
- dlatrz
- dlauu2
- dlauum
- dopgtr
- dopmtr
- dorbdb
- dorcsd
- dorg2l
- dorg2r
- dorgbr
- dorghr
- dorgl2
- dorglq
- dorgql
- dorgqr
- dorgr2
- dorgrq
- dorgtr
- dorm2l
- dorm2r
- dormbr
- dormhr
- dorml2
- dormlq
- dormql
- dormqr
- dormr2
- dormr3
- dormrq
- dormrz
- dormtr
- dpbcon
- dpbequ
- dpbrfs
- dpbstf
- dpbsv
- dpbsvx
- dpbtf2
- dpbtrf
- dpbtrs
- dpftrf
- dpftri
- dpftrs
- dpocon
- dpoequ
- dpoequb
- dporfs
- dposv
- dposvx
- dpotf2
- dpotrf
- dpotri
- dpotrs
- dppcon
- dppequ
- dpprfs
- dppsv
- dppsvx
- dpptrf
- dpptri
- dpptrs
- dpstf2
- dpstrf
- dptcon
- dpteqr
- dptrfs
- dptsv
- dptsvx
- dpttrf
- dpttrs
- dptts2
- drscl
- dsbev
- dsbevd
- dsbevx
- dsbgst
- dsbgv
- dsbgvd
- dsbgvx
- dsbtrd
- dsfrk
- dsgesv
- dspcon
- dspev
- dspevd
- dspevx
- dspgst
- dspgv
- dspgvd
- dspgvx
- dsposv
- dsprfs
- dspsv
- dspsvx
- dsptrd
- dsptrf
- dsptri
- dsptrs
- dstebz
- dstedc
- dstegr
- dstein
- dstemr
- dsteqr
- dsterf
- dstev
- dstevd
- dstevr
- dstevx
- dsycon
- dsyconv
- dsyequb
- dsyev
- dsyevd
- dsyevr
- dsyevx
- dsygs2
- dsygst
- dsygv
- dsygvd
- dsygvx
- dsyrfs
- dsysv
- dsysvx
- dsyswapr
- dsytd2
- dsytf2
- dsytrd
- dsytrf
- dsytri
- dsytri2
- dsytri2x
- dsytrs
- dsytrs2
- dtbcon
- dtbrfs
- dtbtrs
- dtfsm
- dtftri
- dtfttp
- dtfttr
- dtgevc
- dtgex2
- dtgexc
- dtgsen
- dtgsja
- dtgsna
- dtgsy2
- dtgsyl
- dtpcon
- dtpmqrt
- dtpqrt
- dtpqrt2
- dtprfb
- dtprfs
- dtptri
- dtptrs
- dtpttf
- dtpttr
- dtrcon
- dtrevc
- dtrexc
- dtrrfs
- dtrsen
- dtrsna
- dtrsyl
- dtrti2
- dtrtri
- dtrtrs
- dtrttf
- dtrttp
- dtzrzf
- dzsum1
- icmax1
- ieeeck
- ilaclc
- ilaclr
- iladiag
- iladlc
- iladlr
- ilaprec
- ilaslc
- ilaslr
- ilatrans
- ilauplo
- ilaver
- ilazlc
- ilazlr
- izmax1
- sbbcsd
- sbdsdc
- sbdsqr
- scsum1
- sdisna
- sgbbrd
- sgbcon
- sgbequ
- sgbequb
- sgbrfs
- sgbsv
- sgbsvx
- sgbtf2
- sgbtrf
- sgbtrs
- sgebak
- sgebal
- sgebd2
- sgebrd
- sgecon
- sgeequ
- sgeequb
- sgees
- sgeesx
- sgeev
- sgeevx
- sgehd2
- sgehrd
- sgejsv
- sgelq2
- sgelqf
- sgels
- sgelsd
- sgelss
- sgelsy
- sgemqrt
- sgeql2
- sgeqlf
- sgeqp3
- sgeqr2
- sgeqr2p
- sgeqrf
- sgeqrfp
- sgeqrt
- sgeqrt2
- sgeqrt3
- sgerfs
- sgerq2
- sgerqf
- sgesc2
- sgesdd
- sgesv
- sgesvd
- sgesvj
- sgesvx
- sgetc2
- sgetf2
- sgetrf
- sgetri
- sgetrs
- sggbak
- sggbal
- sgges
- sggesx
- sggev
- sggevx
- sggglm
- sgghrd
- sgglse
- sggqrf
- sggrqf
- sgsvj0
- sgsvj1
- sgtcon
- sgtrfs
- sgtsv
- sgtsvx
- sgttrf
- sgttrs
- sgtts2
- shgeqz
- shsein
- shseqr
- slabad
- slabrd
- slacn2
- slacon
- slacpy
- sladiv
- slae2
- slaebz
- slaed0
- slaed1
- slaed2
- slaed3
- slaed4
- slaed5
- slaed6
- slaed7
- slaed8
- slaed9
- slaeda
- slaein
- slaev2
- slaexc
- slag2
- slag2d
- slags2
- slagtf
- slagtm
- slagts
- slagv2
- slahqr
- slahr2
- slaic1
- slaln2
- slals0
- slalsa
- slalsd
- slamch
- slamrg
- slangb
- slange
- slangt
- slanhs
- slansb
- slansf
- slansp
- slanst
- slansy
- slantb
- slantp
- slantr
- slanv2
- slapll
- slapmr
- slapmt
- slapy2
- slapy3
- slaqgb
- slaqge
- slaqp2
- slaqps
- slaqr0
- slaqr1
- slaqr2
- slaqr3
- slaqr4
- slaqr5
- slaqsb
- slaqsp
- slaqsy
- slaqtr
- slar1v
- slar2v
- slarf
- slarfb
- slarfg
- slarfgp
- slarft
- slarfx
- slargv
- slarnv
- slarra
- slarrb
- slarrc
- slarrd
- slarre
- slarrf
- slarrj
- slarrk
- slarrr
- slarrv
- slartg
- slartgp
- slartgs
- slartv
- slaruv
- slarz
- slarzb
- slarzt
- slas2
- slascl
- slasd0
- slasd1
- slasd2
- slasd3
- slasd4
- slasd5
- slasd6
- slasd7
- slasd8
- slasda
- slasdq
- slasdt
- slaset
- slasq1
- slasq2
- slasq3
- slasq4
- slasq6
- slasr
- slasrt
- slassq
- slasv2
- slaswp
- slasy2
- slasyf
- slatbs
- slatdf
- slatps
- slatrd
- slatrs
- slatrz
- slauu2
- slauum
- sopgtr
- sopmtr
- sorbdb
- sorcsd
- sorg2l
- sorg2r
- sorgbr
- sorghr
- sorgl2
- sorglq
- sorgql
- sorgqr
- sorgr2
- sorgrq
- sorgtr
- sorm2l
- sorm2r
- sormbr
- sormhr
- sorml2
- sormlq
- sormql
- sormqr
- sormr2
- sormr3
- sormrq
- sormrz
- sormtr
- spbcon
- spbequ
- spbrfs
- spbstf
- spbsv
- spbsvx
- spbtf2
- spbtrf
- spbtrs
- spftrf
- spftri
- spftrs
- spocon
- spoequ
- spoequb
- sporfs
- sposv
- sposvx
- spotf2
- spotrf
- spotri
- spotrs
- sppcon
- sppequ
- spprfs
- sppsv
- sppsvx
- spptrf
- spptri
- spptrs
- spstf2
- spstrf
- sptcon
- spteqr
- sptrfs
- sptsv
- sptsvx
- spttrf
- spttrs
- sptts2
- srscl
- ssbev
- ssbevd
- ssbevx
- ssbgst
- ssbgv
- ssbgvd
- ssbgvx
- ssbtrd
- ssfrk
- sspcon
- sspev
- sspevd
- sspevx
- sspgst
- sspgv
- sspgvd
- sspgvx
- ssprfs
- sspsv
- sspsvx
- ssptrd
- ssptrf
- ssptri
- ssptrs
- sstebz
- sstedc
- sstegr
- sstein
- sstemr
- ssteqr
- ssterf
- sstev
- sstevd
- sstevr
- sstevx
- ssycon
- ssyconv
- ssyequb
- ssyev
- ssyevd
- ssyevr
- ssyevx
- ssygs2
- ssygst
- ssygv
- ssygvd
- ssygvx
- ssyrfs
- ssysv
- ssysvx
- ssyswapr
- ssytd2
- ssytf2
- ssytrd
- ssytrf
- ssytri
- ssytri2
- ssytri2x
- ssytrs
- ssytrs2
- stbcon
- stbrfs
- stbtrs
- stfsm
- stftri
- stfttp
- stfttr
- stgevc
- stgex2
- stgexc
- stgsen
- stgsja
- stgsna
- stgsy2
- stgsyl
- stpcon
- stpmqrt
- stpqrt
- stpqrt2
- stprfb
- stprfs
- stptri
- stptrs
- stpttf
- stpttr
- strcon
- strevc
- strexc
- strrfs
- strsen
- strsna
- strsyl
- strti2
- strtri
- strtrs
- strttf
- strttp
- stzrzf
- xerbla_array
- zbbcsd
- zbdsqr
- zcgesv
- zcposv
- zdrscl
- zgbbrd
- zgbcon
- zgbequ
- zgbequb
- zgbrfs
- zgbsv
- zgbsvx
- zgbtf2
- zgbtrf
- zgbtrs
- zgebak
- zgebal
- zgebd2
- zgebrd
- zgecon
- zgeequ
- zgeequb
- zgees
- zgeesx
- zgeev
- zgeevx
- zgehd2
- zgehrd
- zgelq2
- zgelqf
- zgels
- zgelsd
- zgelss
- zgelsy
- zgemqrt
- zgeql2
- zgeqlf
- zgeqp3
- zgeqr2
- zgeqr2p
- zgeqrf
- zgeqrfp
- zgeqrt
- zgeqrt2
- zgeqrt3
- zgerfs
- zgerq2
- zgerqf
- zgesc2
- zgesdd
- zgesv
- zgesvd
- zgesvx
- zgetc2
- zgetf2
- zgetrf
- zgetri
- zgetrs
- zggbak
- zggbal
- zgges
- zggesx
- zggev
- zggevx
- zggglm
- zgghrd
- zgglse
- zggqrf
- zggrqf
- zgtcon
- zgtrfs
- zgtsv
- zgtsvx
- zgttrf
- zgttrs
- zgtts2
- zhbev
- zhbevd
- zhbevx
- zhbgst
- zhbgv
- zhbgvd
- zhbgvx
- zhbtrd
- zhecon
- zheequb
- zheev
- zheevd
- zheevr
- zheevx
- zhegs2
- zhegst
- zhegv
- zhegvd
- zhegvx
- zherfs
- zhesv
- zhesvx
- zheswapr
- zhetd2
- zhetf2
- zhetrd
- zhetrf
- zhetri
- zhetri2
- zhetri2x
- zhetrs
- zhetrs2
- zhfrk
- zhgeqz
- zhpcon
- zhpev
- zhpevd
- zhpevx
- zhpgst
- zhpgv
- zhpgvd
- zhpgvx
- zhprfs
- zhpsv
- zhpsvx
- zhptrd
- zhptrf
- zhptri
- zhptrs
- zhsein
- zhseqr
- zlabrd
- zlacgv
- zlacn2
- zlacon
- zlacp2
- zlacpy
- zlacrm
- zlacrt
- zladiv
- zlaed0
- zlaed7
- zlaed8
- zlaein
- zlaesy
- zlaev2
- zlag2c
- zlags2
- zlagtm
- zlahef
- zlahqr
- zlahr2
- zlaic1
- zlals0
- zlalsa
- zlalsd
- zlangb
- zlange
- zlangt
- zlanhb
- zlanhe
- zlanhf
- zlanhp
- zlanhs
- zlanht
- zlansb
- zlansp
- zlansy
- zlantb
- zlantp
- zlantr
- zlapll
- zlapmr
- zlapmt
- zlaqgb
- zlaqge
- zlaqhb
- zlaqhe
- zlaqhp
- zlaqp2
- zlaqps
- zlaqr0
- zlaqr1
- zlaqr2
- zlaqr3
- zlaqr4
- zlaqr5
- zlaqsb
- zlaqsp
- zlaqsy
- zlar1v
- zlar2v
- zlarcm
- zlarf
- zlarfb
- zlarfg
- zlarfgp
- zlarft
- zlarfx
- zlargv
- zlarnv
- zlarrv
- zlartg
- zlartv
- zlarz
- zlarzb
- zlarzt
- zlascl
- zlaset
- zlasr
- zlassq
- zlaswp
- zlasyf
- zlat2c
- zlatbs
- zlatdf
- zlatps
- zlatrd
- zlatrs
- zlatrz
- zlauu2
- zlauum
- zpbcon
- zpbequ
- zpbrfs
- zpbstf
- zpbsv
- zpbsvx
- zpbtf2
- zpbtrf
- zpbtrs
- zpftrf
- zpftri
- zpftrs
- zpocon
- zpoequ
- zpoequb
- zporfs
- zposv
- zposvx
- zpotf2
- zpotrf
- zpotri
- zpotrs
- zppcon
- zppequ
- zpprfs
- zppsv
- zppsvx
- zpptrf
- zpptri
- zpptrs
- zpstf2
- zpstrf
- zptcon
- zpteqr
- zptrfs
- zptsv
- zptsvx
- zpttrf
- zpttrs
- zptts2
- zrot
- zspcon
- zspmv
- zspr
- zsprfs
- zspsv
- zspsvx
- zsptrf
- zsptri
- zsptrs
- zstedc
- zstegr
- zstein
- zstemr
- zsteqr
- zsycon
- zsyconv
- zsyequb
- zsymv
- zsyr
- zsyrfs
- zsysv
- zsysvx
- zsyswapr
- zsytf2
- zsytrf
- zsytri
- zsytri2
- zsytri2x
- zsytrs
- zsytrs2
- ztbcon
- ztbrfs
- ztbtrs
- ztfsm
- ztftri
- ztfttp
- ztfttr
- ztgevc
- ztgex2
- ztgexc
- ztgsen
- ztgsja
- ztgsna
- ztgsy2
- ztgsyl
- ztpcon
- ztpmqrt
- ztpqrt
- ztpqrt2
- ztprfb
- ztprfs
- ztptri
- ztptrs
- ztpttf
- ztpttr
- ztrcon
- ztrevc
- ztrexc
- ztrrfs
- ztrsen
- ztrsna
- ztrsyl
- ztrti2
- ztrtri
- ztrtrs
- ztrttf
- ztrttp
- ztzrzf
- zunbdb
- zuncsd
- zung2l
- zung2r
- zungbr
- zunghr
- zungl2
- zunglq
- zungql
- zungqr
- zungr2
- zungrq
- zungtr
- zunm2l
- zunm2r
- zunmbr
- zunmhr
- zunml2
- zunmlq
- zunmql
- zunmqr
- zunmr2
- zunmr3
- zunmrq
- zunmrz
- zunmtr
- zupgtr
- zupmtr
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def _test_dlamch(*args, **kwargs): # real signature unknown
    pass

def _test_slamch(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9bc919d0>'

__pyx_capi__ = {
    'cbbcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bc918d0>'
    'cbdsqr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc91990>'
    'cgbbrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc91960>'
    'cgbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc919f0>'
    'cgbequ': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc91a20>'
    'cgbequb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc91a50>'
    'cgbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc91a80>'
    'cgbsv': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc91ab0>'
    'cgbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc91ae0>'
    'cgbtf2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0xffff9bc91b10>'
    'cgbtrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0xffff9bc91b40>'
    'cgbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc91b70>'
    'cgebak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc91ba0>'
    'cgebal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc91bd0>'
    'cgebd2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc91c00>'
    'cgebrd': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc91c30>'
    'cgecon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc91c60>'
    'cgeequ': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc91c90>'
    'cgeequb': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc91cc0>'
    'cgees': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_cselect1 *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bc91cf0>'
    'cgeesx': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_cselect1 *, char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bc91d20>'
    'cgeev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc91d50>'
    'cgeevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc91d80>'
    'cgehd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc91db0>'
    'cgehrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc91de0>'
    'cgelq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc91e10>'
    'cgelqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc91e40>'
    'cgels': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc91e70>'
    'cgelsd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bc91ea0>'
    'cgelss': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc91ed0>'
    'cgelsy': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc91f00>'
    'cgemqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc91f30>'
    'cgeql2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc91f60>'
    'cgeqlf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc91f90>'
    'cgeqp3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc91fc0>'
    'cgeqr2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc94030>'
    'cgeqr2p': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc94060>'
    'cgeqrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94090>'
    'cgeqrfp': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc940c0>'
    'cgeqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc940f0>'
    'cgeqrt2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94120>'
    'cgeqrt3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94150>'
    'cgerfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc94180>'
    'cgerq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc941b0>'
    'cgerqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc941e0>'
    'cgesc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc94210>'
    'cgesdd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bc94240>'
    'cgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94270>'
    'cgesvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc942a0>'
    'cgesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc942d0>'
    'cgetc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, int *, int *, int *)" at 0xffff9bc94300>'
    'cgetf2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0xffff9bc94330>'
    'cgetrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0xffff9bc94360>'
    'cgetri': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94390>'
    'cgetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc943c0>'
    'cggbak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc943f0>'
    'cggbal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc94420>'
    'cgges': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_cselect2 *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bc94450>'
    'cggesx': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_cselect2 *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bc94480>'
    'cggev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc944b0>'
    'cggevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bc944e0>'
    'cggglm': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94510>'
    'cgghrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94540>'
    'cgglse': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94570>'
    'cggqrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc945a0>'
    'cggrqf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc945d0>'
    'cgtcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0xffff9bc94600>'
    'cgtrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc94630>'
    'cgtsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94660>'
    'cgtsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc94690>'
    'cgttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc946c0>'
    'cgttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc946f0>'
    'cgtts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc94720>'
    'chbev': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc94750>'
    'chbevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bc94780>'
    'chbevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bc947b0>'
    'chbgst': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc947e0>'
    'chbgv': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc94810>'
    'chbgvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bc94840>'
    'chbgvx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bc94870>'
    'chbtrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc948a0>'
    'checon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0xffff9bc948d0>'
    'cheequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0xffff9bc94900>'
    'cheev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc94930>'
    'cheevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bc94960>'
    'cheevr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bc94990>'
    'cheevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bc949c0>'
    'chegs2': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc949f0>'
    'chegst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94a20>'
    'chegv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc94a50>'
    'chegvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bc94a80>'
    'chegvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bc94ab0>'
    'cherfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc94ae0>'
    'chesv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94b10>'
    'chesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc94b40>'
    'cheswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0xffff9bc94b70>'
    'chetd2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0xffff9bc94ba0>'
    'chetf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0xffff9bc94bd0>'
    'chetrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94c00>'
    'chetrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94c30>'
    'chetri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc94c60>'
    'chetri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94c90>'
    'chetri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94cc0>'
    'chetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94cf0>'
    'chetrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc94d20>'
    'chfrk': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0xffff9bc94d50>'
    'chgeqz': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc94d80>'
    'chla_transtype': None, # (!) real value is '<capsule object "char (int *)" at 0xffff9bc94db0>'
    'chpcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0xffff9bc94de0>'
    'chpev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc94e10>'
    'chpevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bc94e40>'
    'chpevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bc94e70>'
    'chpgst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc94ea0>'
    'chpgv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc94ed0>'
    'chpgvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bc94f00>'
    'chpgvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bc94f30>'
    'chprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc94f60>'
    'chpsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc94f90>'
    'chpsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc94fc0>'
    'chptrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0xffff9bc96030>'
    'chptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc96060>'
    'chptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc96090>'
    'chptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc960c0>'
    'chsein': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bc960f0>'
    'chseqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc96120>'
    'clabrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc96150>'
    'clacgv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *)" at 0xffff9bc96180>'
    'clacn2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bc961b0>'
    'clacon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc961e0>'
    'clacp2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc96210>'
    'clacpy': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc96240>'
    'clacrm': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc96270>'
    'clacrt': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0xffff9bc962a0>'
    'cladiv': None, # (!) real value is '<capsule object "__pyx_t_float_complex (__pyx_t_float_complex *, __pyx_t_float_complex *)" at 0xffff9bc962d0>'
    'claed0': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bc96300>'
    'claed7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bc96330>'
    'claed8': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc96360>'
    'claein': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc96390>'
    'claesy': None, # (!) real value is '<capsule object "void (__pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0xffff9bc963c0>'
    'claev2': None, # (!) real value is '<capsule object "void (__pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0xffff9bc963f0>'
    'clag2z': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bc96420>'
    'clags2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0xffff9bc96450>'
    'clagtm': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0xffff9bc96480>'
    'clahef': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc964b0>'
    'clahqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc964e0>'
    'clahr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc96510>'
    'claic1': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0xffff9bc96540>'
    'clals0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc96570>'
    'clalsa': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bc965a0>'
    'clalsd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bc965d0>'
    'clangb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc96600>'
    'clange': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc96630>'
    'clangt': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0xffff9bc96660>'
    'clanhb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc96690>'
    'clanhe': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc966c0>'
    'clanhf': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc966f0>'
    'clanhp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc96720>'
    'clanhs': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc96750>'
    'clanht': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0xffff9bc96780>'
    'clansb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc967b0>'
    'clansp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc967e0>'
    'clansy': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc96810>'
    'clantb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc96840>'
    'clantp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc96870>'
    'clantr': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc968a0>'
    'clapll': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc968d0>'
    'clapmr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc96900>'
    'clapmt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc96930>'
    'claqgb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0xffff9bc96960>'
    'claqge': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0xffff9bc96990>'
    'claqhb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0xffff9bc969c0>'
    'claqhe': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0xffff9bc969f0>'
    'claqhp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0xffff9bc96a20>'
    'claqp2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0xffff9bc96a50>'
    'claqps': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc96a80>'
    'claqr0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc96ab0>'
    'claqr1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0xffff9bc96ae0>'
    'claqr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc96b10>'
    'claqr3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc96b40>'
    'claqr4': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc96b70>'
    'claqr5': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc96ba0>'
    'claqsb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0xffff9bc96bd0>'
    'claqsp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0xffff9bc96c00>'
    'claqsy': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0xffff9bc96c30>'
    'clar1v': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc96c60>'
    'clar2v': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0xffff9bc96c90>'
    'clarcm': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc96cc0>'
    'clarf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0xffff9bc96cf0>'
    'clarfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc96d20>'
    'clarfg': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0xffff9bc96d50>'
    'clarfgp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0xffff9bc96d80>'
    'clarft': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc96db0>'
    'clarfx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0xffff9bc96de0>'
    'clargv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc96e10>'
    'clarnv': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *)" at 0xffff9bc96e40>'
    'clarrv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bc96e70>'
    'clartg': None, # (!) real value is '<capsule object "void (__pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0xffff9bc96ea0>'
    'clartv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0xffff9bc96ed0>'
    'clarz': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0xffff9bc96f00>'
    'clarzb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc96f30>'
    'clarzt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc96f60>'
    'clascl': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc96f90>'
    'claset': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc96fc0>'
    'clasr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0xffff9bc99030>'
    'classq': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bc99060>'
    'claswp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, int *, int *, int *, int *)" at 0xffff9bc99090>'
    'clasyf': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc990c0>'
    'clatbs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc990f0>'
    'clatdf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bc99120>'
    'clatps': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc99150>'
    'clatrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc99180>'
    'clatrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc991b0>'
    'clatrz': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *)" at 0xffff9bc991e0>'
    'clauu2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99210>'
    'clauum': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99240>'
    'cpbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc99270>'
    'cpbequ': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc992a0>'
    'cpbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc992d0>'
    'cpbstf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99300>'
    'cpbsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99330>'
    'cpbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc99360>'
    'cpbtf2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99390>'
    'cpbtrf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc993c0>'
    'cpbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc993f0>'
    'cpftrf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc99420>'
    'cpftri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc99450>'
    'cpftrs': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99480>'
    'cpocon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc994b0>'
    'cpoequ': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc994e0>'
    'cpoequb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc99510>'
    'cporfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc99540>'
    'cposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99570>'
    'cposvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc995a0>'
    'cpotf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc995d0>'
    'cpotrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99600>'
    'cpotri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99630>'
    'cpotrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99660>'
    'cppcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc99690>'
    'cppequ': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc996c0>'
    'cpprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc996f0>'
    'cppsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99720>'
    'cppsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc99750>'
    'cpptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc99780>'
    'cpptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc997b0>'
    'cpptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc997e0>'
    'cpstf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc99810>'
    'cpstrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc99840>'
    'cptcon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc99870>'
    'cpteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc998a0>'
    'cptrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc998d0>'
    'cptsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99900>'
    'cptsvx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc99930>'
    'cpttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0xffff9bc99960>'
    'cpttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99990>'
    'cptts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc999c0>'
    'crot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *)" at 0xffff9bc999f0>'
    'cspcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0xffff9bc99a20>'
    'cspmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc99a50>'
    'cspr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0xffff9bc99a80>'
    'csprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc99ab0>'
    'cspsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99ae0>'
    'cspsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc99b10>'
    'csptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99b40>'
    'csptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc99b70>'
    'csptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99ba0>'
    'csrscl': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0xffff9bc99bd0>'
    'cstedc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bc99c00>'
    'cstegr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bc99c30>'
    'cstein': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bc99c60>'
    'cstemr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bc99c90>'
    'csteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc99cc0>'
    'csycon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0xffff9bc99cf0>'
    'csyconv': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc99d20>'
    'csyequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *)" at 0xffff9bc99d50>'
    'csymv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc99d80>'
    'csyr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc99db0>'
    'csyrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc99de0>'
    'csysv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99e10>'
    'csysvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc99e40>'
    'csyswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0xffff9bc99e70>'
    'csytf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0xffff9bc99ea0>'
    'csytrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99ed0>'
    'csytri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc99f00>'
    'csytri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99f30>'
    'csytri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99f60>'
    'csytrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc99f90>'
    'csytrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc99fc0>'
    'ctbcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc9a030>'
    'ctbrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc9a060>'
    'ctbtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a090>'
    'ctfsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc9a0c0>'
    'ctftri': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc9a0f0>'
    'ctfttp': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc9a120>'
    'ctfttr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a150>'
    'ctgevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc9a180>'
    'ctgex2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0xffff9bc9a1b0>'
    'ctgexc': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, int *)" at 0xffff9bc9a1e0>'
    'ctgsen': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, int *, int *)" at 0xffff9bc9a210>'
    'ctgsja': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a240>'
    'ctgsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_float_complex *, int *, int *, int *)" at 0xffff9bc9a270>'
    'ctgsy2': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc9a2a0>'
    'ctgsyl': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *, int *)" at 0xffff9bc9a2d0>'
    'ctpcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc9a300>'
    'ctpmqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc9a330>'
    'ctpqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc9a360>'
    'ctpqrt2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a390>'
    'ctprfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc9a3c0>'
    'ctprfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc9a3f0>'
    'ctptri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc9a420>'
    'ctptrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a450>'
    'ctpttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc9a480>'
    'ctpttr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a4b0>'
    'ctrcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc9a4e0>'
    'ctrevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc9a510>'
    'ctrexc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *, int *, int *)" at 0xffff9bc9a540>'
    'ctrrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc9a570>'
    'ctrsen': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a5a0>'
    'ctrsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc9a5d0>'
    'ctrsyl': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bc9a600>'
    'ctrti2': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a630>'
    'ctrtri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a660>'
    'ctrtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a690>'
    'ctrttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc9a6c0>'
    'ctrttp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc9a6f0>'
    'ctzrzf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a720>'
    'cunbdb': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a750>'
    'cuncsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bc9a780>'
    'cung2l': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc9a7b0>'
    'cung2r': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc9a7e0>'
    'cungbr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a810>'
    'cunghr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a840>'
    'cungl2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc9a870>'
    'cunglq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a8a0>'
    'cungql': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a8d0>'
    'cungqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a900>'
    'cungr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0xffff9bc9a930>'
    'cungrq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a960>'
    'cungtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9a990>'
    'cunm2l': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc9a9c0>'
    'cunm2r': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc9a9f0>'
    'cunmbr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9aa20>'
    'cunmhr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9aa50>'
    'cunml2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc9aa80>'
    'cunmlq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9aab0>'
    'cunmql': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9aae0>'
    'cunmqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9ab10>'
    'cunmr2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc9ab40>'
    'cunmr3': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc9ab70>'
    'cunmrq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9aba0>'
    'cunmrz': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9abd0>'
    'cunmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bc9ac00>'
    'cupgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc9ac30>'
    'cupmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bc9ac60>'
    'dbbcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9ac90>'
    'dbdsdc': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9acc0>'
    'dbdsqr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9acf0>'
    'ddisna': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9ad20>'
    'dgbbrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9ad50>'
    'dgbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9ad80>'
    'dgbequ': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9adb0>'
    'dgbequb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9ade0>'
    'dgbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9ae10>'
    'dgbsv': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9ae40>'
    'dgbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9ae70>'
    'dgbtf2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bc9aea0>'
    'dgbtrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bc9aed0>'
    'dgbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9af00>'
    'dgebak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9af30>'
    'dgebal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9af60>'
    'dgebd2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9af90>'
    'dgebrd': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9afc0>'
    'dgecon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c030>'
    'dgeequ': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9c060>'
    'dgeequb': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9c090>'
    'dgees': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_dselect2 *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bc9c0c0>'
    'dgeesx': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_dselect2 *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *)" at 0xffff9bc9c0f0>'
    'dgeev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c120>'
    'dgeevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bc9c150>'
    'dgehd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9c180>'
    'dgehrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c1b0>'
    'dgejsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bc9c1e0>'
    'dgelq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9c210>'
    'dgelqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c240>'
    'dgels': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c270>'
    'dgelsd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bc9c2a0>'
    'dgelss': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c2d0>'
    'dgelsy': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c300>'
    'dgemqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9c330>'
    'dgeql2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9c360>'
    'dgeqlf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c390>'
    'dgeqp3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c3c0>'
    'dgeqr2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9c3f0>'
    'dgeqr2p': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9c420>'
    'dgeqrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c450>'
    'dgeqrfp': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c480>'
    'dgeqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9c4b0>'
    'dgeqrt2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c4e0>'
    'dgeqrt3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c510>'
    'dgerfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c540>'
    'dgerq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9c570>'
    'dgerqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c5a0>'
    'dgesc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9c5d0>'
    'dgesdd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bc9c600>'
    'dgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c630>'
    'dgesvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c660>'
    'dgesvj': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c690>'
    'dgesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c6c0>'
    'dgetc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bc9c6f0>'
    'dgetf2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bc9c720>'
    'dgetrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bc9c750>'
    'dgetri': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c780>'
    'dgetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c7b0>'
    'dggbak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c7e0>'
    'dggbal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9c810>'
    'dgges': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_dselect3 *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bc9c840>'
    'dggesx': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_dselect3 *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *)" at 0xffff9bc9c870>'
    'dggev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c8a0>'
    'dggevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bc9c8d0>'
    'dggglm': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c900>'
    'dgghrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c930>'
    'dgglse': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c960>'
    'dggqrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c990>'
    'dggrqf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c9c0>'
    'dgsvj0': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9c9f0>'
    'dgsvj1': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9ca20>'
    'dgtcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9ca50>'
    'dgtrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9ca80>'
    'dgtsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9cab0>'
    'dgtsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9cae0>'
    'dgttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9cb10>'
    'dgttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9cb40>'
    'dgtts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9cb70>'
    'dhgeqz': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9cba0>'
    'dhsein': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bc9cbd0>'
    'dhseqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9cc00>'
    'disnan': None, # (!) real value is '<capsule object "int (__pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9cc30>'
    'dlabad': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9cc60>'
    'dlabrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9cc90>'
    'dlacn2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9ccc0>'
    'dlacon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9ccf0>'
    'dlacpy': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9cd20>'
    'dladiv': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9cd50>'
    'dlae2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9cd80>'
    'dlaebz': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9cdb0>'
    'dlaed0': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9cde0>'
    'dlaed1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9ce10>'
    'dlaed2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *)" at 0xffff9bc9ce40>'
    'dlaed3': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9ce70>'
    'dlaed4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9cea0>'
    'dlaed5': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9ced0>'
    'dlaed6': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9cf00>'
    'dlaed7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9cf30>'
    'dlaed8': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bc9cf60>'
    'dlaed9': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9cf90>'
    'dlaeda': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9cfc0>'
    'dlaein': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9e030>'
    'dlaev2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e060>'
    'dlaexc': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9e090>'
    'dlag2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e0c0>'
    'dlag2s': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bc9e0f0>'
    'dlags2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e120>'
    'dlagtf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9e150>'
    'dlagtm': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9e180>'
    'dlagts': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9e1b0>'
    'dlagv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e1e0>'
    'dlahqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9e210>'
    'dlahr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9e240>'
    'dlaic1': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e270>'
    'dlaln2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9e2a0>'
    'dlals0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9e2d0>'
    'dlalsa': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9e300>'
    'dlalsd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9e330>'
    'dlamch': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *)" at 0xffff9bc9e360>'
    'dlamrg': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bc9e390>'
    'dlaneg': None, # (!) real value is '<capsule object "int (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9e3c0>'
    'dlangb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e3f0>'
    'dlange': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e420>'
    'dlangt': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e450>'
    'dlanhs': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e480>'
    'dlansb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e4b0>'
    'dlansf': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e4e0>'
    'dlansp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e510>'
    'dlanst': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e540>'
    'dlansy': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e570>'
    'dlantb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e5a0>'
    'dlantp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e5d0>'
    'dlantr': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e600>'
    'dlanv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e630>'
    'dlapll': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e660>'
    'dlapmr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9e690>'
    'dlapmt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9e6c0>'
    'dlapy2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e6f0>'
    'dlapy3': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e720>'
    'dlaqgb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0xffff9bc9e750>'
    'dlaqge': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0xffff9bc9e780>'
    'dlaqp2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e7b0>'
    'dlaqps': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9e7e0>'
    'dlaqr0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9e810>'
    'dlaqr1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e840>'
    'dlaqr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9e870>'
    'dlaqr3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9e8a0>'
    'dlaqr4': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9e8d0>'
    'dlaqr5': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9e900>'
    'dlaqsb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0xffff9bc9e930>'
    'dlaqsp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0xffff9bc9e960>'
    'dlaqsy': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0xffff9bc9e990>'
    'dlaqtr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9e9c0>'
    'dlar1v': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9e9f0>'
    'dlar2v': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9ea20>'
    'dlarf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9ea50>'
    'dlarfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9ea80>'
    'dlarfg': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9eab0>'
    'dlarfgp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9eae0>'
    'dlarft': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9eb10>'
    'dlarfx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9eb40>'
    'dlargv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9eb70>'
    'dlarnv': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9eba0>'
    'dlarra': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bc9ebd0>'
    'dlarrb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9ec00>'
    'dlarrc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bc9ec30>'
    'dlarrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9ec60>'
    'dlarre': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9ec90>'
    'dlarrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9ecc0>'
    'dlarrj': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9ecf0>'
    'dlarrk': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9ed20>'
    'dlarrr': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9ed50>'
    'dlarrv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9ed80>'
    'dlartg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9edb0>'
    'dlartgp': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9ede0>'
    'dlartgs': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9ee10>'
    'dlartv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9ee40>'
    'dlaruv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9ee70>'
    'dlarz': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9eea0>'
    'dlarzb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9eed0>'
    'dlarzt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9ef00>'
    'dlas2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bc9ef30>'
    'dlascl': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bc9ef60>'
    'dlasd0': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9ef90>'
    'dlasd1': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bc9efc0>'
    'dlasd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, int *, int *)" at 0xffff9bca0030>'
    'dlasd3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0060>'
    'dlasd4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0090>'
    'dlasd5': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bca00c0>'
    'dlasd6': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca00f0>'
    'dlasd7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0120>'
    'dlasd8': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0150>'
    'dlasda': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0180>'
    'dlasdq': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca01b0>'
    'dlasdt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *)" at 0xffff9bca01e0>'
    'dlaset': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0210>'
    'dlasq1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0240>'
    'dlasq2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0270>'
    'dlasq3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bca02a0>'
    'dlasq4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bca02d0>'
    'dlasq6': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bca0300>'
    'dlasr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0330>'
    'dlasrt': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0360>'
    'dlassq': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bca0390>'
    'dlasv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bca03c0>'
    'dlaswp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *)" at 0xffff9bca03f0>'
    'dlasy2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0420>'
    'dlasyf': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0450>'
    'dlat2s': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca0480>'
    'dlatbs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca04b0>'
    'dlatdf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca04e0>'
    'dlatps': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0510>'
    'dlatrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0540>'
    'dlatrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0570>'
    'dlatrz': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bca05a0>'
    'dlauu2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca05d0>'
    'dlauum': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0600>'
    'dopgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0660>'
    'dopmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca06c0>'
    'dorbdb': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca06f0>'
    'dorcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bca0720>'
    'dorg2l': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0750>'
    'dorg2r': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0780>'
    'dorgbr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca07b0>'
    'dorghr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca07e0>'
    'dorgl2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0810>'
    'dorglq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0840>'
    'dorgql': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0870>'
    'dorgqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca08a0>'
    'dorgr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca08d0>'
    'dorgrq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0900>'
    'dorgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0930>'
    'dorm2l': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0990>'
    'dorm2r': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0960>'
    'dormbr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca09c0>'
    'dormhr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca09f0>'
    'dorml2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0a20>'
    'dormlq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0a50>'
    'dormql': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0a80>'
    'dormqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0ab0>'
    'dormr2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0ae0>'
    'dormr3': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0b10>'
    'dormrq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0b40>'
    'dormrz': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0b70>'
    'dormtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0ba0>'
    'dpbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0bd0>'
    'dpbequ': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0c00>'
    'dpbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0c30>'
    'dpbstf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0c60>'
    'dpbsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0c90>'
    'dpbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0690>'
    'dpbtf2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0cc0>'
    'dpbtrf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0cf0>'
    'dpbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0d20>'
    'dpftrf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0d50>'
    'dpftri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0d80>'
    'dpftrs': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0db0>'
    'dpocon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0de0>'
    'dpoequ': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0e10>'
    'dpoequb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0e40>'
    'dporfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0e70>'
    'dposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0ea0>'
    'dposvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0ed0>'
    'dpotf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0f00>'
    'dpotrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0f60>'
    'dpotri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0f30>'
    'dpotrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0f90>'
    'dppcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca0fc0>'
    'dppequ': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca0630>'
    'dpprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2030>'
    'dppsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2060>'
    'dppsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2090>'
    'dpptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca20c0>'
    'dpptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca20f0>'
    'dpptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2120>'
    'dpstf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2150>'
    'dpstrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2180>'
    'dptcon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca21e0>'
    'dpteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2210>'
    'dptrfs': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca21b0>'
    'dptsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2270>'
    'dptsvx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca22a0>'
    'dpttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca22d0>'
    'dpttrs': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2300>'
    'dptts2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2330>'
    'drscl': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2360>'
    'dsbev': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2390>'
    'dsbevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bca23c0>'
    'dsbevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bca23f0>'
    'dsbgst': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2420>'
    'dsbgv': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2450>'
    'dsbgvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bca2480>'
    'dsbgvx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bca24b0>'
    'dsbtrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca24e0>'
    'dsfrk': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bca2510>'
    'dsgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca2540>'
    'dspcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca25a0>'
    'dspev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca25d0>'
    'dspevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bca2600>'
    'dspevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bca2630>'
    'dspgst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2660>'
    'dspgv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2690>'
    'dspgvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bca26c0>'
    'dspgvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bca26f0>'
    'dsposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca2720>'
    'dsprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2750>'
    'dspsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2780>'
    'dspsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca27b0>'
    'dsptrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca27e0>'
    'dsptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2810>'
    'dsptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2840>'
    'dsptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2870>'
    'dstebz': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca28a0>'
    'dstedc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bca2570>'
    'dstegr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bca28d0>'
    'dstein': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bca2900>'
    'dstemr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bca2930>'
    'dsteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2960>'
    'dsterf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2990>'
    'dstev': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca29c0>'
    'dstevd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bca29f0>'
    'dstevr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bca2a20>'
    'dstevx': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bca2a50>'
    'dsycon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2a80>'
    'dsyconv': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2ab0>'
    'dsyequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2ae0>'
    'dsyev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2b10>'
    'dsyevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bca2b40>'
    'dsyevr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bca2b70>'
    'dsyevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bca2ba0>'
    'dsygs2': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2bd0>'
    'dsygst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2c00>'
    'dsygv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2c30>'
    'dsygvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bca2c60>'
    'dsygvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bca2c90>'
    'dsyrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2cc0>'
    'dsysv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2cf0>'
    'dsysvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bca2d20>'
    'dsyswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bca2d50>'
    'dsytd2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2d80>'
    'dsytf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bca2db0>'
    'dsytrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2de0>'
    'dsytrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2e10>'
    'dsytri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2e40>'
    'dsytri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2240>'
    'dsytri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2e70>'
    'dsytrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2ed0>'
    'dsytrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2ea0>'
    'dtbcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2f00>'
    'dtbrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2f60>'
    'dtbtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca2f90>'
    'dtfsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2fc0>'
    'dtftri': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca2f30>'
    'dtfttp': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca4030>'
    'dtfttr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca4060>'
    'dtgevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca4090>'
    'dtgex2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca40c0>'
    'dtgexc': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca40f0>'
    'dtgsen': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bca4120>'
    'dtgsja': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca4150>'
    'dtgsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bca4180>'
    'dtgsy2': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bca41b0>'
    'dtgsyl': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bca41e0>'
    'dtpcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca4210>'
    'dtpmqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca4240>'
    'dtpqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca42a0>'
    'dtpqrt2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca4270>'
    'dtprfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca42d0>'
    'dtprfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca4300>'
    'dtptri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca4330>'
    'dtptrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca4360>'
    'dtpttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca4390>'
    'dtpttr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca43c0>'
    'dtrcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca43f0>'
    'dtrevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca4420>'
    'dtrexc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca4450>'
    'dtrrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca4480>'
    'dtrsen': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bca44b0>'
    'dtrsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bca44e0>'
    'dtrsyl': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca4510>'
    'dtrti2': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca4540>'
    'dtrtri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca4570>'
    'dtrtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca45a0>'
    'dtrttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca45d0>'
    'dtrttp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca4600>'
    'dtzrzf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca4630>'
    'dzsum1': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (int *, __pyx_t_double_complex *, int *)" at 0xffff9bca4660>'
    'icmax1': None, # (!) real value is '<capsule object "int (int *, __pyx_t_float_complex *, int *)" at 0xffff9bca4690>'
    'ieeeck': None, # (!) real value is '<capsule object "int (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bca46c0>'
    'ilaclc': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bca46f0>'
    'ilaclr': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_float_complex *, int *)" at 0xffff9bca4720>'
    'iladiag': None, # (!) real value is '<capsule object "int (char *)" at 0xffff9bca4750>'
    'iladlc': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca4780>'
    'iladlr': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bca47b0>'
    'ilaprec': None, # (!) real value is '<capsule object "int (char *)" at 0xffff9bca47e0>'
    'ilaslc': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca4810>'
    'ilaslr': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca4840>'
    'ilatrans': None, # (!) real value is '<capsule object "int (char *)" at 0xffff9bca4870>'
    'ilauplo': None, # (!) real value is '<capsule object "int (char *)" at 0xffff9bca48a0>'
    'ilaver': None, # (!) real value is '<capsule object "void (int *, int *, int *)" at 0xffff9bca48d0>'
    'ilazlc': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bca4900>'
    'ilazlr': None, # (!) real value is '<capsule object "int (int *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bca4930>'
    'izmax1': None, # (!) real value is '<capsule object "int (int *, __pyx_t_double_complex *, int *)" at 0xffff9bca4960>'
    'sbbcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca49c0>'
    'sbdsdc': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca4990>'
    'sbdsqr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca49f0>'
    'scsum1': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (int *, __pyx_t_float_complex *, int *)" at 0xffff9bca4a20>'
    'sdisna': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca4a50>'
    'sgbbrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca4a80>'
    'sgbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca4ab0>'
    'sgbequ': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca4ae0>'
    'sgbequb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca4b10>'
    'sgbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca4b40>'
    'sgbsv': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca4b70>'
    'sgbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca4ba0>'
    'sgbtf2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bca4bd0>'
    'sgbtrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bca4c00>'
    'sgbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca4c30>'
    'sgebak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca4c60>'
    'sgebal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca4c90>'
    'sgebd2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca4cc0>'
    'sgebrd': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca4cf0>'
    'sgecon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca4d20>'
    'sgeequ': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca4d50>'
    'sgeequb': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca4db0>'
    'sgees': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_sselect2 *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bca4de0>'
    'sgeesx': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_sselect2 *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *)" at 0xffff9bca4e10>'
    'sgeev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca4e40>'
    'sgeevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bca4e70>'
    'sgehd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca4ea0>'
    'sgehrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca4ed0>'
    'sgejsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bca4f00>'
    'sgelq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca4f30>'
    'sgelqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca4f60>'
    'sgels': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca4f90>'
    'sgelsd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bca4fc0>'
    'sgelss': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca4d80>'
    'sgelsy': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6030>'
    'sgemqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6060>'
    'sgeql2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6090>'
    'sgeqlf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca60c0>'
    'sgeqp3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca60f0>'
    'sgeqr2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6120>'
    'sgeqr2p': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6180>'
    'sgeqrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca61e0>'
    'sgeqrfp': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6210>'
    'sgeqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6240>'
    'sgeqrt2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6270>'
    'sgeqrt3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca62a0>'
    'sgerfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca62d0>'
    'sgerq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6300>'
    'sgerqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6330>'
    'sgesc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bca6360>'
    'sgesdd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bca6390>'
    'sgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca63c0>'
    'sgesvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca63f0>'
    'sgesvj': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6420>'
    'sgesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6450>'
    'sgetc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bca64b0>'
    'sgetf2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bca6480>'
    'sgetrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bca64e0>'
    'sgetri': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6510>'
    'sgetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6540>'
    'sggbak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6570>'
    'sggbal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca65a0>'
    'sgges': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_sselect3 *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bca65d0>'
    'sggesx': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_sselect3 *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *)" at 0xffff9bca6600>'
    'sggev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6630>'
    'sggevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bca6660>'
    'sggglm': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6690>'
    'sgghrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca66c0>'
    'sgglse': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca66f0>'
    'sggqrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6720>'
    'sggrqf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6750>'
    'sgsvj0': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6780>'
    'sgsvj1': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca67b0>'
    'sgtcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca61b0>'
    'sgtrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6810>'
    'sgtsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6840>'
    'sgtsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6870>'
    'sgttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca68a0>'
    'sgttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca68d0>'
    'sgtts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6900>'
    'shgeqz': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6930>'
    'shsein': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bca6960>'
    'shseqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6990>'
    'slabad': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bca69c0>'
    'slabrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca69f0>'
    'slacn2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6a20>'
    'slacon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6a50>'
    'slacpy': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6a80>'
    'sladiv': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bca67e0>'
    'slae2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bca6ab0>'
    'slaebz': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6ae0>'
    'slaed0': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6b40>'
    'slaed1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6b70>'
    'slaed2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *)" at 0xffff9bca6ba0>'
    'slaed3': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6bd0>'
    'slaed4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6c00>'
    'slaed5': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bca6c30>'
    'slaed6': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6c60>'
    'slaed7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6c90>'
    'slaed8': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bca6cc0>'
    'slaed9': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6cf0>'
    'slaeda': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6b10>'
    'slaein': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6d20>'
    'slaev2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bca6d50>'
    'slaexc': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6d80>'
    'slag2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bca6db0>'
    'slag2d': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bca6de0>'
    'slags2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bca6e10>'
    'slagtf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6e40>'
    'slagtm': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6e70>'
    'slagts': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6ea0>'
    'slagv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bca6ed0>'
    'slahqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6f00>'
    'slahr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6f30>'
    'slaic1': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bca6f60>'
    'slaln2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6f90>'
    'slals0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca6fc0>'
    'slalsa': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca6150>'
    'slalsd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaa030>'
    'slamch': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *)" at 0xffff9bcaa060>'
    'slamrg': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bcaa090>'
    'slangb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa0c0>'
    'slange': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa0f0>'
    'slangt': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa120>'
    'slanhs': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa150>'
    'slansb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa180>'
    'slansf': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa1b0>'
    'slansp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa1e0>'
    'slanst': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa210>'
    'slansy': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa240>'
    'slantb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa270>'
    'slantp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa2a0>'
    'slantr': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa2d0>'
    'slanv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa300>'
    'slapll': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa330>'
    'slapmr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaa360>'
    'slapmt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaa390>'
    'slapy2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa3c0>'
    'slapy3': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_s (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa3f0>'
    'slaqgb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0xffff9bcaa420>'
    'slaqge': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0xffff9bcaa450>'
    'slaqp2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa480>'
    'slaqps': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaa4b0>'
    'slaqr0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaa4e0>'
    'slaqr1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa510>'
    'slaqr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaa540>'
    'slaqr3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaa570>'
    'slaqr4': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaa5a0>'
    'slaqr5': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaa5d0>'
    'slaqsb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0xffff9bcaa600>'
    'slaqsp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0xffff9bcaa630>'
    'slaqsy': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *)" at 0xffff9bcaa660>'
    'slaqtr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaa690>'
    'slar1v': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa6c0>'
    'slar2v': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaa6f0>'
    'slarf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa720>'
    'slarfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaa750>'
    'slarfg': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa780>'
    'slarfgp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa7b0>'
    'slarft': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaa7e0>'
    'slarfx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa810>'
    'slargv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaa840>'
    'slarnv': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaa870>'
    'slarra': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bcaa8a0>'
    'slarrb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaa8d0>'
    'slarrc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcaa900>'
    'slarrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaa930>'
    'slarre': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaa960>'
    'slarrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaa990>'
    'slarrj': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaa9c0>'
    'slarrk': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaa9f0>'
    'slarrr': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaaa20>'
    'slarrv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaaa50>'
    'slartg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaaa80>'
    'slartgp': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaaab0>'
    'slartgs': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaaae0>'
    'slartv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaab10>'
    'slaruv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaab40>'
    'slarz': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaab70>'
    'slarzb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaaba0>'
    'slarzt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaabd0>'
    'slas2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaac00>'
    'slascl': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaac30>'
    'slasd0': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaac60>'
    'slasd1': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaac90>'
    'slasd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, int *, int *)" at 0xffff9bcaacc0>'
    'slasd3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaacf0>'
    'slasd4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaad20>'
    'slasd5': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaad50>'
    'slasd6': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaad80>'
    'slasd7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaadb0>'
    'slasd8': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaade0>'
    'slasda': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaae10>'
    'slasdq': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaae40>'
    'slasdt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *)" at 0xffff9bcaae70>'
    'slaset': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaaea0>'
    'slasq1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaaed0>'
    'slasq2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaaf00>'
    'slasq3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaaf30>'
    'slasq4': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaaf60>'
    'slasq6': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcaaf90>'
    'slasr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaafc0>'
    'slasrt': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9030>'
    'slassq': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bca9060>'
    'slasv2': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bca9090>'
    'slaswp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, int *)" at 0xffff9bca90c0>'
    'slasy2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca90f0>'
    'slasyf': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9120>'
    'slatbs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9150>'
    'slatdf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9180>'
    'slatps': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca91b0>'
    'slatrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca91e0>'
    'slatrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9210>'
    'slatrz': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bca9240>'
    'slauu2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9270>'
    'slauum': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca92a0>'
    'sopgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca92d0>'
    'sopmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9300>'
    'sorbdb': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9330>'
    'sorcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bca9360>'
    'sorg2l': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9390>'
    'sorg2r': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca93c0>'
    'sorgbr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca93f0>'
    'sorghr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9420>'
    'sorgl2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9450>'
    'sorglq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9480>'
    'sorgql': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca94b0>'
    'sorgqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca94e0>'
    'sorgr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9510>'
    'sorgrq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9540>'
    'sorgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9570>'
    'sorm2l': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca95a0>'
    'sorm2r': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca95d0>'
    'sormbr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9600>'
    'sormhr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9630>'
    'sorml2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9660>'
    'sormlq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9690>'
    'sormql': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca96c0>'
    'sormqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca96f0>'
    'sormr2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9720>'
    'sormr3': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9780>'
    'sormrq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca97b0>'
    'sormrz': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca97e0>'
    'sormtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9810>'
    'spbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9840>'
    'spbequ': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9870>'
    'spbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca98a0>'
    'spbstf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca98d0>'
    'spbsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9900>'
    'spbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9930>'
    'spbtf2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9960>'
    'spbtrf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9990>'
    'spbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca99c0>'
    'spftrf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca99f0>'
    'spftri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9a20>'
    'spftrs': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9a50>'
    'spocon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9750>'
    'spoequ': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9a80>'
    'spoequb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9ab0>'
    'sporfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9ae0>'
    'sposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9b10>'
    'sposvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9b40>'
    'spotf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9b70>'
    'spotrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9ba0>'
    'spotri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9bd0>'
    'spotrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9c00>'
    'sppcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9c30>'
    'sppequ': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9c60>'
    'spprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9c90>'
    'sppsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9cc0>'
    'sppsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9cf0>'
    'spptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9d20>'
    'spptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9d80>'
    'spptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9de0>'
    'spstf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9e10>'
    'spstrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9e40>'
    'sptcon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9e70>'
    'spteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9ea0>'
    'sptrfs': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9ed0>'
    'sptsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9f00>'
    'sptsvx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9f30>'
    'spttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9f60>'
    'spttrs': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bca9f90>'
    'sptts2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9fc0>'
    'srscl': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9db0>'
    'ssbev': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bca9d50>'
    'ssbevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcae030>'
    'ssbevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bcae060>'
    'ssbgst': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcae090>'
    'ssbgv': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcae0c0>'
    'ssbgvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcae0f0>'
    'ssbgvx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bcae120>'
    'ssbtrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcae150>'
    'ssfrk': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *)" at 0xffff9bcae180>'
    'sspcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcae1b0>'
    'sspev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcae1e0>'
    'sspevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcae210>'
    'sspevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bcae240>'
    'sspgst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcae270>'
    'sspgv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcae2a0>'
    'sspgvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcae2d0>'
    'sspgvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bcae300>'
    'ssprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcae330>'
    'sspsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcae360>'
    'sspsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcae390>'
    'ssptrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcae3c0>'
    'ssptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcae3f0>'
    'ssptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcae420>'
    'ssptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcae450>'
    'sstebz': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcae480>'
    'sstedc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcae4b0>'
    'sstegr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcae4e0>'
    'sstein': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bcae510>'
    'sstemr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcae540>'
    'ssteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcae570>'
    'ssterf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcae5a0>'
    'sstev': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcae5d0>'
    'sstevd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcae600>'
    'sstevr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcae630>'
    'sstevx': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bcae660>'
    'ssycon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcae690>'
    'ssyconv': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcae6c0>'
    'ssyequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcae6f0>'
    'ssyev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcae720>'
    'ssyevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcae750>'
    'ssyevr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcae780>'
    'ssyevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcae7b0>'
    'ssygs2': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcae7e0>'
    'ssygst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcae810>'
    'ssygv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcae840>'
    'ssygvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcae870>'
    'ssygvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcae8a0>'
    'ssyrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcae8d0>'
    'ssysv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcae900>'
    'ssysvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bcae930>'
    'ssyswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bcae960>'
    'ssytd2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcae990>'
    'ssytf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bcae9c0>'
    'ssytrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcae9f0>'
    'ssytrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaea20>'
    'ssytri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaea50>'
    'ssytri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaea80>'
    'ssytri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaeab0>'
    'ssytrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaeae0>'
    'ssytrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaeb10>'
    'stbcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaeb40>'
    'stbrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaeb70>'
    'stbtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaeba0>'
    'stfsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaebd0>'
    'stftri': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaec00>'
    'stfttp': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaec30>'
    'stfttr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaec60>'
    'stgevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaec90>'
    'stgex2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaecc0>'
    'stgexc': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaecf0>'
    'stgsen': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcaed20>'
    'stgsja': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaed50>'
    'stgsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bcaed80>'
    'stgsy2': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bcaedb0>'
    'stgsyl': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bcaede0>'
    'stpcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaee10>'
    'stpmqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaee40>'
    'stpqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaee70>'
    'stpqrt2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaeea0>'
    'stprfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaeed0>'
    'stprfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaef00>'
    'stptri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaef30>'
    'stptrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaef60>'
    'stpttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcaef90>'
    'stpttr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcaefc0>'
    'strcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcad030>'
    'strevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcad060>'
    'strexc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcad090>'
    'strrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcad0c0>'
    'strsen': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *, int *)" at 0xffff9bcad0f0>'
    'strsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *, int *)" at 0xffff9bcad120>'
    'strsyl': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcad150>'
    'strti2': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcad180>'
    'strtri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcad1b0>'
    'strtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcad1e0>'
    'strttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcad210>'
    'strttp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *)" at 0xffff9bcad270>'
    'stzrzf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, __pyx_t_5scipy_6linalg_13cython_lapack_s *, int *, int *)" at 0xffff9bcad2a0>'
    'xerbla_array': None, # (!) real value is '<capsule object "void (char *, int *, int *)" at 0xffff9bcad2d0>'
    'zbbcsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bcad300>'
    'zbdsqr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcad330>'
    'zcgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bcad360>'
    'zcposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bcad390>'
    'zdrscl': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcad3c0>'
    'zgbbrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcad3f0>'
    'zgbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcad420>'
    'zgbequ': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcad240>'
    'zgbequb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcad450>'
    'zgbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcad480>'
    'zgbsv': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcad4b0>'
    'zgbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcad4e0>'
    'zgbtf2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0xffff9bcad510>'
    'zgbtrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0xffff9bcad540>'
    'zgbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcad570>'
    'zgebak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcad5a0>'
    'zgebal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcad5d0>'
    'zgebd2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcad600>'
    'zgebrd': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcad630>'
    'zgecon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcad660>'
    'zgeequ': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcad690>'
    'zgeequb': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcad6c0>'
    'zgees': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_zselect1 *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bcad6f0>'
    'zgeesx': None, # (!) real value is '<capsule object "void (char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_zselect1 *, char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bcad720>'
    'zgeev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcad750>'
    'zgeevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcad780>'
    'zgehd2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcad7b0>'
    'zgehrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcad7e0>'
    'zgelq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcad810>'
    'zgelqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcad870>'
    'zgels': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcad840>'
    'zgelsd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bcad8a0>'
    'zgelss': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcad8d0>'
    'zgelsy': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcad900>'
    'zgemqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcad930>'
    'zgeql2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcad960>'
    'zgeqlf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcad990>'
    'zgeqp3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcad9c0>'
    'zgeqr2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcad9f0>'
    'zgeqr2p': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcada20>'
    'zgeqrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcada50>'
    'zgeqrfp': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcada80>'
    'zgeqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcadab0>'
    'zgeqrt2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcadae0>'
    'zgeqrt3': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcadb10>'
    'zgerfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcadb40>'
    'zgerq2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcadb70>'
    'zgerqf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcadba0>'
    'zgesc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcadbd0>'
    'zgesdd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bcadc00>'
    'zgesv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcadc30>'
    'zgesvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcadc60>'
    'zgesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcadc90>'
    'zgetc2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, int *, int *, int *)" at 0xffff9bcadcc0>'
    'zgetf2': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0xffff9bcadcf0>'
    'zgetrf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0xffff9bcadd20>'
    'zgetri': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcadd50>'
    'zgetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcadd80>'
    'zggbak': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcaddb0>'
    'zggbal': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcade10>'
    'zgges': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_zselect2 *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bcade40>'
    'zggesx': None, # (!) real value is '<capsule object "void (char *, char *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_zselect2 *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bcade70>'
    'zggev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcadea0>'
    'zggevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bcaded0>'
    'zggglm': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcadf00>'
    'zgghrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcadf30>'
    'zgglse': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcadf60>'
    'zggqrf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcadf90>'
    'zggrqf': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcadfc0>'
    'zgtcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcadde0>'
    'zgtrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcaf030>'
    'zgtsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcaf060>'
    'zgtsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcaf090>'
    'zgttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcaf0c0>'
    'zgttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcaf0f0>'
    'zgtts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcaf120>'
    'zhbev': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcaf180>'
    'zhbevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bcaf150>'
    'zhbevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bcaf1b0>'
    'zhbgst': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcaf1e0>'
    'zhbgv': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcaf210>'
    'zhbgvd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bcaf240>'
    'zhbgvx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bcaf270>'
    'zhbtrd': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcaf2a0>'
    'zhecon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcaf2d0>'
    'zheequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcaf300>'
    'zheev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcaf330>'
    'zheevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bcaf360>'
    'zheevr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bcaf390>'
    'zheevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bcaf3c0>'
    'zhegs2': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcaf3f0>'
    'zhegst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcaf420>'
    'zhegv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcaf480>'
    'zhegvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bcaf4b0>'
    'zhegvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bcaf4e0>'
    'zherfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcaf510>'
    'zhesv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcaf540>'
    'zhesvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcaf570>'
    'zheswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0xffff9bcaf5a0>'
    'zhetd2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcaf5d0>'
    'zhetf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0xffff9bcaf600>'
    'zhetrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcaf630>'
    'zhetrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcaf660>'
    'zhetri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcaf690>'
    'zhetri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcaf6c0>'
    'zhetri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcaf6f0>'
    'zhetrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcaf720>'
    'zhetrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcaf750>'
    'zhfrk': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0xffff9bcaf780>'
    'zhgeqz': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcaf450>'
    'zhpcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcaf7b0>'
    'zhpev': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcaf7e0>'
    'zhpevd': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bcaf810>'
    'zhpevx': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bcaf840>'
    'zhpgst': None, # (!) real value is '<capsule object "void (int *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcaf870>'
    'zhpgv': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcaf8a0>'
    'zhpgvd': None, # (!) real value is '<capsule object "void (int *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bcaf8d0>'
    'zhpgvx': None, # (!) real value is '<capsule object "void (int *, char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bcaf900>'
    'zhprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcaf930>'
    'zhpsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcaf960>'
    'zhpsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcaf990>'
    'zhptrd': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcaf9c0>'
    'zhptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcaf9f0>'
    'zhptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcafa20>'
    'zhptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcafa80>'
    'zhsein': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bcafae0>'
    'zhseqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcafb10>'
    'zlabrd': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcafb40>'
    'zlacgv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *)" at 0xffff9bcafb70>'
    'zlacn2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bcafba0>'
    'zlacon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcafbd0>'
    'zlacp2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcafc00>'
    'zlacpy': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcafc30>'
    'zlacrm': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcafc60>'
    'zlacrt': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0xffff9bcafc90>'
    'zladiv': None, # (!) real value is '<capsule object "__pyx_t_double_complex (__pyx_t_double_complex *, __pyx_t_double_complex *)" at 0xffff9bcafcc0>'
    'zlaed0': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bcafcf0>'
    'zlaed7': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bcafd20>'
    'zlaed8': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcafd50>'
    'zlaein': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcafdb0>'
    'zlaesy': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0xffff9bcafab0>'
    'zlaev2': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0xffff9bcafd80>'
    'zlag2c': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bcafde0>'
    'zlags2': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0xffff9bcafe10>'
    'zlagtm': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcafe40>'
    'zlahef': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcafe70>'
    'zlahqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcafea0>'
    'zlahr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcafed0>'
    'zlaic1': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0xffff9bcaff00>'
    'zlals0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcaff30>'
    'zlalsa': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bcaff60>'
    'zlalsd': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bcaff90>'
    'zlangb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcaffc0>'
    'zlange': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcafa50>'
    'zlangt': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0xffff9bcb1030>'
    'zlanhb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcb1060>'
    'zlanhe': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcb1090>'
    'zlanhf': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcb10c0>'
    'zlanhp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcb10f0>'
    'zlanhs': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcb1120>'
    'zlanht': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0xffff9bcb1150>'
    'zlansb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcb1180>'
    'zlansp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcb11b0>'
    'zlansy': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcb11e0>'
    'zlantb': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcb1210>'
    'zlantp': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcb1240>'
    'zlantr': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_13cython_lapack_d (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcb1270>'
    'zlapll': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcb12a0>'
    'zlapmr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb12d0>'
    'zlapmt': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb1300>'
    'zlaqgb': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0xffff9bcb1330>'
    'zlaqge': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0xffff9bcb1360>'
    'zlaqhb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0xffff9bcb1390>'
    'zlaqhe': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0xffff9bcb13c0>'
    'zlaqhp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0xffff9bcb13f0>'
    'zlaqp2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0xffff9bcb1420>'
    'zlaqps': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcb1450>'
    'zlaqr0': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb1480>'
    'zlaqr1': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0xffff9bcb14b0>'
    'zlaqr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb14e0>'
    'zlaqr3': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb1510>'
    'zlaqr4': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb1540>'
    'zlaqr5': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb1570>'
    'zlaqsb': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0xffff9bcb15a0>'
    'zlaqsp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0xffff9bcb15d0>'
    'zlaqsy': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, char *)" at 0xffff9bcb1600>'
    'zlar1v': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcb1630>'
    'zlar2v': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcb1660>'
    'zlarcm': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcb1690>'
    'zlarf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0xffff9bcb16c0>'
    'zlarfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb16f0>'
    'zlarfg': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0xffff9bcb1720>'
    'zlarfgp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0xffff9bcb1750>'
    'zlarft': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcb1780>'
    'zlarfx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0xffff9bcb17b0>'
    'zlargv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb17e0>'
    'zlarnv': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *)" at 0xffff9bcb1810>'
    'zlarrv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bcb1840>'
    'zlartg': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0xffff9bcb1870>'
    'zlartv': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcb18a0>'
    'zlarz': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0xffff9bcb18d0>'
    'zlarzb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb1900>'
    'zlarzt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcb1930>'
    'zlascl': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb1960>'
    'zlaset': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcb1990>'
    'zlasr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcb19c0>'
    'zlassq': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *)" at 0xffff9bcb19f0>'
    'zlaswp': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, int *, int *, int *, int *)" at 0xffff9bcb1a20>'
    'zlasyf': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb1a50>'
    'zlat2c': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_float_complex *, int *, int *)" at 0xffff9bcb1a80>'
    'zlatbs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb1ab0>'
    'zlatdf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *)" at 0xffff9bcb1ae0>'
    'zlatps': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb1b10>'
    'zlatrd': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcb1b40>'
    'zlatrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb1b70>'
    'zlatrz': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *)" at 0xffff9bcb1ba0>'
    'zlauu2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb1bd0>'
    'zlauum': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb1c00>'
    'zpbcon': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb1c30>'
    'zpbequ': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb1c60>'
    'zpbrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb1c90>'
    'zpbstf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb1cc0>'
    'zpbsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb1cf0>'
    'zpbsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb1d20>'
    'zpbtf2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb1d50>'
    'zpbtrf': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb1d80>'
    'zpbtrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb1db0>'
    'zpftrf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb1de0>'
    'zpftri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb1e10>'
    'zpftrs': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb1e40>'
    'zpocon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb1e70>'
    'zpoequ': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb1ea0>'
    'zpoequb': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb1ed0>'
    'zporfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb1f00>'
    'zposv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb1f30>'
    'zposvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb1f60>'
    'zpotf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb1f90>'
    'zpotrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb1fc0>'
    'zpotri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3030>'
    'zpotrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3060>'
    'zppcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3090>'
    'zppequ': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb30c0>'
    'zpprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb30f0>'
    'zppsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3120>'
    'zppsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, char *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3150>'
    'zpptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3180>'
    'zpptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb31b0>'
    'zpptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb31e0>'
    'zpstf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3210>'
    'zpstrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3240>'
    'zptcon': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3270>'
    'zpteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb32a0>'
    'zptrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb32d0>'
    'zptsv': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3300>'
    'zptsvx': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3330>'
    'zpttrf': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3360>'
    'zpttrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3390>'
    'zptts2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcb33c0>'
    'zrot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *)" at 0xffff9bcb33f0>'
    'zspcon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3420>'
    'zspmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3450>'
    'zspr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0xffff9bcb3480>'
    'zsprfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb34b0>'
    'zspsv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb34e0>'
    'zspsvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3510>'
    'zsptrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3540>'
    'zsptri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3570>'
    'zsptrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb35a0>'
    'zstedc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bcb35d0>'
    'zstegr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bcb3600>'
    'zstein': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bcb3630>'
    'zstemr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *, int *)" at 0xffff9bcb3660>'
    'zsteqr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb36c0>'
    'zsycon': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcb36f0>'
    'zsyconv': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3720>'
    'zsyequb': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3750>'
    'zsymv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3780>'
    'zsyr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb37b0>'
    'zsyrfs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb37e0>'
    'zsysv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3810>'
    'zsysvx': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3840>'
    'zsyswapr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0xffff9bcb3870>'
    'zsytf2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0xffff9bcb38a0>'
    'zsytrf': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb38d0>'
    'zsytri': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3900>'
    'zsytri2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3930>'
    'zsytri2x': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3960>'
    'zsytrs': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3990>'
    'zsytrs2': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb39c0>'
    'ztbcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb39f0>'
    'ztbrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3690>'
    'ztbtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3a20>'
    'ztfsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3a80>'
    'ztftri': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3a50>'
    'ztfttp': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3ab0>'
    'ztfttr': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3b10>'
    'ztgevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3b40>'
    'ztgex2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0xffff9bcb3b70>'
    'ztgexc': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, int *)" at 0xffff9bcb3ba0>'
    'ztgsen': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, int *, int *)" at 0xffff9bcb3bd0>'
    'ztgsja': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3c00>'
    'ztgsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_double_complex *, int *, int *, int *)" at 0xffff9bcb3c30>'
    'ztgsy2': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3c60>'
    'ztgsyl': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *, int *)" at 0xffff9bcb3c90>'
    'ztpcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3cc0>'
    'ztpmqrt': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3cf0>'
    'ztpqrt': None, # (!) real value is '<capsule object "void (int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3d20>'
    'ztpqrt2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3d50>'
    'ztprfb': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3d80>'
    'ztprfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3db0>'
    'ztptri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3de0>'
    'ztptrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3e10>'
    'ztpttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcb3e40>'
    'ztpttr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3ae0>'
    'ztrcon': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3e70>'
    'ztrevc': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3ea0>'
    'ztrexc': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *, int *, int *)" at 0xffff9bcb3ed0>'
    'ztrrfs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3f00>'
    'ztrsen': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3f60>'
    'ztrsna': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3f90>'
    'ztrsyl': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *)" at 0xffff9bcb3fc0>'
    'ztrti2': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb3f30>'
    'ztrtri': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb4030>'
    'ztrtrs': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb4060>'
    'ztrttf': None, # (!) real value is '<capsule object "void (char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb4090>'
    'ztrttp': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb40c0>'
    'ztzrzf': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb40f0>'
    'zunbdb': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb4120>'
    'zuncsd': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_13cython_lapack_d *, int *, int *, int *)" at 0xffff9bcb4150>'
    'zung2l': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcb4180>'
    'zung2r': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcb41b0>'
    'zungbr': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb41e0>'
    'zunghr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb4210>'
    'zungl2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcb4240>'
    'zunglq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb4270>'
    'zungql': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb42a0>'
    'zungqr': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb42d0>'
    'zungr2': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0xffff9bcb4330>'
    'zungrq': None, # (!) real value is '<capsule object "void (int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb4390>'
    'zungtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb43c0>'
    'zunm2l': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb43f0>'
    'zunm2r': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb4420>'
    'zunmbr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb4450>'
    'zunmhr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb4480>'
    'zunml2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb44b0>'
    'zunmlq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb44e0>'
    'zunmql': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb4510>'
    'zunmqr': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb4540>'
    'zunmr2': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb4570>'
    'zunmr3': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb45a0>'
    'zunmrq': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb45d0>'
    'zunmrz': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb4600>'
    'zunmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, int *)" at 0xffff9bcb4660>'
    'zupgtr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb4360>'
    'zupmtr': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0xffff9bcb4630>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.linalg.cython_lapack', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9bc919d0>, origin='/.venv/lib/python3.8/site-packages/scipy/linalg/cython_lapack.cpython-38-aarch64-linux-gnu.so')"

__test__ = {}

