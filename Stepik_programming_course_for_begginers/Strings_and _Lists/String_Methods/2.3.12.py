gl = ' ' + input().lower()
g = ["a", "o", "y", "e", "u", "i"]
a = gl.replace(g[0], '')
a1 = a.replace(g[1], '')
a2 = a1.replace(g[2], '')
a3 = a2.replace(g[3], '')
a4 = a3.replace(g[4], '')
a5 = a4.replace(g[5], '')
r = '.'.join(a5)
print(r)
