#!/bin/env python

class Student(object):
	def __init__(self, name, conf):
		self.name = name
		self.conf = conf
		self.exam = 0
		self.labs = {}
	def make_lab(self, m, n):
		self.labs[m] = n if n <= self.conf['lab_max'] else self.conf['lab_max']
		return self
	def make_exam(self, m):
		self.exam = m if m <= self.conf['exam_max'] else self.conf['exam_max']
		return self
	def is_certifed(self):
		sum = self.__get_sum()
		return (sum, sum / self.__get_max() >= self.conf['k'])
	def __get_max(self):
		return self.conf['exam_max'] + self.conf['lab_max'] * self.conf['lab_num']
	def __get_sum(self):
		res = self.exam
		for i in self.labs:
			res += self.labs[i]
		return res

conf = {
	'exam_max': 30, # количество баллов, доступная за сдачу экзамена
	'lab_max': 7,   # количество баллов, доступная за выполнение 1 практической работы
	'lab_num': 10,  # количество практических работ в курсе
	'k': 0.61,      # доля баллов от максимума, которую необходимо набрать для получения сертификата
}

s = Student('Ivanov', conf)
print(s.is_certifed())
s.make_lab(1, 5)
s.make_lab(2, 7)
s.make_lab(4, 10)
s.make_lab(2, 0)
s.make_exam(20)
print(s.is_certifed())
s.make_lab(1, 9)
s.make_lab(2, 9)
s.make_lab(3, 9)
s.make_lab(4, 9)
s.make_lab(5, 9)
s.make_exam(99)
print(s.is_certifed())
