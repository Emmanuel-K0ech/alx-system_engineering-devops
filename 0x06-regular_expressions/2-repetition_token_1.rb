#!/usr/bin/env ruby
# Regex for mutliple chars in between string
if ARGV.length != 0
  if ARGV[0].scan(/hb?tn/).join
      puts ARGV[0]
    end
else
  puts "Please provide argument (atlest 1)"
end
