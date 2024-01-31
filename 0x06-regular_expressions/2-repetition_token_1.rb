#!/usr/bin/env ruby
# Regex for one or no chars in between string
if ARGV.length != 0
    if ARGV[0] =~ /hbt{0,1}n/
      puts ARGV[0]
    end
else
  puts "Please provide argument (atlest 1)"
end
