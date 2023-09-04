class SubsetGenerator:
    def __init__(self, nums):
        self.nums = nums

    def generate(self):
        subsets = [[]]
        for num in self.nums:
            current_subsets = [subset + [num] for subset in subsets]
            subsets.extend(current_subsets)
        return subsets

# Sample input
sample_input = [4, 5, 6]

# Create an instance of the SubsetGenerator class
subset_generator = SubsetGenerator(sample_input)

# Generate and print all possible unique subsets
subsets = subset_generator.generate()
print(subsets)
