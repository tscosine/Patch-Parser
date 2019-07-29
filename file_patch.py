import re
class FilePatch:
	def __init__(self,file_name,patch):
		self.file_name = file_name
		self.total_patch = patch
		self.func_list = []
		self.func_patch_list = []
		self.__getFuncList()

	def __detectFunc(self,funcstr):
		
	def __getFuncList(self):
		pattern_func = re.compile(r'@@ -\d+,\d+ \+\d+,\d+ @@')
		match_result_func = re.split(pattern_func,self.total_patch)
		for i in match_result_func:
			print(i)


	def toString(self):
		s = ''
		s += self.file_name + '\n'
		s += self.total_patch + '\n'
		return s