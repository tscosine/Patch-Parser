#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @ Filename : file_patch.py
# @ Date 	 : 2019-7-29
# @ Author   : Wang Runzhe
# @ Funciton : parse patch 工具中数据结构的定义

import re
class FilePatch:
	def __init__(self,file_name,patch):
		self.file_name = file_name
		self.total_patch = patch
		self.func_list = []
		self.func_patch_list = []
		self.__getFuncList()
		
	def __getFuncList(self):
		pattern_func_head = re.compile(r'@@ -\d+,\d+ \+\d+,\d+ @@')
		pattern_func = re.compile(r'\w+ \w+\(\w|\s+\)')
		match_result_func = re.split(pattern_func_head,self.total_patch)
		for func_diff_str in match_result_func:
			func_name = func_diff_str.split('\n')[0]
			if re.search(pattern_func,func_name):
				self.func_list.append(func_name)
				self.func_patch_list.append(func_diff_str)

	def toString(self):
		s = ''
		s += '[Patched File Name]' + self.file_name
		if self.func_list.__len__() > 0:
			s += 'Patched Func:' + '\n'
			for func_name in self.func_list:
				s += func_name
		else:
			s += 'No func detected'
		s += '\n'
		return s