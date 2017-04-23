def valid_pass(passw):
    p_check = [False,False,False]
    p_check[0] = any([False if p_check[0] == False and (ord(x) < 65 or ord(x) > 90) else True for x in passw])
    p_check[1] = any([False if p_check[1] == False and (ord(x) < 97 or ord(x) > 122) else True for x in passw]) 
    p_check[2] = any([False if p_check[2] == False and (ord(x) < 48 or ord(x) > 57) else True for x in passw])
    return  p_check[0] and p_check[1] and p_check[2]


def pass_strength(passw):
    spe = ['.', '?', '!', '&', '#', ',', ';', ':', '-', '_', '*']
    
    u = [x for x in passw if ord(x) >= 65 and ord(x) <= 90]
    l = [x for x in passw if ord(x) >= 97 and ord(x) <= 122]
    n = [x for x in passw if ord(x) >= 48 and ord(x) <= 57]
    c = [x for x in passw if x in spe]

    tscore = (len(u)*2+len(l)*2+len(n)*4+len(c)*6) 
    streng = tscore/45.0 * 10

    if streng > 10:
        streng = 10
        
    return int(streng)

