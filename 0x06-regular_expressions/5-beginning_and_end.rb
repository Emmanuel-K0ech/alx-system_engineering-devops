#!/usr/bin/env ruby
# Regex for string starting with 'h' and ending wit 'n'
# Can have any single character in between
if ARGV.length != 0
    if ARGV[0] =~ /\bh[a-zA-Z0-9]\Bn/
      puts ARGV[0]
    end
else
  puts "\n"
end
