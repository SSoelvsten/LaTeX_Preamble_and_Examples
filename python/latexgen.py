#!/usr/bin/env python

import os
import base64
import argparse
template = """JSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJQolIExvYWQgUHJlYW1wbGUgICAgICAgICAlCiUlJSUl
JSUlJSUlJSUlJSUlJSUlJSUlJSUKClxkb2N1bWVudGNsYXNzW2E0LCBlbmdsaXNoXXthcnRpY2xl
fQoKJUltcG9ydCBmcm9tIHRoZSBzYW1lIGZvbGRlcgolXGlucHV0e3ByZWFtYmxlX2VuLnRleH0K
CiVJbXBvcnQgZnJvbSBhYnNvbHV0ZSBwYXRoCiVcdXNlcGFja2FnZXtpbXBvcnR9CiVcaW1wb3J0
e0M6L0dpdEh1Yi9MYVRlWF9QcmVhbWJsZV9hbmRfRXhhbXBsZXMvcHJlYW1ibGUvfXtwcmVhbWJs
ZV9kay50ZXh9CgolSW1wb3J0IGZyb20gYSByZWxhdGl2ZSBwYXRoClx1c2VwYWNrYWdle2ltcG9y
dH0KXHN1YmltcG9ydHsuLi9wcmVhbWJsZS99e3ByZWFtYmxlX2VuLnRleH0KCiUlJSUlJSUlJSUl
JSUlJSUlJSUlJSUlJSUKJSBEb2N1bWVudCBzdGFydHMgaGVyZSEgJQolJSUlJSUlJSUlJSUlJSUl
JSUlJSUlJSUlCgpcYmVnaW57ZG9jdW1lbnR9CgolIERlZmluZSB0aXRsZSBhbmQgbW9yZSBvbiBm
cm9udHBhZ2UKCVxzZXR0aXRsZXtUaXRsZX17U3VidGl0bGV9CiAgICBcYWRkYXV0aHtTdGVmZmFu
IFPDuGx2c3Rlbn17MjAxNTA1ODMyQHBvc3QuYXUuZGt9e1wsIGF1NTM0MDY4fQpcbWFrZXRpdGxl
CgpcYmVnaW57YWJzdHJhY3R9Clxub2luZGVudApMb3JlbSBpcHN1bSBkb2xvciBzaXQgYW1ldCwg
Y29uc2VjdGV0dXIgYWRpcGlzY2luZyBlbGl0LCBzZWQgZG8gZWl1c21vZCB0ZW1wb3IgaW5jaWRp
ZHVudCB1dCBsYWJvcmUgZXQgZG9sb3JlIG1hZ25hIGFsaXF1YS4gVXQgZW5pbSBhZCBtaW5pbSB2
ZW5pYW0sIHF1aXMgbm9zdHJ1ZCBleGVyY2l0YXRpb24gdWxsYW1jbyBsYWJvcmlzIG5pc2kgdXQg
YWxpcXVpcCBleCBlYSBjb21tb2RvIGNvbnNlcXVhdC4KXGVuZHthYnN0cmFjdH0KClx0YWJsZW9m
Y29udGVudHMKClxuZXdwYWdlClxzZWN0aW9ue0ludHJvZHVjdGlvbn0gXGxhYmVse3NlYzppbnRy
b30KTG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxp
dCwgc2VkIGRvIGVpdXNtb2QgdGVtcG9yIGluY2lkaWR1bnQgdXQgbGFib3JlIGV0IGRvbG9yZSBt
YWduYSBhbGlxdWEuIFV0IGVuaW0gYWQgbWluaW0gdmVuaWFtLCBxdWlzIG5vc3RydWQgZXhlcmNp
dGF0aW9uIHVsbGFtY28gbGFib3JpcyBuaXNpIHV0IGFsaXF1aXAgZXggZWEgY29tbW9kbyBjb25z
ZXF1YXQuCgoKClxiZWdpbnt0aGViaWJsaW9ncmFwaHl9ezl9ClxiaWJpdGVte2JpYml0ZW19CglM
YXN0LCBGaXJzdDogXGVtcGh7VGl0bGV9LCBwdWJsaWNhdGlvbiwgZWRpdGlvbiwgeWVhcgpcZW5k
e3RoZWJpYmxpb2dyYXBoeX0KXGJpYmxpb2dyYXBoeXN0eWxle2FiYnJ2fQpcYmlibGlvZ3JhcGh5
e3JlZmVyZW5jZXJ9CgpcbmV3cGFnZQpcYXBwZW5kaXgKXHNlY3Rpb257QXBwZW5kaXh9CkxvcmVt
IGlwc3VtIGRvbG9yIHNpdCBhbWV0LCBjb25zZWN0ZXR1ciBhZGlwaXNjaW5nIGVsaXQsIHNlZCBk
byBlaXVzbW9kIHRlbXBvciBpbmNpZGlkdW50IHV0IGxhYm9yZSBldCBkb2xvcmUgbWFnbmEgYWxp
cXVhLiBVdCBlbmltIGFkIG1pbmltIHZlbmlhbSwgcXVpcyBub3N0cnVkIGV4ZXJjaXRhdGlvbiB1
bGxhbWNvIGxhYm9yaXMgbmlzaSB1dCBhbGlxdWlwIGV4IGVhIGNvbW1vZG8gY29uc2VxdWF0LgoK
XGVuZHtkb2N1bWVudH0=
"""
preamble_base = """JSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKJSAgICBQYXBlcnNpemUgYW5kIGVuY29k
aW5nICAgICUKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKCiUgU2l6ZSBvZiBtYXJn
aW5zIGNhbiBiZSBjaGFuZ2VkIGhlcmUgaW4gdGhlIG91dGNvbW1lbnRlZCB2ZXJzaW9uIQolXHVz
ZXBhY2thZ2VbYTRwYXBlciwgdG90YWw9ezZpbiwgOGlufV17Z2VvbWV0cnl9CSV0b3RhbD17d2lk
dGgsIGhlaWdodH0KXHVzZXBhY2thZ2VbYTRwYXBlcl17Z2VvbWV0cnl9CgolIEJhc2ljczogZm9u
dCwgY29kZWMgZXRjLgpcdXNlcGFja2FnZVt1dGY4XXtpbnB1dGVuY30JCQkJCQklIGVuY29kaW5n
OiB1dGYtOCAobm9yZGljIGxldHRlcnMpClx1c2VwYWNrYWdlW1QxXXtmb250ZW5jfQkJCQkJCSUg
dXNlIDgtYml0IGVuY29kZWQgZm9udHMKXHJlbmV3Y29tbWFuZHtcc2ZkZWZhdWx0fXtwaHZ9CQkJ
CQklIGNoYW5nZXMgdGhlIGRlZmF1bHQgZm9udAoKJVx1c2VwYWNrYWdlW3BhcmZpbGxde3BhcnNr
aXB9ICAgICAgJUluc3RlYWQgb2YgaW5kZW50aW5nIG9uIGEgbmV3bGluZSBhZGRzIHdoaXRlc3Bh
Y2UKCgoKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKJSAgICAgIFRhYmxlcyBhbmQg
ZmlndXJlcyAgICAgICUKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKClx1c2VwYWNr
YWdle3RhYnVsYXJ4LGJvb2t0YWJzLGF1dGhibGt9CQkgICAgJSB2YXJpb3VzIGJhc2ljIHN0dWZm
IGZvciB0YWJsZXMgYW5kIG1vcmUKCiUgRmlndXJlcyBhbmQgY2FwdGlvbnMKXHVzZXBhY2thZ2V7
Y2FwdGlvbn0JCQkJCQkJJSBjcmVhdGUgY2FwdGlvbnMgZm9yIGZpZ3VyZXMKXHVzZXBhY2thZ2V7
c3ViZmlnfQkJCQkJCQkJJSBjcmVhdGUgc3ViZmlndXJlcyBvZiBhIGZpZ3VyZQolXHVzZXBhY2th
Z2V7c3ViY2FwdGlvbn0JCQkJCSUgY3JlYXRlIGNhcHRpb25zIGZvciBzdWJmaWd1cmVzCiAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAlICAgICBjdXJyZW50bHkgb2ZmLCBkdWUgdG8g
Y29uZmxpY3RzCgpcdXNlcGFja2FnZXt3cmFwZmlnfQkJCQkJCQklIGxldHRpbmcgZmlndXJlcyBi
ZSBpbiB0ZXh0CgpcdXNlcGFja2FnZXtyb3RhdGluZ30gICAgICAgICAgICAgJSBsZXQgYW55IGVu
dmlyb25tZW50IGJlIHJvdGF0ZWQgKGZpZ3VyZXMgc2lkZXdheXMpCiAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAlICAgICBcYmVnaW57c2lkZXdheXN9IG9yIFxiZWdpbnt0dXJufXsz
MH0KCgoKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlCiUgICAgICAgICAgIFZh
cmlhYmxlcyAgICAgICAgICAgICAgJQolJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUl
JSUKXHVzZXBhY2thZ2V7cGdma2V5c30JCQklSW5pdGlhbGl6ZSB0aGUgdmFyaWFibGUga2V5LXZh
bHVlIHBhcmlycwoKXG5ld2NvbW1hbmR7XHNldHZhbHVlfVsxXXtccGdma2V5c3svdmFyaWFibGVz
LyMxfX0KXG5ld2NvbW1hbmR7XGdldHZhbHVlfVsxXXtccGdma2V5c3ZhbHVlb2Z7L3ZhcmlhYmxl
cy8jMX19ClxuZXdjb21tYW5ke1xkZWNsYXJlfVsxXXslCiBccGdma2V5c3sKICAvdmFyaWFibGVz
LyMxLmlzIGZhbWlseSwKICAvdmFyaWFibGVzLyMxLnVua25vd24vLnN0eWxlID0ge1xwZ2ZrZXlz
Y3VycmVudHBhdGgvXHBnZmtleXNjdXJyZW50bmFtZS8uaW5pdGlhbCA9ICMjMX0KIH0lCn0KClxk
ZWNsYXJle30KCgoKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKJSAgICAgIExhVGVY
IFByb2dyYW1taW5nICAgICAgICUKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKClx1
c2VwYWNrYWdle3hwYXJzZX0JCQkJCQkJCSUgU2Nhbm5pbmcgYXJndW1lbnRzClx1c2VwYWNrYWdl
e3hpZnRoZW59CQkJCQkJCSUgQ29uZGl0aW9uYWxzClx1c2VwYWNrYWdle3hzdHJpbmd9ICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICUgU3RyaW5nIGZ1bmN0aW9ucwpcdXNlcGFja2FnZXtjYWxj
fQkJCQkJCQkJJSBDYWxjdWxhdGlvbnMKCgoKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUl
JSUKJSAgICAgICAgICBIeXBlcm1lZGlhICAgICAgICAgICUKJSUlJSUlJSUlJSUlJSUlJSUlJSUl
JSUlJSUlJSUlJSUKClx1c2VwYWNrYWdle3VybCwgaHlwZXJyZWZ9CQkJCQkJCSUgXHVybHtsaW5r
fSBhbmQgXGhyZWZ7bGlua317cmVwbGFjaW5nIHRleHR9CgolTWFjcm9zIHRha2VuIGZyb20gdGhl
IHByZWFtYmxlIG9mIHRoZSBNYXRGeXNUdXRvciBMYVRlWCBHdWlkZS4KXG5ld2NvbW1hbmQqe1xo
dHRwfVsxXXtcaHJlZntodHRwOi8vIzF9eyMxfX0JCSUgbWFjcm8gZm9yIGh0dHAgbGlua3M6IFxo
dHRwe3d3dy5tYXRmeXN0dXRvci5ka30KXG5ld2NvbW1hbmQqe1xtYWlsdG99WzFde1xocmVme21h
aWx0bzojMX17IzF9fQkJJSBtYWNybyBmb3IgbWFpbHM6IFxtYWlsdG97ZW1haWxAZW1haWwuY29t
fQoKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKJSAgICAgICAgIFN0eWxpemF0aW9u
ICAgICAgICAgICUKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKCiUgSGVhZGVycyBv
ZyBmb290ZXJzClx1c2VwYWNrYWdle2xhc3RwYWdlfSAgICAgICAgICAgICAgICAgICAgICAgICAg
ICUgXGxhc3RwYWdlIGNvbW1hbmQgZm9yIG51bWJlcnMgb2YgcGFnZXMKXHVzZXBhY2thZ2V7ZmFu
Y3loZHJ9ICAgICAgICAgICAgICAgICAgICAgICAgICAgJSBjcmVhdGUgY29vbCBoZWFkZXJzIGFu
ZCBmb290ZXJzClxwYWdlc3R5bGV7ZmFuY3l9ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICUgd2hvIGRvZXNuJ3Qgd2FudCB0aGVpciBwYWdlIHRvIGJlIGZhbmN5PwoKJSBVc2Ugb2YgY29s
dW1ucwpcdXNlcGFja2FnZXttdWx0aWNvbH0KCiUgUXVvdGF0aW9ucwolICJkYW5pc2giIG9yICJi
cml0aXNoIgpcdXNlcGFja2FnZVtkYW5pc2g9Z3VpbGxlbWV0c117Y3NxdW90ZXN9ICAgIAklIHR3
byBzdHlsZXM6ICJxdW90ZXMiIG9yID4+Z3VpbGxlbWV0czw8CiVcTWFrZUF1dG9RdW90ZXvCu317
wqt9ICAgICAgICAgICAgICAgICAgICAgICAJJSBkZWNvbW1lbnQgZm9yIGVhc3kgbWFjcm8KJVxN
YWtlQXV0b1F1b3RlKnvigLp9e+KAuX0gICAgICAgICAgICAgICAgICAgICAgCSUgZGVjb21tZW50
IGZvciBldmVuIGVhc2llciBtYWNyb3MKCiUgTGlrZSBhIHBhcmFncmFwaCwgYnV0IGFkZHMgYWxz
byBhIGxpbmVicmVhayBhZnRlci4gKEFsc28gaXMgbm90IHJlY29yZGVkIG9uIGxhYmVsbGluZykK
XG5ld2NvbW1hbmR7XGxicGFyYWdyYXBofVsxXXtcdnNwYWNlezAuM2VtfSBcbm9pbmRlbnQgXHRl
eHRiZnsjMX1cXCBcbm9pbmRlbnR9CgolJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJQol
ICAgICAgICAgICAgIE1hdGggICAgICAgICAgICAgJQolJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUl
JSUlJSUlJQolXG5ld2NvbW1hbmR7XGhtbWF4fXswfQkJCQkJCQkJJSBtaW5pbWl6ZXMgdGhlIGFt
b3VudCBvZiBib2xkIGZhbWlsaWVzCiVcbmV3Y29tbWFuZHtcYm1tYXh9ezF9CQkJCQkJCQklIHRo
aXMgYWxsb3dzIGZvciBtb3JlIG1hdGggZmFtaWxpZXMKCiUgdmFyaW91cyBiYXNpYyBzdHVmZgpc
dXNlcGFja2FnZXttYXRodG9vbHMsIGFtc21hdGh9ClxhbGxvd2Rpc3BsYXlicmVha3MgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAlIGFsbG93IHBhZ2VicmVha3MgaW4gYWxpZ24qID8K
CiUgVmFyaW91cyBzeW1ib2wgcGFja2FnZXMKXHVzZXBhY2thZ2V7YW1zc3ltYn0KXHVzZXBhY2th
Z2VbdXRvcGlhXXttYXRoZGVzaWdufQkJCQkJICAgICUgZnVsbCBvdmVyd3JpdGUgb2YgdGhlIGZv
bnQgc3lzdGVtClx1c2VwYWNrYWdle3N0bWFyeXJkfQkJCQkJCQkJJSBldmVuIG1vcmUgc3ltYm9s
cwoKXERlY2xhcmVNYXRoQWxwaGFiZXR7XG1hdGhwemN9e09UMX17cHpjfXttfXtpdH0gICAgICUg
XG1hdGhwemMgYSBsZXNzIHBvbXBvdXMgY3VybHkgdHlwZXNldAoKJSBNYXRoIHNob3J0Y3V0cwpc
cmVuZXdjb21tYW5ke1xkfXtcLCBcbWF0aHJte2R9fSAgICAgICAgICAgICAgICAgICAgJSBcZCA9
IGRpZmZlcmVudGlhbCBkIHdpdGggYSBiaXQgb2Ygc3BhY2luZwpcbmV3Y29tbWFuZHtcZX17XG1h
dGhybXtlfX0gICAgICAgICAgICAgICAgICAgICAgICAgJSBcZSA9IGV1bGVycyBudW1iZXIKXG5l
d2NvbW1hbmR7XFJ9e1xtYXRoYmJ7Un19ICAgICAgICAgICAgICAgICAgICAgICAgICUgXFIgPSBS
ZWFsIG51bWJlcnMKXG5ld2NvbW1hbmR7XE59e1xtYXRoYmJ7Tn19ICAgICAgICAgICAgICAgICAg
ICAgICAgICUgXE4gPSBOYXR1cmFsIG51bWJlcnMKXG5ld2NvbW1hbmR7XEN9e1xtYXRoYmJ7Q319
ICAgICAgICAgICAgICAgICAgICAgICAgICUgXEMgPSBDb21wbGV4IG51bWJlcnMKXG5ld2NvbW1h
bmR7XFF9e1xtYXRoYmJ7UX19ICAgICAgICAgICAgICAgICAgICAgICAgICUgXFEgPSBSYXRpb25h
bCBudW1iZXJzClxuZXdjb21tYW5ke1xGfXtcbWF0aGJie0Z9fQkJCQkJCQklIFxGCgpcbmV3Y29t
bWFuZHtcYWJzfVsxXXtcbGVmdFxsdmVydCAjMSBccmlnaHRccnZlcnR9CQkJJSBcYWJze2FyZ30J
CWFic29sdXRlL21vZHVsbyBvZiB2YWx1ZQpcbmV3Y29tbWFuZHtcbm9ybX1bMV17XGxlZnRcbFZl
cnQgIzEgXHJpZ2h0XHJWZXJ0fQkJCSUgXG5vcm17YXJnfQlub3JtIG9mIGEgdmFsdWUKXG5ld2Nv
bW1hbmR7XGNlaWx9WzFde1xsZWZ0XGxjZWlsICMxIFxyaWdodFxyY2VpbH0JCQklIFxjZWlse2Fy
Z30JY2VpbGluZyBvZiBhIHZhbHVlClxuZXdjb21tYW5ke1xmbG9vcn1bMV17XGxlZnRcbGZsb29y
ICMxIFxyaWdodFxyZmxvb3J9CQklIFxmbG9vcnthcmd9CWZsb29yIG9mIGEgdmFsdWUKXG5ld2Nv
bW1hbmR7XGlucHJvZH1bMl17XGxlZnRcbGFuZ2xlICMxICwgIzIgXHJpZ2h0XHJhbmdsZX0JJSBc
aW5wcm9ke2FyZ30JaW5uZXIgcHJvZHVjdAoKXG5ld2NvdW50ZXJ7aX0KClxEZWNsYXJlRG9jdW1l
bnRDb21tYW5kIFxzZXEgeyBnIGcgZyBnIH0gewkJCSUgXHNlcXt4fXtpfXtqfXtzfQoJXHNldGNv
dW50ZXJ7aX17MH0JCQkJCQkJCSUgeF9pLCB4X2krcywgLi4uIHhfagoJXElmVmFsdWVUIHsjMn0g
eyBcYWRkdG9jb3VudGVye2l9eyMyfSB9CglcSWZWYWx1ZVRGIHsjMX0KCQl7IzF9CgkJe3h9Cglf
eyBcYXJhYmlje2l9IH0sCglcSWZWYWx1ZVRGIHsjNH0gCgkJe1xhZGR0b2NvdW50ZXJ7aX17IzR9
fQoJCXtcYWRkdG9jb3VudGVye2l9ezF9fQoJXElmVmFsdWVURiB7IzF9IAoJCXsjMX0KCQl7eH0g
CglfeyBcYXJhYmlje2l9IH0sCglcZG90cwoJXElmVmFsdWVURiB7IzN9CgkJeyAsICMxX3sjM30g
fQoJCXt9Cn0KClxEZWNsYXJlRG9jdW1lbnRDb21tYW5kIFxlcm8geyBnIGcgfSB7CQkJCSUgXGVy
byB7eCwgeX0KCVxiZWdpbnthcnJheX17Y30JCQkJCQkJCSUJeAoJCVxJZlZhbHVlVEZ7IzF9CQkJ
CQkJCQklCX4KCQkJe197IzF9fQkJCQkJCQkJCSUJeQoJCQl7XHBoYW50b217XHNpbX19CglcXAoJ
CVxzaW0KCVxcCgkJXElmVmFsdWVURnsjMn0KCQkJe157IzJ9fQoJCQl7XHBoYW50b217XHNpbX19
CglcZW5ke2FycmF5fQp9CgpcRGVjbGFyZURvY3VtZW50Q29tbWFuZCBcc2V0IHsgbSBnIH17IAkJ
CQklIFxzZXRze1h9e0N9CgkgXGxlZnRcbGJyYWNlCQkJCQkJCQkJJSB7WCB8IEN9CgkgCSMxIFxJ
ZlZhbHVlVCB7IzJ9IHsgXCB8IFwgICMyIH0KCSBccmlnaHRccmJyYWNlCn0KClxtYWtlYXRsZXR0
ZXIJCQkJCQkJCQkJJSBhZGRzIHZlcnRpY2FsIGxpbmVzIHRvIG1hdHJpY2VzClxyZW5ld2NvbW1h
bmQqXGVudkBtYXRyaXhbMV1bKlxjQE1heE1hdHJpeENvbHMgY117CiAgXGhza2lwIC1cYXJyYXlj
b2xzZXAKICBcbGV0XEBpZm5leHRjaGFyXG5ld0BpZm5leHRjaGFyCiAgXGFycmF5eyMxfX0KXG1h
a2VhdG90aGVyCgolJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJQolICAgICAgTG9naWMg
YW5kIHByb29mcyAgICAgICAgJQolJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJQoKJSBQ
cm9vZnMKXHVzZXBhY2thZ2V7YW1zdGhtfQkJCQkJCQkJJSBUaGVvcmVtIHBhY2thZ2UKXHRoZW9y
ZW1zdHlsZXtkZWZpbml0aW9ufQkJCQkJCSUgcGxhaW4sIGRlZmluaXRpb24sIHJlbWFyawolXHN3
YXBudW1iZXJzCQkJCQkJCQkJJSBJZiB5b3Ugd2FudCB0byBoYXZlIHRoZSBudW1iZXIgZmlyc3QK
CiUgTG9naWMgcGFja2FnZXMKXHVzZXBhY2thZ2V7bHBsZml0Y2h9CQkJCQkJJSBmaXRjaCBzdHls
ZSBwcm9vZnMKCiVcdXNlcGFja2FnZXtsb2dpY3Byb29mfQkJCQkJJSBhbHRlcm5hdGl2ZSBwYWNr
YWdlLCByZXNlbWJsaW5nIHRoZSBkQmVyTG9nIGJvb2sKJVxzZXRsZW5ndGhcc3VicHJvb2Zob3Jp
enNwYWNlezJlbX0JCQklIEluZGVudCBmb3Igc3VicHJvb2ZzLiBDaGFuZ2VkIGZvciBmcmVzaCB2
YXJpYWJsZXMKCgoKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKJSAgICAgIENvbG9y
IGFuZCBwcmVzZXRzICAgICAgICUKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKCiVc
dXNlcGFja2FnZXt4Y29sb3J9CQkJCQkJCSUgYmFzaWMgeGNvbG9yIHBhY2thZ2UKXHVzZXBhY2th
Z2VbdGFibGUseGNkcmF3XXt4Y29sb3J9CQkJCSUgeGNvbG9yIHBhY2thZ2Ugd2l0aCBzdXBwb3J0
IGZvciB0YWJsZXMKXGRlZmluZWNvbG9ye2xzdENvbW1lbnR9e3JnYn17MC40NSwwLjQ1LDAuNDV9
CSUgY29kZTogY29tbWVudHMgKEdyZXkpClxkZWZpbmVjb2xvcntsc3RLZXl9e3JnYn17MC4xMyww
LjIxLDF9CQkJJSBjb2RlOiBwcmltYXJ5IGtleXdvcmRzIChCbHVlKQpcZGVmaW5lY29sb3J7bHN0
S2V5Mn17cmdifXsxLDAuNjY2NjY3LDAuMTM3MjZ9ICAlIGNvZGU6IHNlY29uZGFyeSBrZXl3b3Jk
cyAoRGF5WzldIE9yYW5nZSkKXGRlZmluZWNvbG9ye2xzdFN0cmluZ317cmdifXswLjEsMC42NSww
LjF9CQklIGNvZGU6IHN0cmluZ3MgKEdyZWVuKQpcZGVmaW5lY29sb3J7bHN0QmFzZX17cmdifXsw
LjAsMC4wLDAuMH0JCQklIGNvZGU6IGJhc2UgKEJsYWNrKQoKCgolJSUlJSUlJSUlJSUlJSUlJSUl
JSUlJSUlJSUlJSUlJQolICAgICAgICAgICAgVGlreiAgICAgICAgICAgICAgJQolJSUlJSUlJSUl
JSUlJSUlJSUlJSUlJSUlJSUlJSUlJQoKXHVzZXBhY2thZ2V7dGlren0JCQkJCQkJCSUgaW1wb3J0
IGJhc2VwYWNrYWdlClx1c2V0aWt6bGlicmFyeXtjYWxjfQkJCQkJCQklIENvb3JkaW5hdGUgY2Fs
Y3VhdGlvbnMKXHVzZXRpa3psaWJyYXJ5e3Bvc2l0aW9uaW5nfSAgICAgICAgICAgICAgICAgICAg
JSBSZWxhdGl2ZSBwb3NpdGlvbmluZwpcdXNldGlremxpYnJhcnl7c2hhcGVzfSAgICAgICAgICAg
ICAgICAgICAgICAgICAlIERlZmluaW5nIG5vZGVzaGFwZXMgYW5kIG1vcmUgKGlzYSBmb3IgRS9S
KQoKJSBTaW1wbGUgdHJlZSBtYWNybyB3aXRoIGNvbXBhYmlsaXR5IHRvIHRpa3oKXHVzZXBhY2th
Z2V7dGlrei1xdHJlZX0JCQkJCQkJJSBpbXBvcnQgc2ltcGxlIHRyZWUgbWFjcm8KXHVzZXRpa3ps
aWJyYXJ5e2Fycm93c30gICAgICAgICAgICAgICAgICAgICAgICAgJSBhcnJvd3MgZm9yIHRyZWVz
CgolIFRpa3ogc2V0dGluZ3MgZm9yIHJlZC1ibGFjayB0cmVlcwpcdGlrenNldHsKICB0cmVlbm9k
ZS8uc3R5bGUgPSB7YWxpZ249Y2VudGVyLCBpbm5lciBzZXA9MHB0LCB0ZXh0IGNlbnRlcmVkLAog
ICAgZm9udD1cc2ZmYW1pbHl9LAogIGFybl9iLy5zdHlsZSA9IHt0cmVlbm9kZSwgY2lyY2xlLCB3
aGl0ZSwgZm9udD1cc2ZmYW1pbHlcYmZzZXJpZXMsIGRyYXc9YmxhY2ssCiAgICBmaWxsPWJsYWNr
LCB0ZXh0IHdpZHRoPTEuNWVtfSwgICAgICAgICAgICAgICUgYmxhY2sgbm9kZQogIGFybl9yLy5z
dHlsZSA9IHt0cmVlbm9kZSwgY2lyY2xlLCB3aGl0ZSwgZm9udD1cc2ZmYW1pbHlcYmZzZXJpZXMs
IGRyYXc9cmVkLAogICAgZmlsbD1yZWQsIHRleHQgd2lkdGg9MS41ZW19LCAgICAgICAgICAgICAg
JSByZWQgbm9kZQogIGFybl94Ly5zdHlsZSA9IHt0cmVlbm9kZSwgcmVjdGFuZ2xlLCBkcmF3PWJs
YWNrLCBmaWxsPWJsYWNrLAogICAgbWluaW11bSB3aWR0aD0wLjVlbSwgbWluaW11bSBoZWlnaHQ9
MC41ZW19ICAlIG5pbCBub2RlCn0KCiUgVGlreiBBdXRvbW90YSBmb3IgVHVyaW5nIE1hY2hpbmVz
Clx1c2V0aWt6bGlicmFyeXthdXRvbWF0YX0KCiUgVGlreiBFL1IgZGlhZ3JhbQpcdXNldGlremxp
YnJhcnl7ZXJ9CgolIEdyYXBoaWNzIGFuZCBwbG90cwpcdXNlcGFja2FnZXtncmFwaGljeH0JCQkJ
CQkJJSBpbXBvcnQgYmFzZXBhY2thZ2UgZm9yIGdyYXBocwpcdXNlcGFja2FnZXtwZ2ZwbG90c30J
CQkJCQkJJSBpbXBvcnQgcGdmcGxvdHMKXHVzZXBnZnBsb3RzbGlicmFyeXtmaWxsYmV0d2Vlbn0J
CQkJJSBhZGQgZmlsbEJldHdlZW4gY29tbWFuZApccGdmcGxvdHNzZXR7Y29tcGF0PTEuMTB9CQkJ
CQkJJSBjaG9vc2UgdmVyc2lvbiBvZiBwZ2ZwbG90cwoKJSBNYWNybyBmb3IgY2lyY2xlIHdpdGgg
c3ltYm9sIGluc2lkZS4KXG5ld2NvbW1hbmQqXGNpcmNsZWRbMV17IFx0aWt6W2Jhc2VsaW5lPShD
LmJhc2UpXVxub2RlW2RyYXcsY2lyY2xlLGlubmVyIHNlcD0wLjVwdF0oQykgeyMxfTtcIX0KCgoK
JSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKJSAgICAgICAgICAgIENvZGUgICAgICAg
ICAgICAgICUKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKXG5ld2NvbW1hbmR7XGNv
ZGV9WzFde3tcc2YgIzF9fQkJCQkJJSBcY29kZXtYfSB3cml0ZXMgWCBpbiBhIGNvZGUtYXBwcm9w
cmlhdGUgZm9udAoKCgoKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKJSAgICAgICAg
IGxzdGxpc3RpbmcgICAgICAgICAgICUKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUK
CiUgSW1wb3J0IGxzdGxpc3RpbmdzIC0gYmVhdXRpZnVsIHNvdXJjZWNvZGUhClx1c2VwYWNrYWdl
e2xpc3RpbmdzfQoKCiUgQ3VzdG9tIGxhbmd1YWdlIGRlZmluaXRpb25zCiUgRGVmaW5pdGlvbiBv
ZiBQc2V1ZG9jb2RlClxsc3RkZWZpbmVsYW5ndWFnZXtwc2V1ZG9jb2RlfXsKICBrZXl3b3Jkcz1b
MV17CiAgCSAgICAgYnJlYWssIGJyZWFrLCBieSwgZG8sIGRvd250bywgZWxzZSwgZXJyb3IsIGZv
ciwgaWYsIHJlcGVhdCwgcmV0dXJuLCB0bywgdW50aWwsIHdoaWxlLCB3aGlsZQogIAl9LAkJCQkJ
CQkJICAgIAkJJSBsaXN0IG9mIGtleXdvcmRzLCBmaXJzdCBhbmQgbGFzdCBhcmUgbm90IHVzZWQK
ICBrZXl3b3Jkcz1bMl17CiAgICAgICAgYW5kLCBhbmQsIG9yLCBOSUwsIE5JTAogIH0KICBzZW5z
aXRpdmU9ZmFsc2UsCQkJCQkJCQklIGtleXdvcmRzIGFyZSBub3QgY2FzZS1zZW5zaXRpdmUKICBt
b3JlY29tbWVudD1bbF17Ly99LAkJCQkJCQklIGwgaXMgZm9yIGxpbmUgY29tbWVudAogIG1vcmVj
b21tZW50PVtzXXsvKn17Ki99LAkJCQkJCSUgcyBpcyBmb3Igc3RhcnQgYW5kIGVuZCBkZWxpbWl0
ZXIKICBtb3Jlc3RyaW5nPVtiXSIJCQkJCQkJCSUgc3RyaW5ncyBhcmUgZW5jbG9zZWQgaW4gZG91
YmxlIHF1b3Rlcwp9CgoKJSBTZXR0aW5ncyBmb3IgbHN0bGlzdGluZ3MKXGxzdHNldHtsYW5ndWFn
ZT1wc2V1ZG9jb2RlLAkJCQkJJSBjaG9vc2UgbGFuZ3VhZ2UKICBjb2x1bW5zPWZsZXhpYmxlLAkJ
CQkJCQkJJSBsZXQgdGhlIGJveCBhbGlnbiB0byB0aGUgd2lkdGggb2YgdGhlIHBhZ2UKICAgIGxp
dGVyYXRlPXvDpn17e1xhZX19MXvDuH17e1xvfX0xe8OlfXt7XGFhfX0xCSUgYWxsb3cgw6YsIMO4
IGFuZCDDpSBpbiBjb2RlCiAgICAgICAgICAge8OGfXt7XEFFfX0xe8OYfXt7XE99fTF7w4V9e3tc
QUF9fTEsCSUgCSh0aGlzIGNoYW5nZSB3YXMgdGFrZW4gZnJvbSB0aGUgcHJlYW1ibGUgb2YgdGhl
IE1hdEZ5c1R1dG9yIExhVGVYIEd1aWRlKQogIGJyZWFrbGluZXM9dHJ1ZSwJCQkJCQkJCSUgYXV0
b21hdGljYWxseSBicmVhayBsaW5lcwogIGJyZWFrYXR3aGl0ZXNwYWNlPXRydWUsCQkJCQkJJSBh
dXRvbWF0aWNhbGx5IGJyZWFrIHNob3VsZCB0aGVyZSBvbmx5IGJlIHdoaXRlIHNwYWNlLgogIG51
bWJlcnM9bGVmdCwJCQkJCQkJCQklIG51bWJlcmluZzogbm9uZSwgbGVmdCwgcmlnaHQKICBudW1i
ZXJzZXA9NXB0LAkJCQkJCQkJJSBkaXN0YW5jZSBiZXR3ZWVuIGxpbmVudW1iZXJzIGFuZCBjb2Rl
CiAgbnVtYmVyc3R5bGU9XGNvbG9ye2xzdENvbW1lbnR9LAkJCQklIGNoYW5nZSBzdHlsZSBvZiBu
dW1iZXJpbmcgLSBjdXJyZW50bHkgZ3JleS4KICBzdGVwbnVtYmVyPTEsCQkJCQkJCQkJJSBzdGVw
IGJldHdlZW4gdG8gbGluZS1udW1iZXJzLiAxID0gZWFjaCBsaW5lIGlzIG51bWJlcmVkCiAgc2hv
d3NwYWNlcz1mYWxzZSwJCQkJCQkJCSUgc2hvdyBzcGFjZXMgZXZlcnl3aGVyZSAtIGFkZGluZyBw
YXJ0aWN1bGFyIHVuZGVyc2NvcmVzCiAgc2hvd3N0cmluZ3NwYWNlcz1mYWxzZSwJCQkJCQklIHVu
ZGVybGluZSBzcGFjZXMgd2l0aGluIHN0cmluZ3Mgb25seS4KICBzaG93dGFicz1mYWxzZSwJCQkJ
CQkJCSUgc2hvdyB0YWJzIHdpdGhpbiBzdHJpbmdzIGFkZGluZyBwYXJ0aWN1bGFyIHVuZGVyc2Nv
cmVzLgogIGVzY2FwZWluc2lkZT17KkB9e0AqfSwgICAgICAgICAgICAgICAgCQklIGlmIHlvdSB3
YW50IHRvIGFkZCBMYVRlWCB3aXRoaW4geW91ciBjb2RlCiAgYmFzaWNzdHlsZT1cdHRmYW1pbHkg
XGNvbG9ye2xzdEJhc2V9LAkJCSUgc2V0IGJhc2ljIGNvbG9yCiAgY29tbWVudHN0eWxlPVxjb2xv
cntsc3RDb21tZW50fSwJCQkJJSBzZXQgY29sb3Igb2YgY29tbWVudHMKICBrZXl3b3Jkc3R5bGU9
WzFdXGNvbG9ye2xzdEtleX0sCQkJCSUgc2V0IGNvbG9yIG9mIHByaW1hcnkga2V5d29yZHMKICBr
ZXl3b3Jkc3R5bGU9WzJdXGNvbG9ye2xzdEtleTJ9LAkJCQklIHNldCBjb2xvciBvZiBzZWNvbmRh
cnkga2V5d29yZHMKICBzdHJpbmdzdHlsZT1cY29sb3J7bHN0U3RyaW5nfSwJCQkJJSBzZXQgY29s
b3Igb2Ygc3RyaW5ncwp9CgolIGxzdGxpc3RpbmcgLSBQdXQgaXQgYmVhdXRpZnVsbHkgaW4gdGhl
IG1pZGRsZQpcbHN0c2V0e3hsZWZ0bWFyZ2luPSAuMVx0ZXh0d2lkdGggLCAgICAgCQkJCQkJCSUg
bGVmdG1hcmdpbiBiZWluZyAxMCUgb2YgdGhlIGN1cnJlbnQgd2lkdGgKICB4cmlnaHRtYXJnaW49
IC4xXHRleHR3aWR0aCwgICAgICAgICAgIAkJCQkJCQklIHJpZ2h0IG1hcmdpbiBhbHNvIDEwJQog
IGZyYW1lPWJvdHRvbWxpbmUgICAgICAgICAgICAgICAgICAgICAgCQkJCQkJCSUgRHJhdyBhIGxp
bmUgb24gdGhlIGJvdHRvbSBvZiB0aGUgc3Vycm91bmRpbmcgYm94Cn0KCiUgbHN0bGlzdGluZyBo
ZWFkZXIKXERlY2xhcmVDYXB0aW9uRm9udHt3aGl0ZX17XGNvbG9ye3doaXRlfX0gICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAlIGZvbnRzdHlsZSBvZiBjYXB0aW9uClxEZWNs
YXJlQ2FwdGlvbkZvcm1hdHtsaXN0aW5nfXtcY29sb3Jib3h7Z3JheX17XHBhcmJveHtcbGluZXdp
ZHRofXsjMSMyIzN9fX0gICAgJSBjcmVhdGUgbmljZSBncmV5IGJveGVzIGZvciBjYXB0aW9ucwpc
Y2FwdGlvbnNldHVwW2xzdGxpc3Rpbmdde2Zvcm1hdD1saXN0aW5nLGxhYmVsZm9udD13aGl0ZSx0
ZXh0Zm9udD13aGl0ZX0gICAgICAgICUgYXBwbHkgc2V0dGluZ3MgdG8gbGlzdGluZwoKCiUlJSUl
JSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJQolICAgICAgVGl0bGUgYW5kIGluZm9ybWF0
aW9uICAgICAgICUKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlClxzZXR2YWx1
ZXt0aXRsZSA9IH0KXHNldHZhbHVle3N1YnRpdGxlID0gfQoKXERlY2xhcmVEb2N1bWVudENvbW1h
bmQgXHNldHRpdGxlIHsgbSBnIH17IAkJCQklIFxzZXRUaXRsZXt0aXRsZX17c3VidGl0bGV9Cgkg
XHNldHZhbHVle3RpdGxlID0gIzF9CgkgXElmVmFsdWVURiB7IzJ9IHsgXHNldHZhbHVle3N1YnRp
dGxlID0gIzJ9IFx0aXRsZXtcaHVnZSBcZ2V0dmFsdWV7dGl0bGV9IFxcIFxsYXJnZSBcZ2V0dmFs
dWV7c3VidGl0bGV9fX0KCSAJCQkJIHsgXHRpdGxle1xodWdlIFxnZXR2YWx1ZXt0aXRsZX19IH0K
fQoKXERlY2xhcmVEb2N1bWVudENvbW1hbmQgXGFkZGF1dGggeyBtIGcgZyB9eyAJCQklIFxhZGRB
dXRoe25hbWV9e2VtYWlsfXtpZH0KICAgICBcSWZWYWx1ZVQgeyMzfSB7CQklU2V0IHRoZSBpZCB0
ZXh0IGFzIGRlc2lyZWQgb24gdGhlIHRvcCBsZWZ0CgkgCVxzZXR2YWx1ZXtpZCA9ICMzfQoJIH0K
ICAgICBccGdma2V5c2lmZGVmaW5lZHsvdmFyaWFibGVzL25hbWV9ewogICAgICAgICBcc2V0dmFs
dWV7aWQgPSBcLCBldCBhbH0KICAgICB9ewogICAgICAgICBcc2V0dmFsdWV7bmFtZSA9ICMxfQog
ICAgIH0JIAoJIFxhdXRob3J7IzF9CgkgXElmVmFsdWVUIHsjMn0gewoJICAgIFxwZ2ZrZXlzaWZk
ZWZpbmVkey92YXJpYWJsZXMvZW1haWx9ewoJICAgICAgICAlIERvIE5vdGhpbmcKCSAgICB9ewoJ
IAkgICAgXHNldHZhbHVle2VtYWlsID0gIzJ9CgkgCX0KCSAJXGFmZmlse1xwcm90ZWN0XGhyZWZ7
bWFpbHRvOiMyfXsjMn19CgkgfQp9Cgpcc2V0dGl0bGV7S2VlcCBDYWxtIGFuZCBcdGV4dGJhY2tz
bGFzaCBzZXR0aXRsZX0KClxkYXRle1x0b2RheX0KClxzZXR2YWx1ZXtvZiA9IG9mfQoKXGxoZWFk
e1xwcm90ZWN0XGhyZWZ7XGdldHZhbHVle2VtYWlsfX17XGdldHZhbHVle25hbWV9XGdldHZhbHVl
e2lkfX0gXFwgXGdldHZhbHVle3RpdGxlfX0KXGNoZWFke30KXHJoZWFke1x0aGVwYWdlXCBcZ2V0
dmFsdWV7b2Z9IFxwYWdlcmVme0xhc3RQYWdlfSBcXCBcbm91cHBlcmNhc2V7XGxlZnRtYXJrfX0K
CiVcbGZvb3R7fQolXGNmb290e30KJVxyZm9vdHt9Cg==
"""
preamble_en = """JSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKJSBTZXR0aW5ncyBmb3IgZG9jdW1l
bnQgKGVuZ2xpc2gpICUKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKCiUgSW5w
dXQgY29tbW9uIGRlZmluaXRpb24KXGlucHV0e3ByZWFtYmxlX2Jhc2UudGV4fQoKCiUlJSUlJSUl
JSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlCiUgICBFbmNvZGluZyBhbmQgaHlwaGVuYXRpb24gICAl
CiUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlCiUgQmFzaWNzOiBmb250LCBjb2RlYyBl
dGMuClx1c2VwYWNrYWdlW2VuZ2xpc2hde2JhYmVsfQkJCQkJCSUgYmFiZWwgaXMgZm9yIGh5cGhl
bmF0aW9uIGFuZCBvdGhlciBnb29kaWVzCgoKCiUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUl
JSUlCiUgICAgICAgICBsc3RsaXN0aW5nICAgICAgICAgICAlCiUlJSUlJSUlJSUlJSUlJSUlJSUl
JSUlJSUlJSUlJSUlClxyZW5ld2NvbW1hbmR7XGxzdGxpc3RpbmduYW1lfXtDb2RlfSAgICAgICAg
ICAgICAgJSBmb3Igb25lIGJsb2NrIG9mIGNvZGUgYWxvbmUKXHJlbmV3Y29tbWFuZHtcbHN0bGlz
dGxpc3RpbmduYW1lfXtMaXN0IG9mIGNvZGV9ICAlIGZvciBtb3JlIHBpZWNlcyBvZiBjb2RlIGlu
IG9uZQoKCgolJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJQolICAgICAgTG9naWMgYW5k
IHByb29mcyAgICAgICAgJQolJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJQolIFRoZW9y
ZW0gZW52aXJvbm1lbnRzClxuZXd0aGVvcmVte3RoZW9yZW19e1RoZW9yZW19W3NlY3Rpb25dClxu
ZXd0aGVvcmVte2xlbW1hfVt0aGVvcmVtXXtMZW1tYX0KXG5ld3RoZW9yZW17cHJvcG9zaXRpb259
W3RoZW9yZW1de1Byb3Bvc2l0aW9ufQpcbmV3dGhlb3JlbXtjb3JvbGxhcnl9W3RoZW9yZW1de0Nv
cm9sbGFyeX0KXG5ld3RoZW9yZW17ZGVmaW5pdGlvbn1bdGhlb3JlbV17RGVmaW5pdGlvbn0KXG5l
d3RoZW9yZW17Y29uamVjdHVyZX1bdGhlb3JlbV17Q29uamVjdHVyZX0KXHJlbmV3Y29tbWFuZCp7
XHByb29mbmFtZX17UHJvb2Z9CgoKCiUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlCiUg
ICAgICBFeGFtcGxlIGVudmlyb25tZW50ICAgICAlCiUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUl
JSUlJSUlClxuZXd0aGVvcmVte2V4YW1wbGV9W3RoZW9yZW1de0V4YW1wbGV9
"""
preamble_dk = """JSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJQolIFNldHRpbmdzIGZvciBkb2N1bWVu
dCAoZGFuaXNoKSAlCiUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKCiUgSW5wdXQg
Y29tbW9uIGRlZmluaXRpb24KXGlucHV0e3ByZWFtYmxlX2Jhc2UudGV4fQoKJSUlJSUlJSUlJSUl
JSUlJSUlJSUlJSUlJSUlJSUlJSUKJSAgIEVuY29kaW5nIGFuZCBoeXBoZW5hdGlvbiAgICUKJSUl
JSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKJSBCYXNpY3M6IGZvbnQsIGNvZGVjIGV0Yy4K
XHVzZXBhY2thZ2VbZGFuaXNoXXtiYWJlbH0JCQkJCQklIGJhYmVsIGlzIGZvciBoeXBoZW5hdGlv
biBhbmQgb3RoZXIgZ29vZGllcwpccmVuZXdjb21tYW5ke1xkYW5pc2hoeXBoZW5taW5zfXsyMn0J
CQklIGV2ZW4gYmV0dGVyIGRhbmlzaCBoeXBoZW5hdGlvbiEKCiUgLmJpYiBkYW5pc2ggcmVkZWZp
bml0aW9uIGZvciBhdXRob3IgaW4gdGl0bGUKXHJlbmV3Y29tbWFuZFxBdXRoYW5keyBvZyB9Clxy
ZW5ld2NvbW1hbmRcQXV0aGFuZHN7LCBvZyB9ClxyZW5ld2NvbW1hbmRcQWZmaWxmb250e1xzbWFs
bH0KCgoKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKJSAgICAgICAgIGxzdGxpc3Rp
bmcgICAgICAgICAgICUKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKCiUgbHN0bGlz
dGluZyBsYW5ndWFnZSByZWRlZmluaXRpb25zClxyZW5ld2NvbW1hbmR7XGxzdGxpc3RpbmduYW1l
fXtLb2RlfSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJSBmb3Ig
b25lIGJsb2NrIG9mIGNvZGUgYWxvbmUKXHJlbmV3Y29tbWFuZHtcbHN0bGlzdGxpc3RpbmduYW1l
fXtMaXN0ZSBhZiBcbHN0bGlzdGluZ25hbWUgcn0gICAgICAgICAgICAgICAgICAlIGZvciBtb3Jl
IHBpZWNlcyBvZiBjb2RlIGluIG9uZQoKCgolJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUl
JQolICAgICAgTG9naWMgYW5kIHByb29mcyAgICAgICAgJQolJSUlJSUlJSUlJSUlJSUlJSUlJSUl
JSUlJSUlJSUlJQolIFRoZW9yZW0gZW52aXJvbm1lbnRzClxuZXd0aGVvcmVte3RoZW9yZW19e1PD
pnRuaW5nfVtzZWN0aW9uXQpcbmV3dGhlb3JlbXtsZW1tYX1bdGhlb3JlbV17TGVtbWF9ClxuZXd0
aGVvcmVte3Byb3Bvc2l0aW9ufVt0aGVvcmVtXXtQcm9wb3NpdGlvbn0KXG5ld3RoZW9yZW17Y29y
b2xsYXJ5fVt0aGVvcmVtXXtLb3JvbGxhcn0KXG5ld3RoZW9yZW17ZGVmaW5pdGlvbn1bdGhlb3Jl
bV17RGVmaW5pdGlvbn0KXG5ld3RoZW9yZW17Y29uamVjdHVyZX1bdGhlb3JlbV17Rm9ybW9kbmlu
Z30KXHJlbmV3Y29tbWFuZCp7XHByb29mbmFtZX17QmV2aXN9CgoKJSUlJSUlJSUlJSUlJSUlJSUl
JSUlJSUlJSUlJSUlJSUKJSAgICAgIEV4YW1wbGUgZW52aXJvbm1lbnQgICAgICUKJSUlJSUlJSUl
JSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKXG5ld3RoZW9yZW17ZXhhbXBsZX1bdGhlb3JlbV17RWtz
ZW1wZWx9CgoKCiUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlCiUgICAgICAgVGl0bGUg
YW5kIGxheW91dCAgICAgICAlCiUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlClxzZXR2
YWx1ZXtvZiA9IGFmfQo=
"""

    
parser = argparse.ArgumentParser(description='Make a LaTeX project from Steffan\'s awesome template')
parser.add_argument('path', type=str, nargs='+', help='the path to build the project')
parser.add_argument('-l', type=str, nargs=1, help='the language of the preamble, "en" or "dk"', default=["en"])
parser.add_argument('--zip', dest='zip', action='store_const', const=True, default=False, help='zip the resulting project')
#TODO: Add -c option to clean folders first / after
args = parser.parse_args()

preamble_locale = 'preamble_dk' if args.l[0] == 'dk' else 'preamble_en'
preamble_l_content = preamble_dk if args.l[0] == 'dk' else preamble_en
preamble_l_content = base64.decodestring( preamble_l_content )
preamble_base_content = base64.decodestring( preamble_base )
template_content = base64.decodestring( template )

#TODO: make this specifiable in the prepare.py
######## MODIFICATIONS ########

template_content = template_content.replace( '\subimport{../preamble/}{preamble_en.tex}',
'\subimport{preamble/}{' + preamble_locale + '.tex}')

###############################

PATH = " ".join(args.path)
if not os.path.exists(PATH):
    os.makedirs(PATH)
os.chdir(PATH)
if not os.path.exists('preamble'):
    os.mkdir('preamble')
with open(os.path.join('preamble', preamble_locale + '.tex'), 'w') as preamble_l_file:
    preamble_l_file.write(preamble_l_content)

with open(os.path.join('preamble', 'preamble_base.tex'), 'w') as preamble_base_file:
    preamble_base_file.write(preamble_base_content)

with open('template.tex', 'w') as template_file:
    template_file.write(template_content)

if args.zip:
    fname = os.getcwd() #includes the filepath, sice we cd'ed to it
    import zipfile
    zipf = zipfile.ZipFile(fname + '.zip', 'w', zipfile.ZIP_DEFLATED)
    zipf.write(os.path.join('preamble', preamble_locale + '.tex'))
    zipf.write(os.path.join('preamble', 'preamble_base.tex'))
    zipf.write('template.tex')
    zipf.close()
raw_input('Success, Press enter to exit')