# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(numbers, target)
  index_of = {}
  numbers.each_with_index do |number, index|
    residual = target - number
    if index_of.key?(residual)
      return [index_of[residual], index]
    end
    index_of[number] = index
  end
  return [-1, -1]
end