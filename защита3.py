x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
l12 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
l13 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
l23 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
if l12 > l13 and l12 > l23:
    l = ((l13 * l23 * (l23 + l13 + l12) * (l23 + l13 - l12)) ** 0.5) / (l23 + l13)
elif l13 > l12 and l13 > l23:
    l = ((l12 * l23 * (l12 + l23 + l13) * (l12 + l23 - l13)) ** 0.5) / (l12 + l23)
else:
    l = ((l12 * l13 * (l12 + l13 + l23) * (l12 + l13 - l23)) ** 0.5) / (l12 + l13)
print(l)