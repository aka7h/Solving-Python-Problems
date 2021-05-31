import itertools
def twoNumberSum(array, targetSum):
	
	hash_table = {}
	
	for xx in range(0,len(array)):
		for yy in range(1,len(array)):
			dt = tuple(sorted([array[xx],array[yy]]))
			if dt in hash_table.keys() or array[xx]==array[yy]:
				pass
			else:
				hash_table[dt] = array[xx]+array[yy]
				
	dd = [k for k,v in hash_table.items() if v==targetSum]
	return(list(itertools.chain(*dd)))
	
	
			
