def compute_perm(perm_list, elements):

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