DIST_CAILLOUX: int = 10
CAILLOUX_EVA: int = 322
RESTE_LEA: int = 156
cailloux_lea: int
cailloux_louis: int
cailloux_mathilde: int
cailloux_roland: int
dist_eva: float
dist_lea: float
dist_louis: float
dist_mathilde: float
dist_roland: float

cailloux_louis = RESTE_LEA * 3
cailloux_mathilde = cailloux_louis + 233
cailloux_lea = CAILLOUX_EVA + 100 + RESTE_LEA
cailloux_roland = cailloux_louis * 2

dist_eva = CAILLOUX_EVA * DIST_CAILLOUX / 1000
dist_lea = cailloux_lea * DIST_CAILLOUX / 1000
dist_louis = cailloux_louis * DIST_CAILLOUX / 1000
dist_mathilde = cailloux_mathilde * DIST_CAILLOUX / 1000
dist_roland = cailloux_roland * DIST_CAILLOUX / 1000

print('Nombre de cailloux et distances :'
      '\n\t- Léa :', cailloux_lea, 'cailloux et', dist_lea, 'Km',
      '\n\t- Louis :', cailloux_louis, 'cailloux et', dist_louis, 'Km',
      '\n\t- Matilde :', cailloux_mathilde, 'cailloux et', dist_mathilde, 'Km',
      '\n\t- Eva :', CAILLOUX_EVA, 'cailloux et', dist_eva, 'Km',
      '\n\t- Roland :', cailloux_roland, 'cailloux et', dist_roland, 'Km')
