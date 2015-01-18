__author__ = 'pinballwizard'

import scipy
from scipy import array, exp, arange, linspace, zeros, sort, sqrt, rot90
from scipy.constants import m_e, pi, hbar, h
from scipy.sparse.linalg import eigs
from matplotlib.pyplot import *
import matplotlib.animation as animation

N = 1000  # количество выборок
row = [4]  # собственные векторы
number = max(row) + 1  # количество собственных векторов
a = 10  # симметричные границы вычисляемой области
V = 100  # потенциал ямы
mu = 0  # смещение ямы относительно нуля
E0 = 0  # собственная энергия частицы
F = -0.2  # Прилагаемая сила
E1 = 0.5  # Энергия удвоения решетки
ty = -1  # Предполагаемое значение интеграла перескока

gaussian = lambda y: -V*exp(-((y-mu)**2))
x = linspace(-a, a, N)
time = linspace(0, a, N)
step = abs(x[1]-x[0])
v = gaussian(x)


def wave():
	# Создаем вектор обсчета
	# vv = 1+(E+v)*step**2 # Одиночная ловушка в виде гауссиана
	E = scipy.zeros(N)+E1/2-E1/2*(-1)**arange(N)
<<<<<<< HEAD
	# print(E)
	vv = E
	# print(vv)
=======
	print(E)
	vv = E
	print(vv)
>>>>>>> github/master1
	# Создаем матрицу значений
	minus_ones = -1*scipy.ones(N-1)
	diagonals = [minus_ones, vv, minus_ones]
	H = scipy.sparse.diags(diagonals, [-1, 0, 1]).todense()  # Формируем гамильтониан
	print(H)
	[e, psi] = eigs(H, k=number, which='SR')  # Вычисляем собственные значения и вектора
	e = e[row]
	psi = psi[:, row]
	return e, psi


def draw(e, psi):
	# вывод проверочной информации
	sorted_e = sort(e)
	if (sorted_e != e).all():
		print("Первые собственные значения не являются минимальными, результаты не являются достоверными")
		print("Действительно минимальные собственные значения --> %s" % sorted_e)
	print("Минимальные собственные веторы --> %s" % e)
	print("Величина шага --> %s" % step)

	# вывод графиков
	fig = figure()
	# plot(x, v)
	# hold(True)
	plot(x, psi)
	hold(False)
	title("Particle")
	xlabel("Range")
	ylabel("Energy")
	grid()
	show()


def reflection(psi):
	b = [x.searchsorted(-2), x.searchsorted(2)]
	sf = lambda x: sum(abs(x) ** 2)
	norm = sqrt(sf(psi))
	C = sf(psi[b[1]:]) / norm
	AB = sf(psi[:b[1]]) / norm
	# AA = sf(psi[:b[0]])/norm
	# print(AA)
	# BC = sf(psi[b[0]:])/norm
	# print(BC)

	D2 = (C / AB) ** 2
	R2 = 1 - D2
	# D1 = (BC/AA)**2
	# R1 = 1-D1
	print("Коэффициент прохождения %s" % D2)
	print("Коэффициент отражения %s" % R2)


def ret():
	[e, psi] = wave()
	reflection(psi)
	draw(e, psi)