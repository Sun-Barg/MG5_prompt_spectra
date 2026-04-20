ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

C     Parameters that should not be recomputed event by event.
C     
      IF(READLHA) THEN

        G = 2 * DSQRT(AS*PI)  ! for the first init

        MDL_SQRT__2 = SQRT(DCMPLX(2.000000D+00))

        MDL_YE = (MDL_YME*MDL_SQRT__2)/MDL_VEV

        MDL_YM = (MDL_YMM*MDL_SQRT__2)/MDL_VEV

        MDL_YTAU = (MDL_YMTAU*MDL_SQRT__2)/MDL_VEV

        MDL_YUP = (MDL_YMUP*MDL_SQRT__2)/MDL_VEV

        MDL_YC = (MDL_YMC*MDL_SQRT__2)/MDL_VEV

        MDL_YT = (MDL_YMT*MDL_SQRT__2)/MDL_VEV

        MDL_YDO = (MDL_YMDO*MDL_SQRT__2)/MDL_VEV

        MDL_YS = (MDL_YMS*MDL_SQRT__2)/MDL_VEV

        MDL_YB = (MDL_YMB*MDL_SQRT__2)/MDL_VEV

        MDL_COS__CABI = COS(MDL_CABI)

        MDL_CKM1X1 = MDL_COS__CABI

        MDL_SIN__CABI = SIN(MDL_CABI)

        MDL_CKM1X2 = MDL_SIN__CABI

        MDL_CKM1X3 = 0.000000D+00

        MDL_CKM2X1 = -MDL_SIN__CABI

        MDL_CKM2X2 = MDL_COS__CABI

        MDL_CKM2X3 = 0.000000D+00

        MDL_CKM3X1 = 0.000000D+00

        MDL_CKM3X2 = 0.000000D+00

        MDL_CKM3X3 = 1.000000D+00

        MDL_SIN__THETA = SIN(MDL_THETA)

        MDL_SINTH = MDL_SIN__THETA

        MDL_SINXI__EXP__2 = MDL_SINXI**2

        MDL_COSXI = SQRT(DCMPLX(1.000000D+00-MDL_SINXI__EXP__2))

        MDL_COS__THETA = COS(MDL_THETA)

        MDL_COSTH = MDL_COS__THETA

        MDL_VEV__EXP__2 = MDL_VEV**2

        MDL_MUSSQ = -5.000000D-01*(MDL_LAM1*MDL_VEV__EXP__2)/MDL_VS
     $   +(MDL_VS*(3.000000D+00*MDL_LAM3+2.000000D+00*MDL_LAM4*MDL_VS))
     $   /6.000000D+00

        MDL_MUHSSQ = MDL_VEV*(MDL_LAM1+2.000000D+00*MDL_LAM2*MDL_VS)

        MDL_MUHSQ = 2.000000D+00*MDL_LAM*MDL_VEV__EXP__2

        MDL_MUH = MDL_LAM*MDL_VEV__EXP__2+MDL_VS*(MDL_LAM1+MDL_LAM2
     $   *MDL_VS)

        MDL_MUSQ = MDL_LAM*MDL_VEV__EXP__2+MDL_VS*(MDL_LAM1+MDL_LAM2
     $   *MDL_VS)

        MDL_VS__EXP__2 = MDL_VS**2

        MDL_MM = -(MDL_LAM2*MDL_VEV__EXP__2)-(MDL_LAM1*MDL_VEV__EXP__2)
     $   /(2.000000D+00*MDL_VS)-(MDL_LAM3*MDL_VS)/2.000000D+00
     $   -(MDL_LAM4*MDL_VS__EXP__2)/6.000000D+00

        MDL_MZ__EXP__2 = MDL_MZ**2

        MDL_MZ__EXP__4 = MDL_MZ**4

        MDL_YHS = (2.000000D+00*MDL_MUHSSQ)/(MDL_MUHSQ-MDL_MUSSQ)

        MDL_YHS__EXP__2 = MDL_YHS**2

        MDL_TTH = MDL_YHS/(1.000000D+00+SQRT(DCMPLX(1.000000D+00
     $   +MDL_YHS__EXP__2)))

        MDL_TTH__EXP__2 = MDL_TTH**2

        MDL_CTH = 1.000000D+00/SQRT(DCMPLX(1.000000D+00
     $   +MDL_TTH__EXP__2))

        MDL_STH = MDL_CTH*MDL_TTH

        MDL_COMPLEXI = DCMPLX(0.000000D+00,1.000000D+00)

        MDL_GAMMA__EXP__5 = MDL_GAMMA**5

        MDL_CTH__EXP__4 = MDL_CTH**4

        MDL_CTH__EXP__3 = MDL_CTH**3

        MDL_CTH__EXP__2 = MDL_CTH**2

        MDL_STH__EXP__2 = MDL_STH**2

        MDL_STH__EXP__3 = MDL_STH**3

        MDL_STH__EXP__4 = MDL_STH**4

        MDL_CONJG__CKM1X1 = CONJG(DCMPLX(MDL_CKM1X1))

        MDL_CONJG__CKM1X2 = CONJG(DCMPLX(MDL_CKM1X2))

        MDL_CONJG__CKM1X3 = CONJG(DCMPLX(MDL_CKM1X3))

        MDL_CONJG__CKM2X1 = CONJG(DCMPLX(MDL_CKM2X1))

        MDL_CONJG__CKM2X2 = CONJG(DCMPLX(MDL_CKM2X2))

        MDL_CONJG__CKM2X3 = CONJG(DCMPLX(MDL_CKM2X3))

        MDL_CONJG__CKM3X1 = CONJG(DCMPLX(MDL_CKM3X1))

        MDL_CONJG__CKM3X2 = CONJG(DCMPLX(MDL_CKM3X2))

        MDL_CONJG__CKM3X3 = CONJG(DCMPLX(MDL_CKM3X3))

        MDL_AEW = 1.000000D+00/AEWM1

        MDL_MW = SQRT(DCMPLX(MDL_MZ__EXP__2/2.000000D+00
     $   +SQRT(DCMPLX(MDL_MZ__EXP__4/4.000000D+00-(MDL_AEW*PI
     $   *MDL_MZ__EXP__2)/(MDL_GF*MDL_SQRT__2)))))

        MDL_SQRT__AEW = SQRT(DCMPLX(MDL_AEW))

        MDL_EE = 2.000000D+00*MDL_SQRT__AEW*SQRT(DCMPLX(PI))

        MDL_MW__EXP__2 = MDL_MW**2

        MDL_SW2 = 1.000000D+00-MDL_MW__EXP__2/MDL_MZ__EXP__2

        MDL_CW = SQRT(DCMPLX(1.000000D+00-MDL_SW2))

        MDL_SQRT__SW2 = SQRT(DCMPLX(MDL_SW2))

        MDL_SW = MDL_SQRT__SW2

        MDL_G1 = MDL_EE/MDL_CW

        MDL_GW = MDL_EE/MDL_SW

        MDL_EE__EXP__2 = MDL_EE**2

        MDL_SW__EXP__2 = MDL_SW**2

        MDL_CW__EXP__2 = MDL_CW**2

      ENDIF
C     
C     Parameters that should be recomputed at an event by even basis.
C     
      AS = G**2/4/PI

      MDL_SQRT__AS = SQRT(DCMPLX(AS))

      MDL_G__EXP__2 = G**2

C     
C     Parameters that should be updated for the loops.
C     
C     
C     Definition of the EW coupling used in the write out of aqed
C     
      GAL(1) = 3.5449077018110318D0 / DSQRT(ABS(AEWM1))
      GAL(2) = 1D0

