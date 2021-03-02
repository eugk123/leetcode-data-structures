def dfs(current, index):
    # Constraint: if end is reached, return
    if index == len(nums):

        # Constraint: target is reached, +1
        if current == S:
            self.count += 1
        return

    dfs(current + nums[index], index + 1)
    dfs(current - nums[index], index + 1)

    return self.count