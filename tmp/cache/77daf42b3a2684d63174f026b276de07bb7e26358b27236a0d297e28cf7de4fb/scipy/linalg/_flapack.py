# encoding: utf-8
# module scipy.linalg._flapack
# from /.venv/lib/python3.8/site-packages/scipy/linalg/_flapack.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
"""
This module '_flapack' is auto-generated with f2py (version:2).
Functions:
  ba,lo,hi,pivscale,info = sgebal(a,scale=0,permute=0,overwrite_a=0)
  ba,lo,hi,pivscale,info = dgebal(a,scale=0,permute=0,overwrite_a=0)
  ba,lo,hi,pivscale,info = cgebal(a,scale=0,permute=0,overwrite_a=0)
  ba,lo,hi,pivscale,info = zgebal(a,scale=0,permute=0,overwrite_a=0)
  ht,tau,info = sgehrd(a,lo=0,hi=n-1,lwork=MAX(n,1),overwrite_a=0)
  ht,tau,info = dgehrd(a,lo=0,hi=n-1,lwork=MAX(n,1),overwrite_a=0)
  ht,tau,info = cgehrd(a,lo=0,hi=n-1,lwork=MAX(n,1),overwrite_a=0)
  ht,tau,info = zgehrd(a,lo=0,hi=n-1,lwork=MAX(n,1),overwrite_a=0)
  work,info = sgehrd_lwork(n,lo=0,hi=n-1)
  work,info = dgehrd_lwork(n,lo=0,hi=n-1)
  work,info = cgehrd_lwork(n,lo=0,hi=n-1)
  work,info = zgehrd_lwork(n,lo=0,hi=n-1)
  lu,piv,x,info = sgesv(a,b,overwrite_a=0,overwrite_b=0)
  lu,piv,x,info = dgesv(a,b,overwrite_a=0,overwrite_b=0)
  lu,piv,x,info = cgesv(a,b,overwrite_a=0,overwrite_b=0)
  lu,piv,x,info = zgesv(a,b,overwrite_a=0,overwrite_b=0)
  as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = sgesvx(a,b,fact='E',trans='N',af=,ipiv=,equed='B',r=,c=,overwrite_a=0,overwrite_b=0)
  as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = dgesvx(a,b,fact='E',trans='N',af=,ipiv=,equed='B',r=,c=,overwrite_a=0,overwrite_b=0)
  as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = cgesvx(a,b,fact='E',trans='N',af=,ipiv=,equed='B',r=,c=,overwrite_a=0,overwrite_b=0)
  as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = zgesvx(a,b,fact='E',trans='N',af=,ipiv=,equed='B',r=,c=,overwrite_a=0,overwrite_b=0)
  rcond,info = sgecon(a,anorm,norm='1')
  rcond,info = dgecon(a,anorm,norm='1')
  rcond,info = cgecon(a,anorm,norm='1')
  rcond,info = zgecon(a,anorm,norm='1')
  lu,piv,info = sgetrf(a,overwrite_a=0)
  lu,piv,info = dgetrf(a,overwrite_a=0)
  lu,piv,info = cgetrf(a,overwrite_a=0)
  lu,piv,info = zgetrf(a,overwrite_a=0)
  x,info = sgetrs(lu,piv,b,trans=0,overwrite_b=0)
  x,info = dgetrs(lu,piv,b,trans=0,overwrite_b=0)
  x,info = cgetrs(lu,piv,b,trans=0,overwrite_b=0)
  x,info = zgetrs(lu,piv,b,trans=0,overwrite_b=0)
  lu,ipiv,jpiv,info = sgetc2(a,overwrite_a=0)
  lu,ipiv,jpiv,info = dgetc2(a,overwrite_a=0)
  lu,ipiv,jpiv,info = cgetc2(a,overwrite_a=0)
  lu,ipiv,jpiv,info = zgetc2(a,overwrite_a=0)
  x,scale = sgesc2(lu,rhs,ipiv,jpiv,overwrite_rhs=0)
  x,scale = dgesc2(lu,rhs,ipiv,jpiv,overwrite_rhs=0)
  x,scale = cgesc2(lu,rhs,ipiv,jpiv,overwrite_rhs=0)
  x,scale = zgesc2(lu,rhs,ipiv,jpiv,overwrite_rhs=0)
  inv_a,info = sgetri(lu,piv,lwork=max(3*n,1),overwrite_lu=0)
  inv_a,info = dgetri(lu,piv,lwork=max(3*n,1),overwrite_lu=0)
  inv_a,info = cgetri(lu,piv,lwork=max(3*n,1),overwrite_lu=0)
  inv_a,info = zgetri(lu,piv,lwork=max(3*n,1),overwrite_lu=0)
  work,info = sgetri_lwork(n)
  work,info = dgetri_lwork(n)
  work,info = cgetri_lwork(n)
  work,info = zgetri_lwork(n)
  u,s,vt,info = sgesdd(a,compute_uv=1,full_matrices=1,lwork=max((compute_uv?4*minmn*minmn+MAX(m,n)+9*minmn:MAX(14*minmn+4,10*minmn+2+25*(25+8))+MAX(m,n)),1),overwrite_a=0)
  u,s,vt,info = dgesdd(a,compute_uv=1,full_matrices=1,lwork=max((compute_uv?4*minmn*minmn+MAX(m,n)+9*minmn:MAX(14*minmn+4,10*minmn+2+25*(25+8))+MAX(m,n)),1),overwrite_a=0)
  work,info = sgesdd_lwork(m,n,compute_uv=1,full_matrices=1)
  work,info = dgesdd_lwork(m,n,compute_uv=1,full_matrices=1)
  u,s,vt,info = cgesdd(a,compute_uv=1,full_matrices=1,lwork=max((compute_uv?2*minmn*minmn+MAX(m,n)+2*minmn:2*minmn+MAX(m,n)),1),overwrite_a=0)
  u,s,vt,info = zgesdd(a,compute_uv=1,full_matrices=1,lwork=max((compute_uv?2*minmn*minmn+MAX(m,n)+2*minmn:2*minmn+MAX(m,n)),1),overwrite_a=0)
  work,info = cgesdd_lwork(m,n,compute_uv=1,full_matrices=1)
  work,info = zgesdd_lwork(m,n,compute_uv=1,full_matrices=1)
  u,s,vt,info = sgesvd(a,compute_uv=1,full_matrices=1,lwork=max(MAX(3*minmn+MAX(m,n),5*minmn),1),overwrite_a=0)
  u,s,vt,info = dgesvd(a,compute_uv=1,full_matrices=1,lwork=max(MAX(3*minmn+MAX(m,n),5*minmn),1),overwrite_a=0)
  work,info = sgesvd_lwork(m,n,compute_uv=1,full_matrices=1)
  work,info = dgesvd_lwork(m,n,compute_uv=1,full_matrices=1)
  u,s,vt,info = cgesvd(a,compute_uv=1,full_matrices=1,lwork=MAX(2*minmn+MAX(m,n),1),overwrite_a=0)
  u,s,vt,info = zgesvd(a,compute_uv=1,full_matrices=1,lwork=MAX(2*minmn+MAX(m,n),1),overwrite_a=0)
  work,info = cgesvd_lwork(m,n,compute_uv=1,full_matrices=1)
  work,info = zgesvd_lwork(m,n,compute_uv=1,full_matrices=1)
  lqr,x,info = sgels(a,b,trans='N',lwork=MAX(MIN(m,n)+MAX(MIN(m,n),nrhs),1),overwrite_a=0,overwrite_b=0)
  lqr,x,info = dgels(a,b,trans='N',lwork=MAX(MIN(m,n)+MAX(MIN(m,n),nrhs),1),overwrite_a=0,overwrite_b=0)
  lqr,x,info = cgels(a,b,trans='N',lwork=MAX(MIN(m,n)+MAX(MIN(m,n),nrhs),1),overwrite_a=0,overwrite_b=0)
  lqr,x,info = zgels(a,b,trans='N',lwork=MAX(MIN(m,n)+MAX(MIN(m,n),nrhs),1),overwrite_a=0,overwrite_b=0)
  work,info = sgels_lwork(m,n,nrhs,trans='N')
  work,info = dgels_lwork(m,n,nrhs,trans='N')
  work,info = cgels_lwork(m,n,nrhs,trans='N')
  work,info = zgels_lwork(m,n,nrhs,trans='N')
  v,x,s,rank,work,info = sgelss(a,b,cond=-1.0,lwork=max(3*minmn+MAX(2*minmn,MAX(maxmn,nrhs)),1),overwrite_a=0,overwrite_b=0)
  v,x,s,rank,work,info = dgelss(a,b,cond=-1.0,lwork=max(3*minmn+MAX(2*minmn,MAX(maxmn,nrhs)),1),overwrite_a=0,overwrite_b=0)
  work,info = sgelss_lwork(m,n,nrhs,cond=-1.0,lwork=-1)
  work,info = dgelss_lwork(m,n,nrhs,cond=-1.0,lwork=-1)
  v,x,s,rank,work,info = cgelss(a,b,cond=-1.0,lwork=max(2*minmn+MAX(maxmn,nrhs),1),overwrite_a=0,overwrite_b=0)
  v,x,s,rank,work,info = zgelss(a,b,cond=-1.0,lwork=max(2*minmn+MAX(maxmn,nrhs),1),overwrite_a=0,overwrite_b=0)
  work,info = cgelss_lwork(m,n,nrhs,cond=-1.0,lwork=-1)
  work,info = zgelss_lwork(m,n,nrhs,cond=-1.0,lwork=-1)
  v,x,j,rank,info = sgelsy(a,b,jptv,cond,lwork,overwrite_a=0,overwrite_b=0)
  v,x,j,rank,info = dgelsy(a,b,jptv,cond,lwork,overwrite_a=0,overwrite_b=0)
  work,info = sgelsy_lwork(m,n,nrhs,cond,lwork=-1)
  work,info = dgelsy_lwork(m,n,nrhs,cond,lwork=-1)
  v,x,j,rank,info = cgelsy(a,b,jptv,cond,lwork,overwrite_a=0,overwrite_b=0)
  v,x,j,rank,info = zgelsy(a,b,jptv,cond,lwork,overwrite_a=0,overwrite_b=0)
  work,info = cgelsy_lwork(m,n,nrhs,cond,lwork=-1)
  work,info = zgelsy_lwork(m,n,nrhs,cond,lwork=-1)
  x,s,rank,info = sgelsd(a,b,lwork,size_iwork,cond=-1.0,overwrite_a=0,overwrite_b=0)
  x,s,rank,info = dgelsd(a,b,lwork,size_iwork,cond=-1.0,overwrite_a=0,overwrite_b=0)
  work,iwork,info = sgelsd_lwork(m,n,nrhs,cond=-1.0,lwork=-1)
  work,iwork,info = dgelsd_lwork(m,n,nrhs,cond=-1.0,lwork=-1)
  x,s,rank,info = cgelsd(a,b,lwork,size_rwork,size_iwork,cond=-1.0,overwrite_a=0,overwrite_b=0)
  x,s,rank,info = zgelsd(a,b,lwork,size_rwork,size_iwork,cond=-1.0,overwrite_a=0,overwrite_b=0)
  work,rwork,iwork,info = cgelsd_lwork(m,n,nrhs,cond=-1.0,lwork=-1)
  work,rwork,iwork,info = zgelsd_lwork(m,n,nrhs,cond=-1.0,lwork=-1)
  qr,jpvt,tau,work,info = sgeqp3(a,lwork=max(3*(n+1),1),overwrite_a=0)
  qr,jpvt,tau,work,info = dgeqp3(a,lwork=max(3*(n+1),1),overwrite_a=0)
  qr,jpvt,tau,work,info = cgeqp3(a,lwork=max(3*(n+1),1),overwrite_a=0)
  qr,jpvt,tau,work,info = zgeqp3(a,lwork=max(3*(n+1),1),overwrite_a=0)
  qr,tau,work,info = sgeqrf(a,lwork=max(3*n,1),overwrite_a=0)
  qr,tau,work,info = dgeqrf(a,lwork=max(3*n,1),overwrite_a=0)
  qr,tau,work,info = cgeqrf(a,lwork=max(3*n,1),overwrite_a=0)
  qr,tau,work,info = zgeqrf(a,lwork=max(3*n,1),overwrite_a=0)
  work,info = sgeqrf_lwork(m,n)
  work,info = dgeqrf_lwork(m,n)
  work,info = cgeqrf_lwork(m,n)
  work,info = zgeqrf_lwork(m,n)
  qr,tau,info = sgeqrfp(a,lwork=MAX(1, n),overwrite_a=0)
  qr,tau,info = dgeqrfp(a,lwork=MAX(1, n),overwrite_a=0)
  qr,tau,info = cgeqrfp(a,lwork=MAX(1, n),overwrite_a=0)
  qr,tau,info = zgeqrfp(a,lwork=MAX(1, n),overwrite_a=0)
  work,info = sgeqrfp_lwork(m,n)
  work,info = dgeqrfp_lwork(m,n)
  work,info = cgeqrfp_lwork(m,n)
  work,info = zgeqrfp_lwork(m,n)
  qr,tau,work,info = sgerqf(a,lwork=max(3*m,1),overwrite_a=0)
  qr,tau,work,info = dgerqf(a,lwork=max(3*m,1),overwrite_a=0)
  qr,tau,work,info = cgerqf(a,lwork=max(3*m,1),overwrite_a=0)
  qr,tau,work,info = zgerqf(a,lwork=max(3*m,1),overwrite_a=0)
  wr,wi,vl,vr,info = sgeev(a,compute_vl=1,compute_vr=1,lwork=max(4*n,1),overwrite_a=0)
  wr,wi,vl,vr,info = dgeev(a,compute_vl=1,compute_vr=1,lwork=max(4*n,1),overwrite_a=0)
  work,info = sgeev_lwork(n,compute_vl=1,compute_vr=1)
  work,info = dgeev_lwork(n,compute_vl=1,compute_vr=1)
  w,vl,vr,info = cgeev(a,compute_vl=1,compute_vr=1,lwork=max(2*n,1),overwrite_a=0)
  w,vl,vr,info = zgeev(a,compute_vl=1,compute_vr=1,lwork=max(2*n,1),overwrite_a=0)
  work,info = cgeev_lwork(n,compute_vl=1,compute_vr=1)
  work,info = zgeev_lwork(n,compute_vl=1,compute_vr=1)
  t,sdim,w,vs,work,info = cgees(cselect,a,compute_v=1,sort_t=0,lwork=max(3*n,1),cselect_extra_args=(),overwrite_a=0)
  t,sdim,w,vs,work,info = zgees(zselect,a,compute_v=1,sort_t=0,lwork=max(3*n,1),zselect_extra_args=(),overwrite_a=0)
  t,sdim,wr,wi,vs,work,info = sgees(sselect,a,compute_v=1,sort_t=0,lwork=max(3*n,1),sselect_extra_args=(),overwrite_a=0)
  t,sdim,wr,wi,vs,work,info = dgees(dselect,a,compute_v=1,sort_t=0,lwork=max(3*n,1),dselect_extra_args=(),overwrite_a=0)
  a,b,sdim,alphar,alphai,beta,vsl,vsr,work,info = sgges(sselect,a,b,jobvsl=1,jobvsr=1,sort_t=0,ldvsl=((jobvsl==1)?n:1),ldvsr=((jobvsr==1)?n:1),lwork=max(8*n+16,1),sselect_extra_args=(),overwrite_a=0,overwrite_b=0)
  a,b,sdim,alphar,alphai,beta,vsl,vsr,work,info = dgges(dselect,a,b,jobvsl=1,jobvsr=1,sort_t=0,ldvsl=((jobvsl==1)?n:1),ldvsr=((jobvsr==1)?n:1),lwork=max(8*n+16,1),dselect_extra_args=(),overwrite_a=0,overwrite_b=0)
  a,b,sdim,alpha,beta,vsl,vsr,work,info = cgges(cselect,a,b,jobvsl=1,jobvsr=1,sort_t=0,ldvsl=((jobvsl==1)?n:1),ldvsr=((jobvsr==1)?n:1),lwork=max(2*n,1),cselect_extra_args=(),overwrite_a=0,overwrite_b=0)
  a,b,sdim,alpha,beta,vsl,vsr,work,info = zgges(zselect,a,b,jobvsl=1,jobvsr=1,sort_t=0,ldvsl=((jobvsl==1)?n:1),ldvsr=((jobvsr==1)?n:1),lwork=max(2*n,1),zselect_extra_args=(),overwrite_a=0,overwrite_b=0)
  alphar,alphai,beta,vl,vr,work,info = sggev(a,b,compute_vl=1,compute_vr=1,lwork=max(8*n,1),overwrite_a=0,overwrite_b=0)
  alphar,alphai,beta,vl,vr,work,info = dggev(a,b,compute_vl=1,compute_vr=1,lwork=max(8*n,1),overwrite_a=0,overwrite_b=0)
  alpha,beta,vl,vr,work,info = cggev(a,b,compute_vl=1,compute_vr=1,lwork=max(2*n,1),overwrite_a=0,overwrite_b=0)
  alpha,beta,vl,vr,work,info = zggev(a,b,compute_vl=1,compute_vr=1,lwork=max(2*n,1),overwrite_a=0,overwrite_b=0)
  r,c,rowcnd,colcnd,amax,info = sgeequ(a)
  r,c,rowcnd,colcnd,amax,info = dgeequ(a)
  r,c,rowcnd,colcnd,amax,info = cgeequ(a)
  r,c,rowcnd,colcnd,amax,info = zgeequ(a)
  r,c,rowcnd,colcnd,amax,info = sgeequb(a)
  r,c,rowcnd,colcnd,amax,info = dgeequb(a)
  r,c,rowcnd,colcnd,amax,info = cgeequb(a)
  r,c,rowcnd,colcnd,amax,info = zgeequb(a)
  lub,piv,x,info = sgbsv(kl,ku,ab,b,overwrite_ab=0,overwrite_b=0)
  lub,piv,x,info = dgbsv(kl,ku,ab,b,overwrite_ab=0,overwrite_b=0)
  lub,piv,x,info = cgbsv(kl,ku,ab,b,overwrite_ab=0,overwrite_b=0)
  lub,piv,x,info = zgbsv(kl,ku,ab,b,overwrite_ab=0,overwrite_b=0)
  lu,ipiv,info = sgbtrf(ab,kl,ku,m=shape(ab,1),n=shape(ab,1),ldab=max(shape(ab,0),1),overwrite_ab=0)
  lu,ipiv,info = dgbtrf(ab,kl,ku,m=shape(ab,1),n=shape(ab,1),ldab=max(shape(ab,0),1),overwrite_ab=0)
  lu,ipiv,info = cgbtrf(ab,kl,ku,m=shape(ab,1),n=shape(ab,1),ldab=max(shape(ab,0),1),overwrite_ab=0)
  lu,ipiv,info = zgbtrf(ab,kl,ku,m=shape(ab,1),n=shape(ab,1),ldab=max(shape(ab,0),1),overwrite_ab=0)
  x,info = sgbtrs(ab,kl,ku,b,ipiv,trans=0,n=shape(ab,1),ldab=shape(ab,0),ldb=shape(b,0),overwrite_b=0)
  x,info = dgbtrs(ab,kl,ku,b,ipiv,trans=0,n=shape(ab,1),ldab=shape(ab,0),ldb=shape(b,0),overwrite_b=0)
  x,info = cgbtrs(ab,kl,ku,b,ipiv,trans=0,n=shape(ab,1),ldab=shape(ab,0),ldb=shape(b,0),overwrite_b=0)
  x,info = zgbtrs(ab,kl,ku,b,ipiv,trans=0,n=shape(ab,1),ldab=shape(ab,0),ldb=shape(b,0),overwrite_b=0)
  du2,d,du,x,info = sgtsv(dl,d,du,b,overwrite_dl=0,overwrite_d=0,overwrite_du=0,overwrite_b=0)
  du2,d,du,x,info = dgtsv(dl,d,du,b,overwrite_dl=0,overwrite_d=0,overwrite_du=0,overwrite_b=0)
  du2,d,du,x,info = cgtsv(dl,d,du,b,overwrite_dl=0,overwrite_d=0,overwrite_du=0,overwrite_b=0)
  du2,d,du,x,info = zgtsv(dl,d,du,b,overwrite_dl=0,overwrite_d=0,overwrite_du=0,overwrite_b=0)
  dl,d,du,du2,ipiv,info = sgttrf(dl,d,du,overwrite_dl=0,overwrite_d=0,overwrite_du=0)
  dl,d,du,du2,ipiv,info = dgttrf(dl,d,du,overwrite_dl=0,overwrite_d=0,overwrite_du=0)
  dl,d,du,du2,ipiv,info = cgttrf(dl,d,du,overwrite_dl=0,overwrite_d=0,overwrite_du=0)
  dl,d,du,du2,ipiv,info = zgttrf(dl,d,du,overwrite_dl=0,overwrite_d=0,overwrite_du=0)
  x,info = sgttrs(dl,d,du,du2,ipiv,b,trans='N',overwrite_b=0)
  x,info = dgttrs(dl,d,du,du2,ipiv,b,trans='N',overwrite_b=0)
  x,info = cgttrs(dl,d,du,du2,ipiv,b,trans='N',overwrite_b=0)
  x,info = zgttrs(dl,d,du,du2,ipiv,b,trans='N',overwrite_b=0)
  dlf,df,duf,du2,ipiv,x,rcond,ferr,berr,info = sgtsvx(dl,d,du,b,fact='N',trans='N',dlf=,df=,duf=,du2=,ipiv=)
  dlf,df,duf,du2,ipiv,x,rcond,ferr,berr,info = dgtsvx(dl,d,du,b,fact='N',trans='N',dlf=,df=,duf=,du2=,ipiv=)
  dlf,df,duf,du2,ipiv,x,rcond,ferr,berr,info = cgtsvx(dl,d,du,b,fact='N',trans='N',dlf=,df=,duf=,du2=,ipiv=)
  dlf,df,duf,du2,ipiv,x,rcond,ferr,berr,info = zgtsvx(dl,d,du,b,fact='N',trans='N',dlf=,df=,duf=,du2=,ipiv=)
  w,v,info = ssyev(a,compute_v=1,lower=0,lwork=max(3*n-1,1),overwrite_a=0)
  w,v,info = dsyev(a,compute_v=1,lower=0,lwork=max(3*n-1,1),overwrite_a=0)
  work,info = ssyev_lwork(n,lower=0)
  work,info = dsyev_lwork(n,lower=0)
  w,v,info = cheev(a,compute_v=1,lower=0,lwork=max(2*n-1,1),overwrite_a=0)
  w,v,info = zheev(a,compute_v=1,lower=0,lwork=max(2*n-1,1),overwrite_a=0)
  work,info = cheev_lwork(n,lower=0)
  work,info = zheev_lwork(n,lower=0)
  w,v,info = ssyevd(a,compute_v=1,lower=0,lwork=max((compute_v?1+6*n+2*n*n:2*n+1),1),liwork=(compute_v?3+5*n:1),overwrite_a=0)
  w,v,info = dsyevd(a,compute_v=1,lower=0,lwork=max((compute_v?1+6*n+2*n*n:2*n+1),1),liwork=(compute_v?3+5*n:1),overwrite_a=0)
  work,iwork,info = ssyevd_lwork(n,compute_v=1,lower=0)
  work,iwork,info = dsyevd_lwork(n,compute_v=1,lower=0)
  w,v,info = cheevd(a,compute_v=1,lower=0,lwork=max((compute_v?2*n+n*n:n+1),1),liwork=(compute_v?3+5*n:1),lrwork=(compute_v?1+5*n+2*n*n:n),overwrite_a=0)
  w,v,info = zheevd(a,compute_v=1,lower=0,lwork=max((compute_v?2*n+n*n:n+1),1),liwork=(compute_v?3+5*n:1),lrwork=(compute_v?1+5*n+2*n*n:n),overwrite_a=0)
  work,iwork,rwork,info = cheevd_lwork(n,compute_v=1,lower=0)
  work,iwork,rwork,info = zheevd_lwork(n,compute_v=1,lower=0)
  ldu,ipiv,info = ssytf2(a,lower=0,overwrite_a=0)
  ldu,ipiv,info = dsytf2(a,lower=0,overwrite_a=0)
  ldu,ipiv,info = csytf2(a,lower=0,overwrite_a=0)
  ldu,ipiv,info = zsytf2(a,lower=0,overwrite_a=0)
  c,info = ssygst(a,b,itype=1,lower=0,overwrite_a=0)
  c,info = dsygst(a,b,itype=1,lower=0,overwrite_a=0)
  ldu,ipiv,info = ssytrf(a,lower=0,lwork=max(n,1),overwrite_a=0)
  ldu,ipiv,info = dsytrf(a,lower=0,lwork=max(n,1),overwrite_a=0)
  ldu,ipiv,info = csytrf(a,lower=0,lwork=max(n,1),overwrite_a=0)
  ldu,ipiv,info = zsytrf(a,lower=0,lwork=max(n,1),overwrite_a=0)
  work,info = ssytrf_lwork(n,lower=0)
  work,info = dsytrf_lwork(n,lower=0)
  work,info = csytrf_lwork(n,lower=0)
  work,info = zsytrf_lwork(n,lower=0)
  udut,ipiv,x,info = ssysv(a,b,lwork=max(n,1),lower=0,overwrite_a=0,overwrite_b=0)
  udut,ipiv,x,info = dsysv(a,b,lwork=max(n,1),lower=0,overwrite_a=0,overwrite_b=0)
  udut,ipiv,x,info = csysv(a,b,lwork=max(n,1),lower=0,overwrite_a=0,overwrite_b=0)
  udut,ipiv,x,info = zsysv(a,b,lwork=max(n,1),lower=0,overwrite_a=0,overwrite_b=0)
  work,info = ssysv_lwork(n,lower=0)
  work,info = dsysv_lwork(n,lower=0)
  work,info = csysv_lwork(n,lower=0)
  work,info = zsysv_lwork(n,lower=0)
  a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = ssysvx(a,b,af=,ipiv=,lwork=max(3*n,1),factored=0,lower=0,overwrite_a=0,overwrite_b=0)
  a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = dsysvx(a,b,af=,ipiv=,lwork=max(3*n,1),factored=0,lower=0,overwrite_a=0,overwrite_b=0)
  a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = csysvx(a,b,af=,ipiv=,lwork=max(3*n,1),factored=0,lower=0,overwrite_a=0,overwrite_b=0)
  a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = zsysvx(a,b,af=,ipiv=,lwork=max(3*n,1),factored=0,lower=0,overwrite_a=0,overwrite_b=0)
  work,info = ssysvx_lwork(n,lower=0)
  work,info = dsysvx_lwork(n,lower=0)
  work,info = csysvx_lwork(n,lower=0)
  work,info = zsysvx_lwork(n,lower=0)
  rcond,info = ssycon(a,ipiv,anorm,lower=0)
  rcond,info = dsycon(a,ipiv,anorm,lower=0)
  rcond,info = csycon(a,ipiv,anorm,lower=0)
  rcond,info = zsycon(a,ipiv,anorm,lower=0)
  rcond,info = checon(a,ipiv,anorm,lower=0)
  rcond,info = zhecon(a,ipiv,anorm,lower=0)
  a,e,info = ssyconv(a,ipiv,lower=0,way=0,overwrite_a=0)
  a,e,info = dsyconv(a,ipiv,lower=0,way=0,overwrite_a=0)
  a,e,info = csyconv(a,ipiv,lower=0,way=0,overwrite_a=0)
  a,e,info = zsyconv(a,ipiv,lower=0,way=0,overwrite_a=0)
  c,info = chegst(a,b,itype=1,lower=0,overwrite_a=0)
  c,info = zhegst(a,b,itype=1,lower=0,overwrite_a=0)
  ldu,ipiv,info = chetrf(a,lower=0,lwork=max(n,1),overwrite_a=0)
  ldu,ipiv,info = zhetrf(a,lower=0,lwork=max(n,1),overwrite_a=0)
  work,info = chetrf_lwork(n,lower=0)
  work,info = zhetrf_lwork(n,lower=0)
  uduh,ipiv,x,info = chesv(a,b,lwork=max(n,1),lower=0,overwrite_a=0,overwrite_b=0)
  uduh,ipiv,x,info = zhesv(a,b,lwork=max(n,1),lower=0,overwrite_a=0,overwrite_b=0)
  work,info = chesv_lwork(n,lower=0)
  work,info = zhesv_lwork(n,lower=0)
  uduh,ipiv,x,rcond,ferr,berr,info = chesvx(a,b,af=,ipiv=,lwork=max(2*n,1),factored=0,lower=0,overwrite_a=0,overwrite_b=0)
  uduh,ipiv,x,rcond,ferr,berr,info = zhesvx(a,b,af=,ipiv=,lwork=max(2*n,1),factored=0,lower=0,overwrite_a=0,overwrite_b=0)
  work,info = chesvx_lwork(n,lower=0)
  work,info = zhesvx_lwork(n,lower=0)
  c,d,e,tau,info = ssytrd(a,lower=0,lwork=MAX(n,1),overwrite_a=0)
  c,d,e,tau,info = dsytrd(a,lower=0,lwork=MAX(n,1),overwrite_a=0)
  work,info = ssytrd_lwork(n,lower=0)
  work,info = dsytrd_lwork(n,lower=0)
  c,d,e,tau,info = chetrd(a,lower=0,lwork=MAX(n,1),overwrite_a=0)
  c,d,e,tau,info = zhetrd(a,lower=0,lwork=MAX(n,1),overwrite_a=0)
  work,info = chetrd_lwork(n,lower=0)
  work,info = zhetrd_lwork(n,lower=0)
  w,z,m,isuppz,info = ssyevr(a,compute_v=1,range='A',lower=0,vl=0.0,vu=1.0,il=1,iu=n,abstol=0.0,lwork=max(26*n,1),liwork=max(1,10*n),overwrite_a=0)
  w,z,m,isuppz,info = dsyevr(a,compute_v=1,range='A',lower=0,vl=0.0,vu=1.0,il=1,iu=n,abstol=0.0,lwork=max(26*n,1),liwork=max(1,10*n),overwrite_a=0)
  work,iwork,info = ssyevr_lwork(n,lower=0)
  work,iwork,info = dsyevr_lwork(n,lower=0)
  w,z,m,isuppz,info = cheevr(a,compute_v=1,range='A',lower=0,vl=0.0,vu=1.0,il=1,iu=n,abstol=0.0,lwork=max(2*n,1),lrwork=max(24*n,1),liwork=max(1,10*n),overwrite_a=0)
  w,z,m,isuppz,info = zheevr(a,compute_v=1,range='A',lower=0,vl=0.0,vu=1.0,il=1,iu=n,abstol=0.0,lwork=max(2*n,1),lrwork=max(24*n,1),liwork=max(1,10*n),overwrite_a=0)
  work,rwork,iwork,info = cheevr_lwork(n,lower=0)
  work,rwork,iwork,info = zheevr_lwork(n,lower=0)
  w,z,m,ifail,info = ssyevx(a,compute_v=1,range='A',lower=0,vl=0.0,vu=1.0,il=1,iu=n,abstol=0.0,lwork=max(8*n,1),overwrite_a=0)
  w,z,m,ifail,info = dsyevx(a,compute_v=1,range='A',lower=0,vl=0.0,vu=1.0,il=1,iu=n,abstol=0.0,lwork=max(8*n,1),overwrite_a=0)
  work,info = ssyevx_lwork(n,lower=0)
  work,info = dsyevx_lwork(n,lower=0)
  w,z,m,ifail,info = cheevx(a,compute_v=1,range='A',lower=0,vl=0.0,vu=1.0,il=1,iu=n,abstol=0.0,lwork=max(2*n,1),overwrite_a=0)
  w,z,m,ifail,info = zheevx(a,compute_v=1,range='A',lower=0,vl=0.0,vu=1.0,il=1,iu=n,abstol=0.0,lwork=max(2*n,1),overwrite_a=0)
  work,info = cheevx_lwork(n,lower=0)
  work,info = zheevx_lwork(n,lower=0)
  w,v,info = ssygv(a,b,itype=1,jobz='V',uplo='L',lwork=max(3*n-1,1),overwrite_a=0,overwrite_b=0)
  w,v,info = dsygv(a,b,itype=1,jobz='V',uplo='L',lwork=max(3*n-1,1),overwrite_a=0,overwrite_b=0)
  work,info = ssygv_lwork(n,uplo='L')
  work,info = dsygv_lwork(n,uplo='L')
  w,v,info = chegv(a,b,itype=1,jobz='V',uplo='L',lwork=max(2*n-1,1),overwrite_a=0,overwrite_b=0)
  w,v,info = zhegv(a,b,itype=1,jobz='V',uplo='L',lwork=max(2*n-1,1),overwrite_a=0,overwrite_b=0)
  work,info = chegv_lwork(n,uplo='L')
  work,info = zhegv_lwork(n,uplo='L')
  w,v,info = ssygvd(a,b,itype=1,jobz='V',uplo='L',lwork=(*jobz=='N'?2*n+1:1+6*n+2*n*n),liwork=(*jobz=='N'?1:5*n+3),overwrite_a=0,overwrite_b=0)
  w,v,info = dsygvd(a,b,itype=1,jobz='V',uplo='L',lwork=(*jobz=='N'?2*n+1:1+6*n+2*n*n),liwork=(*jobz=='N'?1:5*n+3),overwrite_a=0,overwrite_b=0)
  w,v,info = chegvd(a,b,itype=1,jobz='V',uplo='L',lwork=(*jobz=='N'?n+1:n*(n+2)),lrwork=max((*jobz=='N'?n:2*n*n+5*n+1),1),liwork=(*jobz=='N'?1:5*n+3),overwrite_a=0,overwrite_b=0)
  w,v,info = zhegvd(a,b,itype=1,jobz='V',uplo='L',lwork=(*jobz=='N'?n+1:n*(n+2)),lrwork=max((*jobz=='N'?n:2*n*n+5*n+1),1),liwork=(*jobz=='N'?1:5*n+3),overwrite_a=0,overwrite_b=0)
  w,z,m,ifail,info = ssygvx(a,b,itype=1,jobz='V',range='A',uplo='L',vl=0.0,vu=1.0,il=1,iu=n,abstol=0.0,lwork=max(8*n,1),overwrite_a=0,overwrite_b=0)
  w,z,m,ifail,info = dsygvx(a,b,itype=1,jobz='V',range='A',uplo='L',vl=0.0,vu=1.0,il=1,iu=n,abstol=0.0,lwork=max(8*n,1),overwrite_a=0,overwrite_b=0)
  work,info = ssygvx_lwork(n,uplo='L')
  work,info = dsygvx_lwork(n,uplo='L')
  w,z,m,ifail,info = chegvx(a,b,itype=1,jobz='V',range='A',uplo='L',vl=0.0,vu=1.0,il=1,iu=n,abstol=0.0,lwork=max(2*n,1),overwrite_a=0,overwrite_b=0)
  w,z,m,ifail,info = zhegvx(a,b,itype=1,jobz='V',range='A',uplo='L',vl=0.0,vu=1.0,il=1,iu=n,abstol=0.0,lwork=max(2*n,1),overwrite_a=0,overwrite_b=0)
  work,info = chegvx_lwork(n,uplo='L')
  work,info = zhegvx_lwork(n,uplo='L')
  s,scond,amax,info = ssyequb(a,lower=0)
  s,scond,amax,info = dsyequb(a,lower=0)
  s,scond,amax,info = csyequb(a,lower=0)
  s,scond,amax,info = zsyequb(a,lower=0)
  s,scond,amax,info = cheequb(a,lower=0)
  s,scond,amax,info = zheequb(a,lower=0)
  c,piv,rank_c,info = spstrf(a,tol=-1.0,lower=0,overwrite_a=0)
  c,piv,rank_c,info = dpstrf(a,tol=-1.0,lower=0,overwrite_a=0)
  c,piv,rank_c,info = cpstrf(a,tol=-1.0,lower=0,overwrite_a=0)
  c,piv,rank_c,info = zpstrf(a,tol=-1.0,lower=0,overwrite_a=0)
  c,piv,rank_c,info = spstf2(a,tol=-1.0,lower=0,overwrite_a=0)
  c,piv,rank_c,info = dpstf2(a,tol=-1.0,lower=0,overwrite_a=0)
  c,piv,rank_c,info = cpstf2(a,tol=-1.0,lower=0,overwrite_a=0)
  c,piv,rank_c,info = zpstf2(a,tol=-1.0,lower=0,overwrite_a=0)
  c,x,info = sposv(a,b,lower=0,overwrite_a=0,overwrite_b=0)
  c,x,info = dposv(a,b,lower=0,overwrite_a=0,overwrite_b=0)
  c,x,info = cposv(a,b,lower=0,overwrite_a=0,overwrite_b=0)
  c,x,info = zposv(a,b,lower=0,overwrite_a=0,overwrite_b=0)
  a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = sposvx(a,b,fact='E',af=,equed='Y',s=,lower=0,overwrite_a=0,overwrite_b=0)
  a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = dposvx(a,b,fact='E',af=,equed='Y',s=,lower=0,overwrite_a=0,overwrite_b=0)
  a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = cposvx(a,b,fact='E',af=,equed='Y',s=,lower=0,overwrite_a=0,overwrite_b=0)
  a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = zposvx(a,b,fact='E',af=,equed='Y',s=,lower=0,overwrite_a=0,overwrite_b=0)
  rcond,info = spocon(a,anorm,uplo='U')
  rcond,info = dpocon(a,anorm,uplo='U')
  rcond,info = cpocon(a,anorm,uplo='U')
  rcond,info = zpocon(a,anorm,uplo='U')
  c,info = spotrf(a,lower=0,clean=1,overwrite_a=0)
  c,info = dpotrf(a,lower=0,clean=1,overwrite_a=0)
  c,info = cpotrf(a,lower=0,clean=1,overwrite_a=0)
  c,info = zpotrf(a,lower=0,clean=1,overwrite_a=0)
  x,info = spotrs(c,b,lower=0,overwrite_b=0)
  x,info = dpotrs(c,b,lower=0,overwrite_b=0)
  x,info = cpotrs(c,b,lower=0,overwrite_b=0)
  x,info = zpotrs(c,b,lower=0,overwrite_b=0)
  inv_a,info = spotri(c,lower=0,overwrite_c=0)
  inv_a,info = dpotri(c,lower=0,overwrite_c=0)
  inv_a,info = cpotri(c,lower=0,overwrite_c=0)
  inv_a,info = zpotri(c,lower=0,overwrite_c=0)
  d,du,x,info = sptsv(d,e,b,overwrite_d=0,overwrite_e=0,overwrite_b=0)
  d,du,x,info = dptsv(d,e,b,overwrite_d=0,overwrite_e=0,overwrite_b=0)
  d,du,x,info = cptsv(d,e,b,overwrite_d=0,overwrite_e=0,overwrite_b=0)
  d,du,x,info = zptsv(d,e,b,overwrite_d=0,overwrite_e=0,overwrite_b=0)
  d,e,info = spttrf(d,e,overwrite_d=0,overwrite_e=0)
  d,e,info = dpttrf(d,e,overwrite_d=0,overwrite_e=0)
  d,e,info = cpttrf(d,e,overwrite_d=0,overwrite_e=0)
  d,e,info = zpttrf(d,e,overwrite_d=0,overwrite_e=0)
  x,info = spttrs(d,e,b,overwrite_b=0)
  x,info = dpttrs(d,e,b,overwrite_b=0)
  x,info = cpttrs(d,e,b,lower=0,overwrite_b=0)
  x,info = zpttrs(d,e,b,lower=0,overwrite_b=0)
  d,e,z,info = spteqr(d,e,z,compute_z=0,overwrite_d=0,overwrite_e=0,overwrite_z=0)
  d,e,z,info = dpteqr(d,e,z,compute_z=0,overwrite_d=0,overwrite_e=0,overwrite_z=0)
  d,e,z,info = cpteqr(d,e,z,compute_z=0,overwrite_d=0,overwrite_e=0,overwrite_z=0)
  d,e,z,info = zpteqr(d,e,z,compute_z=0,overwrite_d=0,overwrite_e=0,overwrite_z=0)
  df,ef,x,rcond,ferr,berr,info = sptsvx(d,e,b,fact='N',df=,ef=)
  df,ef,x,rcond,ferr,berr,info = dptsvx(d,e,b,fact='N',df=,ef=)
  df,ef,x,rcond,ferr,berr,info = cptsvx(d,e,b,fact='N',df=,ef=)
  df,ef,x,rcond,ferr,berr,info = zptsvx(d,e,b,fact='N',df=,ef=)
  sva,u,v,workout,iworkout,info = sgejsv(a,joba=4,jobu=0,jobv=0,jobr=1,jobt=0,jobp=1,lwork=max(6*n+2*n*n, max(2*m+n, max(4*n+n*n, max(2*n+n*n+6, 7)))),overwrite_a=0)
  sva,u,v,workout,iworkout,info = dgejsv(a,joba=4,jobu=0,jobv=0,jobr=1,jobt=0,jobp=1,lwork=max(6*n+2*n*n, max(2*m+n, max(4*n+n*n, max(2*n+n*n+6, 7)))),overwrite_a=0)
  a,q,info = strexc(a,q,ifst,ilst,wantq=1,overwrite_a=0,overwrite_q=0)
  a,q,info = dtrexc(a,q,ifst,ilst,wantq=1,overwrite_a=0,overwrite_q=0)
  a,q,info = ctrexc(a,q,ifst,ilst,wantq=1,overwrite_a=0,overwrite_q=0)
  a,q,info = ztrexc(a,q,ifst,ilst,wantq=1,overwrite_a=0,overwrite_q=0)
  a,b,q,z,work,info = stgexc(a,b,q,z,ifst,ilst,wantq=1,wantz=1,lwork=max(4*n+16,1),overwrite_a=0,overwrite_b=0,overwrite_q=0,overwrite_z=0)
  a,b,q,z,work,info = dtgexc(a,b,q,z,ifst,ilst,wantq=1,wantz=1,lwork=max(4*n+16,1),overwrite_a=0,overwrite_b=0,overwrite_q=0,overwrite_z=0)
  a,b,q,z,info = ctgexc(a,b,q,z,ifst,ilst,wantq=1,wantz=1,overwrite_a=0,overwrite_b=0,overwrite_q=0,overwrite_z=0)
  a,b,q,z,info = ztgexc(a,b,q,z,ifst,ilst,wantq=1,wantz=1,overwrite_a=0,overwrite_b=0,overwrite_q=0,overwrite_z=0)
  ts,qs,wr,wi,m,s,sep,info = strsen(select,t,q,job='B',wantq=1,lwork=MAX(1,n),liwork=1,overwrite_t=0,overwrite_q=0)
  ts,qs,wr,wi,m,s,sep,info = dtrsen(select,t,q,job='B',wantq=1,lwork=MAX(1,n),liwork=1,overwrite_t=0,overwrite_q=0)
  work,iwork,info = strsen_lwork(select,t,job='B')
  work,iwork,info = dtrsen_lwork(select,t,job='B')
  ts,qs,w,m,s,sep,info = ctrsen(select,t,q,job='B',wantq=1,lwork=MAX(1,n),overwrite_t=0,overwrite_q=0)
  ts,qs,w,m,s,sep,info = ztrsen(select,t,q,job='B',wantq=1,lwork=MAX(1,n),overwrite_t=0,overwrite_q=0)
  work,info = ctrsen_lwork(select,t,job='B')
  work,info = ztrsen_lwork(select,t,job='B')
  as,bs,alphar,alphai,beta,qs,zs,m,pl,pr,dif,info = stgsen(select,a,b,q,z,ijob=4,wantq=1,wantz=1,lwork=4*n+16,liwork=n+6,overwrite_a=0,overwrite_b=0,overwrite_q=0,overwrite_z=0)
  as,bs,alphar,alphai,beta,qs,zs,m,pl,pr,dif,info = dtgsen(select,a,b,q,z,ijob=4,wantq=1,wantz=1,lwork=4*n+16,liwork=n+6,overwrite_a=0,overwrite_b=0,overwrite_q=0,overwrite_z=0)
  work,iwork,info = stgsen_lwork(select,a,ijob=4)
  work,iwork,info = dtgsen_lwork(select,a,ijob=4)
  as,bs,alpha,beta,qs,zs,m,pl,pr,dif,info = ctgsen(select,a,b,q,z,ijob=4,wantq=1,wantz=1,lwork=(ijob==0?1:n+2),liwork=(ijob==0?1:n+2),overwrite_a=0,overwrite_b=0,overwrite_q=0,overwrite_z=0)
  as,bs,alpha,beta,qs,zs,m,pl,pr,dif,info = ztgsen(select,a,b,q,z,ijob=4,wantq=1,wantz=1,lwork=(ijob==0?1:n+2),liwork=(ijob==0?1:n+2),overwrite_a=0,overwrite_b=0,overwrite_q=0,overwrite_z=0)
  work,iwork,info = ctgsen_lwork(select,a,b,ijob=4)
  work,iwork,info = ztgsen_lwork(select,a,b,ijob=4)
  c,info = spbtrf(ab,lower=0,ldab=shape(ab,0),overwrite_ab=0)
  c,info = dpbtrf(ab,lower=0,ldab=shape(ab,0),overwrite_ab=0)
  c,info = cpbtrf(ab,lower=0,ldab=shape(ab,0),overwrite_ab=0)
  c,info = zpbtrf(ab,lower=0,ldab=shape(ab,0),overwrite_ab=0)
  x,info = spbtrs(ab,b,lower=0,ldab=shape(ab,0),overwrite_b=0)
  x,info = dpbtrs(ab,b,lower=0,ldab=shape(ab,0),overwrite_b=0)
  x,info = cpbtrs(ab,b,lower=0,ldab=shape(ab,0),overwrite_b=0)
  x,info = zpbtrs(ab,b,lower=0,ldab=shape(ab,0),overwrite_b=0)
  x,info = strtrs(a,b,lower=0,trans=0,unitdiag=0,lda=shape(a,0),overwrite_b=0)
  x,info = dtrtrs(a,b,lower=0,trans=0,unitdiag=0,lda=shape(a,0),overwrite_b=0)
  x,info = ctrtrs(a,b,lower=0,trans=0,unitdiag=0,lda=shape(a,0),overwrite_b=0)
  x,info = ztrtrs(a,b,lower=0,trans=0,unitdiag=0,lda=shape(a,0),overwrite_b=0)
  x,info = stbtrs(ab,b,uplo='U',trans='N',diag='N',overwrite_b=0)
  x,info = dtbtrs(ab,b,uplo='U',trans='N',diag='N',overwrite_b=0)
  x,info = ctbtrs(ab,b,uplo='U',trans='N',diag='N',overwrite_b=0)
  x,info = ztbtrs(ab,b,uplo='U',trans='N',diag='N',overwrite_b=0)
  c,x,info = spbsv(ab,b,lower=0,ldab=shape(ab,0),overwrite_ab=0,overwrite_b=0)
  c,x,info = dpbsv(ab,b,lower=0,ldab=shape(ab,0),overwrite_ab=0,overwrite_b=0)
  c,x,info = cpbsv(ab,b,lower=0,ldab=shape(ab,0),overwrite_ab=0,overwrite_b=0)
  c,x,info = zpbsv(ab,b,lower=0,ldab=shape(ab,0),overwrite_ab=0,overwrite_b=0)
  cs11,cs12,cs21,cs22,theta,u1,u2,v1t,v2t,info = sorcsd(x11,x12,x21,x22,compute_u1=1,compute_u2=1,compute_v1t=1,compute_v2t=1,trans=0,signs=0,lwork=2+2*m+5*MAX(1,q-1)+4*MAX(1,q)+8*q,overwrite_x11=0,overwrite_x12=0,overwrite_x21=0,overwrite_x22=0)
  cs11,cs12,cs21,cs22,theta,u1,u2,v1t,v2t,info = dorcsd(x11,x12,x21,x22,compute_u1=1,compute_u2=1,compute_v1t=1,compute_v2t=1,trans=0,signs=0,lwork=2+2*m+5*MAX(1,q-1)+4*MAX(1,q)+8*q,overwrite_x11=0,overwrite_x12=0,overwrite_x21=0,overwrite_x22=0)
  work,info = sorcsd_lwork(m,p,q)
  work,info = dorcsd_lwork(m,p,q)
  cs11,cs12,cs21,cs22,theta,u1,u2,v1t,v2t,info = cuncsd(x11,x12,x21,x22,compute_u1=1,compute_u2=1,compute_v1t=1,compute_v2t=1,trans=0,signs=0,lwork=2*m+MAX(1,MAX(mmp,mmq))+1,lrwork=5*MAX(1,q-1)+4*MAX(1,q)+8*q+1,overwrite_x11=0,overwrite_x12=0,overwrite_x21=0,overwrite_x22=0)
  cs11,cs12,cs21,cs22,theta,u1,u2,v1t,v2t,info = zuncsd(x11,x12,x21,x22,compute_u1=1,compute_u2=1,compute_v1t=1,compute_v2t=1,trans=0,signs=0,lwork=2*m+MAX(1,MAX(mmp,mmq))+1,lrwork=5*MAX(1,q-1)+4*MAX(1,q)+8*q+1,overwrite_x11=0,overwrite_x12=0,overwrite_x21=0,overwrite_x22=0)
  work,rwork,info = cuncsd_lwork(m,p,q)
  work,rwork,info = zuncsd_lwork(m,p,q)
  ht,info = sorghr(a,tau,lo=0,hi=n-1,lwork=max(hi-lo,1),overwrite_a=0)
  ht,info = dorghr(a,tau,lo=0,hi=n-1,lwork=max(hi-lo,1),overwrite_a=0)
  work,info = sorghr_lwork(n,lo=0,hi=n-1)
  work,info = dorghr_lwork(n,lo=0,hi=n-1)
  ht,info = cunghr(a,tau,lo=0,hi=n-1,lwork=max(hi-lo,1),overwrite_a=0)
  ht,info = zunghr(a,tau,lo=0,hi=n-1,lwork=max(hi-lo,1),overwrite_a=0)
  work,info = cunghr_lwork(n,lo=0,hi=n-1)
  work,info = zunghr_lwork(n,lo=0,hi=n-1)
  q,work,info = sorgqr(a,tau,lwork=max(3*n,1),overwrite_a=0)
  q,work,info = dorgqr(a,tau,lwork=max(3*n,1),overwrite_a=0)
  q,work,info = cungqr(a,tau,lwork=max(3*n,1),overwrite_a=0)
  q,work,info = zungqr(a,tau,lwork=max(3*n,1),overwrite_a=0)
  cq,work,info = sormqr(side,trans,a,tau,c,lwork,overwrite_c=0)
  cq,work,info = dormqr(side,trans,a,tau,c,lwork,overwrite_c=0)
  cq,work,info = cunmqr(side,trans,a,tau,c,lwork,overwrite_c=0)
  cq,work,info = zunmqr(side,trans,a,tau,c,lwork,overwrite_c=0)
  a,t,info = sgeqrt(nb,a,overwrite_a=0)
  a,t,info = dgeqrt(nb,a,overwrite_a=0)
  a,t,info = cgeqrt(nb,a,overwrite_a=0)
  a,t,info = zgeqrt(nb,a,overwrite_a=0)
  c,info = sgemqrt(v,t,c,side='L',trans='N',overwrite_c=0)
  c,info = dgemqrt(v,t,c,side='L',trans='N',overwrite_c=0)
  c,info = cgemqrt(v,t,c,side='L',trans='N',overwrite_c=0)
  c,info = zgemqrt(v,t,c,side='L',trans='N',overwrite_c=0)
  a,b,t,info = stpqrt(l,nb,a,b,overwrite_a=0,overwrite_b=0)
  a,b,t,info = dtpqrt(l,nb,a,b,overwrite_a=0,overwrite_b=0)
  a,b,t,info = ctpqrt(l,nb,a,b,overwrite_a=0,overwrite_b=0)
  a,b,t,info = ztpqrt(l,nb,a,b,overwrite_a=0,overwrite_b=0)
  a,b,info = stpmqrt(l,v,t,a,b,side='L',trans='N',overwrite_a=0,overwrite_b=0)
  a,b,info = dtpmqrt(l,v,t,a,b,side='L',trans='N',overwrite_a=0,overwrite_b=0)
  a,b,info = ctpmqrt(l,v,t,a,b,side='L',trans='N',overwrite_a=0,overwrite_b=0)
  a,b,info = ztpmqrt(l,v,t,a,b,side='L',trans='N',overwrite_a=0,overwrite_b=0)
  cq,info = sormrz(a,tau,c,side='L',trans='N',lwork=MAX((side[0]=='L'?n:m),1),overwrite_c=0)
  cq,info = dormrz(a,tau,c,side='L',trans='N',lwork=MAX((side[0]=='L'?n:m),1),overwrite_c=0)
  cq,info = cunmrz(a,tau,c,side='L',trans='N',lwork=MAX((side[0]=='L'?n:m),1),overwrite_c=0)
  cq,info = zunmrz(a,tau,c,side='L',trans='N',lwork=MAX((side[0]=='L'?n:m),1),overwrite_c=0)
  work,info = sormrz_lwork(m,n,side='L',trans='N')
  work,info = dormrz_lwork(m,n,side='L',trans='N')
  work,info = cunmrz_lwork(m,n,side='L',trans='N')
  work,info = zunmrz_lwork(m,n,side='L',trans='N')
  q,work,info = sorgrq(a,tau,lwork=max(3*m,1),overwrite_a=0)
  q,work,info = dorgrq(a,tau,lwork=max(3*m,1),overwrite_a=0)
  q,work,info = cungrq(a,tau,lwork=max(3*m,1),overwrite_a=0)
  q,work,info = zungrq(a,tau,lwork=max(3*m,1),overwrite_a=0)
  inv_c,info = strtri(c,lower=0,unitdiag=0,overwrite_c=0)
  inv_c,info = dtrtri(c,lower=0,unitdiag=0,overwrite_c=0)
  inv_c,info = ctrtri(c,lower=0,unitdiag=0,overwrite_c=0)
  inv_c,info = ztrtri(c,lower=0,unitdiag=0,overwrite_c=0)
  x,scale,info = strsyl(a,b,c,trana='N',tranb='N',isgn=1,overwrite_c=0)
  x,scale,info = dtrsyl(a,b,c,trana='N',tranb='N',isgn=1,overwrite_c=0)
  x,scale,info = ctrsyl(a,b,c,trana='N',tranb='N',isgn=1,overwrite_c=0)
  x,scale,info = ztrsyl(a,b,c,trana='N',tranb='N',isgn=1,overwrite_c=0)
  w,z,info = chbevd(ab,compute_v=1,lower=0,ldab=shape(ab,0),lrwork=(compute_v?1+5*n+2*n*n:n),liwork=(compute_v?3+5*n:1),overwrite_ab=1)
  w,z,info = zhbevd(ab,compute_v=1,lower=0,ldab=shape(ab,0),lrwork=(compute_v?1+5*n+2*n*n:n),liwork=(compute_v?3+5*n:1),overwrite_ab=1)
  w,z,m,ifail,info = chbevx(ab,vl,vu,il,iu,ldab=shape(ab,0),compute_v=1,range=0,lower=0,abstol=0.0,mmax=(compute_v?(range==2?(iu-il+1):n):1),overwrite_ab=1)
  w,z,m,ifail,info = zhbevx(ab,vl,vu,il,iu,ldab=shape(ab,0),compute_v=1,range=0,lower=0,abstol=0.0,mmax=(compute_v?(range==2?(iu-il+1):n):1),overwrite_ab=1)
  t,r,res,x,info = sgglse(a,b,c,d,lwork=max(m+n+p,1),overwrite_a=0,overwrite_b=0,overwrite_c=0,overwrite_d=0)
  t,r,res,x,info = dgglse(a,b,c,d,lwork=max(m+n+p,1),overwrite_a=0,overwrite_b=0,overwrite_c=0,overwrite_d=0)
  t,r,res,x,info = cgglse(a,b,c,d,lwork=max(m+n+p,1),overwrite_a=0,overwrite_b=0,overwrite_c=0,overwrite_d=0)
  t,r,res,x,info = zgglse(a,b,c,d,lwork=max(m+n+p,1),overwrite_a=0,overwrite_b=0,overwrite_c=0,overwrite_d=0)
  work,info = sgglse_lwork(m,n,p)
  work,info = dgglse_lwork(m,n,p)
  work,info = cgglse_lwork(m,n,p)
  work,info = zgglse_lwork(m,n,p)
  rcond,info = sppcon(n,ap,anorm,lower=0)
  rcond,info = dppcon(n,ap,anorm,lower=0)
  rcond,info = cppcon(n,ap,anorm,lower=0)
  rcond,info = zppcon(n,ap,anorm,lower=0)
  x,info = sppsv(n,ap,b,lower=0,overwrite_b=0)
  x,info = dppsv(n,ap,b,lower=0,overwrite_b=0)
  x,info = cppsv(n,ap,b,lower=0,overwrite_b=0)
  x,info = zppsv(n,ap,b,lower=0,overwrite_b=0)
  ul,info = spptrf(n,ap,lower=0,overwrite_ap=0)
  ul,info = dpptrf(n,ap,lower=0,overwrite_ap=0)
  ul,info = cpptrf(n,ap,lower=0,overwrite_ap=0)
  ul,info = zpptrf(n,ap,lower=0,overwrite_ap=0)
  uli,info = spptri(n,ap,lower=0,overwrite_ap=0)
  uli,info = dpptri(n,ap,lower=0,overwrite_ap=0)
  uli,info = cpptri(n,ap,lower=0,overwrite_ap=0)
  uli,info = zpptri(n,ap,lower=0,overwrite_ap=0)
  x,info = spptrs(n,ap,b,lower=0,overwrite_b=0)
  x,info = dpptrs(n,ap,b,lower=0,overwrite_b=0)
  x,info = cpptrs(n,ap,b,lower=0,overwrite_b=0)
  x,info = zpptrs(n,ap,b,lower=0,overwrite_b=0)
  w,z,info = ssbev(ab,compute_v=1,lower=0,ldab=shape(ab,0),overwrite_ab=1)
  w,z,info = dsbev(ab,compute_v=1,lower=0,ldab=shape(ab,0),overwrite_ab=1)
  w,z,info = ssbevd(ab,compute_v=1,lower=0,ldab=shape(ab,0),liwork=(compute_v?3+5*n:1),overwrite_ab=1)
  w,z,info = dsbevd(ab,compute_v=1,lower=0,ldab=shape(ab,0),liwork=(compute_v?3+5*n:1),overwrite_ab=1)
  w,z,m,ifail,info = ssbevx(ab,vl,vu,il,iu,ldab=shape(ab,0),compute_v=1,range=0,lower=0,abstol=0.0,mmax=(compute_v?(range==2?(iu-il+1):n):1),overwrite_ab=1)
  w,z,m,ifail,info = dsbevx(ab,vl,vu,il,iu,ldab=shape(ab,0),compute_v=1,range=0,lower=0,abstol=0.0,mmax=(compute_v?(range==2?(iu-il+1):n):1),overwrite_ab=1)
  m,w,iblock,isplit,info = sstebz(d,e,range,vl,vu,il,iu,tol,order)
  m,w,iblock,isplit,info = dstebz(d,e,range,vl,vu,il,iu,tol,order)
  vals,info = ssterf(d,e,overwrite_d=0,overwrite_e=0)
  vals,info = dsterf(d,e,overwrite_d=0,overwrite_e=0)
  z,info = sstein(d,e,w,iblock,isplit)
  z,info = dstein(d,e,w,iblock,isplit)
  m,w,z,info = sstemr(d,e,range,vl,vu,il,iu,compute_v=1,lwork=max((compute_v?18*n:12*n),1),liwork=(compute_v?10*n:8*n),overwrite_d=0)
  m,w,z,info = dstemr(d,e,range,vl,vu,il,iu,compute_v=1,lwork=max((compute_v?18*n:12*n),1),liwork=(compute_v?10*n:8*n),overwrite_d=0)
  work,iwork,info = sstemr_lwork(d,e,range,vl,vu,il,iu,compute_v=1,overwrite_d=0,overwrite_e=0)
  work,iwork,info = dstemr_lwork(d,e,range,vl,vu,il,iu,compute_v=1,overwrite_d=0,overwrite_e=0)
  vals,z,info = sstev(d,e,compute_v=1,overwrite_d=0,overwrite_e=0)
  vals,z,info = dstev(d,e,compute_v=1,overwrite_d=0,overwrite_e=0)
  cout = ssfrk(n,k,alpha,a,beta,c,transr='N',uplo='U',trans='N',overwrite_c=0)
  cout = dsfrk(n,k,alpha,a,beta,c,transr='N',uplo='U',trans='N',overwrite_c=0)
  cout = chfrk(n,k,alpha,a,beta,c,transr='N',uplo='U',trans='N',overwrite_c=0)
  cout = zhfrk(n,k,alpha,a,beta,c,transr='N',uplo='U',trans='N',overwrite_c=0)
  arf,info = stpttf(n,ap,transr='N',uplo='U')
  arf,info = dtpttf(n,ap,transr='N',uplo='U')
  arf,info = ctpttf(n,ap,transr='N',uplo='U')
  arf,info = ztpttf(n,ap,transr='N',uplo='U')
  a,info = stpttr(n,ap,uplo='U')
  a,info = dtpttr(n,ap,uplo='U')
  a,info = ctpttr(n,ap,uplo='U')
  a,info = ztpttr(n,ap,uplo='U')
  ap,info = stfttp(n,arf,transr='N',uplo='U')
  ap,info = dtfttp(n,arf,transr='N',uplo='U')
  ap,info = ctfttp(n,arf,transr='N',uplo='U')
  ap,info = ztfttp(n,arf,transr='N',uplo='U')
  a,info = stfttr(n,arf,transr='N',uplo='U')
  a,info = dtfttr(n,arf,transr='N',uplo='U')
  a,info = ctfttr(n,arf,transr='N',uplo='U')
  a,info = ztfttr(n,arf,transr='N',uplo='U')
  arf,info = strttf(a,transr='N',uplo='U')
  arf,info = dtrttf(a,transr='N',uplo='U')
  arf,info = ctrttf(a,transr='N',uplo='U')
  arf,info = ztrttf(a,transr='N',uplo='U')
  ap,info = strttp(a,uplo='U')
  ap,info = dtrttp(a,uplo='U')
  ap,info = ctrttp(a,uplo='U')
  ap,info = ztrttp(a,uplo='U')
  x = stfsm(alpha,a,b,transr='N',side='L',uplo='U',trans='N',diag='N',overwrite_b=0)
  x = dtfsm(alpha,a,b,transr='N',side='L',uplo='U',trans='N',diag='N',overwrite_b=0)
  x = ctfsm(alpha,a,b,transr='N',side='L',uplo='U',trans='N',diag='N',overwrite_b=0)
  x = ztfsm(alpha,a,b,transr='N',side='L',uplo='U',trans='N',diag='N',overwrite_b=0)
  achol,info = spftrf(n,a,transr='N',uplo='U',overwrite_a=0)
  achol,info = dpftrf(n,a,transr='N',uplo='U',overwrite_a=0)
  achol,info = cpftrf(n,a,transr='N',uplo='U',overwrite_a=0)
  achol,info = zpftrf(n,a,transr='N',uplo='U',overwrite_a=0)
  ainv,info = spftri(n,a,transr='N',uplo='U',overwrite_a=0)
  ainv,info = dpftri(n,a,transr='N',uplo='U',overwrite_a=0)
  ainv,info = cpftri(n,a,transr='N',uplo='U',overwrite_a=0)
  ainv,info = zpftri(n,a,transr='N',uplo='U',overwrite_a=0)
  x,info = spftrs(n,a,b,transr='N',uplo='U',overwrite_b=0)
  x,info = dpftrs(n,a,b,transr='N',uplo='U',overwrite_b=0)
  x,info = cpftrs(n,a,b,transr='N',uplo='U',overwrite_b=0)
  x,info = zpftrs(n,a,b,transr='N',uplo='U',overwrite_b=0)
  rz,tau,info = stzrzf(a,lwork=MAX(m,1),overwrite_a=0)
  rz,tau,info = dtzrzf(a,lwork=MAX(m,1),overwrite_a=0)
  rz,tau,info = ctzrzf(a,lwork=MAX(m,1),overwrite_a=0)
  rz,tau,info = ztzrzf(a,lwork=MAX(m,1),overwrite_a=0)
  work,info = stzrzf_lwork(m,n)
  work,info = dtzrzf_lwork(m,n)
  work,info = ctzrzf_lwork(m,n)
  work,info = ztzrzf_lwork(m,n)
  delta,sigma,work,info = slasd4(i,d,z,rho=1.0)
  delta,sigma,work,info = dlasd4(i,d,z,rho=1.0)
  a,info = slauum(c,lower=0,overwrite_c=0)
  a,info = dlauum(c,lower=0,overwrite_c=0)
  a,info = clauum(c,lower=0,overwrite_c=0)
  a,info = zlauum(c,lower=0,overwrite_c=0)
  a = slaswp(a,piv,k1=0,k2=npiv-1,off=0,inc=1,overwrite_a=0)
  a = dlaswp(a,piv,k1=0,k2=npiv-1,off=0,inc=1,overwrite_a=0)
  a = claswp(a,piv,k1=0,k2=npiv-1,off=0,inc=1,overwrite_a=0)
  a = zlaswp(a,piv,k1=0,k2=npiv-1,off=0,inc=1,overwrite_a=0)
  dlamch = dlamch(cmach)
  slamch = slamch(cmach)
  n2 = slange(norm,a)
  n2 = dlange(norm,a)
  n2 = clange(norm,a)
  n2 = zlange(norm,a)
  alpha,x,tau = slarfg(n,alpha,x,incx=1,overwrite_x=0)
  alpha,x,tau = dlarfg(n,alpha,x,incx=1,overwrite_x=0)
  alpha,x,tau = clarfg(n,alpha,x,incx=1,overwrite_x=0)
  alpha,x,tau = zlarfg(n,alpha,x,incx=1,overwrite_x=0)
  c = slarf(v,tau,c,work,side='L',incv=1,overwrite_c=0)
  c = dlarf(v,tau,c,work,side='L',incv=1,overwrite_c=0)
  c = clarf(v,tau,c,work,side='L',incv=1,overwrite_c=0)
  c = zlarf(v,tau,c,work,side='L',incv=1,overwrite_c=0)
  cs,sn,r = slartg(f,g)
  cs,sn,r = dlartg(f,g)
  cs,sn,r = clartg(f,g)
  cs,sn,r = zlartg(f,g)
  x,y = crot(x,y,c,s,n=(lx-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)
  x,y = zrot(x,y,c,s,n=(lx-1-offx)/abs(incx)+1,offx=0,incx=1,offy=0,incy=1,overwrite_x=0,overwrite_y=0)
  major,minor,patch = ilaver()
.
"""
# no imports

# Variables with simple values

__version__ = b'$Revision: $'

# functions

def cgbsv(kl, ku, ab, b, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lub,piv,x,info = cgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])
    
    Wrapper for ``cgbsv``.
    
    Parameters
    ----------
    kl : input int
    ku : input int
    ab : input rank-2 array('F') with bounds (2*kl+ku+1,n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lub : rank-2 array('F') with bounds (2*kl+ku+1,n) and ab storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('F') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def cgbtrf(ab, kl, ku, m=None, n=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    lu,ipiv,info = cgbtrf(ab,kl,ku,[m,n,ldab,overwrite_ab])
    
    Wrapper for ``cgbtrf``.
    
    Parameters
    ----------
    ab : input rank-2 array('F') with bounds (ldab,n)
    kl : input int
    ku : input int
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(ab,1)
    n : input int, optional
        Default: shape(ab,1)
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: max(shape(ab,0),1)
    
    Returns
    -------
    lu : rank-2 array('F') with bounds (ldab,n) and ab storage
    ipiv : rank-1 array('i') with bounds (MIN(m,n))
    info : int
    """
    pass

def cgbtrs(ab, kl, ku, b, ipiv, trans=None, n=None, ldab=None, ldb=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = cgbtrs(ab,kl,ku,b,ipiv,[trans,n,ldab,ldb,overwrite_b])
    
    Wrapper for ``cgbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('F') with bounds (ldab,n)
    kl : input int
    ku : input int
    b : input rank-2 array('F') with bounds (ldb,nrhs)
    ipiv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    n : input int, optional
        Default: shape(ab,1)
    ldab : input int, optional
        Default: shape(ab,0)
    ldb : input int, optional
        Default: shape(b,0)
    
    Returns
    -------
    x : rank-2 array('F') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def cgebal(a, scale=None, permute=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ba,lo,hi,pivscale,info = cgebal(a,[scale,permute,overwrite_a])
    
    Wrapper for ``cgebal``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    scale : input int, optional
        Default: 0
    permute : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    ba : rank-2 array('F') with bounds (m,n) and a storage
    lo : int
    hi : int
    pivscale : rank-1 array('f') with bounds (n)
    info : int
    """
    pass

def cgecon(a, anorm, norm=None): # real signature unknown; restored from __doc__
    """
    rcond,info = cgecon(a,anorm,[norm])
    
    Wrapper for ``cgecon``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    anorm : input float
    
    Other Parameters
    ----------------
    norm : input string(len=1), optional
        Default: '1'
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def cgeequ(a): # real signature unknown; restored from __doc__
    """
    r,c,rowcnd,colcnd,amax,info = cgeequ(a)
    
    Wrapper for ``cgeequ``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Returns
    -------
    r : rank-1 array('f') with bounds (m)
    c : rank-1 array('f') with bounds (n)
    rowcnd : float
    colcnd : float
    amax : float
    info : int
    """
    pass

def cgeequb(a): # real signature unknown; restored from __doc__
    """
    r,c,rowcnd,colcnd,amax,info = cgeequb(a)
    
    Wrapper for ``cgeequb``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Returns
    -------
    r : rank-1 array('f') with bounds (m)
    c : rank-1 array('f') with bounds (n)
    rowcnd : float
    colcnd : float
    amax : float
    info : int
    """
    pass

def cgees(cselect, a, compute_v=None, sort_t=None, lwork=None, cselect_extra_args=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    t,sdim,w,vs,work,info = cgees(cselect,a,[compute_v,sort_t,lwork,cselect_extra_args,overwrite_a])
    
    Wrapper for ``cgees``.
    
    Parameters
    ----------
    cselect : call-back function
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    sort_t : input int, optional
        Default: 0
    cselect_extra_args : input tuple, optional
        Default: ()
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    
    Returns
    -------
    t : rank-2 array('F') with bounds (n,n) and a storage
    sdim : int
    w : rank-1 array('F') with bounds (n)
    vs : rank-2 array('F') with bounds (ldvs,n)
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def cselect(arg): return cselect
      Required arguments:
        arg : input complex
      Return objects:
        cselect : int
    """
    pass

def cgeev(a, compute_vl=None, compute_vr=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,vl,vr,info = cgeev(a,[compute_vl,compute_vr,lwork,overwrite_a])
    
    Wrapper for ``cgeev``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(2*n,1)
    
    Returns
    -------
    w : rank-1 array('F') with bounds (n)
    vl : rank-2 array('F') with bounds (ldvl,n)
    vr : rank-2 array('F') with bounds (ldvr,n)
    info : int
    """
    pass

def cgeev_lwork(n, compute_vl=None, compute_vr=None): # real signature unknown; restored from __doc__
    """
    work,info = cgeev_lwork(n,[compute_vl,compute_vr])
    
    Wrapper for ``cgeev_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgehrd(a, lo=None, hi=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ht,tau,info = cgehrd(a,[lo,hi,lwork,overwrite_a])
    
    Wrapper for ``cgehrd``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(n,1)
    
    Returns
    -------
    ht : rank-2 array('F') with bounds (n,n) and a storage
    tau : rank-1 array('F') with bounds (n - 1)
    info : int
    """
    pass

def cgehrd_lwork(n, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    work,info = cgehrd_lwork(n,[lo,hi])
    
    Wrapper for ``cgehrd_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgels(a, b, trans=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lqr,x,info = cgels(a,b,[trans,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``cgels``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    b : input rank-2 array('F') with bounds (MAX(m,n),nrhs)
    
    Other Parameters
    ----------------
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(MIN(m,n)+MAX(MIN(m,n),nrhs),1)
    
    Returns
    -------
    lqr : rank-2 array('F') with bounds (m,n) and a storage
    x : rank-2 array('F') with bounds (MAX(m,n),nrhs) and b storage
    info : int
    """
    pass

def cgelsd(a, b, lwork, size_rwork, size_iwork, cond=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,s,rank,info = cgelsd(a,b,lwork,size_rwork,size_iwork,[cond,overwrite_a,overwrite_b])
    
    Wrapper for ``cgelsd``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    b : input rank-2 array('F') with bounds (maxmn,nrhs)
    lwork : input int
    size_rwork : input int
    size_iwork : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    cond : input float, optional
        Default: -1.0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (maxmn,nrhs) and b storage
    s : rank-1 array('f') with bounds (minmn)
    rank : int
    info : int
    """
    pass

def cgelsd_lwork(m, n, nrhs, cond=None, lwork=None): # real signature unknown; restored from __doc__
    """
    work,rwork,iwork,info = cgelsd_lwork(m,n,nrhs,[cond,lwork])
    
    Wrapper for ``cgelsd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : complex
    rwork : float
    iwork : int
    info : int
    """
    pass

def cgelss(a, b, cond=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    v,x,s,rank,work,info = cgelss(a,b,[cond,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``cgelss``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    b : input rank-2 array('F') with bounds (maxmn,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: max(2*minmn+MAX(maxmn,nrhs),1)
    
    Returns
    -------
    v : rank-2 array('F') with bounds (m,n) and a storage
    x : rank-2 array('F') with bounds (maxmn,nrhs) and b storage
    s : rank-1 array('f') with bounds (minmn)
    rank : int
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def cgelss_lwork(m, n, nrhs, cond=None, lwork=None): # real signature unknown; restored from __doc__
    """
    work,info = cgelss_lwork(m,n,nrhs,[cond,lwork])
    
    Wrapper for ``cgelss_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgelsy(a, b, jptv, cond, lwork, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    v,x,j,rank,info = cgelsy(a,b,jptv,cond,lwork,[overwrite_a,overwrite_b])
    
    Wrapper for ``cgelsy``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    b : input rank-2 array('F') with bounds (maxmn,nrhs)
    jptv : input rank-1 array('i') with bounds (n)
    cond : input float
    lwork : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    v : rank-2 array('F') with bounds (m,n) and a storage
    x : rank-2 array('F') with bounds (maxmn,nrhs) and b storage
    j : rank-1 array('i') with bounds (n) and jptv storage
    rank : int
    info : int
    """
    pass

def cgelsy_lwork(m, n, nrhs, cond, lwork=None): # real signature unknown; restored from __doc__
    """
    work,info = cgelsy_lwork(m,n,nrhs,cond,[lwork])
    
    Wrapper for ``cgelsy_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    cond : input float
    
    Other Parameters
    ----------------
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgels_lwork(m, n, nrhs, trans=None): # real signature unknown; restored from __doc__
    """
    work,info = cgels_lwork(m,n,nrhs,[trans])
    
    Wrapper for ``cgels_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    trans : input string(len=1), optional
        Default: 'N'
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgemqrt(v, t, c, side=None, trans=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c,info = cgemqrt(v,t,c,[side,trans,overwrite_c])
    
    Wrapper for ``cgemqrt``.
    
    Parameters
    ----------
    v : input rank-2 array('F') with bounds ((side[0]=='L'?m:n),k)
    t : input rank-2 array('F') with bounds (nb,k)
    c : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (m,n)
    info : int
    """
    pass

def cgeqp3(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,jpvt,tau,work,info = cgeqp3(a,[lwork,overwrite_a])
    
    Wrapper for ``cgeqp3``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*(n+1),1)
    
    Returns
    -------
    qr : rank-2 array('F') with bounds (m,n) and a storage
    jpvt : rank-1 array('i') with bounds (n)
    tau : rank-1 array('F') with bounds (MIN(m,n))
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def cgeqrf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,work,info = cgeqrf(a,[lwork,overwrite_a])
    
    Wrapper for ``cgeqrf``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    
    Returns
    -------
    qr : rank-2 array('F') with bounds (m,n) and a storage
    tau : rank-1 array('F') with bounds (MIN(m,n))
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def cgeqrfp(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,info = cgeqrfp(a,[lwork,overwrite_a])
    
    Wrapper for ``cgeqrfp``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(1, n)
    
    Returns
    -------
    qr : rank-2 array('F') with bounds (m,n) and a storage
    tau : rank-1 array('F') with bounds (MIN(m,n))
    info : int
    """
    pass

def cgeqrfp_lwork(m, n): # real signature unknown; restored from __doc__
    """
    work,info = cgeqrfp_lwork(m,n)
    
    Wrapper for ``cgeqrfp_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgeqrf_lwork(m, n): # real signature unknown; restored from __doc__
    """
    work,info = cgeqrf_lwork(m,n)
    
    Wrapper for ``cgeqrf_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgeqrt(nb, a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a,t,info = cgeqrt(nb,a,[overwrite_a])
    
    Wrapper for ``cgeqrt``.
    
    Parameters
    ----------
    nb : input int
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (m,n)
    t : rank-2 array('F') with bounds (nb,MIN(m,n))
    info : int
    """
    pass

def cgerqf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,work,info = cgerqf(a,[lwork,overwrite_a])
    
    Wrapper for ``cgerqf``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*m,1)
    
    Returns
    -------
    qr : rank-2 array('F') with bounds (m,n) and a storage
    tau : rank-1 array('F') with bounds (MIN(m,n))
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def cgesc2(lu, rhs, ipiv, jpiv, overwrite_rhs=None): # real signature unknown; restored from __doc__
    """
    x,scale = cgesc2(lu,rhs,ipiv,jpiv,[overwrite_rhs])
    
    Wrapper for ``cgesc2``.
    
    Parameters
    ----------
    lu : input rank-2 array('F') with bounds (n,n)
    rhs : input rank-1 array('F') with bounds (n)
    ipiv : input rank-1 array('i') with bounds (n)
    jpiv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_rhs : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-1 array('F') with bounds (n) and rhs storage
    scale : float
    """
    pass

def cgesdd(a, compute_uv=None, full_matrices=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    u,s,vt,info = cgesdd(a,[compute_uv,full_matrices,lwork,overwrite_a])
    
    Wrapper for ``cgesdd``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    lwork : input int, optional
        Default: max((compute_uv?2*minmn*minmn+MAX(m,n)+2*minmn:2*minmn+MAX(m,n)),1)
    
    Returns
    -------
    u : rank-2 array('F') with bounds (u0,u1)
    s : rank-1 array('f') with bounds (minmn)
    vt : rank-2 array('F') with bounds (vt0,vt1)
    info : int
    """
    pass

def cgesdd_lwork(m, n, compute_uv=None, full_matrices=None): # real signature unknown; restored from __doc__
    """
    work,info = cgesdd_lwork(m,n,[compute_uv,full_matrices])
    
    Wrapper for ``cgesdd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgesv(a, b, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lu,piv,x,info = cgesv(a,b,[overwrite_a,overwrite_b])
    
    Wrapper for ``cgesv``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('F') with bounds (n,n) and a storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('F') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def cgesvd(a, compute_uv=None, full_matrices=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    u,s,vt,info = cgesvd(a,[compute_uv,full_matrices,lwork,overwrite_a])
    
    Wrapper for ``cgesvd``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    lwork : input int, optional
        Default: MAX(2*minmn+MAX(m,n),1)
    
    Returns
    -------
    u : rank-2 array('F') with bounds (u0,u1)
    s : rank-1 array('f') with bounds (minmn)
    vt : rank-2 array('F') with bounds (vt0,vt1)
    info : int
    """
    pass

def cgesvd_lwork(m, n, compute_uv=None, full_matrices=None): # real signature unknown; restored from __doc__
    """
    work,info = cgesvd_lwork(m,n,[compute_uv,full_matrices])
    
    Wrapper for ``cgesvd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgesvx(a, b, fact=None, trans=None, af=None, ipiv=None, equed=None, r=None, c=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = cgesvx(a,b,[fact,trans,af,ipiv,equed,r,c,overwrite_a,overwrite_b])
    
    Wrapper for ``cgesvx``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    fact : input string(len=1), optional
        Default: 'E'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_a : input int, optional
        Default: 0
    af : input rank-2 array('F') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    equed : input string(len=1), optional
        Default: 'B'
    r : input rank-1 array('f') with bounds (n)
    c : input rank-1 array('f') with bounds (n)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    as : rank-2 array('F') with bounds (n,n) and a storage
    lu : rank-2 array('F') with bounds (n,n) and af storage
    ipiv : rank-1 array('i') with bounds (n)
    equed : string(len=1)
    rs : rank-1 array('f') with bounds (n) and r storage
    cs : rank-1 array('f') with bounds (n) and c storage
    bs : rank-2 array('F') with bounds (n,nrhs) and b storage
    x : rank-2 array('F') with bounds (n,nrhs)
    rcond : float
    ferr : rank-1 array('f') with bounds (nrhs)
    berr : rank-1 array('f') with bounds (nrhs)
    info : int
    """
    pass

def cgetc2(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    lu,ipiv,jpiv,info = cgetc2(a,[overwrite_a])
    
    Wrapper for ``cgetc2``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('F') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    jpiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def cgetrf(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    lu,piv,info = cgetrf(a,[overwrite_a])
    
    Wrapper for ``cgetrf``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('F') with bounds (m,n) and a storage
    piv : rank-1 array('i') with bounds (MIN(m,n))
    info : int
    """
    pass

def cgetri(lu, piv, lwork=None, overwrite_lu=None): # real signature unknown; restored from __doc__
    """
    inv_a,info = cgetri(lu,piv,[lwork,overwrite_lu])
    
    Wrapper for ``cgetri``.
    
    Parameters
    ----------
    lu : input rank-2 array('F') with bounds (n,n)
    piv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_lu : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    
    Returns
    -------
    inv_a : rank-2 array('F') with bounds (n,n) and lu storage
    info : int
    """
    pass

def cgetri_lwork(n): # real signature unknown; restored from __doc__
    """
    work,info = cgetri_lwork(n)
    
    Wrapper for ``cgetri_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgetrs(lu, piv, b, trans=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = cgetrs(lu,piv,b,[trans,overwrite_b])
    
    Wrapper for ``cgetrs``.
    
    Parameters
    ----------
    lu : input rank-2 array('F') with bounds (n,n)
    piv : input rank-1 array('i') with bounds (n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def cgges(cselect, a, b, jobvsl=None, jobvsr=None, sort_t=None, ldvsl=None, ldvsr=None, lwork=None, cselect_extra_args=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,b,sdim,alpha,beta,vsl,vsr,work,info = cgges(cselect,a,b,[jobvsl,jobvsr,sort_t,ldvsl,ldvsr,lwork,cselect_extra_args,overwrite_a,overwrite_b])
    
    Wrapper for ``cgges``.
    
    Parameters
    ----------
    cselect : call-back function
    a : input rank-2 array('F') with bounds (lda,n)
    b : input rank-2 array('F') with bounds (ldb,n)
    
    Other Parameters
    ----------------
    jobvsl : input int, optional
        Default: 1
    jobvsr : input int, optional
        Default: 1
    sort_t : input int, optional
        Default: 0
    cselect_extra_args : input tuple, optional
        Default: ()
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    ldvsl : input int, optional
        Default: ((jobvsl==1)?n:1)
    ldvsr : input int, optional
        Default: ((jobvsr==1)?n:1)
    lwork : input int, optional
        Default: max(2*n,1)
    
    Returns
    -------
    a : rank-2 array('F') with bounds (lda,n)
    b : rank-2 array('F') with bounds (ldb,n)
    sdim : int
    alpha : rank-1 array('F') with bounds (n)
    beta : rank-1 array('F') with bounds (n)
    vsl : rank-2 array('F') with bounds (ldvsl,n)
    vsr : rank-2 array('F') with bounds (ldvsr,n)
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def cselect(alpha,beta): return cselect
      Required arguments:
        alpha : input complex
        beta : input complex
      Return objects:
        cselect : int
    """
    pass

def cggev(a, b, compute_vl=None, compute_vr=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    alpha,beta,vl,vr,work,info = cggev(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``cggev``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(2*n,1)
    
    Returns
    -------
    alpha : rank-1 array('F') with bounds (n)
    beta : rank-1 array('F') with bounds (n)
    vl : rank-2 array('F') with bounds (ldvl,n)
    vr : rank-2 array('F') with bounds (ldvr,n)
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def cgglse(a, b, c, d, lwork=None, overwrite_a=None, overwrite_b=None, overwrite_c=None, overwrite_d=None): # real signature unknown; restored from __doc__
    """
    t,r,res,x,info = cgglse(a,b,c,d,[lwork,overwrite_a,overwrite_b,overwrite_c,overwrite_d])
    
    Wrapper for ``cgglse``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    b : input rank-2 array('F') with bounds (p,n)
    c : input rank-1 array('F') with bounds (m)
    d : input rank-1 array('F') with bounds (p)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    overwrite_c : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(m+n+p,1)
    
    Returns
    -------
    t : rank-2 array('F') with bounds (m,n) and a storage
    r : rank-2 array('F') with bounds (p,n) and b storage
    res : rank-1 array('F') with bounds (m) and c storage
    x : rank-1 array('F') with bounds (n)
    info : int
    """
    pass

def cgglse_lwork(m, n, p): # real signature unknown; restored from __doc__
    """
    work,info = cgglse_lwork(m,n,p)
    
    Wrapper for ``cgglse_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    p : input int
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cgtsv(dl, d, du, b, overwrite_dl=None, overwrite_d=None, overwrite_du=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    du2,d,du,x,info = cgtsv(dl,d,du,b,[overwrite_dl,overwrite_d,overwrite_du,overwrite_b])
    
    Wrapper for ``cgtsv``.
    
    Parameters
    ----------
    dl : input rank-1 array('F') with bounds (n - 1)
    d : input rank-1 array('F') with bounds (n)
    du : input rank-1 array('F') with bounds (n - 1)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_dl : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    overwrite_du : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    du2 : rank-1 array('F') with bounds (n - 1) and dl storage
    d : rank-1 array('F') with bounds (n)
    du : rank-1 array('F') with bounds (n - 1)
    x : rank-2 array('F') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def cgtsvx(dl, d, du, b, fact=None, trans=None, dlf=None, df=None, duf=None, du2=None, ipiv=None): # real signature unknown; restored from __doc__
    """
    dlf,df,duf,du2,ipiv,x,rcond,ferr,berr,info = cgtsvx(dl,d,du,b,[fact,trans,dlf,df,duf,du2,ipiv])
    
    Wrapper for ``cgtsvx``.
    
    Parameters
    ----------
    dl : input rank-1 array('F') with bounds (MAX(0, n-1))
    d : input rank-1 array('F') with bounds (n)
    du : input rank-1 array('F') with bounds (MAX(0, n-1))
    b : input rank-2 array('F') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    fact : input string(len=1), optional
        Default: 'N'
    trans : input string(len=1), optional
        Default: 'N'
    dlf : input rank-1 array('F') with bounds (MAX(0,n-1))
    df : input rank-1 array('F') with bounds (n)
    duf : input rank-1 array('F') with bounds (MAX(0,n-1))
    du2 : input rank-1 array('F') with bounds (MAX(0,n-2))
    ipiv : input rank-1 array('i') with bounds (n)
    
    Returns
    -------
    dlf : rank-1 array('F') with bounds (MAX(0,n-1))
    df : rank-1 array('F') with bounds (n)
    duf : rank-1 array('F') with bounds (MAX(0,n-1))
    du2 : rank-1 array('F') with bounds (MAX(0,n-2))
    ipiv : rank-1 array('i') with bounds (n)
    x : rank-2 array('F') with bounds (ldx,nrhs)
    rcond : float
    ferr : rank-1 array('f') with bounds (nrhs)
    berr : rank-1 array('f') with bounds (nrhs)
    info : int
    """
    pass

def cgttrf(dl, d, du, overwrite_dl=None, overwrite_d=None, overwrite_du=None): # real signature unknown; restored from __doc__
    """
    dl,d,du,du2,ipiv,info = cgttrf(dl,d,du,[overwrite_dl,overwrite_d,overwrite_du])
    
    Wrapper for ``cgttrf``.
    
    Parameters
    ----------
    dl : input rank-1 array('F') with bounds (n - 1)
    d : input rank-1 array('F') with bounds (n)
    du : input rank-1 array('F') with bounds (n - 1)
    
    Other Parameters
    ----------------
    overwrite_dl : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    overwrite_du : input int, optional
        Default: 0
    
    Returns
    -------
    dl : rank-1 array('F') with bounds (n - 1)
    d : rank-1 array('F') with bounds (n)
    du : rank-1 array('F') with bounds (n - 1)
    du2 : rank-1 array('F') with bounds (n - 2)
    ipiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def cgttrs(dl, d, du, du2, ipiv, b, trans=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = cgttrs(dl,d,du,du2,ipiv,b,[trans,overwrite_b])
    
    Wrapper for ``cgttrs``.
    
    Parameters
    ----------
    dl : input rank-1 array('F') with bounds (n - 1)
    d : input rank-1 array('F') with bounds (n)
    du : input rank-1 array('F') with bounds (n - 1)
    du2 : input rank-1 array('F') with bounds (n - 2)
    ipiv : input rank-1 array('i') with bounds (n)
    b : input rank-2 array('F') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def chbevd(ab, compute_v=None, lower=None, ldab=None, lrwork=None, liwork=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,info = chbevd(ab,[compute_v,lower,ldab,lrwork,liwork,overwrite_ab])
    
    Wrapper for ``chbevd``.
    
    Parameters
    ----------
    ab : input rank-2 array('F') with bounds (ldab,n)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    lrwork : input int, optional
        Default: (compute_v?1+5*n+2*n*n:n)
    liwork : input int, optional
        Default: (compute_v?3+5*n:1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('F') with bounds (ldz,ldz)
    info : int
    """
    pass

def chbevx(ab, vl, vu, il, iu, ldab=None, compute_v=None, range=None, lower=None, abstol=None, mmax=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,m,ifail,info = chbevx(ab,vl,vu,il,iu,[ldab,compute_v,range,lower,abstol,mmax,overwrite_ab])
    
    Wrapper for ``chbevx``.
    
    Parameters
    ----------
    ab : input rank-2 array('F') with bounds (ldab,n)
    vl : input float
    vu : input float
    il : input int
    iu : input int
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    ldab : input int, optional
        Default: shape(ab,0)
    compute_v : input int, optional
        Default: 1
    range : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    abstol : input float, optional
        Default: 0.0
    mmax : input int, optional
        Default: (compute_v?(range==2?(iu-il+1):n):1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('F') with bounds (ldz,mmax)
    m : int
    ifail : rank-1 array('i') with bounds ((compute_v?n:1))
    info : int
    """
    pass

def checon(a, ipiv, anorm, lower=None): # real signature unknown; restored from __doc__
    """
    rcond,info = checon(a,ipiv,anorm,[lower])
    
    Wrapper for ``checon``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    anorm : input float
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def cheequb(a, lower=None): # real signature unknown; restored from __doc__
    """
    s,scond,amax,info = cheequb(a,[lower])
    
    Wrapper for ``cheequb``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (lda,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    s : rank-1 array('f') with bounds (n)
    scond : float
    amax : float
    info : int
    """
    pass

def cheev(a, compute_v=None, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,v,info = cheev(a,[compute_v,lower,lwork,overwrite_a])
    
    Wrapper for ``cheev``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(2*n-1,1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    v : rank-2 array('F') with bounds (n,n) and a storage
    info : int
    """
    pass

def cheevd(a, compute_v=None, lower=None, lwork=None, liwork=None, lrwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,v,info = cheevd(a,[compute_v,lower,lwork,liwork,lrwork,overwrite_a])
    
    Wrapper for ``cheevd``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max((compute_v?2*n+n*n:n+1),1)
    liwork : input int, optional
        Default: (compute_v?3+5*n:1)
    lrwork : input int, optional
        Default: (compute_v?1+5*n+2*n*n:n)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    v : rank-2 array('F') with bounds (n,n) and a storage
    info : int
    """
    pass

def cheevd_lwork(n, compute_v=None, lower=None): # real signature unknown; restored from __doc__
    """
    work,iwork,rwork,info = cheevd_lwork(n,[compute_v,lower])
    
    Wrapper for ``cheevd_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    iwork : int
    rwork : float
    info : int
    """
    pass

def cheevr(a, compute_v=None, range=None, lower=None, vl=None, vu=None, il=None, iu=None, abstol=None, lwork=None, lrwork=None, liwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,z,m,isuppz,info = cheevr(a,[compute_v,range,lower,vl,vu,il,iu,abstol,lwork,lrwork,liwork,overwrite_a])
    
    Wrapper for ``cheevr``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds ``(n,n)``
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default ``1``
    range : input string(len=1), optional
        Default ``'A'``
    lower : input int, optional
        Default ``0``
    overwrite_a : input int, optional
        Default ``0``
    vl : input float, optional
        Default ``0.0``
    vu : input float, optional
        Default ``1.0``
    il : input int, optional
        Default ``1``
    iu : input int, optional
        Default ``n``
    abstol : input float, optional
        Default ``0.0``
    lwork : input int, optional
        Default ``max(2*n,1)``
    lrwork : input int, optional
        Default ``max(24*n,1)``
    liwork : input int, optional
        Default ``max(1,10*n)``
    
    Returns
    -------
    w : rank-1 array('f') with bounds ``(n)``
    z : rank-2 array('F') with bounds ``((compute_v?MAX(0,n):0),(compute_v?((*range=='I')?(iu-il+1):MAX(1,n)):0))``
    m : int
    isuppz : rank-1 array('i') with bounds ``(2*max(1,n))``
    info : int
    """
    pass

def cheevr_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,rwork,iwork,info = cheevr_lwork(n,[lower])
    
    Wrapper for ``cheevr_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    rwork : float
    iwork : int
    info : int
    """
    pass

def cheevx(a, compute_v=None, range=None, lower=None, vl=None, vu=None, il=None, iu=None, abstol=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,z,m,ifail,info = cheevx(a,[compute_v,range,lower,vl,vu,il,iu,abstol,lwork,overwrite_a])
    
    Wrapper for ``cheevx``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds ``(n,n)``
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default ``1``
    range : input string(len=1), optional
        Default ``'A'``
    lower : input int, optional
        Default ``0``
    overwrite_a : input int, optional
        Default ``0``
    vl : input float, optional
        Default ``0.0``
    vu : input float, optional
        Default ``1.0``
    il : input int, optional
        Default ``1``
    iu : input int, optional
        Default ``n``
    abstol : input float, optional
        Default ``0.0``
    lwork : input int, optional
        Default ``max(2*n,1)``
    
    Returns
    -------
    w : rank-1 array('f') with bounds ``(n)``
    z : rank-2 array('F') with bounds ``((compute_v*n),(compute_v?((*range=='I')?(iu-il+1):MAX(1,n)):0))``
    m : int
    ifail : rank-1 array('i') with bounds ``(compute_v*n)``
    info : int
    """
    pass

def cheevx_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = cheevx_lwork(n,[lower])
    
    Wrapper for ``cheevx_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cheev_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = cheev_lwork(n,[lower])
    
    Wrapper for ``cheev_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def chegst(a, b, itype=None, lower=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,info = chegst(a,b,[itype,lower,overwrite_a])
    
    Wrapper for ``chegst``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    itype : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (n,n) and a storage
    info : int
    """
    pass

def chegv(a, b, itype=None, jobz=None, uplo=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    w,v,info = chegv(a,b,[itype,jobz,uplo,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``chegv``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(2*n-1,1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    v : rank-2 array('F') with bounds (n,n) and a storage
    info : int
    """
    pass

def chegvd(a, b, itype=None, jobz=None, uplo=None, lwork=None, lrwork=None, liwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    w,v,info = chegvd(a,b,[itype,jobz,uplo,lwork,lrwork,liwork,overwrite_a,overwrite_b])
    
    Wrapper for ``chegvd``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds ``(n,n)``
    b : input rank-2 array('F') with bounds ``(n,n)``
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default ``1``
    jobz : input string(len=1), optional
        Default ``'V'``
    uplo : input string(len=1), optional
        Default ``'L'``
    overwrite_a : input int, optional
        Default ``0``
    overwrite_b : input int, optional
        Default ``0``
    lwork : input int, optional
        Default ``(*jobz=='N'?n+1:n*(n+2))``
    lrwork : input int, optional
        Default ``max((*jobz=='N'?n:2*n*n+5*n+1),1)``
    liwork : input int, optional
        Default ``(*jobz=='N'?1:5*n+3)``
    
    Returns
    -------
    w : rank-1 array('f') with bounds ``(n)``
    v : rank-2 array('F') with bounds ``(n,n)`` with ``a`` storage
    info : int
    """
    pass

def chegvx(a, b, itype=None, jobz=None, range=None, uplo=None, vl=None, vu=None, il=None, iu=None, abstol=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    w,z,m,ifail,info = chegvx(a,b,[itype,jobz,range,uplo,vl,vu,il,iu,abstol,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``chegvx``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    range : input string(len=1), optional
        Default: 'A'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    vl : input float, optional
        Default: 0.0
    vu : input float, optional
        Default: 1.0
    il : input int, optional
        Default: 1
    iu : input int, optional
        Default: n
    abstol : input float, optional
        Default: 0.0
    lwork : input int, optional
        Default: max(2*n,1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('F') with bounds ((jobz[0]=='V'?MAX(0,n):0),(jobz[0]=='V'?((range[0]=='I')?(iu-il+1):MAX(1,n)):0))
    m : int
    ifail : rank-1 array('i') with bounds ((jobz[0]=='N'?0:n))
    info : int
    """
    pass

def chegvx_lwork(n, uplo=None): # real signature unknown; restored from __doc__
    """
    work,info = chegvx_lwork(n,[uplo])
    
    Wrapper for ``chegvx_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'L'
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def chegv_lwork(n, uplo=None): # real signature unknown; restored from __doc__
    """
    work,info = chegv_lwork(n,[uplo])
    
    Wrapper for ``chegv_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'L'
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def chesv(a, b, lwork=None, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    uduh,ipiv,x,info = chesv(a,b,[lwork,lower,overwrite_a,overwrite_b])
    
    Wrapper for ``chesv``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(n,1)
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    uduh : rank-2 array('F') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    x : rank-2 array('F') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def chesvx(a, b, af=None, ipiv=None, lwork=None, factored=None, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    uduh,ipiv,x,rcond,ferr,berr,info = chesvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])
    
    Wrapper for ``chesvx``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    af : input rank-2 array('F') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(2*n,1)
    factored : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    uduh : rank-2 array('F') with bounds (n,n) and af storage
    ipiv : rank-1 array('i') with bounds (n)
    x : rank-2 array('F') with bounds (n,nrhs)
    rcond : float
    ferr : rank-1 array('f') with bounds (nrhs)
    berr : rank-1 array('f') with bounds (nrhs)
    info : int
    """
    pass

def chesvx_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = chesvx_lwork(n,[lower])
    
    Wrapper for ``chesvx_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def chesv_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = chesv_lwork(n,[lower])
    
    Wrapper for ``chesv_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def chetrd(a, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,d,e,tau,info = chetrd(a,[lower,lwork,overwrite_a])
    
    Wrapper for ``chetrd``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (lda,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(n,1)
    
    Returns
    -------
    c : rank-2 array('F') with bounds (lda,n) and a storage
    d : rank-1 array('f') with bounds (n)
    e : rank-1 array('f') with bounds (n - 1)
    tau : rank-1 array('F') with bounds (n - 1)
    info : int
    """
    pass

def chetrd_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = chetrd_lwork(n,[lower])
    
    Wrapper for ``chetrd_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def chetrf(a, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ldu,ipiv,info = chetrf(a,[lower,lwork,overwrite_a])
    
    Wrapper for ``chetrf``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(n,1)
    
    Returns
    -------
    ldu : rank-2 array('F') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def chetrf_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = chetrf_lwork(n,[lower])
    
    Wrapper for ``chetrf_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def chfrk(n, k, alpha, a, beta, c, transr=None, uplo=None, trans=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    cout = chfrk(n,k,alpha,a,beta,c,[transr,uplo,trans,overwrite_c])
    
    Wrapper for ``chfrk``.
    
    Parameters
    ----------
    n : input int
    k : input int
    alpha : input float
    a : input rank-2 array('F') with bounds (lda,ka)
    beta : input float
    c : input rank-1 array('F') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    cout : rank-1 array('F') with bounds (nt) and c storage
    """
    pass

def clange(norm, a): # real signature unknown; restored from __doc__
    """
    n2 = clange(norm,a)
    
    Wrapper for ``clange``.
    
    Parameters
    ----------
    norm : input string(len=1)
    a : input rank-2 array('F') with bounds (m,n)
    
    Returns
    -------
    n2 : float
    """
    pass

def clarf(v, tau, c, work, side=None, incv=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = clarf(v,tau,c,work,[side,incv,overwrite_c])
    
    Wrapper for ``clarf``.
    
    Parameters
    ----------
    v : input rank-1 array('F') with bounds ((side[0]=='L'?(1 + (m-1)*abs(incv)):(1 + (n-1)*abs(incv))))
    tau : input complex
    c : input rank-2 array('F') with bounds (m,n)
    work : input rank-1 array('F') with bounds (lwork)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    incv : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (m,n)
    """
    pass

def clarfg(n, alpha, x, incx=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    alpha,x,tau = clarfg(n,alpha,x,[incx,overwrite_x])
    
    Wrapper for ``clarfg``.
    
    Parameters
    ----------
    n : input int
    alpha : input complex
    x : input rank-1 array('F') with bounds (lx)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    alpha : complex
    x : rank-1 array('F') with bounds (lx)
    tau : complex
    """
    pass

def clartg(f, g): # real signature unknown; restored from __doc__
    """
    cs,sn,r = clartg(f,g)
    
    Wrapper for ``clartg``.
    
    Parameters
    ----------
    f : input complex
    g : input complex
    
    Returns
    -------
    cs : float
    sn : complex
    r : complex
    """
    pass

def claswp(a, piv, k1=None, k2=None, off=None, inc=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = claswp(a,piv,[k1,k2,off,inc,overwrite_a])
    
    Wrapper for ``claswp``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (nrows,n)
    piv : input rank-1 array('i') with bounds (npiv)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    k1 : input int, optional
        Default: 0
    k2 : input int, optional
        Default: npiv-1
    off : input int, optional
        Default: 0
    inc : input int, optional
        Default: 1
    
    Returns
    -------
    a : rank-2 array('F') with bounds (nrows,n)
    """
    pass

def clauum(c, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    a,info = clauum(c,[lower,overwrite_c])
    
    Wrapper for ``clauum``.
    
    Parameters
    ----------
    c : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (n,n) and c storage
    info : int
    """
    pass

def cpbsv(ab, b, lower=None, ldab=None, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    c,x,info = cpbsv(ab,b,[lower,ldab,overwrite_ab,overwrite_b])
    
    Wrapper for ``cpbsv``.
    
    Parameters
    ----------
    ab : input rank-2 array('F') with bounds (ldab,n)
    b : input rank-2 array('F') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (ldab,n) and ab storage
    x : rank-2 array('F') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def cpbtrf(ab, lower=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    c,info = cpbtrf(ab,[lower,ldab,overwrite_ab])
    
    Wrapper for ``cpbtrf``.
    
    Parameters
    ----------
    ab : input rank-2 array('F') with bounds (ldab,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    
    Returns
    -------
    c : rank-2 array('F') with bounds (ldab,n) and ab storage
    info : int
    """
    pass

def cpbtrs(ab, b, lower=None, ldab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = cpbtrs(ab,b,[lower,ldab,overwrite_b])
    
    Wrapper for ``cpbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('F') with bounds (ldab,n)
    b : input rank-2 array('F') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def cpftrf(n, a, transr=None, uplo=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    achol,info = cpftrf(n,a,[transr,uplo,overwrite_a])
    
    Wrapper for ``cpftrf``.
    
    Parameters
    ----------
    n : input int
    a : input rank-1 array('F') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    achol : rank-1 array('F') with bounds (nt) and a storage
    info : int
    """
    pass

def cpftri(n, a, transr=None, uplo=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ainv,info = cpftri(n,a,[transr,uplo,overwrite_a])
    
    Wrapper for ``cpftri``.
    
    Parameters
    ----------
    n : input int
    a : input rank-1 array('F') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    ainv : rank-1 array('F') with bounds (nt) and a storage
    info : int
    """
    pass

def cpftrs(n, a, b, transr=None, uplo=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = cpftrs(n,a,b,[transr,uplo,overwrite_b])
    
    Wrapper for ``cpftrs``.
    
    Parameters
    ----------
    n : input int
    a : input rank-1 array('F') with bounds (nt)
    b : input rank-2 array('F') with bounds (ldb,nhrs)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (ldb,nhrs) and b storage
    info : int
    """
    pass

def cpocon(a, anorm, uplo=None): # real signature unknown; restored from __doc__
    """
    rcond,info = cpocon(a,anorm,[uplo])
    
    Wrapper for ``cpocon``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    anorm : input float
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def cposv(a, b, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    c,x,info = cposv(a,b,[lower,overwrite_a,overwrite_b])
    
    Wrapper for ``cposv``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (n,n) and a storage
    x : rank-2 array('F') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def cposvx(a, b, fact=None, af=None, equed=None, s=None, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = cposvx(a,b,[fact,af,equed,s,lower,overwrite_a,overwrite_b])
    
    Wrapper for ``cposvx``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    fact : input string(len=1), optional
        Default: 'E'
    overwrite_a : input int, optional
        Default: 0
    af : input rank-2 array('F') with bounds (n,n)
    equed : input string(len=1), optional
        Default: 'Y'
    s : input rank-1 array('f') with bounds (n)
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    a_s : rank-2 array('F') with bounds (n,n) and a storage
    lu : rank-2 array('F') with bounds (n,n) and af storage
    equed : string(len=1)
    s : rank-1 array('f') with bounds (n)
    b_s : rank-2 array('F') with bounds (n,nrhs) and b storage
    x : rank-2 array('F') with bounds (n,nrhs)
    rcond : float
    ferr : rank-1 array('f') with bounds (nrhs)
    berr : rank-1 array('f') with bounds (nrhs)
    info : int
    """
    pass

def cpotrf(a, lower=None, clean=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,info = cpotrf(a,[lower,clean,overwrite_a])
    
    Wrapper for ``cpotrf``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    clean : input int, optional
        Default: 1
    
    Returns
    -------
    c : rank-2 array('F') with bounds (n,n) and a storage
    info : int
    """
    pass

def cpotri(c, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    inv_a,info = cpotri(c,[lower,overwrite_c])
    
    Wrapper for ``cpotri``.
    
    Parameters
    ----------
    c : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    inv_a : rank-2 array('F') with bounds (n,n) and c storage
    info : int
    """
    pass

def cpotrs(c, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = cpotrs(c,b,[lower,overwrite_b])
    
    Wrapper for ``cpotrs``.
    
    Parameters
    ----------
    c : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def cppcon(n, ap, anorm, lower=None): # real signature unknown; restored from __doc__
    """
    rcond,info = cppcon(n,ap,anorm,[lower])
    
    Wrapper for ``cppcon``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('F') with bounds (L)
    anorm : input float
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def cppsv(n, ap, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = cppsv(n,ap,b,[lower,overwrite_b])
    
    Wrapper for ``cppsv``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('F') with bounds (L)
    b : input rank-2 array('F') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def cpptrf(n, ap, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    ul,info = cpptrf(n,ap,[lower,overwrite_ap])
    
    Wrapper for ``cpptrf``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('F') with bounds (L)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    
    Returns
    -------
    ul : rank-1 array('F') with bounds (L) and ap storage
    info : int
    """
    pass

def cpptri(n, ap, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    uli,info = cpptri(n,ap,[lower,overwrite_ap])
    
    Wrapper for ``cpptri``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('F') with bounds (L)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    
    Returns
    -------
    uli : rank-1 array('F') with bounds (L) and ap storage
    info : int
    """
    pass

def cpptrs(n, ap, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = cpptrs(n,ap,b,[lower,overwrite_b])
    
    Wrapper for ``cpptrs``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('F') with bounds (L)
    b : input rank-2 array('F') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def cpstf2(a, tol=None, lower=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,piv,rank_c,info = cpstf2(a,[tol,lower,overwrite_a])
    
    Wrapper for ``cpstf2``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    tol : input float, optional
        Default: -1.0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (n,n) and a storage
    piv : rank-1 array('i') with bounds (n)
    rank_c : int
    info : int
    """
    pass

def cpstrf(a, tol=None, lower=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,piv,rank_c,info = cpstrf(a,[tol,lower,overwrite_a])
    
    Wrapper for ``cpstrf``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    tol : input float, optional
        Default: -1.0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('F') with bounds (n,n) and a storage
    piv : rank-1 array('i') with bounds (n)
    rank_c : int
    info : int
    """
    pass

def cpteqr(d, e, z, compute_z=None, overwrite_d=None, overwrite_e=None, overwrite_z=None): # real signature unknown; restored from __doc__
    """
    d,e,z,info = cpteqr(d,e,z,[compute_z,overwrite_d,overwrite_e,overwrite_z])
    
    Wrapper for ``cpteqr``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (n)
    e : input rank-1 array('f') with bounds ((n>0?n-1:0))
    z : input rank-2 array('F') with bounds ((compute_z==0?shape(z, 0):max(1,n)),(compute_z==0?shape(z, 1):n))
    
    Other Parameters
    ----------------
    compute_z : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    overwrite_z : input int, optional
        Default: 0
    
    Returns
    -------
    d : rank-1 array('f') with bounds (n)
    e : rank-1 array('f') with bounds ((n>0?n-1:0))
    z : rank-2 array('F') with bounds ((compute_z==0?shape(z, 0):max(1,n)),(compute_z==0?shape(z, 1):n))
    info : int
    """
    pass

def cptsv(d, e, b, overwrite_d=None, overwrite_e=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    d,du,x,info = cptsv(d,e,b,[overwrite_d,overwrite_e,overwrite_b])
    
    Wrapper for ``cptsv``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (n)
    e : input rank-1 array('F') with bounds (n - 1)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    d : rank-1 array('f') with bounds (n)
    du : rank-1 array('F') with bounds (n - 1) and e storage
    x : rank-2 array('F') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def cptsvx(d, e, b, fact=None, df=None, ef=None): # real signature unknown; restored from __doc__
    """
    df,ef,x,rcond,ferr,berr,info = cptsvx(d,e,b,[fact,df,ef])
    
    Wrapper for ``cptsvx``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (n)
    e : input rank-1 array('F') with bounds (max(0, n-1))
    b : input rank-2 array('F') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    fact : input string(len=1), optional
        Default: 'N'
    df : input rank-1 array('f') with bounds (n)
    ef : input rank-1 array('F') with bounds (max(0, n-1))
    
    Returns
    -------
    df : rank-1 array('f') with bounds (n)
    ef : rank-1 array('F') with bounds (max(0, n-1))
    x : rank-2 array('F') with bounds (ldx,nrhs)
    rcond : float
    ferr : rank-1 array('f') with bounds (nrhs)
    berr : rank-1 array('f') with bounds (nrhs)
    info : int
    """
    pass

def cpttrf(d, e, overwrite_d=None, overwrite_e=None): # real signature unknown; restored from __doc__
    """
    d,e,info = cpttrf(d,e,[overwrite_d,overwrite_e])
    
    Wrapper for ``cpttrf``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (n)
    e : input rank-1 array('F') with bounds ((n>0?n-1:0))
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    
    Returns
    -------
    d : rank-1 array('f') with bounds (n)
    e : rank-1 array('F') with bounds ((n>0?n-1:0))
    info : int
    """
    pass

def cpttrs(d, e, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = cpttrs(d,e,b,[lower,overwrite_b])
    
    Wrapper for ``cpttrs``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (n)
    e : input rank-1 array('F') with bounds ((n>0?n-1:0))
    b : input rank-2 array('F') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def crot(x, y, c, s, n=None, offx=None, incx=None, offy=None, incy=None, overwrite_x=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    x,y = crot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])
    
    Wrapper for ``crot``.
    
    Parameters
    ----------
    x : input rank-1 array('F') with bounds (lx)
    y : input rank-1 array('F') with bounds (ly)
    c : input float
    s : input complex
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (lx-1-offx)/abs(incx)+1
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 0
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('F') with bounds (lx)
    y : rank-1 array('F') with bounds (ly)
    """
    pass

def csycon(a, ipiv, anorm, lower=None): # real signature unknown; restored from __doc__
    """
    rcond,info = csycon(a,ipiv,anorm,[lower])
    
    Wrapper for ``csycon``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    anorm : input float
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def csyconv(a, ipiv, lower=None, way=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a,e,info = csyconv(a,ipiv,[lower,way,overwrite_a])
    
    Wrapper for ``csyconv``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    way : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (n,n)
    e : rank-1 array('F') with bounds (n)
    info : int
    """
    pass

def csyequb(a, lower=None): # real signature unknown; restored from __doc__
    """
    s,scond,amax,info = csyequb(a,[lower])
    
    Wrapper for ``csyequb``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (lda,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    s : rank-1 array('f') with bounds (n)
    scond : float
    amax : float
    info : int
    """
    pass

def csysv(a, b, lwork=None, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    udut,ipiv,x,info = csysv(a,b,[lwork,lower,overwrite_a,overwrite_b])
    
    Wrapper for ``csysv``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(n,1)
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    udut : rank-2 array('F') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    x : rank-2 array('F') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def csysvx(a, b, af=None, ipiv=None, lwork=None, factored=None, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = csysvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])
    
    Wrapper for ``csysvx``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    af : input rank-2 array('F') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    factored : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    a_s : rank-2 array('F') with bounds (n,n) and a storage
    udut : rank-2 array('F') with bounds (n,n) and af storage
    ipiv : rank-1 array('i') with bounds (n)
    b_s : rank-2 array('F') with bounds (n,nrhs) and b storage
    x : rank-2 array('F') with bounds (n,nrhs)
    rcond : float
    ferr : rank-1 array('f') with bounds (nrhs)
    berr : rank-1 array('f') with bounds (nrhs)
    info : int
    """
    pass

def csysvx_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = csysvx_lwork(n,[lower])
    
    Wrapper for ``csysvx_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def csysv_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = csysv_lwork(n,[lower])
    
    Wrapper for ``csysv_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def csytf2(a, lower=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ldu,ipiv,info = csytf2(a,[lower,overwrite_a])
    
    Wrapper for ``csytf2``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    ldu : rank-2 array('F') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def csytrf(a, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ldu,ipiv,info = csytrf(a,[lower,lwork,overwrite_a])
    
    Wrapper for ``csytrf``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(n,1)
    
    Returns
    -------
    ldu : rank-2 array('F') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def csytrf_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = csytrf_lwork(n,[lower])
    
    Wrapper for ``csytrf_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def ctbtrs(ab, b, uplo=None, trans=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = ctbtrs(ab,b,[uplo,trans,diag,overwrite_b])
    
    Wrapper for ``ctbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('F') with bounds (ldab,n)
    b : input rank-2 array('F') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'U'
    trans : input string(len=1), optional
        Default: 'N'
    diag : input string(len=1), optional
        Default: 'N'
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def ctfsm(alpha, a, b, transr=None, side=None, uplo=None, trans=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x = ctfsm(alpha,a,b,[transr,side,uplo,trans,diag,overwrite_b])
    
    Wrapper for ``ctfsm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-1 array('F') with bounds (nt)
    b : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    side : input string(len=1), optional
        Default: 'L'
    uplo : input string(len=1), optional
        Default: 'U'
    trans : input string(len=1), optional
        Default: 'N'
    diag : input string(len=1), optional
        Default: 'N'
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (m,n) and b storage
    """
    pass

def ctfttp(n, arf, transr=None, uplo=None): # real signature unknown; restored from __doc__
    """
    ap,info = ctfttp(n,arf,[transr,uplo])
    
    Wrapper for ``ctfttp``.
    
    Parameters
    ----------
    n : input int
    arf : input rank-1 array('F') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    ap : rank-1 array('F') with bounds (nt)
    info : int
    """
    pass

def ctfttr(n, arf, transr=None, uplo=None): # real signature unknown; restored from __doc__
    """
    a,info = ctfttr(n,arf,[transr,uplo])
    
    Wrapper for ``ctfttr``.
    
    Parameters
    ----------
    n : input int
    arf : input rank-1 array('F') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    a : rank-2 array('F') with bounds (lda,n)
    info : int
    """
    pass

def ctgexc(a, b, q, z, ifst, ilst, wantq=None, wantz=None, overwrite_a=None, overwrite_b=None, overwrite_q=None, overwrite_z=None): # real signature unknown; restored from __doc__
    """
    a,b,q,z,info = ctgexc(a,b,q,z,ifst,ilst,[wantq,wantz,overwrite_a,overwrite_b,overwrite_q,overwrite_z])
    
    Wrapper for ``ctgexc``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (lda,n)
    b : input rank-2 array('F') with bounds (ldb,n)
    q : input rank-2 array('F') with bounds (ldq,n)
    z : input rank-2 array('F') with bounds (ldz,n)
    ifst : input int
    ilst : input int
    
    Other Parameters
    ----------------
    wantq : input int, optional
        Default: 1
    wantz : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    overwrite_z : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (lda,n)
    b : rank-2 array('F') with bounds (ldb,n)
    q : rank-2 array('F') with bounds (ldq,n)
    z : rank-2 array('F') with bounds (ldz,n)
    info : int
    """
    pass

def ctgsen(select, a, b, q, z, ijob=None, wantq=None, wantz=None, lwork=None, liwork=None, overwrite_a=None, overwrite_b=None, overwrite_q=None, overwrite_z=None): # real signature unknown; restored from __doc__
    """
    as,bs,alpha,beta,qs,zs,m,pl,pr,dif,info = ctgsen(select,a,b,q,z,[ijob,wantq,wantz,lwork,liwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])
    
    Wrapper for ``ctgsen``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,n)
    q : input rank-2 array('F') with bounds (n,n)
    z : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    ijob : input int, optional
        Default: 4
    wantq : input int, optional
        Default: 1
    wantz : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    overwrite_z : input int, optional
        Default: 0
    lwork : input int, optional
        Default: (ijob==0?1:n+2)
    liwork : input int, optional
        Default: (ijob==0?1:n+2)
    
    Returns
    -------
    as : rank-2 array('F') with bounds (n,n) and a storage
    bs : rank-2 array('F') with bounds (n,n) and b storage
    alpha : rank-1 array('F') with bounds (n)
    beta : rank-1 array('F') with bounds (n)
    qs : rank-2 array('F') with bounds (n,n) and q storage
    zs : rank-2 array('F') with bounds (n,n) and z storage
    m : int
    pl : float
    pr : float
    dif : rank-1 array('f') with bounds (2)
    info : int
    """
    pass

def ctgsen_lwork(select, a, b, ijob=None): # real signature unknown; restored from __doc__
    """
    work,iwork,info = ctgsen_lwork(select,a,b,[ijob])
    
    Wrapper for ``ctgsen_lwork``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    ijob : input int, optional
        Default: 4
    
    Returns
    -------
    work : complex
    iwork : int
    info : int
    """
    pass

def ctpmqrt(l, v, t, a, b, side=None, trans=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,b,info = ctpmqrt(l,v,t,a,b,[side,trans,overwrite_a,overwrite_b])
    
    Wrapper for ``ctpmqrt``.
    
    Parameters
    ----------
    l : input int
    v : input rank-2 array('F') with bounds ((side[0]=='L'?m:n),k)
    t : input rank-2 array('F') with bounds (nb,k)
    a : input rank-2 array('F') with bounds ((side[0]=='L'?k:m),(side[0]=='L'?n:k))
    b : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds ((side[0]=='L'?k:m),(side[0]=='L'?n:k))
    b : rank-2 array('F') with bounds (m,n)
    info : int
    """
    pass

def ctpqrt(l, nb, a, b, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,b,t,info = ctpqrt(l,nb,a,b,[overwrite_a,overwrite_b])
    
    Wrapper for ``ctpqrt``.
    
    Parameters
    ----------
    l : input int
    nb : input int
    a : input rank-2 array('F') with bounds (n,n)
    b : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (n,n)
    b : rank-2 array('F') with bounds (m,n)
    t : rank-2 array('F') with bounds (nb,n)
    info : int
    """
    pass

def ctpttf(n, ap, transr=None, uplo=None): # real signature unknown; restored from __doc__
    """
    arf,info = ctpttf(n,ap,[transr,uplo])
    
    Wrapper for ``ctpttf``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('F') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    arf : rank-1 array('F') with bounds (nt)
    info : int
    """
    pass

def ctpttr(n, ap, uplo=None): # real signature unknown; restored from __doc__
    """
    a,info = ctpttr(n,ap,[uplo])
    
    Wrapper for ``ctpttr``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('F') with bounds (nt)
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    a : rank-2 array('F') with bounds (n,n)
    info : int
    """
    pass

def ctrexc(a, q, ifst, ilst, wantq=None, overwrite_a=None, overwrite_q=None): # real signature unknown; restored from __doc__
    """
    a,q,info = ctrexc(a,q,ifst,ilst,[wantq,overwrite_a,overwrite_q])
    
    Wrapper for ``ctrexc``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (lda,n)
    q : input rank-2 array('F') with bounds (ldq,n)
    ifst : input int
    ilst : input int
    
    Other Parameters
    ----------------
    wantq : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('F') with bounds (lda,n)
    q : rank-2 array('F') with bounds (ldq,n)
    info : int
    """
    pass

def ctrsen(select, t, q, job=None, wantq=None, lwork=None, overwrite_t=None, overwrite_q=None): # real signature unknown; restored from __doc__
    """
    ts,qs,w,m,s,sep,info = ctrsen(select,t,q,[job,wantq,lwork,overwrite_t,overwrite_q])
    
    Wrapper for ``ctrsen``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    t : input rank-2 array('F') with bounds (n,n)
    q : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    job : input string(len=1), optional
        Default: 'B'
    wantq : input int, optional
        Default: 1
    overwrite_t : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(1,n)
    
    Returns
    -------
    ts : rank-2 array('F') with bounds (n,n) and t storage
    qs : rank-2 array('F') with bounds (n,n) and q storage
    w : rank-1 array('F') with bounds (n)
    m : int
    s : float
    sep : float
    info : int
    """
    pass

def ctrsen_lwork(select, t, job=None): # real signature unknown; restored from __doc__
    """
    work,info = ctrsen_lwork(select,t,[job])
    
    Wrapper for ``ctrsen_lwork``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    t : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    job : input string(len=1), optional
        Default: 'B'
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def ctrsyl(a, b, c, trana=None, tranb=None, isgn=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    x,scale,info = ctrsyl(a,b,c,[trana,tranb,isgn,overwrite_c])
    
    Wrapper for ``ctrsyl``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,m)
    b : input rank-2 array('F') with bounds (n,n)
    c : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    trana : input string(len=1), optional
        Default: 'N'
    tranb : input string(len=1), optional
        Default: 'N'
    isgn : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (m,n) and c storage
    scale : float
    info : int
    """
    pass

def ctrtri(c, lower=None, unitdiag=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    inv_c,info = ctrtri(c,[lower,unitdiag,overwrite_c])
    
    Wrapper for ``ctrtri``.
    
    Parameters
    ----------
    c : input rank-2 array('F') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    
    Returns
    -------
    inv_c : rank-2 array('F') with bounds (n,n) and c storage
    info : int
    """
    pass

def ctrtrs(a, b, lower=None, trans=None, unitdiag=None, lda=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = ctrtrs(a,b,[lower,trans,unitdiag,lda,overwrite_b])
    
    Wrapper for ``ctrtrs``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (lda,n)
    b : input rank-2 array('F') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    lda : input int, optional
        Default: shape(a,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('F') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def ctrttf(a, transr=None, uplo=None): # real signature unknown; restored from __doc__
    """
    arf,info = ctrttf(a,[transr,uplo])
    
    Wrapper for ``ctrttf``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (lda,n)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    arf : rank-1 array('F') with bounds (n*(n+1)/2)
    info : int
    """
    pass

def ctrttp(a, uplo=None): # real signature unknown; restored from __doc__
    """
    ap,info = ctrttp(a,[uplo])
    
    Wrapper for ``ctrttp``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (lda,n)
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    ap : rank-1 array('F') with bounds (n*(n+1)/2)
    info : int
    """
    pass

def ctzrzf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    rz,tau,info = ctzrzf(a,[lwork,overwrite_a])
    
    Wrapper for ``ctzrzf``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(m,1)
    
    Returns
    -------
    rz : rank-2 array('F') with bounds (m,n) and a storage
    tau : rank-1 array('F') with bounds (m)
    info : int
    """
    pass

def ctzrzf_lwork(m, n): # real signature unknown; restored from __doc__
    """
    work,info = ctzrzf_lwork(m,n)
    
    Wrapper for ``ctzrzf_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cuncsd(x11, x12, x21, x22, compute_u1=None, compute_u2=None, compute_v1t=None, compute_v2t=None, trans=None, signs=None, lwork=None, lrwork=None, overwrite_x11=None, overwrite_x12=None, overwrite_x21=None, overwrite_x22=None): # real signature unknown; restored from __doc__
    """
    cs11,cs12,cs21,cs22,theta,u1,u2,v1t,v2t,info = cuncsd(x11,x12,x21,x22,[compute_u1,compute_u2,compute_v1t,compute_v2t,trans,signs,lwork,lrwork,overwrite_x11,overwrite_x12,overwrite_x21,overwrite_x22])
    
    Wrapper for ``cuncsd``.
    
    Parameters
    ----------
    x11 : input rank-2 array('F') with bounds (p,q)
    x12 : input rank-2 array('F') with bounds (p,mmq)
    x21 : input rank-2 array('F') with bounds (mmp,q)
    x22 : input rank-2 array('F') with bounds (mmp,mmq)
    
    Other Parameters
    ----------------
    compute_u1 : input int, optional
        Default: 1
    compute_u2 : input int, optional
        Default: 1
    compute_v1t : input int, optional
        Default: 1
    compute_v2t : input int, optional
        Default: 1
    trans : input int, optional
        Default: 0
    signs : input int, optional
        Default: 0
    overwrite_x11 : input int, optional
        Default: 0
    overwrite_x12 : input int, optional
        Default: 0
    overwrite_x21 : input int, optional
        Default: 0
    overwrite_x22 : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 2*m+MAX(1,MAX(mmp,mmq))+1
    lrwork : input int, optional
        Default: 5*MAX(1,q-1)+4*MAX(1,q)+8*q+1
    
    Returns
    -------
    cs11 : rank-2 array('F') with bounds (p,q) and x11 storage
    cs12 : rank-2 array('F') with bounds (p,mmq) and x12 storage
    cs21 : rank-2 array('F') with bounds (mmp,q) and x21 storage
    cs22 : rank-2 array('F') with bounds (mmp,mmq) and x22 storage
    theta : rank-1 array('f') with bounds (min(min(p,mmp),min(q,mmq)))
    u1 : rank-2 array('F') with bounds ((compute_u1?p:0),(compute_u1?p:0))
    u2 : rank-2 array('F') with bounds ((compute_u2?mmp:0),(compute_u2?mmp:0))
    v1t : rank-2 array('F') with bounds ((compute_v1t?q:0),(compute_v1t?q:0))
    v2t : rank-2 array('F') with bounds ((compute_v2t?mmq:0),(compute_v2t?mmq:0))
    info : int
    """
    pass

def cuncsd_lwork(m, p, q): # real signature unknown; restored from __doc__
    """
    work,rwork,info = cuncsd_lwork(m,p,q)
    
    Wrapper for ``cuncsd_lwork``.
    
    Parameters
    ----------
    m : input int
    p : input int
    q : input int
    
    Returns
    -------
    work : complex
    rwork : float
    info : int
    """
    pass

def cunghr(a, tau, lo=None, hi=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ht,info = cunghr(a,tau,[lo,hi,lwork,overwrite_a])
    
    Wrapper for ``cunghr``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (n,n)
    tau : input rank-1 array('F') with bounds (n - 1)
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(hi-lo,1)
    
    Returns
    -------
    ht : rank-2 array('F') with bounds (n,n) and a storage
    info : int
    """
    pass

def cunghr_lwork(n, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    work,info = cunghr_lwork(n,[lo,hi])
    
    Wrapper for ``cunghr_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def cungqr(a, tau, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    q,work,info = cungqr(a,tau,[lwork,overwrite_a])
    
    Wrapper for ``cungqr``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    tau : input rank-1 array('F') with bounds (k)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    
    Returns
    -------
    q : rank-2 array('F') with bounds (m,n) and a storage
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def cungrq(a, tau, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    q,work,info = cungrq(a,tau,[lwork,overwrite_a])
    
    Wrapper for ``cungrq``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (m,n)
    tau : input rank-1 array('F') with bounds (k)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*m,1)
    
    Returns
    -------
    q : rank-2 array('F') with bounds (m,n) and a storage
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def cunmqr(side, trans, a, tau, c, lwork, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    cq,work,info = cunmqr(side,trans,a,tau,c,lwork,[overwrite_c])
    
    Wrapper for ``cunmqr``.
    
    Parameters
    ----------
    side : input string(len=1)
    trans : input string(len=1)
    a : input rank-2 array('F') with bounds (lda,k)
    tau : input rank-1 array('F') with bounds (k)
    c : input rank-2 array('F') with bounds (ldc,n)
    lwork : input int
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    cq : rank-2 array('F') with bounds (ldc,n) and c storage
    work : rank-1 array('F') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def cunmrz(a, tau, c, side=None, trans=None, lwork=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    cq,info = cunmrz(a,tau,c,[side,trans,lwork,overwrite_c])
    
    Wrapper for ``cunmrz``.
    
    Parameters
    ----------
    a : input rank-2 array('F') with bounds (k,nt)
    tau : input rank-1 array('F') with bounds (k)
    c : input rank-2 array('F') with bounds (m,n)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_c : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX((side[0]=='L'?n:m),1)
    
    Returns
    -------
    cq : rank-2 array('F') with bounds (m,n) and c storage
    info : int
    """
    pass

def cunmrz_lwork(m, n, side=None, trans=None): # real signature unknown; restored from __doc__
    """
    work,info = cunmrz_lwork(m,n,[side,trans])
    
    Wrapper for ``cunmrz_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    trans : input string(len=1), optional
        Default: 'N'
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def dgbsv(kl, ku, ab, b, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lub,piv,x,info = dgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])
    
    Wrapper for ``dgbsv``.
    
    Parameters
    ----------
    kl : input int
    ku : input int
    ab : input rank-2 array('d') with bounds (2*kl+ku+1,n)
    b : input rank-2 array('d') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lub : rank-2 array('d') with bounds (2*kl+ku+1,n) and ab storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('d') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def dgbtrf(ab, kl, ku, m=None, n=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    lu,ipiv,info = dgbtrf(ab,kl,ku,[m,n,ldab,overwrite_ab])
    
    Wrapper for ``dgbtrf``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,n)
    kl : input int
    ku : input int
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(ab,1)
    n : input int, optional
        Default: shape(ab,1)
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: max(shape(ab,0),1)
    
    Returns
    -------
    lu : rank-2 array('d') with bounds (ldab,n) and ab storage
    ipiv : rank-1 array('i') with bounds (MIN(m,n))
    info : int
    """
    pass

def dgbtrs(ab, kl, ku, b, ipiv, trans=None, n=None, ldab=None, ldb=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = dgbtrs(ab,kl,ku,b,ipiv,[trans,n,ldab,ldb,overwrite_b])
    
    Wrapper for ``dgbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,n)
    kl : input int
    ku : input int
    b : input rank-2 array('d') with bounds (ldb,nrhs)
    ipiv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    n : input int, optional
        Default: shape(ab,1)
    ldab : input int, optional
        Default: shape(ab,0)
    ldb : input int, optional
        Default: shape(b,0)
    
    Returns
    -------
    x : rank-2 array('d') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def dgebal(a, scale=None, permute=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ba,lo,hi,pivscale,info = dgebal(a,[scale,permute,overwrite_a])
    
    Wrapper for ``dgebal``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    scale : input int, optional
        Default: 0
    permute : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    ba : rank-2 array('d') with bounds (m,n) and a storage
    lo : int
    hi : int
    pivscale : rank-1 array('d') with bounds (n)
    info : int
    """
    pass

def dgecon(a, anorm, norm=None): # real signature unknown; restored from __doc__
    """
    rcond,info = dgecon(a,anorm,[norm])
    
    Wrapper for ``dgecon``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    anorm : input float
    
    Other Parameters
    ----------------
    norm : input string(len=1), optional
        Default: '1'
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def dgeequ(a): # real signature unknown; restored from __doc__
    """
    r,c,rowcnd,colcnd,amax,info = dgeequ(a)
    
    Wrapper for ``dgeequ``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Returns
    -------
    r : rank-1 array('d') with bounds (m)
    c : rank-1 array('d') with bounds (n)
    rowcnd : float
    colcnd : float
    amax : float
    info : int
    """
    pass

def dgeequb(a): # real signature unknown; restored from __doc__
    """
    r,c,rowcnd,colcnd,amax,info = dgeequb(a)
    
    Wrapper for ``dgeequb``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Returns
    -------
    r : rank-1 array('d') with bounds (m)
    c : rank-1 array('d') with bounds (n)
    rowcnd : float
    colcnd : float
    amax : float
    info : int
    """
    pass

def dgees(dselect, a, compute_v=None, sort_t=None, lwork=None, dselect_extra_args=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    t,sdim,wr,wi,vs,work,info = dgees(dselect,a,[compute_v,sort_t,lwork,dselect_extra_args,overwrite_a])
    
    Wrapper for ``dgees``.
    
    Parameters
    ----------
    dselect : call-back function
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    sort_t : input int, optional
        Default: 0
    dselect_extra_args : input tuple, optional
        Default: ()
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    
    Returns
    -------
    t : rank-2 array('d') with bounds (n,n) and a storage
    sdim : int
    wr : rank-1 array('d') with bounds (n)
    wi : rank-1 array('d') with bounds (n)
    vs : rank-2 array('d') with bounds (ldvs,n)
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def dselect(arg1,arg2): return dselect
      Required arguments:
        arg1 : input float
        arg2 : input float
      Return objects:
        dselect : int
    """
    pass

def dgeev(a, compute_vl=None, compute_vr=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    wr,wi,vl,vr,info = dgeev(a,[compute_vl,compute_vr,lwork,overwrite_a])
    
    Wrapper for ``dgeev``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(4*n,1)
    
    Returns
    -------
    wr : rank-1 array('d') with bounds (n)
    wi : rank-1 array('d') with bounds (n)
    vl : rank-2 array('d') with bounds (ldvl,n)
    vr : rank-2 array('d') with bounds (ldvr,n)
    info : int
    """
    pass

def dgeev_lwork(n, compute_vl=None, compute_vr=None): # real signature unknown; restored from __doc__
    """
    work,info = dgeev_lwork(n,[compute_vl,compute_vr])
    
    Wrapper for ``dgeev_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgehrd(a, lo=None, hi=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ht,tau,info = dgehrd(a,[lo,hi,lwork,overwrite_a])
    
    Wrapper for ``dgehrd``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(n,1)
    
    Returns
    -------
    ht : rank-2 array('d') with bounds (n,n) and a storage
    tau : rank-1 array('d') with bounds (n - 1)
    info : int
    """
    pass

def dgehrd_lwork(n, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    work,info = dgehrd_lwork(n,[lo,hi])
    
    Wrapper for ``dgehrd_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgejsv(a, joba=None, jobu=None, jobv=None, jobr=None, jobt=None, jobp=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    sva,u,v,workout,iworkout,info = dgejsv(a,[joba,jobu,jobv,jobr,jobt,jobp,lwork,overwrite_a])
    
    Wrapper for ``dgejsv``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (lda,n)
    
    Other Parameters
    ----------------
    joba : input int, optional
        Default: 4
    jobu : input int, optional
        Default: 0
    jobv : input int, optional
        Default: 0
    jobr : input int, optional
        Default: 1
    jobt : input int, optional
        Default: 0
    jobp : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(6*n+2*n*n, max(2*m+n, max(4*n+n*n, max(2*n+n*n+6, 7))))
    
    Returns
    -------
    sva : rank-1 array('d') with bounds (n)
    u : rank-2 array('d') with bounds (((jobt == 0)&&(jobu == 3)?0:m),((jobt == 0)&&(jobu == 3)?0:(jobu == 1?m:n)))
    v : rank-2 array('d') with bounds (((jobt == 0)&&(jobv == 3)?0:ldv),((jobt == 0)&&(jobv == 3)?0:n))
    workout : rank-1 array('d') with bounds (7)
    iworkout : rank-1 array('i') with bounds (3)
    info : int
    """
    pass

def dgels(a, b, trans=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lqr,x,info = dgels(a,b,[trans,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``dgels``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    b : input rank-2 array('d') with bounds (MAX(m,n),nrhs)
    
    Other Parameters
    ----------------
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(MIN(m,n)+MAX(MIN(m,n),nrhs),1)
    
    Returns
    -------
    lqr : rank-2 array('d') with bounds (m,n) and a storage
    x : rank-2 array('d') with bounds (MAX(m,n),nrhs) and b storage
    info : int
    """
    pass

def dgelsd(a, b, lwork, size_iwork, cond=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,s,rank,info = dgelsd(a,b,lwork,size_iwork,[cond,overwrite_a,overwrite_b])
    
    Wrapper for ``dgelsd``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    b : input rank-2 array('d') with bounds (maxmn,nrhs)
    lwork : input int
    size_iwork : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    cond : input float, optional
        Default: -1.0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (maxmn,nrhs) and b storage
    s : rank-1 array('d') with bounds (minmn)
    rank : int
    info : int
    """
    pass

def dgelsd_lwork(m, n, nrhs, cond=None, lwork=None): # real signature unknown; restored from __doc__
    """
    work,iwork,info = dgelsd_lwork(m,n,nrhs,[cond,lwork])
    
    Wrapper for ``dgelsd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : float
    iwork : int
    info : int
    """
    pass

def dgelss(a, b, cond=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    v,x,s,rank,work,info = dgelss(a,b,[cond,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``dgelss``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    b : input rank-2 array('d') with bounds (maxmn,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: max(3*minmn+MAX(2*minmn,MAX(maxmn,nrhs)),1)
    
    Returns
    -------
    v : rank-2 array('d') with bounds (m,n) and a storage
    x : rank-2 array('d') with bounds (maxmn,nrhs) and b storage
    s : rank-1 array('d') with bounds (minmn)
    rank : int
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dgelss_lwork(m, n, nrhs, cond=None, lwork=None): # real signature unknown; restored from __doc__
    """
    work,info = dgelss_lwork(m,n,nrhs,[cond,lwork])
    
    Wrapper for ``dgelss_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgelsy(a, b, jptv, cond, lwork, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    v,x,j,rank,info = dgelsy(a,b,jptv,cond,lwork,[overwrite_a,overwrite_b])
    
    Wrapper for ``dgelsy``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    b : input rank-2 array('d') with bounds (maxmn,nrhs)
    jptv : input rank-1 array('i') with bounds (n)
    cond : input float
    lwork : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    v : rank-2 array('d') with bounds (m,n) and a storage
    x : rank-2 array('d') with bounds (maxmn,nrhs) and b storage
    j : rank-1 array('i') with bounds (n) and jptv storage
    rank : int
    info : int
    """
    pass

def dgelsy_lwork(m, n, nrhs, cond, lwork=None): # real signature unknown; restored from __doc__
    """
    work,info = dgelsy_lwork(m,n,nrhs,cond,[lwork])
    
    Wrapper for ``dgelsy_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    cond : input float
    
    Other Parameters
    ----------------
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgels_lwork(m, n, nrhs, trans=None): # real signature unknown; restored from __doc__
    """
    work,info = dgels_lwork(m,n,nrhs,[trans])
    
    Wrapper for ``dgels_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    trans : input string(len=1), optional
        Default: 'N'
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgemqrt(v, t, c, side=None, trans=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c,info = dgemqrt(v,t,c,[side,trans,overwrite_c])
    
    Wrapper for ``dgemqrt``.
    
    Parameters
    ----------
    v : input rank-2 array('d') with bounds ((side[0]=='L'?m:n),k)
    t : input rank-2 array('d') with bounds (nb,k)
    c : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (m,n)
    info : int
    """
    pass

def dgeqp3(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,jpvt,tau,work,info = dgeqp3(a,[lwork,overwrite_a])
    
    Wrapper for ``dgeqp3``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*(n+1),1)
    
    Returns
    -------
    qr : rank-2 array('d') with bounds (m,n) and a storage
    jpvt : rank-1 array('i') with bounds (n)
    tau : rank-1 array('d') with bounds (MIN(m,n))
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dgeqrf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,work,info = dgeqrf(a,[lwork,overwrite_a])
    
    Wrapper for ``dgeqrf``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    
    Returns
    -------
    qr : rank-2 array('d') with bounds (m,n) and a storage
    tau : rank-1 array('d') with bounds (MIN(m,n))
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dgeqrfp(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,info = dgeqrfp(a,[lwork,overwrite_a])
    
    Wrapper for ``dgeqrfp``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(1, n)
    
    Returns
    -------
    qr : rank-2 array('d') with bounds (m,n) and a storage
    tau : rank-1 array('d') with bounds (MIN(m,n))
    info : int
    """
    pass

def dgeqrfp_lwork(m, n): # real signature unknown; restored from __doc__
    """
    work,info = dgeqrfp_lwork(m,n)
    
    Wrapper for ``dgeqrfp_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgeqrf_lwork(m, n): # real signature unknown; restored from __doc__
    """
    work,info = dgeqrf_lwork(m,n)
    
    Wrapper for ``dgeqrf_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgeqrt(nb, a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a,t,info = dgeqrt(nb,a,[overwrite_a])
    
    Wrapper for ``dgeqrt``.
    
    Parameters
    ----------
    nb : input int
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('d') with bounds (m,n)
    t : rank-2 array('d') with bounds (nb,MIN(m,n))
    info : int
    """
    pass

def dgerqf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,work,info = dgerqf(a,[lwork,overwrite_a])
    
    Wrapper for ``dgerqf``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*m,1)
    
    Returns
    -------
    qr : rank-2 array('d') with bounds (m,n) and a storage
    tau : rank-1 array('d') with bounds (MIN(m,n))
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dgesc2(lu, rhs, ipiv, jpiv, overwrite_rhs=None): # real signature unknown; restored from __doc__
    """
    x,scale = dgesc2(lu,rhs,ipiv,jpiv,[overwrite_rhs])
    
    Wrapper for ``dgesc2``.
    
    Parameters
    ----------
    lu : input rank-2 array('d') with bounds (n,n)
    rhs : input rank-1 array('d') with bounds (n)
    ipiv : input rank-1 array('i') with bounds (n)
    jpiv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_rhs : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-1 array('d') with bounds (n) and rhs storage
    scale : float
    """
    pass

def dgesdd(a, compute_uv=None, full_matrices=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    u,s,vt,info = dgesdd(a,[compute_uv,full_matrices,lwork,overwrite_a])
    
    Wrapper for ``dgesdd``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    lwork : input int, optional
        Default: max((compute_uv?4*minmn*minmn+MAX(m,n)+9*minmn:MAX(14*minmn+4,10*minmn+2+25*(25+8))+MAX(m,n)),1)
    
    Returns
    -------
    u : rank-2 array('d') with bounds (u0,u1)
    s : rank-1 array('d') with bounds (minmn)
    vt : rank-2 array('d') with bounds (vt0,vt1)
    info : int
    """
    pass

def dgesdd_lwork(m, n, compute_uv=None, full_matrices=None): # real signature unknown; restored from __doc__
    """
    work,info = dgesdd_lwork(m,n,[compute_uv,full_matrices])
    
    Wrapper for ``dgesdd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgesv(a, b, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lu,piv,x,info = dgesv(a,b,[overwrite_a,overwrite_b])
    
    Wrapper for ``dgesv``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('d') with bounds (n,n) and a storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('d') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def dgesvd(a, compute_uv=None, full_matrices=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    u,s,vt,info = dgesvd(a,[compute_uv,full_matrices,lwork,overwrite_a])
    
    Wrapper for ``dgesvd``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    lwork : input int, optional
        Default: max(MAX(3*minmn+MAX(m,n),5*minmn),1)
    
    Returns
    -------
    u : rank-2 array('d') with bounds (u0,u1)
    s : rank-1 array('d') with bounds (minmn)
    vt : rank-2 array('d') with bounds (vt0,vt1)
    info : int
    """
    pass

def dgesvd_lwork(m, n, compute_uv=None, full_matrices=None): # real signature unknown; restored from __doc__
    """
    work,info = dgesvd_lwork(m,n,[compute_uv,full_matrices])
    
    Wrapper for ``dgesvd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgesvx(a, b, fact=None, trans=None, af=None, ipiv=None, equed=None, r=None, c=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = dgesvx(a,b,[fact,trans,af,ipiv,equed,r,c,overwrite_a,overwrite_b])
    
    Wrapper for ``dgesvx``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    fact : input string(len=1), optional
        Default: 'E'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_a : input int, optional
        Default: 0
    af : input rank-2 array('d') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    equed : input string(len=1), optional
        Default: 'B'
    r : input rank-1 array('d') with bounds (n)
    c : input rank-1 array('d') with bounds (n)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    as : rank-2 array('d') with bounds (n,n) and a storage
    lu : rank-2 array('d') with bounds (n,n) and af storage
    ipiv : rank-1 array('i') with bounds (n)
    equed : string(len=1)
    rs : rank-1 array('d') with bounds (n) and r storage
    cs : rank-1 array('d') with bounds (n) and c storage
    bs : rank-2 array('d') with bounds (n,nrhs) and b storage
    x : rank-2 array('d') with bounds (n,nrhs)
    rcond : float
    ferr : rank-1 array('d') with bounds (nrhs)
    berr : rank-1 array('d') with bounds (nrhs)
    info : int
    """
    pass

def dgetc2(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    lu,ipiv,jpiv,info = dgetc2(a,[overwrite_a])
    
    Wrapper for ``dgetc2``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('d') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    jpiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def dgetrf(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    lu,piv,info = dgetrf(a,[overwrite_a])
    
    Wrapper for ``dgetrf``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('d') with bounds (m,n) and a storage
    piv : rank-1 array('i') with bounds (MIN(m,n))
    info : int
    """
    pass

def dgetri(lu, piv, lwork=None, overwrite_lu=None): # real signature unknown; restored from __doc__
    """
    inv_a,info = dgetri(lu,piv,[lwork,overwrite_lu])
    
    Wrapper for ``dgetri``.
    
    Parameters
    ----------
    lu : input rank-2 array('d') with bounds (n,n)
    piv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_lu : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    
    Returns
    -------
    inv_a : rank-2 array('d') with bounds (n,n) and lu storage
    info : int
    """
    pass

def dgetri_lwork(n): # real signature unknown; restored from __doc__
    """
    work,info = dgetri_lwork(n)
    
    Wrapper for ``dgetri_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgetrs(lu, piv, b, trans=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = dgetrs(lu,piv,b,[trans,overwrite_b])
    
    Wrapper for ``dgetrs``.
    
    Parameters
    ----------
    lu : input rank-2 array('d') with bounds (n,n)
    piv : input rank-1 array('i') with bounds (n)
    b : input rank-2 array('d') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def dgges(dselect, a, b, jobvsl=None, jobvsr=None, sort_t=None, ldvsl=None, ldvsr=None, lwork=None, dselect_extra_args=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,b,sdim,alphar,alphai,beta,vsl,vsr,work,info = dgges(dselect,a,b,[jobvsl,jobvsr,sort_t,ldvsl,ldvsr,lwork,dselect_extra_args,overwrite_a,overwrite_b])
    
    Wrapper for ``dgges``.
    
    Parameters
    ----------
    dselect : call-back function
    a : input rank-2 array('d') with bounds (lda,n)
    b : input rank-2 array('d') with bounds (ldb,n)
    
    Other Parameters
    ----------------
    jobvsl : input int, optional
        Default: 1
    jobvsr : input int, optional
        Default: 1
    sort_t : input int, optional
        Default: 0
    dselect_extra_args : input tuple, optional
        Default: ()
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    ldvsl : input int, optional
        Default: ((jobvsl==1)?n:1)
    ldvsr : input int, optional
        Default: ((jobvsr==1)?n:1)
    lwork : input int, optional
        Default: max(8*n+16,1)
    
    Returns
    -------
    a : rank-2 array('d') with bounds (lda,n)
    b : rank-2 array('d') with bounds (ldb,n)
    sdim : int
    alphar : rank-1 array('d') with bounds (n)
    alphai : rank-1 array('d') with bounds (n)
    beta : rank-1 array('d') with bounds (n)
    vsl : rank-2 array('d') with bounds (ldvsl,n)
    vsr : rank-2 array('d') with bounds (ldvsr,n)
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def dselect(alphar,alphai,beta): return dselect
      Required arguments:
        alphar : input float
        alphai : input float
        beta : input float
      Return objects:
        dselect : int
    """
    pass

def dggev(a, b, compute_vl=None, compute_vr=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    alphar,alphai,beta,vl,vr,work,info = dggev(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``dggev``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(8*n,1)
    
    Returns
    -------
    alphar : rank-1 array('d') with bounds (n)
    alphai : rank-1 array('d') with bounds (n)
    beta : rank-1 array('d') with bounds (n)
    vl : rank-2 array('d') with bounds (ldvl,n)
    vr : rank-2 array('d') with bounds (ldvr,n)
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dgglse(a, b, c, d, lwork=None, overwrite_a=None, overwrite_b=None, overwrite_c=None, overwrite_d=None): # real signature unknown; restored from __doc__
    """
    t,r,res,x,info = dgglse(a,b,c,d,[lwork,overwrite_a,overwrite_b,overwrite_c,overwrite_d])
    
    Wrapper for ``dgglse``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    b : input rank-2 array('d') with bounds (p,n)
    c : input rank-1 array('d') with bounds (m)
    d : input rank-1 array('d') with bounds (p)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    overwrite_c : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(m+n+p,1)
    
    Returns
    -------
    t : rank-2 array('d') with bounds (m,n) and a storage
    r : rank-2 array('d') with bounds (p,n) and b storage
    res : rank-1 array('d') with bounds (m) and c storage
    x : rank-1 array('d') with bounds (n)
    info : int
    """
    pass

def dgglse_lwork(m, n, p): # real signature unknown; restored from __doc__
    """
    work,info = dgglse_lwork(m,n,p)
    
    Wrapper for ``dgglse_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    p : input int
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dgtsv(dl, d, du, b, overwrite_dl=None, overwrite_d=None, overwrite_du=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    du2,d,du,x,info = dgtsv(dl,d,du,b,[overwrite_dl,overwrite_d,overwrite_du,overwrite_b])
    
    Wrapper for ``dgtsv``.
    
    Parameters
    ----------
    dl : input rank-1 array('d') with bounds (n - 1)
    d : input rank-1 array('d') with bounds (n)
    du : input rank-1 array('d') with bounds (n - 1)
    b : input rank-2 array('d') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_dl : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    overwrite_du : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    du2 : rank-1 array('d') with bounds (n - 1) and dl storage
    d : rank-1 array('d') with bounds (n)
    du : rank-1 array('d') with bounds (n - 1)
    x : rank-2 array('d') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def dgtsvx(dl, d, du, b, fact=None, trans=None, dlf=None, df=None, duf=None, du2=None, ipiv=None): # real signature unknown; restored from __doc__
    """
    dlf,df,duf,du2,ipiv,x,rcond,ferr,berr,info = dgtsvx(dl,d,du,b,[fact,trans,dlf,df,duf,du2,ipiv])
    
    Wrapper for ``dgtsvx``.
    
    Parameters
    ----------
    dl : input rank-1 array('d') with bounds (MAX(0, n-1))
    d : input rank-1 array('d') with bounds (n)
    du : input rank-1 array('d') with bounds (MAX(0, n-1))
    b : input rank-2 array('d') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    fact : input string(len=1), optional
        Default: 'N'
    trans : input string(len=1), optional
        Default: 'N'
    dlf : input rank-1 array('d') with bounds (MAX(0,n-1))
    df : input rank-1 array('d') with bounds (n)
    duf : input rank-1 array('d') with bounds (MAX(0,n-1))
    du2 : input rank-1 array('d') with bounds (MAX(0,n-2))
    ipiv : input rank-1 array('i') with bounds (n)
    
    Returns
    -------
    dlf : rank-1 array('d') with bounds (MAX(0,n-1))
    df : rank-1 array('d') with bounds (n)
    duf : rank-1 array('d') with bounds (MAX(0,n-1))
    du2 : rank-1 array('d') with bounds (MAX(0,n-2))
    ipiv : rank-1 array('i') with bounds (n)
    x : rank-2 array('d') with bounds (ldx,nrhs)
    rcond : float
    ferr : rank-1 array('d') with bounds (nrhs)
    berr : rank-1 array('d') with bounds (nrhs)
    info : int
    """
    pass

def dgttrf(dl, d, du, overwrite_dl=None, overwrite_d=None, overwrite_du=None): # real signature unknown; restored from __doc__
    """
    dl,d,du,du2,ipiv,info = dgttrf(dl,d,du,[overwrite_dl,overwrite_d,overwrite_du])
    
    Wrapper for ``dgttrf``.
    
    Parameters
    ----------
    dl : input rank-1 array('d') with bounds (n - 1)
    d : input rank-1 array('d') with bounds (n)
    du : input rank-1 array('d') with bounds (n - 1)
    
    Other Parameters
    ----------------
    overwrite_dl : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    overwrite_du : input int, optional
        Default: 0
    
    Returns
    -------
    dl : rank-1 array('d') with bounds (n - 1)
    d : rank-1 array('d') with bounds (n)
    du : rank-1 array('d') with bounds (n - 1)
    du2 : rank-1 array('d') with bounds (n - 2)
    ipiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def dgttrs(dl, d, du, du2, ipiv, b, trans=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = dgttrs(dl,d,du,du2,ipiv,b,[trans,overwrite_b])
    
    Wrapper for ``dgttrs``.
    
    Parameters
    ----------
    dl : input rank-1 array('d') with bounds (n - 1)
    d : input rank-1 array('d') with bounds (n)
    du : input rank-1 array('d') with bounds (n - 1)
    du2 : input rank-1 array('d') with bounds (n - 2)
    ipiv : input rank-1 array('i') with bounds (n)
    b : input rank-2 array('d') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def dlamch(cmach): # real signature unknown; restored from __doc__
    """
    dlamch = dlamch(cmach)
    
    Wrapper for ``dlamch``.
    
    Parameters
    ----------
    cmach : input string(len=1)
    
    Returns
    -------
    dlamch : float
    """
    pass

def dlange(norm, a): # real signature unknown; restored from __doc__
    """
    n2 = dlange(norm,a)
    
    Wrapper for ``dlange``.
    
    Parameters
    ----------
    norm : input string(len=1)
    a : input rank-2 array('d') with bounds (m,n)
    
    Returns
    -------
    n2 : float
    """
    pass

def dlarf(v, tau, c, work, side=None, incv=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = dlarf(v,tau,c,work,[side,incv,overwrite_c])
    
    Wrapper for ``dlarf``.
    
    Parameters
    ----------
    v : input rank-1 array('d') with bounds ((side[0]=='L'?(1 + (m-1)*abs(incv)):(1 + (n-1)*abs(incv))))
    tau : input float
    c : input rank-2 array('d') with bounds (m,n)
    work : input rank-1 array('d') with bounds (lwork)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    incv : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (m,n)
    """
    pass

def dlarfg(n, alpha, x, incx=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    alpha,x,tau = dlarfg(n,alpha,x,[incx,overwrite_x])
    
    Wrapper for ``dlarfg``.
    
    Parameters
    ----------
    n : input int
    alpha : input float
    x : input rank-1 array('d') with bounds (lx)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    alpha : float
    x : rank-1 array('d') with bounds (lx)
    tau : float
    """
    pass

def dlartg(f, g): # real signature unknown; restored from __doc__
    """
    cs,sn,r = dlartg(f,g)
    
    Wrapper for ``dlartg``.
    
    Parameters
    ----------
    f : input float
    g : input float
    
    Returns
    -------
    cs : float
    sn : float
    r : float
    """
    pass

def dlasd4(i, d, z, rho=None): # real signature unknown; restored from __doc__
    """
    delta,sigma,work,info = dlasd4(i,d,z,[rho])
    
    Wrapper for ``dlasd4``.
    
    Parameters
    ----------
    i : input int
    d : input rank-1 array('d') with bounds (n)
    z : input rank-1 array('d') with bounds (n)
    
    Other Parameters
    ----------------
    rho : input float, optional
        Default: 1.0
    
    Returns
    -------
    delta : rank-1 array('d') with bounds (n)
    sigma : float
    work : rank-1 array('d') with bounds (n)
    info : int
    """
    pass

def dlaswp(a, piv, k1=None, k2=None, off=None, inc=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = dlaswp(a,piv,[k1,k2,off,inc,overwrite_a])
    
    Wrapper for ``dlaswp``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (nrows,n)
    piv : input rank-1 array('i') with bounds (npiv)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    k1 : input int, optional
        Default: 0
    k2 : input int, optional
        Default: npiv-1
    off : input int, optional
        Default: 0
    inc : input int, optional
        Default: 1
    
    Returns
    -------
    a : rank-2 array('d') with bounds (nrows,n)
    """
    pass

def dlauum(c, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    a,info = dlauum(c,[lower,overwrite_c])
    
    Wrapper for ``dlauum``.
    
    Parameters
    ----------
    c : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('d') with bounds (n,n) and c storage
    info : int
    """
    pass

def dorcsd(x11, x12, x21, x22, compute_u1=None, compute_u2=None, compute_v1t=None, compute_v2t=None, trans=None, signs=None, lwork=None, overwrite_x11=None, overwrite_x12=None, overwrite_x21=None, overwrite_x22=None): # real signature unknown; restored from __doc__
    """
    cs11,cs12,cs21,cs22,theta,u1,u2,v1t,v2t,info = dorcsd(x11,x12,x21,x22,[compute_u1,compute_u2,compute_v1t,compute_v2t,trans,signs,lwork,overwrite_x11,overwrite_x12,overwrite_x21,overwrite_x22])
    
    Wrapper for ``dorcsd``.
    
    Parameters
    ----------
    x11 : input rank-2 array('d') with bounds (p,q)
    x12 : input rank-2 array('d') with bounds (p,mmq)
    x21 : input rank-2 array('d') with bounds (mmp,q)
    x22 : input rank-2 array('d') with bounds (mmp,mmq)
    
    Other Parameters
    ----------------
    compute_u1 : input int, optional
        Default: 1
    compute_u2 : input int, optional
        Default: 1
    compute_v1t : input int, optional
        Default: 1
    compute_v2t : input int, optional
        Default: 1
    trans : input int, optional
        Default: 0
    signs : input int, optional
        Default: 0
    overwrite_x11 : input int, optional
        Default: 0
    overwrite_x12 : input int, optional
        Default: 0
    overwrite_x21 : input int, optional
        Default: 0
    overwrite_x22 : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 2+2*m+5*MAX(1,q-1)+4*MAX(1,q)+8*q
    
    Returns
    -------
    cs11 : rank-2 array('d') with bounds (p,q) and x11 storage
    cs12 : rank-2 array('d') with bounds (p,mmq) and x12 storage
    cs21 : rank-2 array('d') with bounds (mmp,q) and x21 storage
    cs22 : rank-2 array('d') with bounds (mmp,mmq) and x22 storage
    theta : rank-1 array('d') with bounds (min(min(p,mmp),min(q,mmq)))
    u1 : rank-2 array('d') with bounds ((compute_u1?p:0),(compute_u1?p:0))
    u2 : rank-2 array('d') with bounds ((compute_u2?mmp:0),(compute_u2?mmp:0))
    v1t : rank-2 array('d') with bounds ((compute_v1t?q:0),(compute_v1t?q:0))
    v2t : rank-2 array('d') with bounds ((compute_v2t?mmq:0),(compute_v2t?mmq:0))
    info : int
    """
    pass

def dorcsd_lwork(m, p, q): # real signature unknown; restored from __doc__
    """
    work,info = dorcsd_lwork(m,p,q)
    
    Wrapper for ``dorcsd_lwork``.
    
    Parameters
    ----------
    m : input int
    p : input int
    q : input int
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dorghr(a, tau, lo=None, hi=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ht,info = dorghr(a,tau,[lo,hi,lwork,overwrite_a])
    
    Wrapper for ``dorghr``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    tau : input rank-1 array('d') with bounds (n - 1)
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(hi-lo,1)
    
    Returns
    -------
    ht : rank-2 array('d') with bounds (n,n) and a storage
    info : int
    """
    pass

def dorghr_lwork(n, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    work,info = dorghr_lwork(n,[lo,hi])
    
    Wrapper for ``dorghr_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dorgqr(a, tau, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    q,work,info = dorgqr(a,tau,[lwork,overwrite_a])
    
    Wrapper for ``dorgqr``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    tau : input rank-1 array('d') with bounds (k)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    
    Returns
    -------
    q : rank-2 array('d') with bounds (m,n) and a storage
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dorgrq(a, tau, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    q,work,info = dorgrq(a,tau,[lwork,overwrite_a])
    
    Wrapper for ``dorgrq``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    tau : input rank-1 array('d') with bounds (k)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*m,1)
    
    Returns
    -------
    q : rank-2 array('d') with bounds (m,n) and a storage
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dormqr(side, trans, a, tau, c, lwork, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    cq,work,info = dormqr(side,trans,a,tau,c,lwork,[overwrite_c])
    
    Wrapper for ``dormqr``.
    
    Parameters
    ----------
    side : input string(len=1)
    trans : input string(len=1)
    a : input rank-2 array('d') with bounds (lda,k)
    tau : input rank-1 array('d') with bounds (k)
    c : input rank-2 array('d') with bounds (ldc,n)
    lwork : input int
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    cq : rank-2 array('d') with bounds (ldc,n) and c storage
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dormrz(a, tau, c, side=None, trans=None, lwork=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    cq,info = dormrz(a,tau,c,[side,trans,lwork,overwrite_c])
    
    Wrapper for ``dormrz``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (k,nt)
    tau : input rank-1 array('d') with bounds (k)
    c : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_c : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX((side[0]=='L'?n:m),1)
    
    Returns
    -------
    cq : rank-2 array('d') with bounds (m,n) and c storage
    info : int
    """
    pass

def dormrz_lwork(m, n, side=None, trans=None): # real signature unknown; restored from __doc__
    """
    work,info = dormrz_lwork(m,n,[side,trans])
    
    Wrapper for ``dormrz_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    trans : input string(len=1), optional
        Default: 'N'
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dpbsv(ab, b, lower=None, ldab=None, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    c,x,info = dpbsv(ab,b,[lower,ldab,overwrite_ab,overwrite_b])
    
    Wrapper for ``dpbsv``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,n)
    b : input rank-2 array('d') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (ldab,n) and ab storage
    x : rank-2 array('d') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def dpbtrf(ab, lower=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    c,info = dpbtrf(ab,[lower,ldab,overwrite_ab])
    
    Wrapper for ``dpbtrf``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    
    Returns
    -------
    c : rank-2 array('d') with bounds (ldab,n) and ab storage
    info : int
    """
    pass

def dpbtrs(ab, b, lower=None, ldab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = dpbtrs(ab,b,[lower,ldab,overwrite_b])
    
    Wrapper for ``dpbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,n)
    b : input rank-2 array('d') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def dpftrf(n, a, transr=None, uplo=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    achol,info = dpftrf(n,a,[transr,uplo,overwrite_a])
    
    Wrapper for ``dpftrf``.
    
    Parameters
    ----------
    n : input int
    a : input rank-1 array('d') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    achol : rank-1 array('d') with bounds (nt) and a storage
    info : int
    """
    pass

def dpftri(n, a, transr=None, uplo=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ainv,info = dpftri(n,a,[transr,uplo,overwrite_a])
    
    Wrapper for ``dpftri``.
    
    Parameters
    ----------
    n : input int
    a : input rank-1 array('d') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    ainv : rank-1 array('d') with bounds (nt) and a storage
    info : int
    """
    pass

def dpftrs(n, a, b, transr=None, uplo=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = dpftrs(n,a,b,[transr,uplo,overwrite_b])
    
    Wrapper for ``dpftrs``.
    
    Parameters
    ----------
    n : input int
    a : input rank-1 array('d') with bounds (nt)
    b : input rank-2 array('d') with bounds (ldb,nhrs)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (ldb,nhrs) and b storage
    info : int
    """
    pass

def dpocon(a, anorm, uplo=None): # real signature unknown; restored from __doc__
    """
    rcond,info = dpocon(a,anorm,[uplo])
    
    Wrapper for ``dpocon``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    anorm : input float
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def dposv(a, b, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    c,x,info = dposv(a,b,[lower,overwrite_a,overwrite_b])
    
    Wrapper for ``dposv``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (n,n) and a storage
    x : rank-2 array('d') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def dposvx(a, b, fact=None, af=None, equed=None, s=None, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = dposvx(a,b,[fact,af,equed,s,lower,overwrite_a,overwrite_b])
    
    Wrapper for ``dposvx``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    fact : input string(len=1), optional
        Default: 'E'
    overwrite_a : input int, optional
        Default: 0
    af : input rank-2 array('d') with bounds (n,n)
    equed : input string(len=1), optional
        Default: 'Y'
    s : input rank-1 array('d') with bounds (n)
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    a_s : rank-2 array('d') with bounds (n,n) and a storage
    lu : rank-2 array('d') with bounds (n,n) and af storage
    equed : string(len=1)
    s : rank-1 array('d') with bounds (n)
    b_s : rank-2 array('d') with bounds (n,nrhs) and b storage
    x : rank-2 array('d') with bounds (n,nrhs)
    rcond : float
    ferr : rank-1 array('d') with bounds (nrhs)
    berr : rank-1 array('d') with bounds (nrhs)
    info : int
    """
    pass

def dpotrf(a, lower=None, clean=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,info = dpotrf(a,[lower,clean,overwrite_a])
    
    Wrapper for ``dpotrf``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    clean : input int, optional
        Default: 1
    
    Returns
    -------
    c : rank-2 array('d') with bounds (n,n) and a storage
    info : int
    """
    pass

def dpotri(c, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    inv_a,info = dpotri(c,[lower,overwrite_c])
    
    Wrapper for ``dpotri``.
    
    Parameters
    ----------
    c : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    inv_a : rank-2 array('d') with bounds (n,n) and c storage
    info : int
    """
    pass

def dpotrs(c, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = dpotrs(c,b,[lower,overwrite_b])
    
    Wrapper for ``dpotrs``.
    
    Parameters
    ----------
    c : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def dppcon(n, ap, anorm, lower=None): # real signature unknown; restored from __doc__
    """
    rcond,info = dppcon(n,ap,anorm,[lower])
    
    Wrapper for ``dppcon``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('d') with bounds (L)
    anorm : input float
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def dppsv(n, ap, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = dppsv(n,ap,b,[lower,overwrite_b])
    
    Wrapper for ``dppsv``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('d') with bounds (L)
    b : input rank-2 array('d') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def dpptrf(n, ap, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    ul,info = dpptrf(n,ap,[lower,overwrite_ap])
    
    Wrapper for ``dpptrf``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('d') with bounds (L)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    
    Returns
    -------
    ul : rank-1 array('d') with bounds (L) and ap storage
    info : int
    """
    pass

def dpptri(n, ap, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    uli,info = dpptri(n,ap,[lower,overwrite_ap])
    
    Wrapper for ``dpptri``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('d') with bounds (L)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    
    Returns
    -------
    uli : rank-1 array('d') with bounds (L) and ap storage
    info : int
    """
    pass

def dpptrs(n, ap, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = dpptrs(n,ap,b,[lower,overwrite_b])
    
    Wrapper for ``dpptrs``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('d') with bounds (L)
    b : input rank-2 array('d') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def dpstf2(a, tol=None, lower=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,piv,rank_c,info = dpstf2(a,[tol,lower,overwrite_a])
    
    Wrapper for ``dpstf2``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    tol : input float, optional
        Default: -1.0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (n,n) and a storage
    piv : rank-1 array('i') with bounds (n)
    rank_c : int
    info : int
    """
    pass

def dpstrf(a, tol=None, lower=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,piv,rank_c,info = dpstrf(a,[tol,lower,overwrite_a])
    
    Wrapper for ``dpstrf``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    tol : input float, optional
        Default: -1.0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (n,n) and a storage
    piv : rank-1 array('i') with bounds (n)
    rank_c : int
    info : int
    """
    pass

def dpteqr(d, e, z, compute_z=None, overwrite_d=None, overwrite_e=None, overwrite_z=None): # real signature unknown; restored from __doc__
    """
    d,e,z,info = dpteqr(d,e,z,[compute_z,overwrite_d,overwrite_e,overwrite_z])
    
    Wrapper for ``dpteqr``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (n)
    e : input rank-1 array('d') with bounds ((n>0?n-1:0))
    z : input rank-2 array('d') with bounds ((compute_z==0?shape(z, 0):max(1,n)),(compute_z==0?shape(z, 1):n))
    
    Other Parameters
    ----------------
    compute_z : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    overwrite_z : input int, optional
        Default: 0
    
    Returns
    -------
    d : rank-1 array('d') with bounds (n)
    e : rank-1 array('d') with bounds ((n>0?n-1:0))
    z : rank-2 array('d') with bounds ((compute_z==0?shape(z, 0):max(1,n)),(compute_z==0?shape(z, 1):n))
    info : int
    """
    pass

def dptsv(d, e, b, overwrite_d=None, overwrite_e=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    d,du,x,info = dptsv(d,e,b,[overwrite_d,overwrite_e,overwrite_b])
    
    Wrapper for ``dptsv``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (n)
    e : input rank-1 array('d') with bounds (n - 1)
    b : input rank-2 array('d') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    d : rank-1 array('d') with bounds (n)
    du : rank-1 array('d') with bounds (n - 1) and e storage
    x : rank-2 array('d') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def dptsvx(d, e, b, fact=None, df=None, ef=None): # real signature unknown; restored from __doc__
    """
    df,ef,x,rcond,ferr,berr,info = dptsvx(d,e,b,[fact,df,ef])
    
    Wrapper for ``dptsvx``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (n)
    e : input rank-1 array('d') with bounds (max(0, n-1))
    b : input rank-2 array('d') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    fact : input string(len=1), optional
        Default: 'N'
    df : input rank-1 array('d') with bounds (n)
    ef : input rank-1 array('d') with bounds (max(0, n-1))
    
    Returns
    -------
    df : rank-1 array('d') with bounds (n)
    ef : rank-1 array('d') with bounds (max(0, n-1))
    x : rank-2 array('d') with bounds (ldx,nrhs)
    rcond : float
    ferr : rank-1 array('d') with bounds (nrhs)
    berr : rank-1 array('d') with bounds (nrhs)
    info : int
    """
    pass

def dpttrf(d, e, overwrite_d=None, overwrite_e=None): # real signature unknown; restored from __doc__
    """
    d,e,info = dpttrf(d,e,[overwrite_d,overwrite_e])
    
    Wrapper for ``dpttrf``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (n)
    e : input rank-1 array('d') with bounds ((n>0?n-1:0))
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    
    Returns
    -------
    d : rank-1 array('d') with bounds (n)
    e : rank-1 array('d') with bounds ((n>0?n-1:0))
    info : int
    """
    pass

def dpttrs(d, e, b, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = dpttrs(d,e,b,[overwrite_b])
    
    Wrapper for ``dpttrs``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (n)
    e : input rank-1 array('d') with bounds ((n>0?n-1:0))
    b : input rank-2 array('d') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def dsbev(ab, compute_v=None, lower=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,info = dsbev(ab,[compute_v,lower,ldab,overwrite_ab])
    
    Wrapper for ``dsbev``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,n)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('d') with bounds (ldz,ldz)
    info : int
    """
    pass

def dsbevd(ab, compute_v=None, lower=None, ldab=None, liwork=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,info = dsbevd(ab,[compute_v,lower,ldab,liwork,overwrite_ab])
    
    Wrapper for ``dsbevd``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,n)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    liwork : input int, optional
        Default: (compute_v?3+5*n:1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('d') with bounds (ldz,ldz)
    info : int
    """
    pass

def dsbevx(ab, vl, vu, il, iu, ldab=None, compute_v=None, range=None, lower=None, abstol=None, mmax=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,m,ifail,info = dsbevx(ab,vl,vu,il,iu,[ldab,compute_v,range,lower,abstol,mmax,overwrite_ab])
    
    Wrapper for ``dsbevx``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,n)
    vl : input float
    vu : input float
    il : input int
    iu : input int
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    ldab : input int, optional
        Default: shape(ab,0)
    compute_v : input int, optional
        Default: 1
    range : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    abstol : input float, optional
        Default: 0.0
    mmax : input int, optional
        Default: (compute_v?(range==2?(iu-il+1):n):1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('d') with bounds (ldz,mmax)
    m : int
    ifail : rank-1 array('i') with bounds ((compute_v?n:1))
    info : int
    """
    pass

def dsfrk(n, k, alpha, a, beta, c, transr=None, uplo=None, trans=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    cout = dsfrk(n,k,alpha,a,beta,c,[transr,uplo,trans,overwrite_c])
    
    Wrapper for ``dsfrk``.
    
    Parameters
    ----------
    n : input int
    k : input int
    alpha : input float
    a : input rank-2 array('d') with bounds (lda,ka)
    beta : input float
    c : input rank-1 array('d') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    cout : rank-1 array('d') with bounds (nt) and c storage
    """
    pass

def dstebz(d, e, range, vl, vu, il, iu, tol, order): # real signature unknown; restored from __doc__
    """
    m,w,iblock,isplit,info = dstebz(d,e,range,vl,vu,il,iu,tol,order)
    
    Wrapper for ``dstebz``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (n)
    e : input rank-1 array('d') with bounds (n - 1)
    range : input int
    vl : input float
    vu : input float
    il : input int
    iu : input int
    tol : input float
    order : input string(len=1)
    
    Returns
    -------
    m : int
    w : rank-1 array('d') with bounds (n)
    iblock : rank-1 array('i') with bounds (n)
    isplit : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def dstein(d, e, w, iblock, isplit): # real signature unknown; restored from __doc__
    """
    z,info = dstein(d,e,w,iblock,isplit)
    
    Wrapper for ``dstein``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (n)
    e : input rank-1 array('d') with bounds (n - 1)
    w : input rank-1 array('d') with bounds (m)
    iblock : input rank-1 array('i') with bounds (n)
    isplit : input rank-1 array('i') with bounds (n)
    
    Returns
    -------
    z : rank-2 array('d') with bounds (ldz,m)
    info : int
    """
    pass

def dstemr(d, e, range, vl, vu, il, iu, compute_v=None, lwork=None, liwork=None, overwrite_d=None): # real signature unknown; restored from __doc__
    """
    m,w,z,info = dstemr(d,e,range,vl,vu,il,iu,[compute_v,lwork,liwork,overwrite_d])
    
    Wrapper for ``dstemr``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (n)
    e : input rank-1 array('d') with bounds (n)
    range : input int
    vl : input float
    vu : input float
    il : input int
    iu : input int
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    compute_v : input int, optional
        Default: 1
    lwork : input int, optional
        Default: max((compute_v?18*n:12*n),1)
    liwork : input int, optional
        Default: (compute_v?10*n:8*n)
    
    Returns
    -------
    m : int
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('d') with bounds (n,n)
    info : int
    """
    pass

def dstemr_lwork(d, e, range, vl, vu, il, iu, compute_v=None, overwrite_d=None, overwrite_e=None): # real signature unknown; restored from __doc__
    """
    work,iwork,info = dstemr_lwork(d,e,range,vl,vu,il,iu,[compute_v,overwrite_d,overwrite_e])
    
    Wrapper for ``dstemr_lwork``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (n)
    e : input rank-1 array('d') with bounds (n)
    range : input int
    vl : input float
    vu : input float
    il : input int
    iu : input int
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    compute_v : input int, optional
        Default: 1
    
    Returns
    -------
    work : float
    iwork : int
    info : int
    """
    pass

def dsterf(d, e, overwrite_d=None, overwrite_e=None): # real signature unknown; restored from __doc__
    """
    vals,info = dsterf(d,e,[overwrite_d,overwrite_e])
    
    Wrapper for ``dsterf``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (n)
    e : input rank-1 array('d') with bounds (n - 1)
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    
    Returns
    -------
    vals : rank-1 array('d') with bounds (n) and d storage
    info : int
    """
    pass

def dstev(d, e, compute_v=None, overwrite_d=None, overwrite_e=None): # real signature unknown; restored from __doc__
    """
    vals,z,info = dstev(d,e,[compute_v,overwrite_d,overwrite_e])
    
    Wrapper for ``dstev``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (n)
    e : input rank-1 array('d') with bounds (MAX(n-1,1))
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    compute_v : input int, optional
        Default: 1
    
    Returns
    -------
    vals : rank-1 array('d') with bounds (n) and d storage
    z : rank-2 array('d') with bounds (ldz,(compute_v?n:1))
    info : int
    """
    pass

def dsycon(a, ipiv, anorm, lower=None): # real signature unknown; restored from __doc__
    """
    rcond,info = dsycon(a,ipiv,anorm,[lower])
    
    Wrapper for ``dsycon``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    anorm : input float
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def dsyconv(a, ipiv, lower=None, way=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a,e,info = dsyconv(a,ipiv,[lower,way,overwrite_a])
    
    Wrapper for ``dsyconv``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    way : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('d') with bounds (n,n)
    e : rank-1 array('d') with bounds (n)
    info : int
    """
    pass

def dsyequb(a, lower=None): # real signature unknown; restored from __doc__
    """
    s,scond,amax,info = dsyequb(a,[lower])
    
    Wrapper for ``dsyequb``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (lda,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    s : rank-1 array('d') with bounds (n)
    scond : float
    amax : float
    info : int
    """
    pass

def dsyev(a, compute_v=None, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,v,info = dsyev(a,[compute_v,lower,lwork,overwrite_a])
    
    Wrapper for ``dsyev``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n-1,1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    v : rank-2 array('d') with bounds (n,n) and a storage
    info : int
    """
    pass

def dsyevd(a, compute_v=None, lower=None, lwork=None, liwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,v,info = dsyevd(a,[compute_v,lower,lwork,liwork,overwrite_a])
    
    Wrapper for ``dsyevd``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max((compute_v?1+6*n+2*n*n:2*n+1),1)
    liwork : input int, optional
        Default: (compute_v?3+5*n:1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    v : rank-2 array('d') with bounds (n,n) and a storage
    info : int
    """
    pass

def dsyevd_lwork(n, compute_v=None, lower=None): # real signature unknown; restored from __doc__
    """
    work,iwork,info = dsyevd_lwork(n,[compute_v,lower])
    
    Wrapper for ``dsyevd_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : float
    iwork : int
    info : int
    """
    pass

def dsyevr(a, compute_v=None, range=None, lower=None, vl=None, vu=None, il=None, iu=None, abstol=None, lwork=None, liwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,z,m,isuppz,info = dsyevr(a,[compute_v,range,lower,vl,vu,il,iu,abstol,lwork,liwork,overwrite_a])
    
    Wrapper for ``dsyevr``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds ``(n,n)``
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default ``1``
    range : input string(len=1), optional
        Default ``'A'``
    lower : input int, optional
        Default ``0``
    overwrite_a : input int, optional
        Default ``0``
    vl : input float, optional
        Default ``0.0``
    vu : input float, optional
        Default ``1.0``
    il : input int, optional
        Default ``1``
    iu : input int, optional
        Default ``n``
    abstol : input float, optional
        Default ``0.0``
    lwork : input int, optional
        Default ``max(26*n,1)``
    liwork : input int, optional
        Default ``max(1,10*n)``
    
    Returns
    -------
    w : rank-1 array('d') with bounds ``(n)``
    z : rank-2 array('d') with bounds ``((compute_v?MAX(0,n):0),(compute_v?((*range=='I')?(iu-il+1):MAX(1,n)):0))``
    m : int
    isuppz : rank-1 array('i') with bounds ``((compute_v?(2*((*range=='A')||((*range=='I') && (iu-il+1==n))?n:0)):0))``
    info : int
    """
    pass

def dsyevr_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,iwork,info = dsyevr_lwork(n,[lower])
    
    Wrapper for ``dsyevr_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : float
    iwork : int
    info : int
    """
    pass

def dsyevx(a, compute_v=None, range=None, lower=None, vl=None, vu=None, il=None, iu=None, abstol=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,z,m,ifail,info = dsyevx(a,[compute_v,range,lower,vl,vu,il,iu,abstol,lwork,overwrite_a])
    
    Wrapper for ``dsyevx``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds ``(n,n)``
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default ``1``
    range : input string(len=1), optional
        Default ``'A'``
    lower : input int, optional
        Default ``0``
    overwrite_a : input int, optional
        Default ``0``
    vl : input float, optional
        Default ``0.0``
    vu : input float, optional
        Default ``1.0``
    il : input int, optional
        Default ``1``
    iu : input int, optional
        Default ``n``
    abstol : input float, optional
        Default ``0.0``
    lwork : input int, optional
        Default ``max(8*n,1)``
    
    Returns
    -------
    w : rank-1 array('d') with bounds ``(n)``
    z : rank-2 array('d') with bounds ``((compute_v?MAX(0,n):0),(compute_v?((*range=='I')?(iu-il+1):MAX(1,n)):0))``
    m : int
    ifail : rank-1 array('i') with bounds ``((compute_v?n:0))``
    info : int
    """
    pass

def dsyevx_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = dsyevx_lwork(n,[lower])
    
    Wrapper for ``dsyevx_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dsyev_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = dsyev_lwork(n,[lower])
    
    Wrapper for ``dsyev_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dsygst(a, b, itype=None, lower=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,info = dsygst(a,b,[itype,lower,overwrite_a])
    
    Wrapper for ``dsygst``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    itype : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('d') with bounds (n,n) and a storage
    info : int
    """
    pass

def dsygv(a, b, itype=None, jobz=None, uplo=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    w,v,info = dsygv(a,b,[itype,jobz,uplo,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``dsygv``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n-1,1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    v : rank-2 array('d') with bounds (n,n) and a storage
    info : int
    """
    pass

def dsygvd(a, b, itype=None, jobz=None, uplo=None, lwork=None, liwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    w,v,info = dsygvd(a,b,[itype,jobz,uplo,lwork,liwork,overwrite_a,overwrite_b])
    
    Wrapper for ``dsygvd``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds ``(n,n)``
    b : input rank-2 array('d') with bounds ``(n,n)``
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default ``1``
    jobz : input string(len=1), optional
        Default ``'V'``
    uplo : input string(len=1), optional
        Default ``'L'``
    overwrite_a : input int, optional
        Default ``0``
    overwrite_b : input int, optional
        Default ``0``
    lwork : input int, optional
        Default ``(*jobz=='N'?2*n+1:1+6*n+2*n*n)``
    liwork : input int, optional
        Default ``(*jobz=='N'?1:5*n+3)``
    
    Returns
    -------
    w : rank-1 array('d') with bounds ``(n)``
    v : rank-2 array('d') with bounds ``(n,n)`` with ``a`` storage
    info : int
    """
    pass

def dsygvx(a, b, itype=None, jobz=None, range=None, uplo=None, vl=None, vu=None, il=None, iu=None, abstol=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    w,z,m,ifail,info = dsygvx(a,b,[itype,jobz,range,uplo,vl,vu,il,iu,abstol,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``dsygvx``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    range : input string(len=1), optional
        Default: 'A'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    vl : input float, optional
        Default: 0.0
    vu : input float, optional
        Default: 1.0
    il : input int, optional
        Default: 1
    iu : input int, optional
        Default: n
    abstol : input float, optional
        Default: 0.0
    lwork : input int, optional
        Default: max(8*n,1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('d') with bounds ((jobz[0]=='V'?MAX(0,n):0),(jobz[0]=='V'?((range[0]=='I')?(iu-il+1):MAX(1,n)):0))
    m : int
    ifail : rank-1 array('i') with bounds ((jobz[0]=='N'?0:n))
    info : int
    """
    pass

def dsygvx_lwork(n, uplo=None): # real signature unknown; restored from __doc__
    """
    work,info = dsygvx_lwork(n,[uplo])
    
    Wrapper for ``dsygvx_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'L'
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dsygv_lwork(n, uplo=None): # real signature unknown; restored from __doc__
    """
    work,info = dsygv_lwork(n,[uplo])
    
    Wrapper for ``dsygv_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'L'
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dsysv(a, b, lwork=None, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    udut,ipiv,x,info = dsysv(a,b,[lwork,lower,overwrite_a,overwrite_b])
    
    Wrapper for ``dsysv``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(n,1)
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    udut : rank-2 array('d') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    x : rank-2 array('d') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def dsysvx(a, b, af=None, ipiv=None, lwork=None, factored=None, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = dsysvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])
    
    Wrapper for ``dsysvx``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    af : input rank-2 array('d') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    factored : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    a_s : rank-2 array('d') with bounds (n,n) and a storage
    udut : rank-2 array('d') with bounds (n,n) and af storage
    ipiv : rank-1 array('i') with bounds (n)
    b_s : rank-2 array('d') with bounds (n,nrhs) and b storage
    x : rank-2 array('d') with bounds (n,nrhs)
    rcond : float
    ferr : rank-1 array('d') with bounds (nrhs)
    berr : rank-1 array('d') with bounds (nrhs)
    info : int
    """
    pass

def dsysvx_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = dsysvx_lwork(n,[lower])
    
    Wrapper for ``dsysvx_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dsysv_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = dsysv_lwork(n,[lower])
    
    Wrapper for ``dsysv_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dsytf2(a, lower=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ldu,ipiv,info = dsytf2(a,[lower,overwrite_a])
    
    Wrapper for ``dsytf2``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    ldu : rank-2 array('d') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def dsytrd(a, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,d,e,tau,info = dsytrd(a,[lower,lwork,overwrite_a])
    
    Wrapper for ``dsytrd``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (lda,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(n,1)
    
    Returns
    -------
    c : rank-2 array('d') with bounds (lda,n) and a storage
    d : rank-1 array('d') with bounds (n)
    e : rank-1 array('d') with bounds (n - 1)
    tau : rank-1 array('d') with bounds (n - 1)
    info : int
    """
    pass

def dsytrd_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = dsytrd_lwork(n,[lower])
    
    Wrapper for ``dsytrd_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dsytrf(a, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ldu,ipiv,info = dsytrf(a,[lower,lwork,overwrite_a])
    
    Wrapper for ``dsytrf``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(n,1)
    
    Returns
    -------
    ldu : rank-2 array('d') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def dsytrf_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = dsytrf_lwork(n,[lower])
    
    Wrapper for ``dsytrf_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def dtbtrs(ab, b, uplo=None, trans=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = dtbtrs(ab,b,[uplo,trans,diag,overwrite_b])
    
    Wrapper for ``dtbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('d') with bounds (ldab,n)
    b : input rank-2 array('d') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'U'
    trans : input string(len=1), optional
        Default: 'N'
    diag : input string(len=1), optional
        Default: 'N'
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def dtfsm(alpha, a, b, transr=None, side=None, uplo=None, trans=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x = dtfsm(alpha,a,b,[transr,side,uplo,trans,diag,overwrite_b])
    
    Wrapper for ``dtfsm``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-1 array('d') with bounds (nt)
    b : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    side : input string(len=1), optional
        Default: 'L'
    uplo : input string(len=1), optional
        Default: 'U'
    trans : input string(len=1), optional
        Default: 'N'
    diag : input string(len=1), optional
        Default: 'N'
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (m,n) and b storage
    """
    pass

def dtfttp(n, arf, transr=None, uplo=None): # real signature unknown; restored from __doc__
    """
    ap,info = dtfttp(n,arf,[transr,uplo])
    
    Wrapper for ``dtfttp``.
    
    Parameters
    ----------
    n : input int
    arf : input rank-1 array('d') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    ap : rank-1 array('d') with bounds (nt)
    info : int
    """
    pass

def dtfttr(n, arf, transr=None, uplo=None): # real signature unknown; restored from __doc__
    """
    a,info = dtfttr(n,arf,[transr,uplo])
    
    Wrapper for ``dtfttr``.
    
    Parameters
    ----------
    n : input int
    arf : input rank-1 array('d') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    a : rank-2 array('d') with bounds (lda,n)
    info : int
    """
    pass

def dtgexc(a, b, q, z, ifst, ilst, wantq=None, wantz=None, lwork=None, overwrite_a=None, overwrite_b=None, overwrite_q=None, overwrite_z=None): # real signature unknown; restored from __doc__
    """
    a,b,q,z,work,info = dtgexc(a,b,q,z,ifst,ilst,[wantq,wantz,lwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])
    
    Wrapper for ``dtgexc``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (lda,n)
    b : input rank-2 array('d') with bounds (ldb,n)
    q : input rank-2 array('d') with bounds (ldq,n)
    z : input rank-2 array('d') with bounds (ldz,n)
    ifst : input int
    ilst : input int
    
    Other Parameters
    ----------------
    wantq : input int, optional
        Default: 1
    wantz : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    overwrite_z : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(4*n+16,1)
    
    Returns
    -------
    a : rank-2 array('d') with bounds (lda,n)
    b : rank-2 array('d') with bounds (ldb,n)
    q : rank-2 array('d') with bounds (ldq,n)
    z : rank-2 array('d') with bounds (ldz,n)
    work : rank-1 array('d') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def dtgsen(select, a, b, q, z, ijob=None, wantq=None, wantz=None, lwork=None, liwork=None, overwrite_a=None, overwrite_b=None, overwrite_q=None, overwrite_z=None): # real signature unknown; restored from __doc__
    """
    as,bs,alphar,alphai,beta,qs,zs,m,pl,pr,dif,info = dtgsen(select,a,b,q,z,[ijob,wantq,wantz,lwork,liwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])
    
    Wrapper for ``dtgsen``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (n,n)
    q : input rank-2 array('d') with bounds (n,n)
    z : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    ijob : input int, optional
        Default: 4
    wantq : input int, optional
        Default: 1
    wantz : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    overwrite_z : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 4*n+16
    liwork : input int, optional
        Default: n+6
    
    Returns
    -------
    as : rank-2 array('d') with bounds (n,n) and a storage
    bs : rank-2 array('d') with bounds (n,n) and b storage
    alphar : rank-1 array('d') with bounds (n)
    alphai : rank-1 array('d') with bounds (n)
    beta : rank-1 array('d') with bounds (n)
    qs : rank-2 array('d') with bounds (n,n) and q storage
    zs : rank-2 array('d') with bounds (n,n) and z storage
    m : int
    pl : float
    pr : float
    dif : rank-1 array('d') with bounds (2)
    info : int
    """
    pass

def dtgsen_lwork(select, a, ijob=None): # real signature unknown; restored from __doc__
    """
    work,iwork,info = dtgsen_lwork(select,a,[ijob])
    
    Wrapper for ``dtgsen_lwork``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    a : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    ijob : input int, optional
        Default: 4
    
    Returns
    -------
    work : float
    iwork : int
    info : int
    """
    pass

def dtpmqrt(l, v, t, a, b, side=None, trans=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,b,info = dtpmqrt(l,v,t,a,b,[side,trans,overwrite_a,overwrite_b])
    
    Wrapper for ``dtpmqrt``.
    
    Parameters
    ----------
    l : input int
    v : input rank-2 array('d') with bounds ((side[0]=='L'?m:n),k)
    t : input rank-2 array('d') with bounds (nb,k)
    a : input rank-2 array('d') with bounds ((side[0]=='L'?k:m),(side[0]=='L'?n:k))
    b : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('d') with bounds ((side[0]=='L'?k:m),(side[0]=='L'?n:k))
    b : rank-2 array('d') with bounds (m,n)
    info : int
    """
    pass

def dtpqrt(l, nb, a, b, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,b,t,info = dtpqrt(l,nb,a,b,[overwrite_a,overwrite_b])
    
    Wrapper for ``dtpqrt``.
    
    Parameters
    ----------
    l : input int
    nb : input int
    a : input rank-2 array('d') with bounds (n,n)
    b : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('d') with bounds (n,n)
    b : rank-2 array('d') with bounds (m,n)
    t : rank-2 array('d') with bounds (nb,n)
    info : int
    """
    pass

def dtpttf(n, ap, transr=None, uplo=None): # real signature unknown; restored from __doc__
    """
    arf,info = dtpttf(n,ap,[transr,uplo])
    
    Wrapper for ``dtpttf``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('d') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    arf : rank-1 array('d') with bounds (nt)
    info : int
    """
    pass

def dtpttr(n, ap, uplo=None): # real signature unknown; restored from __doc__
    """
    a,info = dtpttr(n,ap,[uplo])
    
    Wrapper for ``dtpttr``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('d') with bounds (nt)
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    a : rank-2 array('d') with bounds (n,n)
    info : int
    """
    pass

def dtrexc(a, q, ifst, ilst, wantq=None, overwrite_a=None, overwrite_q=None): # real signature unknown; restored from __doc__
    """
    a,q,info = dtrexc(a,q,ifst,ilst,[wantq,overwrite_a,overwrite_q])
    
    Wrapper for ``dtrexc``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (lda,n)
    q : input rank-2 array('d') with bounds (ldq,n)
    ifst : input int
    ilst : input int
    
    Other Parameters
    ----------------
    wantq : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('d') with bounds (lda,n)
    q : rank-2 array('d') with bounds (ldq,n)
    info : int
    """
    pass

def dtrsen(select, t, q, job=None, wantq=None, lwork=None, liwork=None, overwrite_t=None, overwrite_q=None): # real signature unknown; restored from __doc__
    """
    ts,qs,wr,wi,m,s,sep,info = dtrsen(select,t,q,[job,wantq,lwork,liwork,overwrite_t,overwrite_q])
    
    Wrapper for ``dtrsen``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    t : input rank-2 array('d') with bounds (n,n)
    q : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    job : input string(len=1), optional
        Default: 'B'
    wantq : input int, optional
        Default: 1
    overwrite_t : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(1,n)
    liwork : input int, optional
        Default: 1
    
    Returns
    -------
    ts : rank-2 array('d') with bounds (n,n) and t storage
    qs : rank-2 array('d') with bounds (n,n) and q storage
    wr : rank-1 array('d') with bounds (n)
    wi : rank-1 array('d') with bounds (n)
    m : int
    s : float
    sep : float
    info : int
    """
    pass

def dtrsen_lwork(select, t, job=None): # real signature unknown; restored from __doc__
    """
    work,iwork,info = dtrsen_lwork(select,t,[job])
    
    Wrapper for ``dtrsen_lwork``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    t : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    job : input string(len=1), optional
        Default: 'B'
    
    Returns
    -------
    work : float
    iwork : int
    info : int
    """
    pass

def dtrsyl(a, b, c, trana=None, tranb=None, isgn=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    x,scale,info = dtrsyl(a,b,c,[trana,tranb,isgn,overwrite_c])
    
    Wrapper for ``dtrsyl``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,m)
    b : input rank-2 array('d') with bounds (n,n)
    c : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    trana : input string(len=1), optional
        Default: 'N'
    tranb : input string(len=1), optional
        Default: 'N'
    isgn : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (m,n) and c storage
    scale : float
    info : int
    """
    pass

def dtrtri(c, lower=None, unitdiag=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    inv_c,info = dtrtri(c,[lower,unitdiag,overwrite_c])
    
    Wrapper for ``dtrtri``.
    
    Parameters
    ----------
    c : input rank-2 array('d') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    
    Returns
    -------
    inv_c : rank-2 array('d') with bounds (n,n) and c storage
    info : int
    """
    pass

def dtrtrs(a, b, lower=None, trans=None, unitdiag=None, lda=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = dtrtrs(a,b,[lower,trans,unitdiag,lda,overwrite_b])
    
    Wrapper for ``dtrtrs``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (lda,n)
    b : input rank-2 array('d') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    lda : input int, optional
        Default: shape(a,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('d') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def dtrttf(a, transr=None, uplo=None): # real signature unknown; restored from __doc__
    """
    arf,info = dtrttf(a,[transr,uplo])
    
    Wrapper for ``dtrttf``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (lda,n)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    arf : rank-1 array('d') with bounds (n*(n+1)/2)
    info : int
    """
    pass

def dtrttp(a, uplo=None): # real signature unknown; restored from __doc__
    """
    ap,info = dtrttp(a,[uplo])
    
    Wrapper for ``dtrttp``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (lda,n)
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    ap : rank-1 array('d') with bounds (n*(n+1)/2)
    info : int
    """
    pass

def dtzrzf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    rz,tau,info = dtzrzf(a,[lwork,overwrite_a])
    
    Wrapper for ``dtzrzf``.
    
    Parameters
    ----------
    a : input rank-2 array('d') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(m,1)
    
    Returns
    -------
    rz : rank-2 array('d') with bounds (m,n) and a storage
    tau : rank-1 array('d') with bounds (m)
    info : int
    """
    pass

def dtzrzf_lwork(m, n): # real signature unknown; restored from __doc__
    """
    work,info = dtzrzf_lwork(m,n)
    
    Wrapper for ``dtzrzf_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def ilaver(): # real signature unknown; restored from __doc__
    """
    major,minor,patch = ilaver()
    
    Wrapper for ``ilaver``.
    
    Returns
    -------
    major : int
    minor : int
    patch : int
    """
    pass

def sgbsv(kl, ku, ab, b, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lub,piv,x,info = sgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])
    
    Wrapper for ``sgbsv``.
    
    Parameters
    ----------
    kl : input int
    ku : input int
    ab : input rank-2 array('f') with bounds (2*kl+ku+1,n)
    b : input rank-2 array('f') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lub : rank-2 array('f') with bounds (2*kl+ku+1,n) and ab storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('f') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def sgbtrf(ab, kl, ku, m=None, n=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    lu,ipiv,info = sgbtrf(ab,kl,ku,[m,n,ldab,overwrite_ab])
    
    Wrapper for ``sgbtrf``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,n)
    kl : input int
    ku : input int
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(ab,1)
    n : input int, optional
        Default: shape(ab,1)
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: max(shape(ab,0),1)
    
    Returns
    -------
    lu : rank-2 array('f') with bounds (ldab,n) and ab storage
    ipiv : rank-1 array('i') with bounds (MIN(m,n))
    info : int
    """
    pass

def sgbtrs(ab, kl, ku, b, ipiv, trans=None, n=None, ldab=None, ldb=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = sgbtrs(ab,kl,ku,b,ipiv,[trans,n,ldab,ldb,overwrite_b])
    
    Wrapper for ``sgbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,n)
    kl : input int
    ku : input int
    b : input rank-2 array('f') with bounds (ldb,nrhs)
    ipiv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    n : input int, optional
        Default: shape(ab,1)
    ldab : input int, optional
        Default: shape(ab,0)
    ldb : input int, optional
        Default: shape(b,0)
    
    Returns
    -------
    x : rank-2 array('f') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def sgebal(a, scale=None, permute=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ba,lo,hi,pivscale,info = sgebal(a,[scale,permute,overwrite_a])
    
    Wrapper for ``sgebal``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    scale : input int, optional
        Default: 0
    permute : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    ba : rank-2 array('f') with bounds (m,n) and a storage
    lo : int
    hi : int
    pivscale : rank-1 array('f') with bounds (n)
    info : int
    """
    pass

def sgecon(a, anorm, norm=None): # real signature unknown; restored from __doc__
    """
    rcond,info = sgecon(a,anorm,[norm])
    
    Wrapper for ``sgecon``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    anorm : input float
    
    Other Parameters
    ----------------
    norm : input string(len=1), optional
        Default: '1'
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def sgeequ(a): # real signature unknown; restored from __doc__
    """
    r,c,rowcnd,colcnd,amax,info = sgeequ(a)
    
    Wrapper for ``sgeequ``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Returns
    -------
    r : rank-1 array('f') with bounds (m)
    c : rank-1 array('f') with bounds (n)
    rowcnd : float
    colcnd : float
    amax : float
    info : int
    """
    pass

def sgeequb(a): # real signature unknown; restored from __doc__
    """
    r,c,rowcnd,colcnd,amax,info = sgeequb(a)
    
    Wrapper for ``sgeequb``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Returns
    -------
    r : rank-1 array('f') with bounds (m)
    c : rank-1 array('f') with bounds (n)
    rowcnd : float
    colcnd : float
    amax : float
    info : int
    """
    pass

def sgees(sselect, a, compute_v=None, sort_t=None, lwork=None, sselect_extra_args=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    t,sdim,wr,wi,vs,work,info = sgees(sselect,a,[compute_v,sort_t,lwork,sselect_extra_args,overwrite_a])
    
    Wrapper for ``sgees``.
    
    Parameters
    ----------
    sselect : call-back function
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    sort_t : input int, optional
        Default: 0
    sselect_extra_args : input tuple, optional
        Default: ()
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    
    Returns
    -------
    t : rank-2 array('f') with bounds (n,n) and a storage
    sdim : int
    wr : rank-1 array('f') with bounds (n)
    wi : rank-1 array('f') with bounds (n)
    vs : rank-2 array('f') with bounds (ldvs,n)
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def sselect(arg1,arg2): return sselect
      Required arguments:
        arg1 : input float
        arg2 : input float
      Return objects:
        sselect : int
    """
    pass

def sgeev(a, compute_vl=None, compute_vr=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    wr,wi,vl,vr,info = sgeev(a,[compute_vl,compute_vr,lwork,overwrite_a])
    
    Wrapper for ``sgeev``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(4*n,1)
    
    Returns
    -------
    wr : rank-1 array('f') with bounds (n)
    wi : rank-1 array('f') with bounds (n)
    vl : rank-2 array('f') with bounds (ldvl,n)
    vr : rank-2 array('f') with bounds (ldvr,n)
    info : int
    """
    pass

def sgeev_lwork(n, compute_vl=None, compute_vr=None): # real signature unknown; restored from __doc__
    """
    work,info = sgeev_lwork(n,[compute_vl,compute_vr])
    
    Wrapper for ``sgeev_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgehrd(a, lo=None, hi=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ht,tau,info = sgehrd(a,[lo,hi,lwork,overwrite_a])
    
    Wrapper for ``sgehrd``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(n,1)
    
    Returns
    -------
    ht : rank-2 array('f') with bounds (n,n) and a storage
    tau : rank-1 array('f') with bounds (n - 1)
    info : int
    """
    pass

def sgehrd_lwork(n, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    work,info = sgehrd_lwork(n,[lo,hi])
    
    Wrapper for ``sgehrd_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgejsv(a, joba=None, jobu=None, jobv=None, jobr=None, jobt=None, jobp=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    sva,u,v,workout,iworkout,info = sgejsv(a,[joba,jobu,jobv,jobr,jobt,jobp,lwork,overwrite_a])
    
    Wrapper for ``sgejsv``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (lda,n)
    
    Other Parameters
    ----------------
    joba : input int, optional
        Default: 4
    jobu : input int, optional
        Default: 0
    jobv : input int, optional
        Default: 0
    jobr : input int, optional
        Default: 1
    jobt : input int, optional
        Default: 0
    jobp : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(6*n+2*n*n, max(2*m+n, max(4*n+n*n, max(2*n+n*n+6, 7))))
    
    Returns
    -------
    sva : rank-1 array('f') with bounds (n)
    u : rank-2 array('f') with bounds (((jobt == 0)&&(jobu == 3)?0:m),((jobt == 0)&&(jobu == 3)?0:(jobu == 1?m:n)))
    v : rank-2 array('f') with bounds (((jobt == 0)&&(jobv == 3)?0:ldv),((jobt == 0)&&(jobv == 3)?0:n))
    workout : rank-1 array('f') with bounds (7)
    iworkout : rank-1 array('i') with bounds (3)
    info : int
    """
    pass

def sgels(a, b, trans=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lqr,x,info = sgels(a,b,[trans,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``sgels``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    b : input rank-2 array('f') with bounds (MAX(m,n),nrhs)
    
    Other Parameters
    ----------------
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(MIN(m,n)+MAX(MIN(m,n),nrhs),1)
    
    Returns
    -------
    lqr : rank-2 array('f') with bounds (m,n) and a storage
    x : rank-2 array('f') with bounds (MAX(m,n),nrhs) and b storage
    info : int
    """
    pass

def sgelsd(a, b, lwork, size_iwork, cond=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,s,rank,info = sgelsd(a,b,lwork,size_iwork,[cond,overwrite_a,overwrite_b])
    
    Wrapper for ``sgelsd``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    b : input rank-2 array('f') with bounds (maxmn,nrhs)
    lwork : input int
    size_iwork : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    cond : input float, optional
        Default: -1.0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (maxmn,nrhs) and b storage
    s : rank-1 array('f') with bounds (minmn)
    rank : int
    info : int
    """
    pass

def sgelsd_lwork(m, n, nrhs, cond=None, lwork=None): # real signature unknown; restored from __doc__
    """
    work,iwork,info = sgelsd_lwork(m,n,nrhs,[cond,lwork])
    
    Wrapper for ``sgelsd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : float
    iwork : int
    info : int
    """
    pass

def sgelss(a, b, cond=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    v,x,s,rank,work,info = sgelss(a,b,[cond,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``sgelss``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    b : input rank-2 array('f') with bounds (maxmn,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: max(3*minmn+MAX(2*minmn,MAX(maxmn,nrhs)),1)
    
    Returns
    -------
    v : rank-2 array('f') with bounds (m,n) and a storage
    x : rank-2 array('f') with bounds (maxmn,nrhs) and b storage
    s : rank-1 array('f') with bounds (minmn)
    rank : int
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def sgelss_lwork(m, n, nrhs, cond=None, lwork=None): # real signature unknown; restored from __doc__
    """
    work,info = sgelss_lwork(m,n,nrhs,[cond,lwork])
    
    Wrapper for ``sgelss_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgelsy(a, b, jptv, cond, lwork, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    v,x,j,rank,info = sgelsy(a,b,jptv,cond,lwork,[overwrite_a,overwrite_b])
    
    Wrapper for ``sgelsy``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    b : input rank-2 array('f') with bounds (maxmn,nrhs)
    jptv : input rank-1 array('i') with bounds (n)
    cond : input float
    lwork : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    v : rank-2 array('f') with bounds (m,n) and a storage
    x : rank-2 array('f') with bounds (maxmn,nrhs) and b storage
    j : rank-1 array('i') with bounds (n) and jptv storage
    rank : int
    info : int
    """
    pass

def sgelsy_lwork(m, n, nrhs, cond, lwork=None): # real signature unknown; restored from __doc__
    """
    work,info = sgelsy_lwork(m,n,nrhs,cond,[lwork])
    
    Wrapper for ``sgelsy_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    cond : input float
    
    Other Parameters
    ----------------
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgels_lwork(m, n, nrhs, trans=None): # real signature unknown; restored from __doc__
    """
    work,info = sgels_lwork(m,n,nrhs,[trans])
    
    Wrapper for ``sgels_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    trans : input string(len=1), optional
        Default: 'N'
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgemqrt(v, t, c, side=None, trans=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c,info = sgemqrt(v,t,c,[side,trans,overwrite_c])
    
    Wrapper for ``sgemqrt``.
    
    Parameters
    ----------
    v : input rank-2 array('f') with bounds ((side[0]=='L'?m:n),k)
    t : input rank-2 array('f') with bounds (nb,k)
    c : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (m,n)
    info : int
    """
    pass

def sgeqp3(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,jpvt,tau,work,info = sgeqp3(a,[lwork,overwrite_a])
    
    Wrapper for ``sgeqp3``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*(n+1),1)
    
    Returns
    -------
    qr : rank-2 array('f') with bounds (m,n) and a storage
    jpvt : rank-1 array('i') with bounds (n)
    tau : rank-1 array('f') with bounds (MIN(m,n))
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def sgeqrf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,work,info = sgeqrf(a,[lwork,overwrite_a])
    
    Wrapper for ``sgeqrf``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    
    Returns
    -------
    qr : rank-2 array('f') with bounds (m,n) and a storage
    tau : rank-1 array('f') with bounds (MIN(m,n))
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def sgeqrfp(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,info = sgeqrfp(a,[lwork,overwrite_a])
    
    Wrapper for ``sgeqrfp``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(1, n)
    
    Returns
    -------
    qr : rank-2 array('f') with bounds (m,n) and a storage
    tau : rank-1 array('f') with bounds (MIN(m,n))
    info : int
    """
    pass

def sgeqrfp_lwork(m, n): # real signature unknown; restored from __doc__
    """
    work,info = sgeqrfp_lwork(m,n)
    
    Wrapper for ``sgeqrfp_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgeqrf_lwork(m, n): # real signature unknown; restored from __doc__
    """
    work,info = sgeqrf_lwork(m,n)
    
    Wrapper for ``sgeqrf_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgeqrt(nb, a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a,t,info = sgeqrt(nb,a,[overwrite_a])
    
    Wrapper for ``sgeqrt``.
    
    Parameters
    ----------
    nb : input int
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('f') with bounds (m,n)
    t : rank-2 array('f') with bounds (nb,MIN(m,n))
    info : int
    """
    pass

def sgerqf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,work,info = sgerqf(a,[lwork,overwrite_a])
    
    Wrapper for ``sgerqf``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*m,1)
    
    Returns
    -------
    qr : rank-2 array('f') with bounds (m,n) and a storage
    tau : rank-1 array('f') with bounds (MIN(m,n))
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def sgesc2(lu, rhs, ipiv, jpiv, overwrite_rhs=None): # real signature unknown; restored from __doc__
    """
    x,scale = sgesc2(lu,rhs,ipiv,jpiv,[overwrite_rhs])
    
    Wrapper for ``sgesc2``.
    
    Parameters
    ----------
    lu : input rank-2 array('f') with bounds (n,n)
    rhs : input rank-1 array('f') with bounds (n)
    ipiv : input rank-1 array('i') with bounds (n)
    jpiv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_rhs : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-1 array('f') with bounds (n) and rhs storage
    scale : float
    """
    pass

def sgesdd(a, compute_uv=None, full_matrices=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    u,s,vt,info = sgesdd(a,[compute_uv,full_matrices,lwork,overwrite_a])
    
    Wrapper for ``sgesdd``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    lwork : input int, optional
        Default: max((compute_uv?4*minmn*minmn+MAX(m,n)+9*minmn:MAX(14*minmn+4,10*minmn+2+25*(25+8))+MAX(m,n)),1)
    
    Returns
    -------
    u : rank-2 array('f') with bounds (u0,u1)
    s : rank-1 array('f') with bounds (minmn)
    vt : rank-2 array('f') with bounds (vt0,vt1)
    info : int
    """
    pass

def sgesdd_lwork(m, n, compute_uv=None, full_matrices=None): # real signature unknown; restored from __doc__
    """
    work,info = sgesdd_lwork(m,n,[compute_uv,full_matrices])
    
    Wrapper for ``sgesdd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgesv(a, b, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lu,piv,x,info = sgesv(a,b,[overwrite_a,overwrite_b])
    
    Wrapper for ``sgesv``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('f') with bounds (n,n) and a storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('f') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def sgesvd(a, compute_uv=None, full_matrices=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    u,s,vt,info = sgesvd(a,[compute_uv,full_matrices,lwork,overwrite_a])
    
    Wrapper for ``sgesvd``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    lwork : input int, optional
        Default: max(MAX(3*minmn+MAX(m,n),5*minmn),1)
    
    Returns
    -------
    u : rank-2 array('f') with bounds (u0,u1)
    s : rank-1 array('f') with bounds (minmn)
    vt : rank-2 array('f') with bounds (vt0,vt1)
    info : int
    """
    pass

def sgesvd_lwork(m, n, compute_uv=None, full_matrices=None): # real signature unknown; restored from __doc__
    """
    work,info = sgesvd_lwork(m,n,[compute_uv,full_matrices])
    
    Wrapper for ``sgesvd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgesvx(a, b, fact=None, trans=None, af=None, ipiv=None, equed=None, r=None, c=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = sgesvx(a,b,[fact,trans,af,ipiv,equed,r,c,overwrite_a,overwrite_b])
    
    Wrapper for ``sgesvx``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    fact : input string(len=1), optional
        Default: 'E'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_a : input int, optional
        Default: 0
    af : input rank-2 array('f') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    equed : input string(len=1), optional
        Default: 'B'
    r : input rank-1 array('f') with bounds (n)
    c : input rank-1 array('f') with bounds (n)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    as : rank-2 array('f') with bounds (n,n) and a storage
    lu : rank-2 array('f') with bounds (n,n) and af storage
    ipiv : rank-1 array('i') with bounds (n)
    equed : string(len=1)
    rs : rank-1 array('f') with bounds (n) and r storage
    cs : rank-1 array('f') with bounds (n) and c storage
    bs : rank-2 array('f') with bounds (n,nrhs) and b storage
    x : rank-2 array('f') with bounds (n,nrhs)
    rcond : float
    ferr : rank-1 array('f') with bounds (nrhs)
    berr : rank-1 array('f') with bounds (nrhs)
    info : int
    """
    pass

def sgetc2(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    lu,ipiv,jpiv,info = sgetc2(a,[overwrite_a])
    
    Wrapper for ``sgetc2``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('f') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    jpiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def sgetrf(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    lu,piv,info = sgetrf(a,[overwrite_a])
    
    Wrapper for ``sgetrf``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('f') with bounds (m,n) and a storage
    piv : rank-1 array('i') with bounds (MIN(m,n))
    info : int
    """
    pass

def sgetri(lu, piv, lwork=None, overwrite_lu=None): # real signature unknown; restored from __doc__
    """
    inv_a,info = sgetri(lu,piv,[lwork,overwrite_lu])
    
    Wrapper for ``sgetri``.
    
    Parameters
    ----------
    lu : input rank-2 array('f') with bounds (n,n)
    piv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_lu : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    
    Returns
    -------
    inv_a : rank-2 array('f') with bounds (n,n) and lu storage
    info : int
    """
    pass

def sgetri_lwork(n): # real signature unknown; restored from __doc__
    """
    work,info = sgetri_lwork(n)
    
    Wrapper for ``sgetri_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgetrs(lu, piv, b, trans=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = sgetrs(lu,piv,b,[trans,overwrite_b])
    
    Wrapper for ``sgetrs``.
    
    Parameters
    ----------
    lu : input rank-2 array('f') with bounds (n,n)
    piv : input rank-1 array('i') with bounds (n)
    b : input rank-2 array('f') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def sgges(sselect, a, b, jobvsl=None, jobvsr=None, sort_t=None, ldvsl=None, ldvsr=None, lwork=None, sselect_extra_args=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,b,sdim,alphar,alphai,beta,vsl,vsr,work,info = sgges(sselect,a,b,[jobvsl,jobvsr,sort_t,ldvsl,ldvsr,lwork,sselect_extra_args,overwrite_a,overwrite_b])
    
    Wrapper for ``sgges``.
    
    Parameters
    ----------
    sselect : call-back function
    a : input rank-2 array('f') with bounds (lda,n)
    b : input rank-2 array('f') with bounds (ldb,n)
    
    Other Parameters
    ----------------
    jobvsl : input int, optional
        Default: 1
    jobvsr : input int, optional
        Default: 1
    sort_t : input int, optional
        Default: 0
    sselect_extra_args : input tuple, optional
        Default: ()
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    ldvsl : input int, optional
        Default: ((jobvsl==1)?n:1)
    ldvsr : input int, optional
        Default: ((jobvsr==1)?n:1)
    lwork : input int, optional
        Default: max(8*n+16,1)
    
    Returns
    -------
    a : rank-2 array('f') with bounds (lda,n)
    b : rank-2 array('f') with bounds (ldb,n)
    sdim : int
    alphar : rank-1 array('f') with bounds (n)
    alphai : rank-1 array('f') with bounds (n)
    beta : rank-1 array('f') with bounds (n)
    vsl : rank-2 array('f') with bounds (ldvsl,n)
    vsr : rank-2 array('f') with bounds (ldvsr,n)
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def sselect(alphar,alphai,beta): return sselect
      Required arguments:
        alphar : input float
        alphai : input float
        beta : input float
      Return objects:
        sselect : int
    """
    pass

def sggev(a, b, compute_vl=None, compute_vr=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    alphar,alphai,beta,vl,vr,work,info = sggev(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``sggev``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(8*n,1)
    
    Returns
    -------
    alphar : rank-1 array('f') with bounds (n)
    alphai : rank-1 array('f') with bounds (n)
    beta : rank-1 array('f') with bounds (n)
    vl : rank-2 array('f') with bounds (ldvl,n)
    vr : rank-2 array('f') with bounds (ldvr,n)
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def sgglse(a, b, c, d, lwork=None, overwrite_a=None, overwrite_b=None, overwrite_c=None, overwrite_d=None): # real signature unknown; restored from __doc__
    """
    t,r,res,x,info = sgglse(a,b,c,d,[lwork,overwrite_a,overwrite_b,overwrite_c,overwrite_d])
    
    Wrapper for ``sgglse``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    b : input rank-2 array('f') with bounds (p,n)
    c : input rank-1 array('f') with bounds (m)
    d : input rank-1 array('f') with bounds (p)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    overwrite_c : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(m+n+p,1)
    
    Returns
    -------
    t : rank-2 array('f') with bounds (m,n) and a storage
    r : rank-2 array('f') with bounds (p,n) and b storage
    res : rank-1 array('f') with bounds (m) and c storage
    x : rank-1 array('f') with bounds (n)
    info : int
    """
    pass

def sgglse_lwork(m, n, p): # real signature unknown; restored from __doc__
    """
    work,info = sgglse_lwork(m,n,p)
    
    Wrapper for ``sgglse_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    p : input int
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sgtsv(dl, d, du, b, overwrite_dl=None, overwrite_d=None, overwrite_du=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    du2,d,du,x,info = sgtsv(dl,d,du,b,[overwrite_dl,overwrite_d,overwrite_du,overwrite_b])
    
    Wrapper for ``sgtsv``.
    
    Parameters
    ----------
    dl : input rank-1 array('f') with bounds (n - 1)
    d : input rank-1 array('f') with bounds (n)
    du : input rank-1 array('f') with bounds (n - 1)
    b : input rank-2 array('f') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_dl : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    overwrite_du : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    du2 : rank-1 array('f') with bounds (n - 1) and dl storage
    d : rank-1 array('f') with bounds (n)
    du : rank-1 array('f') with bounds (n - 1)
    x : rank-2 array('f') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def sgtsvx(dl, d, du, b, fact=None, trans=None, dlf=None, df=None, duf=None, du2=None, ipiv=None): # real signature unknown; restored from __doc__
    """
    dlf,df,duf,du2,ipiv,x,rcond,ferr,berr,info = sgtsvx(dl,d,du,b,[fact,trans,dlf,df,duf,du2,ipiv])
    
    Wrapper for ``sgtsvx``.
    
    Parameters
    ----------
    dl : input rank-1 array('f') with bounds (MAX(0, n-1))
    d : input rank-1 array('f') with bounds (n)
    du : input rank-1 array('f') with bounds (MAX(0, n-1))
    b : input rank-2 array('f') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    fact : input string(len=1), optional
        Default: 'N'
    trans : input string(len=1), optional
        Default: 'N'
    dlf : input rank-1 array('f') with bounds (MAX(0,n-1))
    df : input rank-1 array('f') with bounds (n)
    duf : input rank-1 array('f') with bounds (MAX(0,n-1))
    du2 : input rank-1 array('f') with bounds (MAX(0,n-2))
    ipiv : input rank-1 array('i') with bounds (n)
    
    Returns
    -------
    dlf : rank-1 array('f') with bounds (MAX(0,n-1))
    df : rank-1 array('f') with bounds (n)
    duf : rank-1 array('f') with bounds (MAX(0,n-1))
    du2 : rank-1 array('f') with bounds (MAX(0,n-2))
    ipiv : rank-1 array('i') with bounds (n)
    x : rank-2 array('f') with bounds (ldx,nrhs)
    rcond : float
    ferr : rank-1 array('f') with bounds (nrhs)
    berr : rank-1 array('f') with bounds (nrhs)
    info : int
    """
    pass

def sgttrf(dl, d, du, overwrite_dl=None, overwrite_d=None, overwrite_du=None): # real signature unknown; restored from __doc__
    """
    dl,d,du,du2,ipiv,info = sgttrf(dl,d,du,[overwrite_dl,overwrite_d,overwrite_du])
    
    Wrapper for ``sgttrf``.
    
    Parameters
    ----------
    dl : input rank-1 array('f') with bounds (n - 1)
    d : input rank-1 array('f') with bounds (n)
    du : input rank-1 array('f') with bounds (n - 1)
    
    Other Parameters
    ----------------
    overwrite_dl : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    overwrite_du : input int, optional
        Default: 0
    
    Returns
    -------
    dl : rank-1 array('f') with bounds (n - 1)
    d : rank-1 array('f') with bounds (n)
    du : rank-1 array('f') with bounds (n - 1)
    du2 : rank-1 array('f') with bounds (n - 2)
    ipiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def sgttrs(dl, d, du, du2, ipiv, b, trans=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = sgttrs(dl,d,du,du2,ipiv,b,[trans,overwrite_b])
    
    Wrapper for ``sgttrs``.
    
    Parameters
    ----------
    dl : input rank-1 array('f') with bounds (n - 1)
    d : input rank-1 array('f') with bounds (n)
    du : input rank-1 array('f') with bounds (n - 1)
    du2 : input rank-1 array('f') with bounds (n - 2)
    ipiv : input rank-1 array('i') with bounds (n)
    b : input rank-2 array('f') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def slamch(cmach): # real signature unknown; restored from __doc__
    """
    slamch = slamch(cmach)
    
    Wrapper for ``slamch``.
    
    Parameters
    ----------
    cmach : input string(len=1)
    
    Returns
    -------
    slamch : float
    """
    pass

def slange(norm, a): # real signature unknown; restored from __doc__
    """
    n2 = slange(norm,a)
    
    Wrapper for ``slange``.
    
    Parameters
    ----------
    norm : input string(len=1)
    a : input rank-2 array('f') with bounds (m,n)
    
    Returns
    -------
    n2 : float
    """
    pass

def slarf(v, tau, c, work, side=None, incv=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = slarf(v,tau,c,work,[side,incv,overwrite_c])
    
    Wrapper for ``slarf``.
    
    Parameters
    ----------
    v : input rank-1 array('f') with bounds ((side[0]=='L'?(1 + (m-1)*abs(incv)):(1 + (n-1)*abs(incv))))
    tau : input float
    c : input rank-2 array('f') with bounds (m,n)
    work : input rank-1 array('f') with bounds (lwork)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    incv : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (m,n)
    """
    pass

def slarfg(n, alpha, x, incx=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    alpha,x,tau = slarfg(n,alpha,x,[incx,overwrite_x])
    
    Wrapper for ``slarfg``.
    
    Parameters
    ----------
    n : input int
    alpha : input float
    x : input rank-1 array('f') with bounds (lx)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    alpha : float
    x : rank-1 array('f') with bounds (lx)
    tau : float
    """
    pass

def slartg(f, g): # real signature unknown; restored from __doc__
    """
    cs,sn,r = slartg(f,g)
    
    Wrapper for ``slartg``.
    
    Parameters
    ----------
    f : input float
    g : input float
    
    Returns
    -------
    cs : float
    sn : float
    r : float
    """
    pass

def slasd4(i, d, z, rho=None): # real signature unknown; restored from __doc__
    """
    delta,sigma,work,info = slasd4(i,d,z,[rho])
    
    Wrapper for ``slasd4``.
    
    Parameters
    ----------
    i : input int
    d : input rank-1 array('f') with bounds (n)
    z : input rank-1 array('f') with bounds (n)
    
    Other Parameters
    ----------------
    rho : input float, optional
        Default: 1.0
    
    Returns
    -------
    delta : rank-1 array('f') with bounds (n)
    sigma : float
    work : rank-1 array('f') with bounds (n)
    info : int
    """
    pass

def slaswp(a, piv, k1=None, k2=None, off=None, inc=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = slaswp(a,piv,[k1,k2,off,inc,overwrite_a])
    
    Wrapper for ``slaswp``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (nrows,n)
    piv : input rank-1 array('i') with bounds (npiv)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    k1 : input int, optional
        Default: 0
    k2 : input int, optional
        Default: npiv-1
    off : input int, optional
        Default: 0
    inc : input int, optional
        Default: 1
    
    Returns
    -------
    a : rank-2 array('f') with bounds (nrows,n)
    """
    pass

def slauum(c, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    a,info = slauum(c,[lower,overwrite_c])
    
    Wrapper for ``slauum``.
    
    Parameters
    ----------
    c : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('f') with bounds (n,n) and c storage
    info : int
    """
    pass

def sorcsd(x11, x12, x21, x22, compute_u1=None, compute_u2=None, compute_v1t=None, compute_v2t=None, trans=None, signs=None, lwork=None, overwrite_x11=None, overwrite_x12=None, overwrite_x21=None, overwrite_x22=None): # real signature unknown; restored from __doc__
    """
    cs11,cs12,cs21,cs22,theta,u1,u2,v1t,v2t,info = sorcsd(x11,x12,x21,x22,[compute_u1,compute_u2,compute_v1t,compute_v2t,trans,signs,lwork,overwrite_x11,overwrite_x12,overwrite_x21,overwrite_x22])
    
    Wrapper for ``sorcsd``.
    
    Parameters
    ----------
    x11 : input rank-2 array('f') with bounds (p,q)
    x12 : input rank-2 array('f') with bounds (p,mmq)
    x21 : input rank-2 array('f') with bounds (mmp,q)
    x22 : input rank-2 array('f') with bounds (mmp,mmq)
    
    Other Parameters
    ----------------
    compute_u1 : input int, optional
        Default: 1
    compute_u2 : input int, optional
        Default: 1
    compute_v1t : input int, optional
        Default: 1
    compute_v2t : input int, optional
        Default: 1
    trans : input int, optional
        Default: 0
    signs : input int, optional
        Default: 0
    overwrite_x11 : input int, optional
        Default: 0
    overwrite_x12 : input int, optional
        Default: 0
    overwrite_x21 : input int, optional
        Default: 0
    overwrite_x22 : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 2+2*m+5*MAX(1,q-1)+4*MAX(1,q)+8*q
    
    Returns
    -------
    cs11 : rank-2 array('f') with bounds (p,q) and x11 storage
    cs12 : rank-2 array('f') with bounds (p,mmq) and x12 storage
    cs21 : rank-2 array('f') with bounds (mmp,q) and x21 storage
    cs22 : rank-2 array('f') with bounds (mmp,mmq) and x22 storage
    theta : rank-1 array('f') with bounds (min(min(p,mmp),min(q,mmq)))
    u1 : rank-2 array('f') with bounds ((compute_u1?p:0),(compute_u1?p:0))
    u2 : rank-2 array('f') with bounds ((compute_u2?mmp:0),(compute_u2?mmp:0))
    v1t : rank-2 array('f') with bounds ((compute_v1t?q:0),(compute_v1t?q:0))
    v2t : rank-2 array('f') with bounds ((compute_v2t?mmq:0),(compute_v2t?mmq:0))
    info : int
    """
    pass

def sorcsd_lwork(m, p, q): # real signature unknown; restored from __doc__
    """
    work,info = sorcsd_lwork(m,p,q)
    
    Wrapper for ``sorcsd_lwork``.
    
    Parameters
    ----------
    m : input int
    p : input int
    q : input int
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sorghr(a, tau, lo=None, hi=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ht,info = sorghr(a,tau,[lo,hi,lwork,overwrite_a])
    
    Wrapper for ``sorghr``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    tau : input rank-1 array('f') with bounds (n - 1)
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(hi-lo,1)
    
    Returns
    -------
    ht : rank-2 array('f') with bounds (n,n) and a storage
    info : int
    """
    pass

def sorghr_lwork(n, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    work,info = sorghr_lwork(n,[lo,hi])
    
    Wrapper for ``sorghr_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def sorgqr(a, tau, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    q,work,info = sorgqr(a,tau,[lwork,overwrite_a])
    
    Wrapper for ``sorgqr``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    tau : input rank-1 array('f') with bounds (k)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    
    Returns
    -------
    q : rank-2 array('f') with bounds (m,n) and a storage
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def sorgrq(a, tau, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    q,work,info = sorgrq(a,tau,[lwork,overwrite_a])
    
    Wrapper for ``sorgrq``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    tau : input rank-1 array('f') with bounds (k)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*m,1)
    
    Returns
    -------
    q : rank-2 array('f') with bounds (m,n) and a storage
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def sormqr(side, trans, a, tau, c, lwork, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    cq,work,info = sormqr(side,trans,a,tau,c,lwork,[overwrite_c])
    
    Wrapper for ``sormqr``.
    
    Parameters
    ----------
    side : input string(len=1)
    trans : input string(len=1)
    a : input rank-2 array('f') with bounds (lda,k)
    tau : input rank-1 array('f') with bounds (k)
    c : input rank-2 array('f') with bounds (ldc,n)
    lwork : input int
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    cq : rank-2 array('f') with bounds (ldc,n) and c storage
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def sormrz(a, tau, c, side=None, trans=None, lwork=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    cq,info = sormrz(a,tau,c,[side,trans,lwork,overwrite_c])
    
    Wrapper for ``sormrz``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (k,nt)
    tau : input rank-1 array('f') with bounds (k)
    c : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_c : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX((side[0]=='L'?n:m),1)
    
    Returns
    -------
    cq : rank-2 array('f') with bounds (m,n) and c storage
    info : int
    """
    pass

def sormrz_lwork(m, n, side=None, trans=None): # real signature unknown; restored from __doc__
    """
    work,info = sormrz_lwork(m,n,[side,trans])
    
    Wrapper for ``sormrz_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    trans : input string(len=1), optional
        Default: 'N'
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def spbsv(ab, b, lower=None, ldab=None, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    c,x,info = spbsv(ab,b,[lower,ldab,overwrite_ab,overwrite_b])
    
    Wrapper for ``spbsv``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,n)
    b : input rank-2 array('f') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (ldab,n) and ab storage
    x : rank-2 array('f') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def spbtrf(ab, lower=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    c,info = spbtrf(ab,[lower,ldab,overwrite_ab])
    
    Wrapper for ``spbtrf``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    
    Returns
    -------
    c : rank-2 array('f') with bounds (ldab,n) and ab storage
    info : int
    """
    pass

def spbtrs(ab, b, lower=None, ldab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = spbtrs(ab,b,[lower,ldab,overwrite_b])
    
    Wrapper for ``spbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,n)
    b : input rank-2 array('f') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def spftrf(n, a, transr=None, uplo=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    achol,info = spftrf(n,a,[transr,uplo,overwrite_a])
    
    Wrapper for ``spftrf``.
    
    Parameters
    ----------
    n : input int
    a : input rank-1 array('f') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    achol : rank-1 array('f') with bounds (nt) and a storage
    info : int
    """
    pass

def spftri(n, a, transr=None, uplo=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ainv,info = spftri(n,a,[transr,uplo,overwrite_a])
    
    Wrapper for ``spftri``.
    
    Parameters
    ----------
    n : input int
    a : input rank-1 array('f') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    ainv : rank-1 array('f') with bounds (nt) and a storage
    info : int
    """
    pass

def spftrs(n, a, b, transr=None, uplo=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = spftrs(n,a,b,[transr,uplo,overwrite_b])
    
    Wrapper for ``spftrs``.
    
    Parameters
    ----------
    n : input int
    a : input rank-1 array('f') with bounds (nt)
    b : input rank-2 array('f') with bounds (ldb,nhrs)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (ldb,nhrs) and b storage
    info : int
    """
    pass

def spocon(a, anorm, uplo=None): # real signature unknown; restored from __doc__
    """
    rcond,info = spocon(a,anorm,[uplo])
    
    Wrapper for ``spocon``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    anorm : input float
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def sposv(a, b, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    c,x,info = sposv(a,b,[lower,overwrite_a,overwrite_b])
    
    Wrapper for ``sposv``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (n,n) and a storage
    x : rank-2 array('f') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def sposvx(a, b, fact=None, af=None, equed=None, s=None, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = sposvx(a,b,[fact,af,equed,s,lower,overwrite_a,overwrite_b])
    
    Wrapper for ``sposvx``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    fact : input string(len=1), optional
        Default: 'E'
    overwrite_a : input int, optional
        Default: 0
    af : input rank-2 array('f') with bounds (n,n)
    equed : input string(len=1), optional
        Default: 'Y'
    s : input rank-1 array('f') with bounds (n)
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    a_s : rank-2 array('f') with bounds (n,n) and a storage
    lu : rank-2 array('f') with bounds (n,n) and af storage
    equed : string(len=1)
    s : rank-1 array('f') with bounds (n)
    b_s : rank-2 array('f') with bounds (n,nrhs) and b storage
    x : rank-2 array('f') with bounds (n,nrhs)
    rcond : float
    ferr : rank-1 array('f') with bounds (nrhs)
    berr : rank-1 array('f') with bounds (nrhs)
    info : int
    """
    pass

def spotrf(a, lower=None, clean=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,info = spotrf(a,[lower,clean,overwrite_a])
    
    Wrapper for ``spotrf``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    clean : input int, optional
        Default: 1
    
    Returns
    -------
    c : rank-2 array('f') with bounds (n,n) and a storage
    info : int
    """
    pass

def spotri(c, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    inv_a,info = spotri(c,[lower,overwrite_c])
    
    Wrapper for ``spotri``.
    
    Parameters
    ----------
    c : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    inv_a : rank-2 array('f') with bounds (n,n) and c storage
    info : int
    """
    pass

def spotrs(c, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = spotrs(c,b,[lower,overwrite_b])
    
    Wrapper for ``spotrs``.
    
    Parameters
    ----------
    c : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def sppcon(n, ap, anorm, lower=None): # real signature unknown; restored from __doc__
    """
    rcond,info = sppcon(n,ap,anorm,[lower])
    
    Wrapper for ``sppcon``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('f') with bounds (L)
    anorm : input float
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def sppsv(n, ap, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = sppsv(n,ap,b,[lower,overwrite_b])
    
    Wrapper for ``sppsv``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('f') with bounds (L)
    b : input rank-2 array('f') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def spptrf(n, ap, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    ul,info = spptrf(n,ap,[lower,overwrite_ap])
    
    Wrapper for ``spptrf``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('f') with bounds (L)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    
    Returns
    -------
    ul : rank-1 array('f') with bounds (L) and ap storage
    info : int
    """
    pass

def spptri(n, ap, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    uli,info = spptri(n,ap,[lower,overwrite_ap])
    
    Wrapper for ``spptri``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('f') with bounds (L)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    
    Returns
    -------
    uli : rank-1 array('f') with bounds (L) and ap storage
    info : int
    """
    pass

def spptrs(n, ap, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = spptrs(n,ap,b,[lower,overwrite_b])
    
    Wrapper for ``spptrs``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('f') with bounds (L)
    b : input rank-2 array('f') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def spstf2(a, tol=None, lower=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,piv,rank_c,info = spstf2(a,[tol,lower,overwrite_a])
    
    Wrapper for ``spstf2``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    tol : input float, optional
        Default: -1.0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (n,n) and a storage
    piv : rank-1 array('i') with bounds (n)
    rank_c : int
    info : int
    """
    pass

def spstrf(a, tol=None, lower=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,piv,rank_c,info = spstrf(a,[tol,lower,overwrite_a])
    
    Wrapper for ``spstrf``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    tol : input float, optional
        Default: -1.0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (n,n) and a storage
    piv : rank-1 array('i') with bounds (n)
    rank_c : int
    info : int
    """
    pass

def spteqr(d, e, z, compute_z=None, overwrite_d=None, overwrite_e=None, overwrite_z=None): # real signature unknown; restored from __doc__
    """
    d,e,z,info = spteqr(d,e,z,[compute_z,overwrite_d,overwrite_e,overwrite_z])
    
    Wrapper for ``spteqr``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (n)
    e : input rank-1 array('f') with bounds ((n>0?n-1:0))
    z : input rank-2 array('f') with bounds ((compute_z==0?shape(z, 0):max(1,n)),(compute_z==0?shape(z, 1):n))
    
    Other Parameters
    ----------------
    compute_z : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    overwrite_z : input int, optional
        Default: 0
    
    Returns
    -------
    d : rank-1 array('f') with bounds (n)
    e : rank-1 array('f') with bounds ((n>0?n-1:0))
    z : rank-2 array('f') with bounds ((compute_z==0?shape(z, 0):max(1,n)),(compute_z==0?shape(z, 1):n))
    info : int
    """
    pass

def sptsv(d, e, b, overwrite_d=None, overwrite_e=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    d,du,x,info = sptsv(d,e,b,[overwrite_d,overwrite_e,overwrite_b])
    
    Wrapper for ``sptsv``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (n)
    e : input rank-1 array('f') with bounds (n - 1)
    b : input rank-2 array('f') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    d : rank-1 array('f') with bounds (n)
    du : rank-1 array('f') with bounds (n - 1) and e storage
    x : rank-2 array('f') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def sptsvx(d, e, b, fact=None, df=None, ef=None): # real signature unknown; restored from __doc__
    """
    df,ef,x,rcond,ferr,berr,info = sptsvx(d,e,b,[fact,df,ef])
    
    Wrapper for ``sptsvx``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (n)
    e : input rank-1 array('f') with bounds (max(0, n-1))
    b : input rank-2 array('f') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    fact : input string(len=1), optional
        Default: 'N'
    df : input rank-1 array('f') with bounds (n)
    ef : input rank-1 array('f') with bounds (max(0, n-1))
    
    Returns
    -------
    df : rank-1 array('f') with bounds (n)
    ef : rank-1 array('f') with bounds (max(0, n-1))
    x : rank-2 array('f') with bounds (ldx,nrhs)
    rcond : float
    ferr : rank-1 array('f') with bounds (nrhs)
    berr : rank-1 array('f') with bounds (nrhs)
    info : int
    """
    pass

def spttrf(d, e, overwrite_d=None, overwrite_e=None): # real signature unknown; restored from __doc__
    """
    d,e,info = spttrf(d,e,[overwrite_d,overwrite_e])
    
    Wrapper for ``spttrf``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (n)
    e : input rank-1 array('f') with bounds ((n>0?n-1:0))
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    
    Returns
    -------
    d : rank-1 array('f') with bounds (n)
    e : rank-1 array('f') with bounds ((n>0?n-1:0))
    info : int
    """
    pass

def spttrs(d, e, b, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = spttrs(d,e,b,[overwrite_b])
    
    Wrapper for ``spttrs``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (n)
    e : input rank-1 array('f') with bounds ((n>0?n-1:0))
    b : input rank-2 array('f') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def ssbev(ab, compute_v=None, lower=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,info = ssbev(ab,[compute_v,lower,ldab,overwrite_ab])
    
    Wrapper for ``ssbev``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,n)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('f') with bounds (ldz,ldz)
    info : int
    """
    pass

def ssbevd(ab, compute_v=None, lower=None, ldab=None, liwork=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,info = ssbevd(ab,[compute_v,lower,ldab,liwork,overwrite_ab])
    
    Wrapper for ``ssbevd``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,n)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    liwork : input int, optional
        Default: (compute_v?3+5*n:1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('f') with bounds (ldz,ldz)
    info : int
    """
    pass

def ssbevx(ab, vl, vu, il, iu, ldab=None, compute_v=None, range=None, lower=None, abstol=None, mmax=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,m,ifail,info = ssbevx(ab,vl,vu,il,iu,[ldab,compute_v,range,lower,abstol,mmax,overwrite_ab])
    
    Wrapper for ``ssbevx``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,n)
    vl : input float
    vu : input float
    il : input int
    iu : input int
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    ldab : input int, optional
        Default: shape(ab,0)
    compute_v : input int, optional
        Default: 1
    range : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    abstol : input float, optional
        Default: 0.0
    mmax : input int, optional
        Default: (compute_v?(range==2?(iu-il+1):n):1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('f') with bounds (ldz,mmax)
    m : int
    ifail : rank-1 array('i') with bounds ((compute_v?n:1))
    info : int
    """
    pass

def ssfrk(n, k, alpha, a, beta, c, transr=None, uplo=None, trans=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    cout = ssfrk(n,k,alpha,a,beta,c,[transr,uplo,trans,overwrite_c])
    
    Wrapper for ``ssfrk``.
    
    Parameters
    ----------
    n : input int
    k : input int
    alpha : input float
    a : input rank-2 array('f') with bounds (lda,ka)
    beta : input float
    c : input rank-1 array('f') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    cout : rank-1 array('f') with bounds (nt) and c storage
    """
    pass

def sstebz(d, e, range, vl, vu, il, iu, tol, order): # real signature unknown; restored from __doc__
    """
    m,w,iblock,isplit,info = sstebz(d,e,range,vl,vu,il,iu,tol,order)
    
    Wrapper for ``sstebz``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (n)
    e : input rank-1 array('f') with bounds (n - 1)
    range : input int
    vl : input float
    vu : input float
    il : input int
    iu : input int
    tol : input float
    order : input string(len=1)
    
    Returns
    -------
    m : int
    w : rank-1 array('f') with bounds (n)
    iblock : rank-1 array('i') with bounds (n)
    isplit : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def sstein(d, e, w, iblock, isplit): # real signature unknown; restored from __doc__
    """
    z,info = sstein(d,e,w,iblock,isplit)
    
    Wrapper for ``sstein``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (n)
    e : input rank-1 array('f') with bounds (n - 1)
    w : input rank-1 array('f') with bounds (m)
    iblock : input rank-1 array('i') with bounds (n)
    isplit : input rank-1 array('i') with bounds (n)
    
    Returns
    -------
    z : rank-2 array('f') with bounds (ldz,m)
    info : int
    """
    pass

def sstemr(d, e, range, vl, vu, il, iu, compute_v=None, lwork=None, liwork=None, overwrite_d=None): # real signature unknown; restored from __doc__
    """
    m,w,z,info = sstemr(d,e,range,vl,vu,il,iu,[compute_v,lwork,liwork,overwrite_d])
    
    Wrapper for ``sstemr``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (n)
    e : input rank-1 array('f') with bounds (n)
    range : input int
    vl : input float
    vu : input float
    il : input int
    iu : input int
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    compute_v : input int, optional
        Default: 1
    lwork : input int, optional
        Default: max((compute_v?18*n:12*n),1)
    liwork : input int, optional
        Default: (compute_v?10*n:8*n)
    
    Returns
    -------
    m : int
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('f') with bounds (n,n)
    info : int
    """
    pass

def sstemr_lwork(d, e, range, vl, vu, il, iu, compute_v=None, overwrite_d=None, overwrite_e=None): # real signature unknown; restored from __doc__
    """
    work,iwork,info = sstemr_lwork(d,e,range,vl,vu,il,iu,[compute_v,overwrite_d,overwrite_e])
    
    Wrapper for ``sstemr_lwork``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (n)
    e : input rank-1 array('f') with bounds (n)
    range : input int
    vl : input float
    vu : input float
    il : input int
    iu : input int
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    compute_v : input int, optional
        Default: 1
    
    Returns
    -------
    work : float
    iwork : int
    info : int
    """
    pass

def ssterf(d, e, overwrite_d=None, overwrite_e=None): # real signature unknown; restored from __doc__
    """
    vals,info = ssterf(d,e,[overwrite_d,overwrite_e])
    
    Wrapper for ``ssterf``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (n)
    e : input rank-1 array('f') with bounds (n - 1)
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    
    Returns
    -------
    vals : rank-1 array('f') with bounds (n) and d storage
    info : int
    """
    pass

def sstev(d, e, compute_v=None, overwrite_d=None, overwrite_e=None): # real signature unknown; restored from __doc__
    """
    vals,z,info = sstev(d,e,[compute_v,overwrite_d,overwrite_e])
    
    Wrapper for ``sstev``.
    
    Parameters
    ----------
    d : input rank-1 array('f') with bounds (n)
    e : input rank-1 array('f') with bounds (MAX(n-1,1))
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    compute_v : input int, optional
        Default: 1
    
    Returns
    -------
    vals : rank-1 array('f') with bounds (n) and d storage
    z : rank-2 array('f') with bounds (ldz,(compute_v?n:1))
    info : int
    """
    pass

def ssycon(a, ipiv, anorm, lower=None): # real signature unknown; restored from __doc__
    """
    rcond,info = ssycon(a,ipiv,anorm,[lower])
    
    Wrapper for ``ssycon``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    anorm : input float
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def ssyconv(a, ipiv, lower=None, way=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a,e,info = ssyconv(a,ipiv,[lower,way,overwrite_a])
    
    Wrapper for ``ssyconv``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    way : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('f') with bounds (n,n)
    e : rank-1 array('f') with bounds (n)
    info : int
    """
    pass

def ssyequb(a, lower=None): # real signature unknown; restored from __doc__
    """
    s,scond,amax,info = ssyequb(a,[lower])
    
    Wrapper for ``ssyequb``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (lda,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    s : rank-1 array('f') with bounds (n)
    scond : float
    amax : float
    info : int
    """
    pass

def ssyev(a, compute_v=None, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,v,info = ssyev(a,[compute_v,lower,lwork,overwrite_a])
    
    Wrapper for ``ssyev``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n-1,1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    v : rank-2 array('f') with bounds (n,n) and a storage
    info : int
    """
    pass

def ssyevd(a, compute_v=None, lower=None, lwork=None, liwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,v,info = ssyevd(a,[compute_v,lower,lwork,liwork,overwrite_a])
    
    Wrapper for ``ssyevd``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max((compute_v?1+6*n+2*n*n:2*n+1),1)
    liwork : input int, optional
        Default: (compute_v?3+5*n:1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    v : rank-2 array('f') with bounds (n,n) and a storage
    info : int
    """
    pass

def ssyevd_lwork(n, compute_v=None, lower=None): # real signature unknown; restored from __doc__
    """
    work,iwork,info = ssyevd_lwork(n,[compute_v,lower])
    
    Wrapper for ``ssyevd_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : float
    iwork : int
    info : int
    """
    pass

def ssyevr(a, compute_v=None, range=None, lower=None, vl=None, vu=None, il=None, iu=None, abstol=None, lwork=None, liwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,z,m,isuppz,info = ssyevr(a,[compute_v,range,lower,vl,vu,il,iu,abstol,lwork,liwork,overwrite_a])
    
    Wrapper for ``ssyevr``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds ``(n,n)``
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default ``1``
    range : input string(len=1), optional
        Default ``'A'``
    lower : input int, optional
        Default ``0``
    overwrite_a : input int, optional
        Default ``0``
    vl : input float, optional
        Default ``0.0``
    vu : input float, optional
        Default ``1.0``
    il : input int, optional
        Default ``1``
    iu : input int, optional
        Default ``n``
    abstol : input float, optional
        Default ``0.0``
    lwork : input int, optional
        Default ``max(26*n,1)``
    liwork : input int, optional
        Default ``max(1,10*n)``
    
    Returns
    -------
    w : rank-1 array('f') with bounds ``(n)``
    z : rank-2 array('f') with bounds ``((compute_v?MAX(0,n):0),(compute_v?((*range=='I')?(iu-il+1):MAX(1,n)):0))``
    m : int
    isuppz : rank-1 array('i') with bounds ``((compute_v?(2*((*range=='A')||((*range=='I') && (iu-il+1==n))?n:0)):0))``
    info : int
    """
    pass

def ssyevr_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,iwork,info = ssyevr_lwork(n,[lower])
    
    Wrapper for ``ssyevr_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : float
    iwork : int
    info : int
    """
    pass

def ssyevx(a, compute_v=None, range=None, lower=None, vl=None, vu=None, il=None, iu=None, abstol=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,z,m,ifail,info = ssyevx(a,[compute_v,range,lower,vl,vu,il,iu,abstol,lwork,overwrite_a])
    
    Wrapper for ``ssyevx``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds ``(n,n)``
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default ``1``
    range : input string(len=1), optional
        Default ``'A'``
    lower : input int, optional
        Default ``0``
    overwrite_a : input int, optional
        Default ``0``
    vl : input float, optional
        Default ``0.0``
    vu : input float, optional
        Default ``1.0``
    il : input int, optional
        Default ``1``
    iu : input int, optional
        Default ``n``
    abstol : input float, optional
        Default ``0.0``
    lwork : input int, optional
        Default ``max(8*n,1)``
    
    Returns
    -------
    w : rank-1 array('f') with bounds ``(n)``
    z : rank-2 array('f') with bounds ``((compute_v?MAX(0,n):0),(compute_v?((*range=='I')?(iu-il+1):MAX(1,n)):0))``
    m : int
    ifail : rank-1 array('i') with bounds ``((compute_v?n:0))``
    info : int
    """
    pass

def ssyevx_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = ssyevx_lwork(n,[lower])
    
    Wrapper for ``ssyevx_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def ssyev_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = ssyev_lwork(n,[lower])
    
    Wrapper for ``ssyev_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def ssygst(a, b, itype=None, lower=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,info = ssygst(a,b,[itype,lower,overwrite_a])
    
    Wrapper for ``ssygst``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    itype : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('f') with bounds (n,n) and a storage
    info : int
    """
    pass

def ssygv(a, b, itype=None, jobz=None, uplo=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    w,v,info = ssygv(a,b,[itype,jobz,uplo,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``ssygv``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n-1,1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    v : rank-2 array('f') with bounds (n,n) and a storage
    info : int
    """
    pass

def ssygvd(a, b, itype=None, jobz=None, uplo=None, lwork=None, liwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    w,v,info = ssygvd(a,b,[itype,jobz,uplo,lwork,liwork,overwrite_a,overwrite_b])
    
    Wrapper for ``ssygvd``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds ``(n,n)``
    b : input rank-2 array('f') with bounds ``(n,n)``
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default ``1``
    jobz : input string(len=1), optional
        Default ``'V'``
    uplo : input string(len=1), optional
        Default ``'L'``
    overwrite_a : input int, optional
        Default ``0``
    overwrite_b : input int, optional
        Default ``0``
    lwork : input int, optional
        Default ``(*jobz=='N'?2*n+1:1+6*n+2*n*n)``
    liwork : input int, optional
        Default ``(*jobz=='N'?1:5*n+3)``
    
    Returns
    -------
    w : rank-1 array('f') with bounds ``(n)``
    v : rank-2 array('f') with bounds ``(n,n)`` with ``a`` storage
    info : int
    """
    pass

def ssygvx(a, b, itype=None, jobz=None, range=None, uplo=None, vl=None, vu=None, il=None, iu=None, abstol=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    w,z,m,ifail,info = ssygvx(a,b,[itype,jobz,range,uplo,vl,vu,il,iu,abstol,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``ssygvx``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    range : input string(len=1), optional
        Default: 'A'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    vl : input float, optional
        Default: 0.0
    vu : input float, optional
        Default: 1.0
    il : input int, optional
        Default: 1
    iu : input int, optional
        Default: n
    abstol : input float, optional
        Default: 0.0
    lwork : input int, optional
        Default: max(8*n,1)
    
    Returns
    -------
    w : rank-1 array('f') with bounds (n)
    z : rank-2 array('f') with bounds ((jobz[0]=='V'?MAX(0,n):0),(jobz[0]=='V'?((range[0]=='I')?(iu-il+1):MAX(1,n)):0))
    m : int
    ifail : rank-1 array('i') with bounds ((jobz[0]=='N'?0:n))
    info : int
    """
    pass

def ssygvx_lwork(n, uplo=None): # real signature unknown; restored from __doc__
    """
    work,info = ssygvx_lwork(n,[uplo])
    
    Wrapper for ``ssygvx_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'L'
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def ssygv_lwork(n, uplo=None): # real signature unknown; restored from __doc__
    """
    work,info = ssygv_lwork(n,[uplo])
    
    Wrapper for ``ssygv_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'L'
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def ssysv(a, b, lwork=None, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    udut,ipiv,x,info = ssysv(a,b,[lwork,lower,overwrite_a,overwrite_b])
    
    Wrapper for ``ssysv``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(n,1)
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    udut : rank-2 array('f') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    x : rank-2 array('f') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def ssysvx(a, b, af=None, ipiv=None, lwork=None, factored=None, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = ssysvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])
    
    Wrapper for ``ssysvx``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    af : input rank-2 array('f') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    factored : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    a_s : rank-2 array('f') with bounds (n,n) and a storage
    udut : rank-2 array('f') with bounds (n,n) and af storage
    ipiv : rank-1 array('i') with bounds (n)
    b_s : rank-2 array('f') with bounds (n,nrhs) and b storage
    x : rank-2 array('f') with bounds (n,nrhs)
    rcond : float
    ferr : rank-1 array('f') with bounds (nrhs)
    berr : rank-1 array('f') with bounds (nrhs)
    info : int
    """
    pass

def ssysvx_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = ssysvx_lwork(n,[lower])
    
    Wrapper for ``ssysvx_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def ssysv_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = ssysv_lwork(n,[lower])
    
    Wrapper for ``ssysv_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def ssytf2(a, lower=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ldu,ipiv,info = ssytf2(a,[lower,overwrite_a])
    
    Wrapper for ``ssytf2``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    ldu : rank-2 array('f') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def ssytrd(a, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,d,e,tau,info = ssytrd(a,[lower,lwork,overwrite_a])
    
    Wrapper for ``ssytrd``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (lda,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(n,1)
    
    Returns
    -------
    c : rank-2 array('f') with bounds (lda,n) and a storage
    d : rank-1 array('f') with bounds (n)
    e : rank-1 array('f') with bounds (n - 1)
    tau : rank-1 array('f') with bounds (n - 1)
    info : int
    """
    pass

def ssytrd_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = ssytrd_lwork(n,[lower])
    
    Wrapper for ``ssytrd_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def ssytrf(a, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ldu,ipiv,info = ssytrf(a,[lower,lwork,overwrite_a])
    
    Wrapper for ``ssytrf``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(n,1)
    
    Returns
    -------
    ldu : rank-2 array('f') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def ssytrf_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = ssytrf_lwork(n,[lower])
    
    Wrapper for ``ssytrf_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def stbtrs(ab, b, uplo=None, trans=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = stbtrs(ab,b,[uplo,trans,diag,overwrite_b])
    
    Wrapper for ``stbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('f') with bounds (ldab,n)
    b : input rank-2 array('f') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'U'
    trans : input string(len=1), optional
        Default: 'N'
    diag : input string(len=1), optional
        Default: 'N'
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def stfsm(alpha, a, b, transr=None, side=None, uplo=None, trans=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x = stfsm(alpha,a,b,[transr,side,uplo,trans,diag,overwrite_b])
    
    Wrapper for ``stfsm``.
    
    Parameters
    ----------
    alpha : input float
    a : input rank-1 array('f') with bounds (nt)
    b : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    side : input string(len=1), optional
        Default: 'L'
    uplo : input string(len=1), optional
        Default: 'U'
    trans : input string(len=1), optional
        Default: 'N'
    diag : input string(len=1), optional
        Default: 'N'
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (m,n) and b storage
    """
    pass

def stfttp(n, arf, transr=None, uplo=None): # real signature unknown; restored from __doc__
    """
    ap,info = stfttp(n,arf,[transr,uplo])
    
    Wrapper for ``stfttp``.
    
    Parameters
    ----------
    n : input int
    arf : input rank-1 array('f') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    ap : rank-1 array('f') with bounds (nt)
    info : int
    """
    pass

def stfttr(n, arf, transr=None, uplo=None): # real signature unknown; restored from __doc__
    """
    a,info = stfttr(n,arf,[transr,uplo])
    
    Wrapper for ``stfttr``.
    
    Parameters
    ----------
    n : input int
    arf : input rank-1 array('f') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    a : rank-2 array('f') with bounds (lda,n)
    info : int
    """
    pass

def stgexc(a, b, q, z, ifst, ilst, wantq=None, wantz=None, lwork=None, overwrite_a=None, overwrite_b=None, overwrite_q=None, overwrite_z=None): # real signature unknown; restored from __doc__
    """
    a,b,q,z,work,info = stgexc(a,b,q,z,ifst,ilst,[wantq,wantz,lwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])
    
    Wrapper for ``stgexc``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (lda,n)
    b : input rank-2 array('f') with bounds (ldb,n)
    q : input rank-2 array('f') with bounds (ldq,n)
    z : input rank-2 array('f') with bounds (ldz,n)
    ifst : input int
    ilst : input int
    
    Other Parameters
    ----------------
    wantq : input int, optional
        Default: 1
    wantz : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    overwrite_z : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(4*n+16,1)
    
    Returns
    -------
    a : rank-2 array('f') with bounds (lda,n)
    b : rank-2 array('f') with bounds (ldb,n)
    q : rank-2 array('f') with bounds (ldq,n)
    z : rank-2 array('f') with bounds (ldz,n)
    work : rank-1 array('f') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def stgsen(select, a, b, q, z, ijob=None, wantq=None, wantz=None, lwork=None, liwork=None, overwrite_a=None, overwrite_b=None, overwrite_q=None, overwrite_z=None): # real signature unknown; restored from __doc__
    """
    as,bs,alphar,alphai,beta,qs,zs,m,pl,pr,dif,info = stgsen(select,a,b,q,z,[ijob,wantq,wantz,lwork,liwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])
    
    Wrapper for ``stgsen``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (n,n)
    q : input rank-2 array('f') with bounds (n,n)
    z : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    ijob : input int, optional
        Default: 4
    wantq : input int, optional
        Default: 1
    wantz : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    overwrite_z : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 4*n+16
    liwork : input int, optional
        Default: n+6
    
    Returns
    -------
    as : rank-2 array('f') with bounds (n,n) and a storage
    bs : rank-2 array('f') with bounds (n,n) and b storage
    alphar : rank-1 array('f') with bounds (n)
    alphai : rank-1 array('f') with bounds (n)
    beta : rank-1 array('f') with bounds (n)
    qs : rank-2 array('f') with bounds (n,n) and q storage
    zs : rank-2 array('f') with bounds (n,n) and z storage
    m : int
    pl : float
    pr : float
    dif : rank-1 array('f') with bounds (2)
    info : int
    """
    pass

def stgsen_lwork(select, a, ijob=None): # real signature unknown; restored from __doc__
    """
    work,iwork,info = stgsen_lwork(select,a,[ijob])
    
    Wrapper for ``stgsen_lwork``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    a : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    ijob : input int, optional
        Default: 4
    
    Returns
    -------
    work : float
    iwork : int
    info : int
    """
    pass

def stpmqrt(l, v, t, a, b, side=None, trans=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,b,info = stpmqrt(l,v,t,a,b,[side,trans,overwrite_a,overwrite_b])
    
    Wrapper for ``stpmqrt``.
    
    Parameters
    ----------
    l : input int
    v : input rank-2 array('f') with bounds ((side[0]=='L'?m:n),k)
    t : input rank-2 array('f') with bounds (nb,k)
    a : input rank-2 array('f') with bounds ((side[0]=='L'?k:m),(side[0]=='L'?n:k))
    b : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('f') with bounds ((side[0]=='L'?k:m),(side[0]=='L'?n:k))
    b : rank-2 array('f') with bounds (m,n)
    info : int
    """
    pass

def stpqrt(l, nb, a, b, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,b,t,info = stpqrt(l,nb,a,b,[overwrite_a,overwrite_b])
    
    Wrapper for ``stpqrt``.
    
    Parameters
    ----------
    l : input int
    nb : input int
    a : input rank-2 array('f') with bounds (n,n)
    b : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('f') with bounds (n,n)
    b : rank-2 array('f') with bounds (m,n)
    t : rank-2 array('f') with bounds (nb,n)
    info : int
    """
    pass

def stpttf(n, ap, transr=None, uplo=None): # real signature unknown; restored from __doc__
    """
    arf,info = stpttf(n,ap,[transr,uplo])
    
    Wrapper for ``stpttf``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('f') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    arf : rank-1 array('f') with bounds (nt)
    info : int
    """
    pass

def stpttr(n, ap, uplo=None): # real signature unknown; restored from __doc__
    """
    a,info = stpttr(n,ap,[uplo])
    
    Wrapper for ``stpttr``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('f') with bounds (nt)
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    a : rank-2 array('f') with bounds (n,n)
    info : int
    """
    pass

def strexc(a, q, ifst, ilst, wantq=None, overwrite_a=None, overwrite_q=None): # real signature unknown; restored from __doc__
    """
    a,q,info = strexc(a,q,ifst,ilst,[wantq,overwrite_a,overwrite_q])
    
    Wrapper for ``strexc``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (lda,n)
    q : input rank-2 array('f') with bounds (ldq,n)
    ifst : input int
    ilst : input int
    
    Other Parameters
    ----------------
    wantq : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('f') with bounds (lda,n)
    q : rank-2 array('f') with bounds (ldq,n)
    info : int
    """
    pass

def strsen(select, t, q, job=None, wantq=None, lwork=None, liwork=None, overwrite_t=None, overwrite_q=None): # real signature unknown; restored from __doc__
    """
    ts,qs,wr,wi,m,s,sep,info = strsen(select,t,q,[job,wantq,lwork,liwork,overwrite_t,overwrite_q])
    
    Wrapper for ``strsen``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    t : input rank-2 array('f') with bounds (n,n)
    q : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    job : input string(len=1), optional
        Default: 'B'
    wantq : input int, optional
        Default: 1
    overwrite_t : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(1,n)
    liwork : input int, optional
        Default: 1
    
    Returns
    -------
    ts : rank-2 array('f') with bounds (n,n) and t storage
    qs : rank-2 array('f') with bounds (n,n) and q storage
    wr : rank-1 array('f') with bounds (n)
    wi : rank-1 array('f') with bounds (n)
    m : int
    s : float
    sep : float
    info : int
    """
    pass

def strsen_lwork(select, t, job=None): # real signature unknown; restored from __doc__
    """
    work,iwork,info = strsen_lwork(select,t,[job])
    
    Wrapper for ``strsen_lwork``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    t : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    job : input string(len=1), optional
        Default: 'B'
    
    Returns
    -------
    work : float
    iwork : int
    info : int
    """
    pass

def strsyl(a, b, c, trana=None, tranb=None, isgn=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    x,scale,info = strsyl(a,b,c,[trana,tranb,isgn,overwrite_c])
    
    Wrapper for ``strsyl``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,m)
    b : input rank-2 array('f') with bounds (n,n)
    c : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    trana : input string(len=1), optional
        Default: 'N'
    tranb : input string(len=1), optional
        Default: 'N'
    isgn : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (m,n) and c storage
    scale : float
    info : int
    """
    pass

def strtri(c, lower=None, unitdiag=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    inv_c,info = strtri(c,[lower,unitdiag,overwrite_c])
    
    Wrapper for ``strtri``.
    
    Parameters
    ----------
    c : input rank-2 array('f') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    
    Returns
    -------
    inv_c : rank-2 array('f') with bounds (n,n) and c storage
    info : int
    """
    pass

def strtrs(a, b, lower=None, trans=None, unitdiag=None, lda=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = strtrs(a,b,[lower,trans,unitdiag,lda,overwrite_b])
    
    Wrapper for ``strtrs``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (lda,n)
    b : input rank-2 array('f') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    lda : input int, optional
        Default: shape(a,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('f') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def strttf(a, transr=None, uplo=None): # real signature unknown; restored from __doc__
    """
    arf,info = strttf(a,[transr,uplo])
    
    Wrapper for ``strttf``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (lda,n)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    arf : rank-1 array('f') with bounds (n*(n+1)/2)
    info : int
    """
    pass

def strttp(a, uplo=None): # real signature unknown; restored from __doc__
    """
    ap,info = strttp(a,[uplo])
    
    Wrapper for ``strttp``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (lda,n)
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    ap : rank-1 array('f') with bounds (n*(n+1)/2)
    info : int
    """
    pass

def stzrzf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    rz,tau,info = stzrzf(a,[lwork,overwrite_a])
    
    Wrapper for ``stzrzf``.
    
    Parameters
    ----------
    a : input rank-2 array('f') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(m,1)
    
    Returns
    -------
    rz : rank-2 array('f') with bounds (m,n) and a storage
    tau : rank-1 array('f') with bounds (m)
    info : int
    """
    pass

def stzrzf_lwork(m, n): # real signature unknown; restored from __doc__
    """
    work,info = stzrzf_lwork(m,n)
    
    Wrapper for ``stzrzf_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Returns
    -------
    work : float
    info : int
    """
    pass

def zgbsv(kl, ku, ab, b, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lub,piv,x,info = zgbsv(kl,ku,ab,b,[overwrite_ab,overwrite_b])
    
    Wrapper for ``zgbsv``.
    
    Parameters
    ----------
    kl : input int
    ku : input int
    ab : input rank-2 array('D') with bounds (2*kl+ku+1,n)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lub : rank-2 array('D') with bounds (2*kl+ku+1,n) and ab storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('D') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def zgbtrf(ab, kl, ku, m=None, n=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    lu,ipiv,info = zgbtrf(ab,kl,ku,[m,n,ldab,overwrite_ab])
    
    Wrapper for ``zgbtrf``.
    
    Parameters
    ----------
    ab : input rank-2 array('D') with bounds (ldab,n)
    kl : input int
    ku : input int
    
    Other Parameters
    ----------------
    m : input int, optional
        Default: shape(ab,1)
    n : input int, optional
        Default: shape(ab,1)
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: max(shape(ab,0),1)
    
    Returns
    -------
    lu : rank-2 array('D') with bounds (ldab,n) and ab storage
    ipiv : rank-1 array('i') with bounds (MIN(m,n))
    info : int
    """
    pass

def zgbtrs(ab, kl, ku, b, ipiv, trans=None, n=None, ldab=None, ldb=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = zgbtrs(ab,kl,ku,b,ipiv,[trans,n,ldab,ldb,overwrite_b])
    
    Wrapper for ``zgbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('D') with bounds (ldab,n)
    kl : input int
    ku : input int
    b : input rank-2 array('D') with bounds (ldb,nrhs)
    ipiv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    n : input int, optional
        Default: shape(ab,1)
    ldab : input int, optional
        Default: shape(ab,0)
    ldb : input int, optional
        Default: shape(b,0)
    
    Returns
    -------
    x : rank-2 array('D') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def zgebal(a, scale=None, permute=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ba,lo,hi,pivscale,info = zgebal(a,[scale,permute,overwrite_a])
    
    Wrapper for ``zgebal``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    scale : input int, optional
        Default: 0
    permute : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    ba : rank-2 array('D') with bounds (m,n) and a storage
    lo : int
    hi : int
    pivscale : rank-1 array('d') with bounds (n)
    info : int
    """
    pass

def zgecon(a, anorm, norm=None): # real signature unknown; restored from __doc__
    """
    rcond,info = zgecon(a,anorm,[norm])
    
    Wrapper for ``zgecon``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    anorm : input float
    
    Other Parameters
    ----------------
    norm : input string(len=1), optional
        Default: '1'
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def zgeequ(a): # real signature unknown; restored from __doc__
    """
    r,c,rowcnd,colcnd,amax,info = zgeequ(a)
    
    Wrapper for ``zgeequ``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Returns
    -------
    r : rank-1 array('d') with bounds (m)
    c : rank-1 array('d') with bounds (n)
    rowcnd : float
    colcnd : float
    amax : float
    info : int
    """
    pass

def zgeequb(a): # real signature unknown; restored from __doc__
    """
    r,c,rowcnd,colcnd,amax,info = zgeequb(a)
    
    Wrapper for ``zgeequb``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Returns
    -------
    r : rank-1 array('d') with bounds (m)
    c : rank-1 array('d') with bounds (n)
    rowcnd : float
    colcnd : float
    amax : float
    info : int
    """
    pass

def zgees(zselect, a, compute_v=None, sort_t=None, lwork=None, zselect_extra_args=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    t,sdim,w,vs,work,info = zgees(zselect,a,[compute_v,sort_t,lwork,zselect_extra_args,overwrite_a])
    
    Wrapper for ``zgees``.
    
    Parameters
    ----------
    zselect : call-back function
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    sort_t : input int, optional
        Default: 0
    zselect_extra_args : input tuple, optional
        Default: ()
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    
    Returns
    -------
    t : rank-2 array('D') with bounds (n,n) and a storage
    sdim : int
    w : rank-1 array('D') with bounds (n)
    vs : rank-2 array('D') with bounds (ldvs,n)
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def zselect(arg): return zselect
      Required arguments:
        arg : input complex
      Return objects:
        zselect : int
    """
    pass

def zgeev(a, compute_vl=None, compute_vr=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,vl,vr,info = zgeev(a,[compute_vl,compute_vr,lwork,overwrite_a])
    
    Wrapper for ``zgeev``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(2*n,1)
    
    Returns
    -------
    w : rank-1 array('D') with bounds (n)
    vl : rank-2 array('D') with bounds (ldvl,n)
    vr : rank-2 array('D') with bounds (ldvr,n)
    info : int
    """
    pass

def zgeev_lwork(n, compute_vl=None, compute_vr=None): # real signature unknown; restored from __doc__
    """
    work,info = zgeev_lwork(n,[compute_vl,compute_vr])
    
    Wrapper for ``zgeev_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgehrd(a, lo=None, hi=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ht,tau,info = zgehrd(a,[lo,hi,lwork,overwrite_a])
    
    Wrapper for ``zgehrd``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(n,1)
    
    Returns
    -------
    ht : rank-2 array('D') with bounds (n,n) and a storage
    tau : rank-1 array('D') with bounds (n - 1)
    info : int
    """
    pass

def zgehrd_lwork(n, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    work,info = zgehrd_lwork(n,[lo,hi])
    
    Wrapper for ``zgehrd_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgels(a, b, trans=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lqr,x,info = zgels(a,b,[trans,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``zgels``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    b : input rank-2 array('D') with bounds (MAX(m,n),nrhs)
    
    Other Parameters
    ----------------
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(MIN(m,n)+MAX(MIN(m,n),nrhs),1)
    
    Returns
    -------
    lqr : rank-2 array('D') with bounds (m,n) and a storage
    x : rank-2 array('D') with bounds (MAX(m,n),nrhs) and b storage
    info : int
    """
    pass

def zgelsd(a, b, lwork, size_rwork, size_iwork, cond=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,s,rank,info = zgelsd(a,b,lwork,size_rwork,size_iwork,[cond,overwrite_a,overwrite_b])
    
    Wrapper for ``zgelsd``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    b : input rank-2 array('D') with bounds (maxmn,nrhs)
    lwork : input int
    size_rwork : input int
    size_iwork : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    cond : input float, optional
        Default: -1.0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (maxmn,nrhs) and b storage
    s : rank-1 array('d') with bounds (minmn)
    rank : int
    info : int
    """
    pass

def zgelsd_lwork(m, n, nrhs, cond=None, lwork=None): # real signature unknown; restored from __doc__
    """
    work,rwork,iwork,info = zgelsd_lwork(m,n,nrhs,[cond,lwork])
    
    Wrapper for ``zgelsd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : complex
    rwork : float
    iwork : int
    info : int
    """
    pass

def zgelss(a, b, cond=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    v,x,s,rank,work,info = zgelss(a,b,[cond,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``zgelss``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    b : input rank-2 array('D') with bounds (maxmn,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: max(2*minmn+MAX(maxmn,nrhs),1)
    
    Returns
    -------
    v : rank-2 array('D') with bounds (m,n) and a storage
    x : rank-2 array('D') with bounds (maxmn,nrhs) and b storage
    s : rank-1 array('d') with bounds (minmn)
    rank : int
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def zgelss_lwork(m, n, nrhs, cond=None, lwork=None): # real signature unknown; restored from __doc__
    """
    work,info = zgelss_lwork(m,n,nrhs,[cond,lwork])
    
    Wrapper for ``zgelss_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    cond : input float, optional
        Default: -1.0
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgelsy(a, b, jptv, cond, lwork, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    v,x,j,rank,info = zgelsy(a,b,jptv,cond,lwork,[overwrite_a,overwrite_b])
    
    Wrapper for ``zgelsy``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    b : input rank-2 array('D') with bounds (maxmn,nrhs)
    jptv : input rank-1 array('i') with bounds (n)
    cond : input float
    lwork : input int
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    v : rank-2 array('D') with bounds (m,n) and a storage
    x : rank-2 array('D') with bounds (maxmn,nrhs) and b storage
    j : rank-1 array('i') with bounds (n) and jptv storage
    rank : int
    info : int
    """
    pass

def zgelsy_lwork(m, n, nrhs, cond, lwork=None): # real signature unknown; restored from __doc__
    """
    work,info = zgelsy_lwork(m,n,nrhs,cond,[lwork])
    
    Wrapper for ``zgelsy_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    cond : input float
    
    Other Parameters
    ----------------
    lwork : input int, optional
        Default: -1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgels_lwork(m, n, nrhs, trans=None): # real signature unknown; restored from __doc__
    """
    work,info = zgels_lwork(m,n,nrhs,[trans])
    
    Wrapper for ``zgels_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    nrhs : input int
    
    Other Parameters
    ----------------
    trans : input string(len=1), optional
        Default: 'N'
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgemqrt(v, t, c, side=None, trans=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c,info = zgemqrt(v,t,c,[side,trans,overwrite_c])
    
    Wrapper for ``zgemqrt``.
    
    Parameters
    ----------
    v : input rank-2 array('D') with bounds ((side[0]=='L'?m:n),k)
    t : input rank-2 array('D') with bounds (nb,k)
    c : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (m,n)
    info : int
    """
    pass

def zgeqp3(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,jpvt,tau,work,info = zgeqp3(a,[lwork,overwrite_a])
    
    Wrapper for ``zgeqp3``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*(n+1),1)
    
    Returns
    -------
    qr : rank-2 array('D') with bounds (m,n) and a storage
    jpvt : rank-1 array('i') with bounds (n)
    tau : rank-1 array('D') with bounds (MIN(m,n))
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def zgeqrf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,work,info = zgeqrf(a,[lwork,overwrite_a])
    
    Wrapper for ``zgeqrf``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    
    Returns
    -------
    qr : rank-2 array('D') with bounds (m,n) and a storage
    tau : rank-1 array('D') with bounds (MIN(m,n))
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def zgeqrfp(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,info = zgeqrfp(a,[lwork,overwrite_a])
    
    Wrapper for ``zgeqrfp``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(1, n)
    
    Returns
    -------
    qr : rank-2 array('D') with bounds (m,n) and a storage
    tau : rank-1 array('D') with bounds (MIN(m,n))
    info : int
    """
    pass

def zgeqrfp_lwork(m, n): # real signature unknown; restored from __doc__
    """
    work,info = zgeqrfp_lwork(m,n)
    
    Wrapper for ``zgeqrfp_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgeqrf_lwork(m, n): # real signature unknown; restored from __doc__
    """
    work,info = zgeqrf_lwork(m,n)
    
    Wrapper for ``zgeqrf_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgeqrt(nb, a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a,t,info = zgeqrt(nb,a,[overwrite_a])
    
    Wrapper for ``zgeqrt``.
    
    Parameters
    ----------
    nb : input int
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (m,n)
    t : rank-2 array('D') with bounds (nb,MIN(m,n))
    info : int
    """
    pass

def zgerqf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    qr,tau,work,info = zgerqf(a,[lwork,overwrite_a])
    
    Wrapper for ``zgerqf``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*m,1)
    
    Returns
    -------
    qr : rank-2 array('D') with bounds (m,n) and a storage
    tau : rank-1 array('D') with bounds (MIN(m,n))
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def zgesc2(lu, rhs, ipiv, jpiv, overwrite_rhs=None): # real signature unknown; restored from __doc__
    """
    x,scale = zgesc2(lu,rhs,ipiv,jpiv,[overwrite_rhs])
    
    Wrapper for ``zgesc2``.
    
    Parameters
    ----------
    lu : input rank-2 array('D') with bounds (n,n)
    rhs : input rank-1 array('D') with bounds (n)
    ipiv : input rank-1 array('i') with bounds (n)
    jpiv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_rhs : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-1 array('D') with bounds (n) and rhs storage
    scale : float
    """
    pass

def zgesdd(a, compute_uv=None, full_matrices=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    u,s,vt,info = zgesdd(a,[compute_uv,full_matrices,lwork,overwrite_a])
    
    Wrapper for ``zgesdd``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    lwork : input int, optional
        Default: max((compute_uv?2*minmn*minmn+MAX(m,n)+2*minmn:2*minmn+MAX(m,n)),1)
    
    Returns
    -------
    u : rank-2 array('D') with bounds (u0,u1)
    s : rank-1 array('d') with bounds (minmn)
    vt : rank-2 array('D') with bounds (vt0,vt1)
    info : int
    """
    pass

def zgesdd_lwork(m, n, compute_uv=None, full_matrices=None): # real signature unknown; restored from __doc__
    """
    work,info = zgesdd_lwork(m,n,[compute_uv,full_matrices])
    
    Wrapper for ``zgesdd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgesv(a, b, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    lu,piv,x,info = zgesv(a,b,[overwrite_a,overwrite_b])
    
    Wrapper for ``zgesv``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('D') with bounds (n,n) and a storage
    piv : rank-1 array('i') with bounds (n)
    x : rank-2 array('D') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def zgesvd(a, compute_uv=None, full_matrices=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    u,s,vt,info = zgesvd(a,[compute_uv,full_matrices,lwork,overwrite_a])
    
    Wrapper for ``zgesvd``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    lwork : input int, optional
        Default: MAX(2*minmn+MAX(m,n),1)
    
    Returns
    -------
    u : rank-2 array('D') with bounds (u0,u1)
    s : rank-1 array('d') with bounds (minmn)
    vt : rank-2 array('D') with bounds (vt0,vt1)
    info : int
    """
    pass

def zgesvd_lwork(m, n, compute_uv=None, full_matrices=None): # real signature unknown; restored from __doc__
    """
    work,info = zgesvd_lwork(m,n,[compute_uv,full_matrices])
    
    Wrapper for ``zgesvd_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    compute_uv : input int, optional
        Default: 1
    full_matrices : input int, optional
        Default: 1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgesvx(a, b, fact=None, trans=None, af=None, ipiv=None, equed=None, r=None, c=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    as,lu,ipiv,equed,rs,cs,bs,x,rcond,ferr,berr,info = zgesvx(a,b,[fact,trans,af,ipiv,equed,r,c,overwrite_a,overwrite_b])
    
    Wrapper for ``zgesvx``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    fact : input string(len=1), optional
        Default: 'E'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_a : input int, optional
        Default: 0
    af : input rank-2 array('D') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    equed : input string(len=1), optional
        Default: 'B'
    r : input rank-1 array('d') with bounds (n)
    c : input rank-1 array('d') with bounds (n)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    as : rank-2 array('D') with bounds (n,n) and a storage
    lu : rank-2 array('D') with bounds (n,n) and af storage
    ipiv : rank-1 array('i') with bounds (n)
    equed : string(len=1)
    rs : rank-1 array('d') with bounds (n) and r storage
    cs : rank-1 array('d') with bounds (n) and c storage
    bs : rank-2 array('D') with bounds (n,nrhs) and b storage
    x : rank-2 array('D') with bounds (n,nrhs)
    rcond : float
    ferr : rank-1 array('d') with bounds (nrhs)
    berr : rank-1 array('d') with bounds (nrhs)
    info : int
    """
    pass

def zgetc2(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    lu,ipiv,jpiv,info = zgetc2(a,[overwrite_a])
    
    Wrapper for ``zgetc2``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('D') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    jpiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def zgetrf(a, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    lu,piv,info = zgetrf(a,[overwrite_a])
    
    Wrapper for ``zgetrf``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    lu : rank-2 array('D') with bounds (m,n) and a storage
    piv : rank-1 array('i') with bounds (MIN(m,n))
    info : int
    """
    pass

def zgetri(lu, piv, lwork=None, overwrite_lu=None): # real signature unknown; restored from __doc__
    """
    inv_a,info = zgetri(lu,piv,[lwork,overwrite_lu])
    
    Wrapper for ``zgetri``.
    
    Parameters
    ----------
    lu : input rank-2 array('D') with bounds (n,n)
    piv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    overwrite_lu : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    
    Returns
    -------
    inv_a : rank-2 array('D') with bounds (n,n) and lu storage
    info : int
    """
    pass

def zgetri_lwork(n): # real signature unknown; restored from __doc__
    """
    work,info = zgetri_lwork(n)
    
    Wrapper for ``zgetri_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgetrs(lu, piv, b, trans=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = zgetrs(lu,piv,b,[trans,overwrite_b])
    
    Wrapper for ``zgetrs``.
    
    Parameters
    ----------
    lu : input rank-2 array('D') with bounds (n,n)
    piv : input rank-1 array('i') with bounds (n)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def zgges(zselect, a, b, jobvsl=None, jobvsr=None, sort_t=None, ldvsl=None, ldvsr=None, lwork=None, zselect_extra_args=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,b,sdim,alpha,beta,vsl,vsr,work,info = zgges(zselect,a,b,[jobvsl,jobvsr,sort_t,ldvsl,ldvsr,lwork,zselect_extra_args,overwrite_a,overwrite_b])
    
    Wrapper for ``zgges``.
    
    Parameters
    ----------
    zselect : call-back function
    a : input rank-2 array('D') with bounds (lda,n)
    b : input rank-2 array('D') with bounds (ldb,n)
    
    Other Parameters
    ----------------
    jobvsl : input int, optional
        Default: 1
    jobvsr : input int, optional
        Default: 1
    sort_t : input int, optional
        Default: 0
    zselect_extra_args : input tuple, optional
        Default: ()
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    ldvsl : input int, optional
        Default: ((jobvsl==1)?n:1)
    ldvsr : input int, optional
        Default: ((jobvsr==1)?n:1)
    lwork : input int, optional
        Default: max(2*n,1)
    
    Returns
    -------
    a : rank-2 array('D') with bounds (lda,n)
    b : rank-2 array('D') with bounds (ldb,n)
    sdim : int
    alpha : rank-1 array('D') with bounds (n)
    beta : rank-1 array('D') with bounds (n)
    vsl : rank-2 array('D') with bounds (ldvsl,n)
    vsr : rank-2 array('D') with bounds (ldvsr,n)
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    
    Notes
    -----
    Call-back functions::
    
      def zselect(alpha,beta): return zselect
      Required arguments:
        alpha : input complex
        beta : input complex
      Return objects:
        zselect : int
    """
    pass

def zggev(a, b, compute_vl=None, compute_vr=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    alpha,beta,vl,vr,work,info = zggev(a,b,[compute_vl,compute_vr,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``zggev``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_vl : input int, optional
        Default: 1
    compute_vr : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(2*n,1)
    
    Returns
    -------
    alpha : rank-1 array('D') with bounds (n)
    beta : rank-1 array('D') with bounds (n)
    vl : rank-2 array('D') with bounds (ldvl,n)
    vr : rank-2 array('D') with bounds (ldvr,n)
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def zgglse(a, b, c, d, lwork=None, overwrite_a=None, overwrite_b=None, overwrite_c=None, overwrite_d=None): # real signature unknown; restored from __doc__
    """
    t,r,res,x,info = zgglse(a,b,c,d,[lwork,overwrite_a,overwrite_b,overwrite_c,overwrite_d])
    
    Wrapper for ``zgglse``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    b : input rank-2 array('D') with bounds (p,n)
    c : input rank-1 array('D') with bounds (m)
    d : input rank-1 array('D') with bounds (p)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    overwrite_c : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(m+n+p,1)
    
    Returns
    -------
    t : rank-2 array('D') with bounds (m,n) and a storage
    r : rank-2 array('D') with bounds (p,n) and b storage
    res : rank-1 array('D') with bounds (m) and c storage
    x : rank-1 array('D') with bounds (n)
    info : int
    """
    pass

def zgglse_lwork(m, n, p): # real signature unknown; restored from __doc__
    """
    work,info = zgglse_lwork(m,n,p)
    
    Wrapper for ``zgglse_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    p : input int
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zgtsv(dl, d, du, b, overwrite_dl=None, overwrite_d=None, overwrite_du=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    du2,d,du,x,info = zgtsv(dl,d,du,b,[overwrite_dl,overwrite_d,overwrite_du,overwrite_b])
    
    Wrapper for ``zgtsv``.
    
    Parameters
    ----------
    dl : input rank-1 array('D') with bounds (n - 1)
    d : input rank-1 array('D') with bounds (n)
    du : input rank-1 array('D') with bounds (n - 1)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_dl : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    overwrite_du : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    du2 : rank-1 array('D') with bounds (n - 1) and dl storage
    d : rank-1 array('D') with bounds (n)
    du : rank-1 array('D') with bounds (n - 1)
    x : rank-2 array('D') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def zgtsvx(dl, d, du, b, fact=None, trans=None, dlf=None, df=None, duf=None, du2=None, ipiv=None): # real signature unknown; restored from __doc__
    """
    dlf,df,duf,du2,ipiv,x,rcond,ferr,berr,info = zgtsvx(dl,d,du,b,[fact,trans,dlf,df,duf,du2,ipiv])
    
    Wrapper for ``zgtsvx``.
    
    Parameters
    ----------
    dl : input rank-1 array('D') with bounds (MAX(0, n-1))
    d : input rank-1 array('D') with bounds (n)
    du : input rank-1 array('D') with bounds (MAX(0, n-1))
    b : input rank-2 array('D') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    fact : input string(len=1), optional
        Default: 'N'
    trans : input string(len=1), optional
        Default: 'N'
    dlf : input rank-1 array('D') with bounds (MAX(0,n-1))
    df : input rank-1 array('D') with bounds (n)
    duf : input rank-1 array('D') with bounds (MAX(0,n-1))
    du2 : input rank-1 array('D') with bounds (MAX(0,n-2))
    ipiv : input rank-1 array('i') with bounds (n)
    
    Returns
    -------
    dlf : rank-1 array('D') with bounds (MAX(0,n-1))
    df : rank-1 array('D') with bounds (n)
    duf : rank-1 array('D') with bounds (MAX(0,n-1))
    du2 : rank-1 array('D') with bounds (MAX(0,n-2))
    ipiv : rank-1 array('i') with bounds (n)
    x : rank-2 array('D') with bounds (ldx,nrhs)
    rcond : float
    ferr : rank-1 array('d') with bounds (nrhs)
    berr : rank-1 array('d') with bounds (nrhs)
    info : int
    """
    pass

def zgttrf(dl, d, du, overwrite_dl=None, overwrite_d=None, overwrite_du=None): # real signature unknown; restored from __doc__
    """
    dl,d,du,du2,ipiv,info = zgttrf(dl,d,du,[overwrite_dl,overwrite_d,overwrite_du])
    
    Wrapper for ``zgttrf``.
    
    Parameters
    ----------
    dl : input rank-1 array('D') with bounds (n - 1)
    d : input rank-1 array('D') with bounds (n)
    du : input rank-1 array('D') with bounds (n - 1)
    
    Other Parameters
    ----------------
    overwrite_dl : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    overwrite_du : input int, optional
        Default: 0
    
    Returns
    -------
    dl : rank-1 array('D') with bounds (n - 1)
    d : rank-1 array('D') with bounds (n)
    du : rank-1 array('D') with bounds (n - 1)
    du2 : rank-1 array('D') with bounds (n - 2)
    ipiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def zgttrs(dl, d, du, du2, ipiv, b, trans=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = zgttrs(dl,d,du,du2,ipiv,b,[trans,overwrite_b])
    
    Wrapper for ``zgttrs``.
    
    Parameters
    ----------
    dl : input rank-1 array('D') with bounds (n - 1)
    d : input rank-1 array('D') with bounds (n)
    du : input rank-1 array('D') with bounds (n - 1)
    du2 : input rank-1 array('D') with bounds (n - 2)
    ipiv : input rank-1 array('i') with bounds (n)
    b : input rank-2 array('D') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def zhbevd(ab, compute_v=None, lower=None, ldab=None, lrwork=None, liwork=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,info = zhbevd(ab,[compute_v,lower,ldab,lrwork,liwork,overwrite_ab])
    
    Wrapper for ``zhbevd``.
    
    Parameters
    ----------
    ab : input rank-2 array('D') with bounds (ldab,n)
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    lrwork : input int, optional
        Default: (compute_v?1+5*n+2*n*n:n)
    liwork : input int, optional
        Default: (compute_v?3+5*n:1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('D') with bounds (ldz,ldz)
    info : int
    """
    pass

def zhbevx(ab, vl, vu, il, iu, ldab=None, compute_v=None, range=None, lower=None, abstol=None, mmax=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    w,z,m,ifail,info = zhbevx(ab,vl,vu,il,iu,[ldab,compute_v,range,lower,abstol,mmax,overwrite_ab])
    
    Wrapper for ``zhbevx``.
    
    Parameters
    ----------
    ab : input rank-2 array('D') with bounds (ldab,n)
    vl : input float
    vu : input float
    il : input int
    iu : input int
    
    Other Parameters
    ----------------
    overwrite_ab : input int, optional
        Default: 1
    ldab : input int, optional
        Default: shape(ab,0)
    compute_v : input int, optional
        Default: 1
    range : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    abstol : input float, optional
        Default: 0.0
    mmax : input int, optional
        Default: (compute_v?(range==2?(iu-il+1):n):1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('D') with bounds (ldz,mmax)
    m : int
    ifail : rank-1 array('i') with bounds ((compute_v?n:1))
    info : int
    """
    pass

def zhecon(a, ipiv, anorm, lower=None): # real signature unknown; restored from __doc__
    """
    rcond,info = zhecon(a,ipiv,anorm,[lower])
    
    Wrapper for ``zhecon``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    anorm : input float
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def zheequb(a, lower=None): # real signature unknown; restored from __doc__
    """
    s,scond,amax,info = zheequb(a,[lower])
    
    Wrapper for ``zheequb``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (lda,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    s : rank-1 array('d') with bounds (n)
    scond : float
    amax : float
    info : int
    """
    pass

def zheev(a, compute_v=None, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,v,info = zheev(a,[compute_v,lower,lwork,overwrite_a])
    
    Wrapper for ``zheev``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(2*n-1,1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    v : rank-2 array('D') with bounds (n,n) and a storage
    info : int
    """
    pass

def zheevd(a, compute_v=None, lower=None, lwork=None, liwork=None, lrwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,v,info = zheevd(a,[compute_v,lower,lwork,liwork,lrwork,overwrite_a])
    
    Wrapper for ``zheevd``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max((compute_v?2*n+n*n:n+1),1)
    liwork : input int, optional
        Default: (compute_v?3+5*n:1)
    lrwork : input int, optional
        Default: (compute_v?1+5*n+2*n*n:n)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    v : rank-2 array('D') with bounds (n,n) and a storage
    info : int
    """
    pass

def zheevd_lwork(n, compute_v=None, lower=None): # real signature unknown; restored from __doc__
    """
    work,iwork,rwork,info = zheevd_lwork(n,[compute_v,lower])
    
    Wrapper for ``zheevd_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    iwork : int
    rwork : float
    info : int
    """
    pass

def zheevr(a, compute_v=None, range=None, lower=None, vl=None, vu=None, il=None, iu=None, abstol=None, lwork=None, lrwork=None, liwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,z,m,isuppz,info = zheevr(a,[compute_v,range,lower,vl,vu,il,iu,abstol,lwork,lrwork,liwork,overwrite_a])
    
    Wrapper for ``zheevr``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds ``(n,n)``
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default ``1``
    range : input string(len=1), optional
        Default ``'A'``
    lower : input int, optional
        Default ``0``
    overwrite_a : input int, optional
        Default ``0``
    vl : input float, optional
        Default ``0.0``
    vu : input float, optional
        Default ``1.0``
    il : input int, optional
        Default ``1``
    iu : input int, optional
        Default ``n``
    abstol : input float, optional
        Default ``0.0``
    lwork : input int, optional
        Default ``max(2*n,1)``
    lrwork : input int, optional
        Default ``max(24*n,1)``
    liwork : input int, optional
        Default ``max(1,10*n)``
    
    Returns
    -------
    w : rank-1 array('d') with bounds ``(n)``
    z : rank-2 array('D') with bounds ``((compute_v?MAX(0,n):0),(compute_v?((*range=='I')?(iu-il+1):MAX(1,n)):0))``
    m : int
    isuppz : rank-1 array('i') with bounds ``(2*max(1,n))``
    info : int
    """
    pass

def zheevr_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,rwork,iwork,info = zheevr_lwork(n,[lower])
    
    Wrapper for ``zheevr_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    rwork : float
    iwork : int
    info : int
    """
    pass

def zheevx(a, compute_v=None, range=None, lower=None, vl=None, vu=None, il=None, iu=None, abstol=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    w,z,m,ifail,info = zheevx(a,[compute_v,range,lower,vl,vu,il,iu,abstol,lwork,overwrite_a])
    
    Wrapper for ``zheevx``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds ``(n,n)``
    
    Other Parameters
    ----------------
    compute_v : input int, optional
        Default ``1``
    range : input string(len=1), optional
        Default ``'A'``
    lower : input int, optional
        Default ``0``
    overwrite_a : input int, optional
        Default ``0``
    vl : input float, optional
        Default ``0.0``
    vu : input float, optional
        Default ``1.0``
    il : input int, optional
        Default ``1``
    iu : input int, optional
        Default ``n``
    abstol : input float, optional
        Default ``0.0``
    lwork : input int, optional
        Default ``max(2*n,1)``
    
    Returns
    -------
    w : rank-1 array('d') with bounds ``(n)``
    z : rank-2 array('D') with bounds ``((compute_v*n),(compute_v?((*range=='I')?(iu-il+1):MAX(1,n)):0))``
    m : int
    ifail : rank-1 array('i') with bounds ``(compute_v*n)``
    info : int
    """
    pass

def zheevx_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = zheevx_lwork(n,[lower])
    
    Wrapper for ``zheevx_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zheev_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = zheev_lwork(n,[lower])
    
    Wrapper for ``zheev_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zhegst(a, b, itype=None, lower=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,info = zhegst(a,b,[itype,lower,overwrite_a])
    
    Wrapper for ``zhegst``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    itype : input int, optional
        Default: 1
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (n,n) and a storage
    info : int
    """
    pass

def zhegv(a, b, itype=None, jobz=None, uplo=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    w,v,info = zhegv(a,b,[itype,jobz,uplo,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``zhegv``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(2*n-1,1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    v : rank-2 array('D') with bounds (n,n) and a storage
    info : int
    """
    pass

def zhegvd(a, b, itype=None, jobz=None, uplo=None, lwork=None, lrwork=None, liwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    w,v,info = zhegvd(a,b,[itype,jobz,uplo,lwork,lrwork,liwork,overwrite_a,overwrite_b])
    
    Wrapper for ``zhegvd``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds ``(n,n)``
    b : input rank-2 array('D') with bounds ``(n,n)``
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default ``1``
    jobz : input string(len=1), optional
        Default ``'V'``
    uplo : input string(len=1), optional
        Default ``'L'``
    overwrite_a : input int, optional
        Default ``0``
    overwrite_b : input int, optional
        Default ``0``
    lwork : input int, optional
        Default ``(*jobz=='N'?n+1:n*(n+2))``
    lrwork : input int, optional
        Default ``max((*jobz=='N'?n:2*n*n+5*n+1),1)``
    liwork : input int, optional
        Default ``(*jobz=='N'?1:5*n+3)``
    
    Returns
    -------
    w : rank-1 array('d') with bounds ``(n)``
    v : rank-2 array('D') with bounds ``(n,n)`` with ``a`` storage
    info : int
    """
    pass

def zhegvx(a, b, itype=None, jobz=None, range=None, uplo=None, vl=None, vu=None, il=None, iu=None, abstol=None, lwork=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    w,z,m,ifail,info = zhegvx(a,b,[itype,jobz,range,uplo,vl,vu,il,iu,abstol,lwork,overwrite_a,overwrite_b])
    
    Wrapper for ``zhegvx``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    itype : input int, optional
        Default: 1
    jobz : input string(len=1), optional
        Default: 'V'
    range : input string(len=1), optional
        Default: 'A'
    uplo : input string(len=1), optional
        Default: 'L'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    vl : input float, optional
        Default: 0.0
    vu : input float, optional
        Default: 1.0
    il : input int, optional
        Default: 1
    iu : input int, optional
        Default: n
    abstol : input float, optional
        Default: 0.0
    lwork : input int, optional
        Default: max(2*n,1)
    
    Returns
    -------
    w : rank-1 array('d') with bounds (n)
    z : rank-2 array('D') with bounds ((jobz[0]=='V'?MAX(0,n):0),(jobz[0]=='V'?((range[0]=='I')?(iu-il+1):MAX(1,n)):0))
    m : int
    ifail : rank-1 array('i') with bounds ((jobz[0]=='N'?0:n))
    info : int
    """
    pass

def zhegvx_lwork(n, uplo=None): # real signature unknown; restored from __doc__
    """
    work,info = zhegvx_lwork(n,[uplo])
    
    Wrapper for ``zhegvx_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'L'
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zhegv_lwork(n, uplo=None): # real signature unknown; restored from __doc__
    """
    work,info = zhegv_lwork(n,[uplo])
    
    Wrapper for ``zhegv_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'L'
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zhesv(a, b, lwork=None, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    uduh,ipiv,x,info = zhesv(a,b,[lwork,lower,overwrite_a,overwrite_b])
    
    Wrapper for ``zhesv``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(n,1)
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    uduh : rank-2 array('D') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    x : rank-2 array('D') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def zhesvx(a, b, af=None, ipiv=None, lwork=None, factored=None, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    uduh,ipiv,x,rcond,ferr,berr,info = zhesvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])
    
    Wrapper for ``zhesvx``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    af : input rank-2 array('D') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(2*n,1)
    factored : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    uduh : rank-2 array('D') with bounds (n,n) and af storage
    ipiv : rank-1 array('i') with bounds (n)
    x : rank-2 array('D') with bounds (n,nrhs)
    rcond : float
    ferr : rank-1 array('d') with bounds (nrhs)
    berr : rank-1 array('d') with bounds (nrhs)
    info : int
    """
    pass

def zhesvx_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = zhesvx_lwork(n,[lower])
    
    Wrapper for ``zhesvx_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zhesv_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = zhesv_lwork(n,[lower])
    
    Wrapper for ``zhesv_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zhetrd(a, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,d,e,tau,info = zhetrd(a,[lower,lwork,overwrite_a])
    
    Wrapper for ``zhetrd``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (lda,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(n,1)
    
    Returns
    -------
    c : rank-2 array('D') with bounds (lda,n) and a storage
    d : rank-1 array('d') with bounds (n)
    e : rank-1 array('d') with bounds (n - 1)
    tau : rank-1 array('D') with bounds (n - 1)
    info : int
    """
    pass

def zhetrd_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = zhetrd_lwork(n,[lower])
    
    Wrapper for ``zhetrd_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zhetrf(a, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ldu,ipiv,info = zhetrf(a,[lower,lwork,overwrite_a])
    
    Wrapper for ``zhetrf``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(n,1)
    
    Returns
    -------
    ldu : rank-2 array('D') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def zhetrf_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = zhetrf_lwork(n,[lower])
    
    Wrapper for ``zhetrf_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zhfrk(n, k, alpha, a, beta, c, transr=None, uplo=None, trans=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    cout = zhfrk(n,k,alpha,a,beta,c,[transr,uplo,trans,overwrite_c])
    
    Wrapper for ``zhfrk``.
    
    Parameters
    ----------
    n : input int
    k : input int
    alpha : input float
    a : input rank-2 array('D') with bounds (lda,ka)
    beta : input float
    c : input rank-1 array('D') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    cout : rank-1 array('D') with bounds (nt) and c storage
    """
    pass

def zlange(norm, a): # real signature unknown; restored from __doc__
    """
    n2 = zlange(norm,a)
    
    Wrapper for ``zlange``.
    
    Parameters
    ----------
    norm : input string(len=1)
    a : input rank-2 array('D') with bounds (m,n)
    
    Returns
    -------
    n2 : float
    """
    pass

def zlarf(v, tau, c, work, side=None, incv=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    c = zlarf(v,tau,c,work,[side,incv,overwrite_c])
    
    Wrapper for ``zlarf``.
    
    Parameters
    ----------
    v : input rank-1 array('D') with bounds ((side[0]=='L'?(1 + (m-1)*abs(incv)):(1 + (n-1)*abs(incv))))
    tau : input complex
    c : input rank-2 array('D') with bounds (m,n)
    work : input rank-1 array('D') with bounds (lwork)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    incv : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (m,n)
    """
    pass

def zlarfg(n, alpha, x, incx=None, overwrite_x=None): # real signature unknown; restored from __doc__
    """
    alpha,x,tau = zlarfg(n,alpha,x,[incx,overwrite_x])
    
    Wrapper for ``zlarfg``.
    
    Parameters
    ----------
    n : input int
    alpha : input complex
    x : input rank-1 array('D') with bounds (lx)
    
    Other Parameters
    ----------------
    overwrite_x : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    
    Returns
    -------
    alpha : complex
    x : rank-1 array('D') with bounds (lx)
    tau : complex
    """
    pass

def zlartg(f, g): # real signature unknown; restored from __doc__
    """
    cs,sn,r = zlartg(f,g)
    
    Wrapper for ``zlartg``.
    
    Parameters
    ----------
    f : input complex
    g : input complex
    
    Returns
    -------
    cs : float
    sn : complex
    r : complex
    """
    pass

def zlaswp(a, piv, k1=None, k2=None, off=None, inc=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a = zlaswp(a,piv,[k1,k2,off,inc,overwrite_a])
    
    Wrapper for ``zlaswp``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (nrows,n)
    piv : input rank-1 array('i') with bounds (npiv)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    k1 : input int, optional
        Default: 0
    k2 : input int, optional
        Default: npiv-1
    off : input int, optional
        Default: 0
    inc : input int, optional
        Default: 1
    
    Returns
    -------
    a : rank-2 array('D') with bounds (nrows,n)
    """
    pass

def zlauum(c, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    a,info = zlauum(c,[lower,overwrite_c])
    
    Wrapper for ``zlauum``.
    
    Parameters
    ----------
    c : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (n,n) and c storage
    info : int
    """
    pass

def zpbsv(ab, b, lower=None, ldab=None, overwrite_ab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    c,x,info = zpbsv(ab,b,[lower,ldab,overwrite_ab,overwrite_b])
    
    Wrapper for ``zpbsv``.
    
    Parameters
    ----------
    ab : input rank-2 array('D') with bounds (ldab,n)
    b : input rank-2 array('D') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (ldab,n) and ab storage
    x : rank-2 array('D') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def zpbtrf(ab, lower=None, ldab=None, overwrite_ab=None): # real signature unknown; restored from __doc__
    """
    c,info = zpbtrf(ab,[lower,ldab,overwrite_ab])
    
    Wrapper for ``zpbtrf``.
    
    Parameters
    ----------
    ab : input rank-2 array('D') with bounds (ldab,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ab : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    
    Returns
    -------
    c : rank-2 array('D') with bounds (ldab,n) and ab storage
    info : int
    """
    pass

def zpbtrs(ab, b, lower=None, ldab=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = zpbtrs(ab,b,[lower,ldab,overwrite_b])
    
    Wrapper for ``zpbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('D') with bounds (ldab,n)
    b : input rank-2 array('D') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    ldab : input int, optional
        Default: shape(ab,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def zpftrf(n, a, transr=None, uplo=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    achol,info = zpftrf(n,a,[transr,uplo,overwrite_a])
    
    Wrapper for ``zpftrf``.
    
    Parameters
    ----------
    n : input int
    a : input rank-1 array('D') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    achol : rank-1 array('D') with bounds (nt) and a storage
    info : int
    """
    pass

def zpftri(n, a, transr=None, uplo=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ainv,info = zpftri(n,a,[transr,uplo,overwrite_a])
    
    Wrapper for ``zpftri``.
    
    Parameters
    ----------
    n : input int
    a : input rank-1 array('D') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    ainv : rank-1 array('D') with bounds (nt) and a storage
    info : int
    """
    pass

def zpftrs(n, a, b, transr=None, uplo=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = zpftrs(n,a,b,[transr,uplo,overwrite_b])
    
    Wrapper for ``zpftrs``.
    
    Parameters
    ----------
    n : input int
    a : input rank-1 array('D') with bounds (nt)
    b : input rank-2 array('D') with bounds (ldb,nhrs)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (ldb,nhrs) and b storage
    info : int
    """
    pass

def zpocon(a, anorm, uplo=None): # real signature unknown; restored from __doc__
    """
    rcond,info = zpocon(a,anorm,[uplo])
    
    Wrapper for ``zpocon``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    anorm : input float
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def zposv(a, b, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    c,x,info = zposv(a,b,[lower,overwrite_a,overwrite_b])
    
    Wrapper for ``zposv``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (n,n) and a storage
    x : rank-2 array('D') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def zposvx(a, b, fact=None, af=None, equed=None, s=None, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a_s,lu,equed,s,b_s,x,rcond,ferr,berr,info = zposvx(a,b,[fact,af,equed,s,lower,overwrite_a,overwrite_b])
    
    Wrapper for ``zposvx``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    fact : input string(len=1), optional
        Default: 'E'
    overwrite_a : input int, optional
        Default: 0
    af : input rank-2 array('D') with bounds (n,n)
    equed : input string(len=1), optional
        Default: 'Y'
    s : input rank-1 array('d') with bounds (n)
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    a_s : rank-2 array('D') with bounds (n,n) and a storage
    lu : rank-2 array('D') with bounds (n,n) and af storage
    equed : string(len=1)
    s : rank-1 array('d') with bounds (n)
    b_s : rank-2 array('D') with bounds (n,nrhs) and b storage
    x : rank-2 array('D') with bounds (n,nrhs)
    rcond : float
    ferr : rank-1 array('d') with bounds (nrhs)
    berr : rank-1 array('d') with bounds (nrhs)
    info : int
    """
    pass

def zpotrf(a, lower=None, clean=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,info = zpotrf(a,[lower,clean,overwrite_a])
    
    Wrapper for ``zpotrf``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    clean : input int, optional
        Default: 1
    
    Returns
    -------
    c : rank-2 array('D') with bounds (n,n) and a storage
    info : int
    """
    pass

def zpotri(c, lower=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    inv_a,info = zpotri(c,[lower,overwrite_c])
    
    Wrapper for ``zpotri``.
    
    Parameters
    ----------
    c : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    inv_a : rank-2 array('D') with bounds (n,n) and c storage
    info : int
    """
    pass

def zpotrs(c, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = zpotrs(c,b,[lower,overwrite_b])
    
    Wrapper for ``zpotrs``.
    
    Parameters
    ----------
    c : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_b : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def zppcon(n, ap, anorm, lower=None): # real signature unknown; restored from __doc__
    """
    rcond,info = zppcon(n,ap,anorm,[lower])
    
    Wrapper for ``zppcon``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('D') with bounds (L)
    anorm : input float
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def zppsv(n, ap, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = zppsv(n,ap,b,[lower,overwrite_b])
    
    Wrapper for ``zppsv``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('D') with bounds (L)
    b : input rank-2 array('D') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def zpptrf(n, ap, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    ul,info = zpptrf(n,ap,[lower,overwrite_ap])
    
    Wrapper for ``zpptrf``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('D') with bounds (L)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    
    Returns
    -------
    ul : rank-1 array('D') with bounds (L) and ap storage
    info : int
    """
    pass

def zpptri(n, ap, lower=None, overwrite_ap=None): # real signature unknown; restored from __doc__
    """
    uli,info = zpptri(n,ap,[lower,overwrite_ap])
    
    Wrapper for ``zpptri``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('D') with bounds (L)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_ap : input int, optional
        Default: 0
    
    Returns
    -------
    uli : rank-1 array('D') with bounds (L) and ap storage
    info : int
    """
    pass

def zpptrs(n, ap, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = zpptrs(n,ap,b,[lower,overwrite_b])
    
    Wrapper for ``zpptrs``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('D') with bounds (L)
    b : input rank-2 array('D') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def zpstf2(a, tol=None, lower=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,piv,rank_c,info = zpstf2(a,[tol,lower,overwrite_a])
    
    Wrapper for ``zpstf2``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    tol : input float, optional
        Default: -1.0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (n,n) and a storage
    piv : rank-1 array('i') with bounds (n)
    rank_c : int
    info : int
    """
    pass

def zpstrf(a, tol=None, lower=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    c,piv,rank_c,info = zpstrf(a,[tol,lower,overwrite_a])
    
    Wrapper for ``zpstrf``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    tol : input float, optional
        Default: -1.0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    c : rank-2 array('D') with bounds (n,n) and a storage
    piv : rank-1 array('i') with bounds (n)
    rank_c : int
    info : int
    """
    pass

def zpteqr(d, e, z, compute_z=None, overwrite_d=None, overwrite_e=None, overwrite_z=None): # real signature unknown; restored from __doc__
    """
    d,e,z,info = zpteqr(d,e,z,[compute_z,overwrite_d,overwrite_e,overwrite_z])
    
    Wrapper for ``zpteqr``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (n)
    e : input rank-1 array('d') with bounds ((n>0?n-1:0))
    z : input rank-2 array('D') with bounds ((compute_z==0?shape(z, 0):max(1,n)),(compute_z==0?shape(z, 1):n))
    
    Other Parameters
    ----------------
    compute_z : input int, optional
        Default: 0
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    overwrite_z : input int, optional
        Default: 0
    
    Returns
    -------
    d : rank-1 array('d') with bounds (n)
    e : rank-1 array('d') with bounds ((n>0?n-1:0))
    z : rank-2 array('D') with bounds ((compute_z==0?shape(z, 0):max(1,n)),(compute_z==0?shape(z, 1):n))
    info : int
    """
    pass

def zptsv(d, e, b, overwrite_d=None, overwrite_e=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    d,du,x,info = zptsv(d,e,b,[overwrite_d,overwrite_e,overwrite_b])
    
    Wrapper for ``zptsv``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (n)
    e : input rank-1 array('D') with bounds (n - 1)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    d : rank-1 array('d') with bounds (n)
    du : rank-1 array('D') with bounds (n - 1) and e storage
    x : rank-2 array('D') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def zptsvx(d, e, b, fact=None, df=None, ef=None): # real signature unknown; restored from __doc__
    """
    df,ef,x,rcond,ferr,berr,info = zptsvx(d,e,b,[fact,df,ef])
    
    Wrapper for ``zptsvx``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (n)
    e : input rank-1 array('D') with bounds (max(0, n-1))
    b : input rank-2 array('D') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    fact : input string(len=1), optional
        Default: 'N'
    df : input rank-1 array('d') with bounds (n)
    ef : input rank-1 array('D') with bounds (max(0, n-1))
    
    Returns
    -------
    df : rank-1 array('d') with bounds (n)
    ef : rank-1 array('D') with bounds (max(0, n-1))
    x : rank-2 array('D') with bounds (ldx,nrhs)
    rcond : float
    ferr : rank-1 array('d') with bounds (nrhs)
    berr : rank-1 array('d') with bounds (nrhs)
    info : int
    """
    pass

def zpttrf(d, e, overwrite_d=None, overwrite_e=None): # real signature unknown; restored from __doc__
    """
    d,e,info = zpttrf(d,e,[overwrite_d,overwrite_e])
    
    Wrapper for ``zpttrf``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (n)
    e : input rank-1 array('D') with bounds ((n>0?n-1:0))
    
    Other Parameters
    ----------------
    overwrite_d : input int, optional
        Default: 0
    overwrite_e : input int, optional
        Default: 0
    
    Returns
    -------
    d : rank-1 array('d') with bounds (n)
    e : rank-1 array('D') with bounds ((n>0?n-1:0))
    info : int
    """
    pass

def zpttrs(d, e, b, lower=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = zpttrs(d,e,b,[lower,overwrite_b])
    
    Wrapper for ``zpttrs``.
    
    Parameters
    ----------
    d : input rank-1 array('d') with bounds (n)
    e : input rank-1 array('D') with bounds ((n>0?n-1:0))
    b : input rank-2 array('D') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def zrot(x, y, c, s, n=None, offx=None, incx=None, offy=None, incy=None, overwrite_x=None, overwrite_y=None): # real signature unknown; restored from __doc__
    """
    x,y = zrot(x,y,c,s,[n,offx,incx,offy,incy,overwrite_x,overwrite_y])
    
    Wrapper for ``zrot``.
    
    Parameters
    ----------
    x : input rank-1 array('D') with bounds (lx)
    y : input rank-1 array('D') with bounds (ly)
    c : input float
    s : input complex
    
    Other Parameters
    ----------------
    n : input int, optional
        Default: (lx-1-offx)/abs(incx)+1
    overwrite_x : input int, optional
        Default: 0
    offx : input int, optional
        Default: 0
    incx : input int, optional
        Default: 1
    overwrite_y : input int, optional
        Default: 0
    offy : input int, optional
        Default: 0
    incy : input int, optional
        Default: 1
    
    Returns
    -------
    x : rank-1 array('D') with bounds (lx)
    y : rank-1 array('D') with bounds (ly)
    """
    pass

def zsycon(a, ipiv, anorm, lower=None): # real signature unknown; restored from __doc__
    """
    rcond,info = zsycon(a,ipiv,anorm,[lower])
    
    Wrapper for ``zsycon``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    anorm : input float
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    rcond : float
    info : int
    """
    pass

def zsyconv(a, ipiv, lower=None, way=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    a,e,info = zsyconv(a,ipiv,[lower,way,overwrite_a])
    
    Wrapper for ``zsyconv``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    way : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (n,n)
    e : rank-1 array('D') with bounds (n)
    info : int
    """
    pass

def zsyequb(a, lower=None): # real signature unknown; restored from __doc__
    """
    s,scond,amax,info = zsyequb(a,[lower])
    
    Wrapper for ``zsyequb``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (lda,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    s : rank-1 array('d') with bounds (n)
    scond : float
    amax : float
    info : int
    """
    pass

def zsysv(a, b, lwork=None, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    udut,ipiv,x,info = zsysv(a,b,[lwork,lower,overwrite_a,overwrite_b])
    
    Wrapper for ``zsysv``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(n,1)
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    udut : rank-2 array('D') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    x : rank-2 array('D') with bounds (n,nrhs) and b storage
    info : int
    """
    pass

def zsysvx(a, b, af=None, ipiv=None, lwork=None, factored=None, lower=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a_s,udut,ipiv,b_s,x,rcond,ferr,berr,info = zsysvx(a,b,[af,ipiv,lwork,factored,lower,overwrite_a,overwrite_b])
    
    Wrapper for ``zsysvx``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,nrhs)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    af : input rank-2 array('D') with bounds (n,n)
    ipiv : input rank-1 array('i') with bounds (n)
    overwrite_b : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    factored : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    a_s : rank-2 array('D') with bounds (n,n) and a storage
    udut : rank-2 array('D') with bounds (n,n) and af storage
    ipiv : rank-1 array('i') with bounds (n)
    b_s : rank-2 array('D') with bounds (n,nrhs) and b storage
    x : rank-2 array('D') with bounds (n,nrhs)
    rcond : float
    ferr : rank-1 array('d') with bounds (nrhs)
    berr : rank-1 array('d') with bounds (nrhs)
    info : int
    """
    pass

def zsysvx_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = zsysvx_lwork(n,[lower])
    
    Wrapper for ``zsysvx_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zsysv_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = zsysv_lwork(n,[lower])
    
    Wrapper for ``zsysv_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zsytf2(a, lower=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ldu,ipiv,info = zsytf2(a,[lower,overwrite_a])
    
    Wrapper for ``zsytf2``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    
    Returns
    -------
    ldu : rank-2 array('D') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def zsytrf(a, lower=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ldu,ipiv,info = zsytrf(a,[lower,lwork,overwrite_a])
    
    Wrapper for ``zsytrf``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(n,1)
    
    Returns
    -------
    ldu : rank-2 array('D') with bounds (n,n) and a storage
    ipiv : rank-1 array('i') with bounds (n)
    info : int
    """
    pass

def zsytrf_lwork(n, lower=None): # real signature unknown; restored from __doc__
    """
    work,info = zsytrf_lwork(n,[lower])
    
    Wrapper for ``zsytrf_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def ztbtrs(ab, b, uplo=None, trans=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = ztbtrs(ab,b,[uplo,trans,diag,overwrite_b])
    
    Wrapper for ``ztbtrs``.
    
    Parameters
    ----------
    ab : input rank-2 array('D') with bounds (ldab,n)
    b : input rank-2 array('D') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'U'
    trans : input string(len=1), optional
        Default: 'N'
    diag : input string(len=1), optional
        Default: 'N'
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def ztfsm(alpha, a, b, transr=None, side=None, uplo=None, trans=None, diag=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x = ztfsm(alpha,a,b,[transr,side,uplo,trans,diag,overwrite_b])
    
    Wrapper for ``ztfsm``.
    
    Parameters
    ----------
    alpha : input complex
    a : input rank-1 array('D') with bounds (nt)
    b : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    side : input string(len=1), optional
        Default: 'L'
    uplo : input string(len=1), optional
        Default: 'U'
    trans : input string(len=1), optional
        Default: 'N'
    diag : input string(len=1), optional
        Default: 'N'
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (m,n) and b storage
    """
    pass

def ztfttp(n, arf, transr=None, uplo=None): # real signature unknown; restored from __doc__
    """
    ap,info = ztfttp(n,arf,[transr,uplo])
    
    Wrapper for ``ztfttp``.
    
    Parameters
    ----------
    n : input int
    arf : input rank-1 array('D') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    ap : rank-1 array('D') with bounds (nt)
    info : int
    """
    pass

def ztfttr(n, arf, transr=None, uplo=None): # real signature unknown; restored from __doc__
    """
    a,info = ztfttr(n,arf,[transr,uplo])
    
    Wrapper for ``ztfttr``.
    
    Parameters
    ----------
    n : input int
    arf : input rank-1 array('D') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    a : rank-2 array('D') with bounds (lda,n)
    info : int
    """
    pass

def ztgexc(a, b, q, z, ifst, ilst, wantq=None, wantz=None, overwrite_a=None, overwrite_b=None, overwrite_q=None, overwrite_z=None): # real signature unknown; restored from __doc__
    """
    a,b,q,z,info = ztgexc(a,b,q,z,ifst,ilst,[wantq,wantz,overwrite_a,overwrite_b,overwrite_q,overwrite_z])
    
    Wrapper for ``ztgexc``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (lda,n)
    b : input rank-2 array('D') with bounds (ldb,n)
    q : input rank-2 array('D') with bounds (ldq,n)
    z : input rank-2 array('D') with bounds (ldz,n)
    ifst : input int
    ilst : input int
    
    Other Parameters
    ----------------
    wantq : input int, optional
        Default: 1
    wantz : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    overwrite_z : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (lda,n)
    b : rank-2 array('D') with bounds (ldb,n)
    q : rank-2 array('D') with bounds (ldq,n)
    z : rank-2 array('D') with bounds (ldz,n)
    info : int
    """
    pass

def ztgsen(select, a, b, q, z, ijob=None, wantq=None, wantz=None, lwork=None, liwork=None, overwrite_a=None, overwrite_b=None, overwrite_q=None, overwrite_z=None): # real signature unknown; restored from __doc__
    """
    as,bs,alpha,beta,qs,zs,m,pl,pr,dif,info = ztgsen(select,a,b,q,z,[ijob,wantq,wantz,lwork,liwork,overwrite_a,overwrite_b,overwrite_q,overwrite_z])
    
    Wrapper for ``ztgsen``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,n)
    q : input rank-2 array('D') with bounds (n,n)
    z : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    ijob : input int, optional
        Default: 4
    wantq : input int, optional
        Default: 1
    wantz : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    overwrite_z : input int, optional
        Default: 0
    lwork : input int, optional
        Default: (ijob==0?1:n+2)
    liwork : input int, optional
        Default: (ijob==0?1:n+2)
    
    Returns
    -------
    as : rank-2 array('D') with bounds (n,n) and a storage
    bs : rank-2 array('D') with bounds (n,n) and b storage
    alpha : rank-1 array('D') with bounds (n)
    beta : rank-1 array('D') with bounds (n)
    qs : rank-2 array('D') with bounds (n,n) and q storage
    zs : rank-2 array('D') with bounds (n,n) and z storage
    m : int
    pl : float
    pr : float
    dif : rank-1 array('d') with bounds (2)
    info : int
    """
    pass

def ztgsen_lwork(select, a, b, ijob=None): # real signature unknown; restored from __doc__
    """
    work,iwork,info = ztgsen_lwork(select,a,b,[ijob])
    
    Wrapper for ``ztgsen_lwork``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    ijob : input int, optional
        Default: 4
    
    Returns
    -------
    work : complex
    iwork : int
    info : int
    """
    pass

def ztpmqrt(l, v, t, a, b, side=None, trans=None, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,b,info = ztpmqrt(l,v,t,a,b,[side,trans,overwrite_a,overwrite_b])
    
    Wrapper for ``ztpmqrt``.
    
    Parameters
    ----------
    l : input int
    v : input rank-2 array('D') with bounds ((side[0]=='L'?m:n),k)
    t : input rank-2 array('D') with bounds (nb,k)
    a : input rank-2 array('D') with bounds ((side[0]=='L'?k:m),(side[0]=='L'?n:k))
    b : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds ((side[0]=='L'?k:m),(side[0]=='L'?n:k))
    b : rank-2 array('D') with bounds (m,n)
    info : int
    """
    pass

def ztpqrt(l, nb, a, b, overwrite_a=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    a,b,t,info = ztpqrt(l,nb,a,b,[overwrite_a,overwrite_b])
    
    Wrapper for ``ztpqrt``.
    
    Parameters
    ----------
    l : input int
    nb : input int
    a : input rank-2 array('D') with bounds (n,n)
    b : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (n,n)
    b : rank-2 array('D') with bounds (m,n)
    t : rank-2 array('D') with bounds (nb,n)
    info : int
    """
    pass

def ztpttf(n, ap, transr=None, uplo=None): # real signature unknown; restored from __doc__
    """
    arf,info = ztpttf(n,ap,[transr,uplo])
    
    Wrapper for ``ztpttf``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('D') with bounds (nt)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    arf : rank-1 array('D') with bounds (nt)
    info : int
    """
    pass

def ztpttr(n, ap, uplo=None): # real signature unknown; restored from __doc__
    """
    a,info = ztpttr(n,ap,[uplo])
    
    Wrapper for ``ztpttr``.
    
    Parameters
    ----------
    n : input int
    ap : input rank-1 array('D') with bounds (nt)
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    a : rank-2 array('D') with bounds (n,n)
    info : int
    """
    pass

def ztrexc(a, q, ifst, ilst, wantq=None, overwrite_a=None, overwrite_q=None): # real signature unknown; restored from __doc__
    """
    a,q,info = ztrexc(a,q,ifst,ilst,[wantq,overwrite_a,overwrite_q])
    
    Wrapper for ``ztrexc``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (lda,n)
    q : input rank-2 array('D') with bounds (ldq,n)
    ifst : input int
    ilst : input int
    
    Other Parameters
    ----------------
    wantq : input int, optional
        Default: 1
    overwrite_a : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    
    Returns
    -------
    a : rank-2 array('D') with bounds (lda,n)
    q : rank-2 array('D') with bounds (ldq,n)
    info : int
    """
    pass

def ztrsen(select, t, q, job=None, wantq=None, lwork=None, overwrite_t=None, overwrite_q=None): # real signature unknown; restored from __doc__
    """
    ts,qs,w,m,s,sep,info = ztrsen(select,t,q,[job,wantq,lwork,overwrite_t,overwrite_q])
    
    Wrapper for ``ztrsen``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    t : input rank-2 array('D') with bounds (n,n)
    q : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    job : input string(len=1), optional
        Default: 'B'
    wantq : input int, optional
        Default: 1
    overwrite_t : input int, optional
        Default: 0
    overwrite_q : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(1,n)
    
    Returns
    -------
    ts : rank-2 array('D') with bounds (n,n) and t storage
    qs : rank-2 array('D') with bounds (n,n) and q storage
    w : rank-1 array('D') with bounds (n)
    m : int
    s : float
    sep : float
    info : int
    """
    pass

def ztrsen_lwork(select, t, job=None): # real signature unknown; restored from __doc__
    """
    work,info = ztrsen_lwork(select,t,[job])
    
    Wrapper for ``ztrsen_lwork``.
    
    Parameters
    ----------
    select : input rank-1 array('i') with bounds (n)
    t : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    job : input string(len=1), optional
        Default: 'B'
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def ztrsyl(a, b, c, trana=None, tranb=None, isgn=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    x,scale,info = ztrsyl(a,b,c,[trana,tranb,isgn,overwrite_c])
    
    Wrapper for ``ztrsyl``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,m)
    b : input rank-2 array('D') with bounds (n,n)
    c : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    trana : input string(len=1), optional
        Default: 'N'
    tranb : input string(len=1), optional
        Default: 'N'
    isgn : input int, optional
        Default: 1
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (m,n) and c storage
    scale : float
    info : int
    """
    pass

def ztrtri(c, lower=None, unitdiag=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    inv_c,info = ztrtri(c,[lower,unitdiag,overwrite_c])
    
    Wrapper for ``ztrtri``.
    
    Parameters
    ----------
    c : input rank-2 array('D') with bounds (n,n)
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    lower : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    
    Returns
    -------
    inv_c : rank-2 array('D') with bounds (n,n) and c storage
    info : int
    """
    pass

def ztrtrs(a, b, lower=None, trans=None, unitdiag=None, lda=None, overwrite_b=None): # real signature unknown; restored from __doc__
    """
    x,info = ztrtrs(a,b,[lower,trans,unitdiag,lda,overwrite_b])
    
    Wrapper for ``ztrtrs``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (lda,n)
    b : input rank-2 array('D') with bounds (ldb,nrhs)
    
    Other Parameters
    ----------------
    lower : input int, optional
        Default: 0
    trans : input int, optional
        Default: 0
    unitdiag : input int, optional
        Default: 0
    lda : input int, optional
        Default: shape(a,0)
    overwrite_b : input int, optional
        Default: 0
    
    Returns
    -------
    x : rank-2 array('D') with bounds (ldb,nrhs) and b storage
    info : int
    """
    pass

def ztrttf(a, transr=None, uplo=None): # real signature unknown; restored from __doc__
    """
    arf,info = ztrttf(a,[transr,uplo])
    
    Wrapper for ``ztrttf``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (lda,n)
    
    Other Parameters
    ----------------
    transr : input string(len=1), optional
        Default: 'N'
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    arf : rank-1 array('D') with bounds (n*(n+1)/2)
    info : int
    """
    pass

def ztrttp(a, uplo=None): # real signature unknown; restored from __doc__
    """
    ap,info = ztrttp(a,[uplo])
    
    Wrapper for ``ztrttp``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (lda,n)
    
    Other Parameters
    ----------------
    uplo : input string(len=1), optional
        Default: 'U'
    
    Returns
    -------
    ap : rank-1 array('D') with bounds (n*(n+1)/2)
    info : int
    """
    pass

def ztzrzf(a, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    rz,tau,info = ztzrzf(a,[lwork,overwrite_a])
    
    Wrapper for ``ztzrzf``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX(m,1)
    
    Returns
    -------
    rz : rank-2 array('D') with bounds (m,n) and a storage
    tau : rank-1 array('D') with bounds (m)
    info : int
    """
    pass

def ztzrzf_lwork(m, n): # real signature unknown; restored from __doc__
    """
    work,info = ztzrzf_lwork(m,n)
    
    Wrapper for ``ztzrzf_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zuncsd(x11, x12, x21, x22, compute_u1=None, compute_u2=None, compute_v1t=None, compute_v2t=None, trans=None, signs=None, lwork=None, lrwork=None, overwrite_x11=None, overwrite_x12=None, overwrite_x21=None, overwrite_x22=None): # real signature unknown; restored from __doc__
    """
    cs11,cs12,cs21,cs22,theta,u1,u2,v1t,v2t,info = zuncsd(x11,x12,x21,x22,[compute_u1,compute_u2,compute_v1t,compute_v2t,trans,signs,lwork,lrwork,overwrite_x11,overwrite_x12,overwrite_x21,overwrite_x22])
    
    Wrapper for ``zuncsd``.
    
    Parameters
    ----------
    x11 : input rank-2 array('D') with bounds (p,q)
    x12 : input rank-2 array('D') with bounds (p,mmq)
    x21 : input rank-2 array('D') with bounds (mmp,q)
    x22 : input rank-2 array('D') with bounds (mmp,mmq)
    
    Other Parameters
    ----------------
    compute_u1 : input int, optional
        Default: 1
    compute_u2 : input int, optional
        Default: 1
    compute_v1t : input int, optional
        Default: 1
    compute_v2t : input int, optional
        Default: 1
    trans : input int, optional
        Default: 0
    signs : input int, optional
        Default: 0
    overwrite_x11 : input int, optional
        Default: 0
    overwrite_x12 : input int, optional
        Default: 0
    overwrite_x21 : input int, optional
        Default: 0
    overwrite_x22 : input int, optional
        Default: 0
    lwork : input int, optional
        Default: 2*m+MAX(1,MAX(mmp,mmq))+1
    lrwork : input int, optional
        Default: 5*MAX(1,q-1)+4*MAX(1,q)+8*q+1
    
    Returns
    -------
    cs11 : rank-2 array('D') with bounds (p,q) and x11 storage
    cs12 : rank-2 array('D') with bounds (p,mmq) and x12 storage
    cs21 : rank-2 array('D') with bounds (mmp,q) and x21 storage
    cs22 : rank-2 array('D') with bounds (mmp,mmq) and x22 storage
    theta : rank-1 array('d') with bounds (min(min(p,mmp),min(q,mmq)))
    u1 : rank-2 array('D') with bounds ((compute_u1?p:0),(compute_u1?p:0))
    u2 : rank-2 array('D') with bounds ((compute_u2?mmp:0),(compute_u2?mmp:0))
    v1t : rank-2 array('D') with bounds ((compute_v1t?q:0),(compute_v1t?q:0))
    v2t : rank-2 array('D') with bounds ((compute_v2t?mmq:0),(compute_v2t?mmq:0))
    info : int
    """
    pass

def zuncsd_lwork(m, p, q): # real signature unknown; restored from __doc__
    """
    work,rwork,info = zuncsd_lwork(m,p,q)
    
    Wrapper for ``zuncsd_lwork``.
    
    Parameters
    ----------
    m : input int
    p : input int
    q : input int
    
    Returns
    -------
    work : complex
    rwork : float
    info : int
    """
    pass

def zunghr(a, tau, lo=None, hi=None, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    ht,info = zunghr(a,tau,[lo,hi,lwork,overwrite_a])
    
    Wrapper for ``zunghr``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (n,n)
    tau : input rank-1 array('D') with bounds (n - 1)
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(hi-lo,1)
    
    Returns
    -------
    ht : rank-2 array('D') with bounds (n,n) and a storage
    info : int
    """
    pass

def zunghr_lwork(n, lo=None, hi=None): # real signature unknown; restored from __doc__
    """
    work,info = zunghr_lwork(n,[lo,hi])
    
    Wrapper for ``zunghr_lwork``.
    
    Parameters
    ----------
    n : input int
    
    Other Parameters
    ----------------
    lo : input int, optional
        Default: 0
    hi : input int, optional
        Default: n-1
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

def zungqr(a, tau, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    q,work,info = zungqr(a,tau,[lwork,overwrite_a])
    
    Wrapper for ``zungqr``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    tau : input rank-1 array('D') with bounds (k)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*n,1)
    
    Returns
    -------
    q : rank-2 array('D') with bounds (m,n) and a storage
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def zungrq(a, tau, lwork=None, overwrite_a=None): # real signature unknown; restored from __doc__
    """
    q,work,info = zungrq(a,tau,[lwork,overwrite_a])
    
    Wrapper for ``zungrq``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (m,n)
    tau : input rank-1 array('D') with bounds (k)
    
    Other Parameters
    ----------------
    overwrite_a : input int, optional
        Default: 0
    lwork : input int, optional
        Default: max(3*m,1)
    
    Returns
    -------
    q : rank-2 array('D') with bounds (m,n) and a storage
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def zunmqr(side, trans, a, tau, c, lwork, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    cq,work,info = zunmqr(side,trans,a,tau,c,lwork,[overwrite_c])
    
    Wrapper for ``zunmqr``.
    
    Parameters
    ----------
    side : input string(len=1)
    trans : input string(len=1)
    a : input rank-2 array('D') with bounds (lda,k)
    tau : input rank-1 array('D') with bounds (k)
    c : input rank-2 array('D') with bounds (ldc,n)
    lwork : input int
    
    Other Parameters
    ----------------
    overwrite_c : input int, optional
        Default: 0
    
    Returns
    -------
    cq : rank-2 array('D') with bounds (ldc,n) and c storage
    work : rank-1 array('D') with bounds (MAX(lwork,1))
    info : int
    """
    pass

def zunmrz(a, tau, c, side=None, trans=None, lwork=None, overwrite_c=None): # real signature unknown; restored from __doc__
    """
    cq,info = zunmrz(a,tau,c,[side,trans,lwork,overwrite_c])
    
    Wrapper for ``zunmrz``.
    
    Parameters
    ----------
    a : input rank-2 array('D') with bounds (k,nt)
    tau : input rank-1 array('D') with bounds (k)
    c : input rank-2 array('D') with bounds (m,n)
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    trans : input string(len=1), optional
        Default: 'N'
    overwrite_c : input int, optional
        Default: 0
    lwork : input int, optional
        Default: MAX((side[0]=='L'?n:m),1)
    
    Returns
    -------
    cq : rank-2 array('D') with bounds (m,n) and c storage
    info : int
    """
    pass

def zunmrz_lwork(m, n, side=None, trans=None): # real signature unknown; restored from __doc__
    """
    work,info = zunmrz_lwork(m,n,[side,trans])
    
    Wrapper for ``zunmrz_lwork``.
    
    Parameters
    ----------
    m : input int
    n : input int
    
    Other Parameters
    ----------------
    side : input string(len=1), optional
        Default: 'L'
    trans : input string(len=1), optional
        Default: 'N'
    
    Returns
    -------
    work : complex
    info : int
    """
    pass

# classes

class __flapack_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f859fa0>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.linalg._flapack', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffff9f859fa0>, origin='/.venv/lib/python3.8/site-packages/scipy/linalg/_flapack.cpython-38-aarch64-linux-gnu.so')"

