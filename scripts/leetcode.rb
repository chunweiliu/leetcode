require 'fuzzy_match'
require 'open-uri'
require 'yaml'

class LeetCode
  LEETCODE_URL = 'https://leetcode.com/problemset/algorithms/'.freeze
  HYPERLINK_REGEX = /<a.+?href="(.+?)"/.freeze
  PROBLEM_DIR = '../problems/'.freeze
  COLUMN_WIDTH = 3 # GitHub table requires at least three hyphens

  def initialize
    @underscore_name_list = underscore_name_list
    @matcher = FuzzyMatch.new(@underscore_name_list)
    @sorted_problem_config_list = sorted_problem_config_list
  end

  def create_solution_folders
    @underscore_name_list.each do |problem|
      folder_path = File.join(PROBLEM_DIR, problem)
      Dir.mkdir folder_path unless File.exists?(folder_path)
    end
  end

  def fuzzy_rename_solutions(folder_path, file_ext)
    # Rename: XXX-ProblemName-ii.xx
    Dir.glob("#{folder_path}*#{file_ext}") do |file_to_be_renamed|
      number = File.basename(file_to_be_renamed)[0..2]
      next if number.match(/\d{3}/).nil?

      underscore_name = @matcher.find(file_to_be_renamed)
      path_prefix = File.join(PROBLEM_DIR, underscore_name, underscore_name)

      new_path = "#{path_prefix}.#{file_ext}"
      p "cp #{file_to_be_renamed} #{new_path}"
      FileUtils.cp file_to_be_renamed, new_path

      setting = { 'name' => underscore_name, 
                  'link' => "https://leetcode.com/problems/#{underscore_name.gsub('_', '-')}/",
                  'number' => number }
      File.open("#{path_prefix}.yaml", 'w') do |file|
        file.write setting.to_yaml
      end
    end
  end

  def generate_readme
    File.open("../README.md", "w") do |file|
      file.write "# Leetcode solutions\n\n"
      file.write a_row_of ['#', 'Problem', 'Solutions']
      file.write a_row_of ['-' * COLUMN_WIDTH] * 3
      @sorted_problem_config_list.each do |problem|
        file.write(a_row_of [problem['number'],
                             "[#{title(problem['name'])}](#{problem['link']})",
                             solutions(problem['name'])])
      end
    end
  end

  private

  def underscore_name_list
    source = open(LEETCODE_URL).read
    source.scan(HYPERLINK_REGEX).select { |url| url[0][0..9] == '/problems/' }.map do |url|
      url[0]['/problems/'.length..-2].gsub('-', '_') # get the problem name only
    end
  end

  def sorted_problem_config_list
    problem_configs = []
    Dir.glob("#{PROBLEM_DIR}*") do |path|
      yaml_path = "#{path}/#{File.basename(path)}.yaml"
      if File.exists? yaml_path
        problem_configs << YAML.load_file(yaml_path)
      end
    end
    problem_configs.sort_by { |config| config['number'] }.reverse
  end

  def title(underscore_name)
    underscore_name.split('_').join(' ')
  end

  def a_row_of (columns)  
    columns.each_with_object('') do |column, string|
      string << '|' + column.ljust(COLUMN_WIDTH, ' ')
    end + "|\n"
  end

  def solutions(underscore_name)
    files = ''
    %w(cc py rb).each do |ext|
      file_path = "#{File.join(PROBLEM_DIR, underscore_name, underscore_name)}.#{ext}"
      if File.exists? file_path
        files << "[#{ext}](#{file_path[1..-1]}) " # Start from the ./ instead of ../
      end
    end
    files
  end
end

# Clean up folder
# LeetCode.new.create_solution_folders
# LeetCode.new.fuzzy_rename_solutions('../Python-2/', 'py')
# LeetCode.new.fuzzy_rename_solutions('../C++/0/', 'cc')
# LeetCode.new.fuzzy_rename_solutions('../C++/1/', 'cc')

# Reindexing
LeetCode.new.generate_readme