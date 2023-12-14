class RangeMap():
    def __init__(self):
        self.mapping_rules = []
    
    def add_mapping_rule(self, start, end, increment):
        rule = {'start': start, 'end': end, 'increment': increment}
        self.mapping_rules.append(rule)
    
    def map_value(self, x):
        for rule in self.mapping_rules:
            if rule['start'] <= x <= rule['end']:
                return x + rule['increment']
        # If no rule matches, return the original value
        return x
    

file_data = open('input.txt','r')
lines = file_data.readlines()

test_data = open('test.txt','r')
test = test_data.readlines()

use_data = lines

maps = []

for i in range(0,7) :
    new_map = RangeMap()
    maps.append(new_map) 

map_counter = -2

# update maps

nums = []

for line in use_data :
    skip = False
    if len(line) == 1:
        skip = True
    elif not line[0].isnumeric():
        skip = True
        map_counter += 1
    
    if not skip :
        #update maps
        nums = line.split()

        dest_start = int(nums[0])
        index_start = int(nums[1])
        range_length = int(nums[2])

        maps[map_counter].add_mapping_rule(index_start,index_start+range_length,dest_start - index_start)


seed_data = use_data[0][7:].split()
seeds = []

minimum = -1

for i in range(int(len(seed_data)/2)) :
    
    seeds = seeds + list(range(int(seed_data[2*i]) , int(seed_data[2*i]) + int(seed_data[2*i + 1])))

print(len(seeds))

for seed in seeds :
    
    for map in maps :
        seed = map.map_value(seed)

    if minimum == -1 :
        minimum = seed
    else :
        minimum = min(minimum,seed)

print(minimum)