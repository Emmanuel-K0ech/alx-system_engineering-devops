#!/usr/bin/env ruby
#Regex for a 10digit phone number
#with a look ahead for spaces
if ARGV.length != 0
  if ARGV[0] =~ /^(?!\s)[0-9]{10}/
      puts ARGV[0]
  end
else
  puts "\n"
end
