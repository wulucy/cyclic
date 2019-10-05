def compute_perm(perm_list, elements):
	"""
	Simplifies permutations written in cyclic
	notation.

	Args:
		perm_list (list): List of integers or strings representing
			permutations in cyclic notation. For example, 
			(12)(34) = [12, 34].
		elements (list): List of elements that are eligible for
			inclusion in a permutation. For example, elements
			for S_4 would be [1, 2, 3, 4].
	
	Returns:
		perm_dict (dict): Dictionary keyed by element, with values
			indicating where the element will be sent by the
			resulting permutation.
	"""

    perm_list = [str(x) for x in perm_list]
    elements = [str(x) for x in elements]
    perm_dict = {}

    for e in elements:
        orig_e = e
        for p in perm_list:
            i = p.find(e)
            if i != -1: # if e in string
                if i == len(p)-1:
                    e = p[0]
                else:
                    e = p[i+1]
        perm_dict[orig_e] = e

    perm_dict = {int(k): int(v) for k, v in perm_dict.items()}

    return perm_dict