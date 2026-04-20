# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.1.0 for Mac OS X ARM (64-bit) (June 16, 2022)
# Date: Fri 11 Jul 2025 16:34:31



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

vev = Parameter(name = 'vev',
                nature = 'external',
                type = 'real',
                value = 246.22,
                texname = '\\text{vev}',
                lhablock = 'FRBlock',
                lhacode = [ 1 ])

lam = Parameter(name = 'lam',
                nature = 'external',
                type = 'real',
                value = 0.13,
                texname = '\\text{lam}',
                lhablock = 'FRBlock',
                lhacode = [ 2 ])

lam1 = Parameter(name = 'lam1',
                 nature = 'external',
                 type = 'real',
                 value = 4.5,
                 texname = '\\text{lam1}',
                 lhablock = 'FRBlock',
                 lhacode = [ 3 ])

lam2 = Parameter(name = 'lam2',
                 nature = 'external',
                 type = 'real',
                 value = -0.0055,
                 texname = '\\text{lam2}',
                 lhablock = 'FRBlock',
                 lhacode = [ 4 ])

lam3 = Parameter(name = 'lam3',
                 nature = 'external',
                 type = 'real',
                 value = -391.51,
                 texname = '\\text{lam3}',
                 lhablock = 'FRBlock',
                 lhacode = [ 5 ])

lam4 = Parameter(name = 'lam4',
                 nature = 'external',
                 type = 'real',
                 value = 2.2,
                 texname = '\\text{lam4}',
                 lhablock = 'FRBlock',
                 lhacode = [ 6 ])

gg = Parameter(name = 'gg',
               nature = 'external',
               type = 'real',
               value = 0.056,
               texname = '\\text{gg}',
               lhablock = 'FRBlock',
               lhacode = [ 7 ])

vs = Parameter(name = 'vs',
               nature = 'external',
               type = 'real',
               value = 276.21,
               texname = '\\text{vs}',
               lhablock = 'FRBlock',
               lhacode = [ 8 ])

mpsi0 = Parameter(name = 'mpsi0',
                  nature = 'external',
                  type = 'real',
                  value = 52.1659,
                  texname = '\\text{mpsi0}',
                  lhablock = 'FRBlock',
                  lhacode = [ 9 ])

sinxi = Parameter(name = 'sinxi',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{sinxi}',
                  lhablock = 'FRBlock',
                  lhacode = [ 10 ])

theta = Parameter(name = 'theta',
                  nature = 'external',
                  type = 'real',
                  value = 1.87183,
                  texname = '\\theta',
                  lhablock = 'FRBlock',
                  lhacode = [ 11 ])

gamma = Parameter(name = 'gamma',
                  nature = 'external',
                  type = 'real',
                  value = 10,
                  texname = '\\gamma',
                  lhablock = 'FRBlock',
                  lhacode = [ 12 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

mh1 = Parameter(name = 'mh1',
                nature = 'external',
                type = 'real',
                value = 125.1,
                texname = '\\text{mh1}',
                lhablock = 'MASS',
                lhacode = [ 25 ])

mh2 = Parameter(name = 'mh2',
                nature = 'external',
                type = 'real',
                value = 35.7,
                texname = '\\text{mh2}',
                lhablock = 'MASS',
                lhacode = [ 38 ])

mpsi = Parameter(name = 'mpsi',
                 nature = 'external',
                 type = 'real',
                 value = 69.2,
                 texname = '\\text{mpsi}',
                 lhablock = 'MASS',
                 lhacode = [ 51 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4115955514522147,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.002524045267459,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.4668768693401673,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

wh1 = Parameter(name = 'wh1',
                nature = 'external',
                type = 'real',
                value = 0.006543253968888762,
                texname = '\\text{wh1}',
                lhablock = 'DECAY',
                lhacode = [ 25 ])

wh2 = Parameter(name = 'wh2',
                nature = 'external',
                type = 'real',
                value = 9.883738596155487e-7,
                texname = '\\text{wh2}',
                lhablock = 'DECAY',
                lhacode = [ 38 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

sinth = Parameter(name = 'sinth',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.sin(theta)',
                  texname = '\\text{sinth}')

cosxi = Parameter(name = 'cosxi',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.sqrt(1 - sinxi**2)',
                  texname = '\\text{cosxi}')

costh = Parameter(name = 'costh',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.cos(theta)',
                  texname = '\\text{costh}')

musSq = Parameter(name = 'musSq',
                  nature = 'internal',
                  type = 'real',
                  value = '-0.5*(lam1*vev**2)/vs + (vs*(3*lam3 + 2*lam4*vs))/6.',
                  texname = '\\text{musSq}')

muhsSq = Parameter(name = 'muhsSq',
                   nature = 'internal',
                   type = 'real',
                   value = 'vev*(lam1 + 2*lam2*vs)',
                   texname = '\\text{muhsSq}')

muhSq = Parameter(name = 'muhSq',
                  nature = 'internal',
                  type = 'real',
                  value = '2*lam*vev**2',
                  texname = '\\text{muhSq}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'lam*vev**2 + vs*(lam1 + lam2*vs)',
                texname = '\\text{muH}')

musq = Parameter(name = 'musq',
                 nature = 'internal',
                 type = 'real',
                 value = 'lam*vev**2 + vs*(lam1 + lam2*vs)',
                 texname = '\\text{musq}')

mm = Parameter(name = 'mm',
               nature = 'internal',
               type = 'real',
               value = '-(lam2*vev**2) - (lam1*vev**2)/(2.*vs) - (lam3*vs)/2. - (lam4*vs**2)/6.',
               texname = '\\text{mm}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

yhs = Parameter(name = 'yhs',
                nature = 'internal',
                type = 'real',
                value = '(2*muhsSq)/(muhSq - musSq)',
                texname = '\\text{yhs}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

tth = Parameter(name = 'tth',
                nature = 'internal',
                type = 'real',
                value = 'yhs/(1 + cmath.sqrt(1 + yhs**2))',
                texname = '\\text{tth}')

CTH = Parameter(name = 'CTH',
                nature = 'internal',
                type = 'real',
                value = '1/cmath.sqrt(1 + tth**2)',
                texname = '\\text{CTH}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

STH = Parameter(name = 'STH',
                nature = 'internal',
                type = 'real',
                value = 'CTH*tth',
                texname = '\\text{STH}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

