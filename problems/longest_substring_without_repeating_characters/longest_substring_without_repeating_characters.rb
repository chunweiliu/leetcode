# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
  return 0 unless s && !s.empty?

  substring = {}
  start_index = 0
  longest = 0
  s.each_char.with_index do |c, index|
  	if substring.key?(c)
      longest = [longest, index - start_index].max

      # start_index never looks back. case: s = 'abba'.
      start_index = [start_index, substring[c] + 1].max
  	end
    substring[c] = index
  end

  [longest, s.length - start_index].max
end
