#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @ Filename : parse_patch.py
# @ Date 	 : 2019-7-29
# @ Author   : Wang Runzhe
# @ Funciton : parse patch 解析 patch 文件工具

from file_patch import FilePatch
import os
import re
import sys

Usage = "Usage : python parse_patch.py [path]"

def loadPatch(patch_file_patch):
	'''
	读patch文件
	'''
	if os.path.isdir(patch_file_patch):
		print("[-] ",patch_file_patch,"is a dir!")
		return 

	elif not os.path.exists(patch_file_patch):
		print("[-] ",patch_file_patch,"is not exists!")
		return 

	else:
		with open(patch_file_patch) as f:
			content = f.read()
			return content


def parsePatch(patch_str):
	def _getFileName(file_diff_str):
		pattern_filename = re.compile(r'\+\+\+|---')
		match_result_filename = re.split(pattern_filename,file_diff_str)
		if match_result_filename.__len__() <= 1:
			return None
		file_name = match_result_filename[1]
		file_diff = match_result_filename[2]

		pattern_at = re.compile(r'@')
		match_result = re.search(pattern_at,file_diff)
		file_diff = file_diff[match_result.span()[0]:]
		return file_name,file_diff


	file_patch_list = []
	pattern_diff = re.compile(r'diff --git.+')
	match_result = re.split(pattern_diff,patch_str)
	if match_result.__len__() > 1:
		match_result = match_result[1:]

	for r in match_result:
		result = _getFileName(r)
		if result == None:
			continue
		else:
			file_name,file_diff = result
			file_patch_list.append(FilePatch(file_name,file_diff))

	return file_patch_list

if __name__ == "__main__":
	if sys.argv.__len__() > 1:
		result = ''
		path = sys.argv[1]
		if os.path.isdir(path):
			for f in os.listdir(path):
				file_path = os.path.join(path,f)
				pstr = loadPatch(file_path)
				diff_file_list = parsePatch(pstr)
				for diff_file in diff_file_list:
					print(diff_file.toString())
					result += diff_file.toString()

		elif os.path.isfile(path):
			pstr = loadPatch(path)
			diff_file_list = parsePatch(pstr)
			for diff_file in diff_file_list:
				print(diff_file.toString())
				result += diff_file.toString()
		else:
			print("[-] path ",path,"is invalid")
			exit(0)
		with open('./patch_result.txt','w') as f:
			f.write(result)
	else:
		print(Usage)
	# dir_path = "./patches"
	# for f in os.listdir(dir_path):
	# 	file_path = os.path.join(dir_path,f)
	# 	pstr = loadPatch(file_path)
	# 	diff_file_list = getFilePatch(pstr)
	# 	for diff_file in diff_file_list:
	# 		print(diff_file.toString())