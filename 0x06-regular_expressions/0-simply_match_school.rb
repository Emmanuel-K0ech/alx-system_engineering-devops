#!/usr/bin/env ruby
if ARGV.length != 0
  for arg in ARGV
    if arg =~ /School/
      match = arg.scan(/School/)
      puts match.join()
    end
  end
end
