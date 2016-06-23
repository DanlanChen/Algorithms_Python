class Solution():
	def subsets(self,nums):
		if nums is None:
			return []
		ret = []
		self.dfs(nums, 0, [], ret)
		return ret

	def dfs(self, nums, pos, list_temp, ret):
		ret.append([] + list_temp)
		for i in xrange(pos, len(nums)):
			list_temp.append(nums[i])
			self.dfs(nums, i + 1, list_temp, ret)
			list_temp.pop()
			