#!/usr/bin/env ruby
# Regex for one or more in between string
# Excluding one occurence - hbon 
if ARGV.length != 0
    if ARGV[0] =~ /hbt*n/
      puts ARGV[0]
    end
else
  puts "Please provide argument (atlest 1)"
end
