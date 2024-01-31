#!/usr/bin/env ruby
#CAPS ONLY
if ARGV.length != 0
  for arg in ARGV
    if arg =~ /[A-Z]/
      match = arg.scan(/[A-Z]/)
      puts match.join()
    end
  end
end
