from common import Config
import git 
import os
import re
from file_patch import FilePatch

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


def getFilePatch(patch_str):
	def _getFileName(file_diff_str):
		pattern_filename = re.compile(r'\+\+\+|---')
		match_result_filename = re.split(pattern_filename,file_diff_str)
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
		file_name,file_diff = _getFileName(r)
		file_patch_list.append(FilePatch(file_name,file_diff))

	return file_patch_list

if __name__ == "__main__":
	pstr = loadPatch("./patches/0010-crypto-caam-qi-simplify-CGR-allocation-freeing.patch")
	diff_file_list = getFilePatch(pstr)
	# print(diff_file_list[0].toString())