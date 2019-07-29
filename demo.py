#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @ Filename : demo.py
# @ Date 	 : 2019-7-29
# @ Author   : Wang Runzhe
# @ Funciton : [Demo]如何在代码中使用parse patch工具


from parse_patch import parsePatch
from parse_patch import loadPatch

if __name__ == "__main__":
	patch = loadPatch('./patches/0012-arm-Convert-arm-boot_lock-to-raw.patch')
	patch_list = parsePatch(patch)

	for fp in patch_list:
		print(fp.file_name)			# 被修改的文件名
		print(fp.total_patch)		# 该文件的完整补丁
		print(fp.func_list)			# 该文件中修改的函数
		print(fp.func_patch_list)	# 该文件中每个函数的补丁