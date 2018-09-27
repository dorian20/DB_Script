
path='ltcmdev_slow.sql'
read_file = function (path)
local file = io.open(path, "rb") 
if not file then return nil end

local lines = {}

for line in io.lines(path) do
    local words = {}
    for word in line:gmatch("%w+") do 
        table.insert(words, word) 
        print(word)
    end    
  table.insert(lines, words)
end

file:close()
return lines;
end
