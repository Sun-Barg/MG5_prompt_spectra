# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.1.0 for Mac OS X ARM (64-bit) (June 16, 2022)
# Date: Fri 11 Jul 2025 16:10:26


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-G',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '(-2*complex(0,1))/gamma**5',
                order = {'DM':-5})

GC_10 = Coupling(name = 'GC_10',
                 value = '-(cosxi*CTH*complex(0,1)*gg)',
                 order = {'DM':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-6*CTH**4*complex(0,1)*lam',
                 order = {'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = 'CTH*gg*sinxi',
                 order = {'DM':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(cosxi*complex(0,1)*gg*STH)',
                 order = {'DM':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '6*CTH**3*complex(0,1)*lam*STH',
                 order = {'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = 'gg*sinxi*STH',
                 order = {'DM':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '-6*CTH**2*complex(0,1)*lam*STH**2',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '6*CTH*complex(0,1)*lam*STH**3',
                 order = {'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '-6*complex(0,1)*lam*STH**4',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '-(CTH**4*complex(0,1)*lam4) - 12*CTH**2*complex(0,1)*lam2*STH**2',
                 order = {'DM':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '6*CTH**3*complex(0,1)*lam2*STH - CTH**3*complex(0,1)*lam4*STH - 6*CTH*complex(0,1)*lam2*STH**3',
                 order = {'DM':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '-6*CTH**3*complex(0,1)*lam2*STH + 6*CTH*complex(0,1)*lam2*STH**3 - CTH*complex(0,1)*lam4*STH**3',
                 order = {'DM':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '-2*CTH**4*complex(0,1)*lam2 + 8*CTH**2*complex(0,1)*lam2*STH**2 - CTH**2*complex(0,1)*lam4*STH**2 - 2*complex(0,1)*lam2*STH**4',
                 order = {'DM':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '-12*CTH**2*complex(0,1)*lam2*STH**2 - complex(0,1)*lam4*STH**4',
                 order = {'DM':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '(CTH**2*ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '-0.5*(CTH*ee**2*complex(0,1)*STH)/sw**2',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '(ee**2*complex(0,1)*STH**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(CKM1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(CKM2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(CKM3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(CKM3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '-0.5*(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '-0.16666666666666666*(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = 'CTH**2*ee**2*complex(0,1) + (CTH**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (CTH**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(CTH*ee**2*complex(0,1)*STH) - (CTH*cw**2*ee**2*complex(0,1)*STH)/(2.*sw**2) - (CTH*ee**2*complex(0,1)*STH*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = 'ee**2*complex(0,1)*STH**2 + (cw**2*ee**2*complex(0,1)*STH**2)/(2.*sw**2) + (ee**2*complex(0,1)*STH**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '-6*CTH**3*complex(0,1)*lam*vev',
                 order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '6*CTH**2*complex(0,1)*lam*STH*vev',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '-6*CTH*complex(0,1)*lam*STH**2*vev',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '6*complex(0,1)*lam*STH**3*vev',
                 order = {'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '(CTH*ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '-0.5*(ee**2*complex(0,1)*STH*vev)/sw**2',
                 order = {'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = 'CTH*ee**2*complex(0,1)*vev + (CTH*cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (CTH*ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '-(ee**2*complex(0,1)*STH*vev) - (cw**2*ee**2*complex(0,1)*STH*vev)/(2.*sw**2) - (ee**2*complex(0,1)*STH*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '-(CTH**3*complex(0,1)*lam3) - 3*CTH*complex(0,1)*lam1*STH**2 + 6*CTH**2*complex(0,1)*lam2*STH*vev - CTH**3*complex(0,1)*lam4*vs - 6*CTH*complex(0,1)*lam2*STH**2*vs',
                 order = {'DM':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-(CTH**3*complex(0,1)*lam1) + 2*CTH*complex(0,1)*lam1*STH**2 - CTH*complex(0,1)*lam3*STH**2 - 4*CTH**2*complex(0,1)*lam2*STH*vev + 2*complex(0,1)*lam2*STH**3*vev - 2*CTH**3*complex(0,1)*lam2*vs + 4*CTH*complex(0,1)*lam2*STH**2*vs - CTH*complex(0,1)*lam4*STH**2*vs',
                 order = {'DM':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '2*CTH**2*complex(0,1)*lam1*STH - CTH**2*complex(0,1)*lam3*STH - complex(0,1)*lam1*STH**3 - 2*CTH**3*complex(0,1)*lam2*vev + 4*CTH*complex(0,1)*lam2*STH**2*vev + 4*CTH**2*complex(0,1)*lam2*STH*vs - CTH**2*complex(0,1)*lam4*STH*vs - 2*complex(0,1)*lam2*STH**3*vs',
                 order = {'DM':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '-3*CTH**2*complex(0,1)*lam1*STH - complex(0,1)*lam3*STH**3 - 6*CTH*complex(0,1)*lam2*STH**2*vev - 6*CTH**2*complex(0,1)*lam2*STH*vs - complex(0,1)*lam4*STH**3*vs',
                 order = {'DM':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-((CTH*complex(0,1)*yb)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '(complex(0,1)*STH*yb)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-((CTH*complex(0,1)*yc)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '(complex(0,1)*STH*yc)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-((CTH*complex(0,1)*ydo)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(complex(0,1)*STH*ydo)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-((CTH*complex(0,1)*ye)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(complex(0,1)*STH*ye)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-((CTH*complex(0,1)*ym)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '(complex(0,1)*STH*ym)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-((CTH*complex(0,1)*ys)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(complex(0,1)*STH*ys)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '-((CTH*complex(0,1)*yt)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '(complex(0,1)*STH*yt)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-((CTH*complex(0,1)*ytau)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '(complex(0,1)*STH*ytau)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '-((CTH*complex(0,1)*yup)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '(complex(0,1)*STH*yup)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x3))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x3))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '(ee*complex(0,1)*complexconjugate(CKM3x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '(ee*complex(0,1)*complexconjugate(CKM3x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

