#!/usr/bin/env ruby
#output phone number or name of sender and receiver
name = ARGV[0].scan(/\[from:(\w+|\+?\d+)\] \[to:(\w+|\+?\d+)\] \[flags:(\-?\d:\-?\d:\-?\d:\-?\d)\]/)
puts "#{name[0][0]},#{name[0][1]}.#{name[0][2]}"
