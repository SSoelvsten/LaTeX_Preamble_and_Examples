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
e2lmdGhlbn0JCQkJCQkJCSUgQ29uZGl0aW9uYWxzClx1c2VwYWNrYWdle2NhbGN9CQkJCQkJCQkl
IENhbGN1bGF0aW9ucwoKCgolJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJQolICAgICAg
ICAgIEh5cGVybWVkaWEgICAgICAgICAgJQolJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUl
JQoKXHVzZXBhY2thZ2V7dXJsLCBoeXBlcnJlZn0JCQkJCQkJJSBcdXJse2xpbmt9IGFuZCBcaHJl
ZntsaW5rfXtyZXBsYWNpbmcgdGV4dH0KCiVNYWNyb3MgdGFrZW4gZnJvbSB0aGUgcHJlYW1ibGUg
b2YgdGhlIE1hdEZ5c1R1dG9yIExhVGVYIEd1aWRlLgpcbmV3Y29tbWFuZCp7XGh0dHB9WzFde1xo
cmVme2h0dHA6Ly8jMX17IzF9fQkJJSBtYWNybyBmb3IgaHR0cCBsaW5rczogXGh0dHB7d3d3Lm1h
dGZ5c3R1dG9yLmRrfQpcbmV3Y29tbWFuZCp7XG1haWx0b31bMV17XGhyZWZ7bWFpbHRvOiMxfXsj
MX19CQklIG1hY3JvIGZvciBtYWlsczogXG1haWx0b3tlbWFpbEBlbWFpbC5jb219CgolJSUlJSUl
JSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJQolICAgICAgICAgU3R5bGl6YXRpb24gICAgICAgICAg
JQolJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJQoKJSBIZWFkZXJzIG9nIGZvb3RlcnMK
XHVzZXBhY2thZ2V7bGFzdHBhZ2V9ICAgICAgICAgICAgICAgICAgICAgICAgICAgJSBcbGFzdHBh
Z2UgY29tbWFuZCBmb3IgbnVtYmVycyBvZiBwYWdlcwpcdXNlcGFja2FnZXtmYW5jeWhkcn0gICAg
ICAgICAgICAgICAgICAgICAgICAgICAlIGNyZWF0ZSBjb29sIGhlYWRlcnMgYW5kIGZvb3RlcnMK
XHBhZ2VzdHlsZXtmYW5jeX0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJSB3aG8gZG9l
c24ndCB3YW50IHRoZWlyIHBhZ2UgdG8gYmUgZmFuY3k/CgolIFVzZSBvZiBjb2x1bW5zClx1c2Vw
YWNrYWdle211bHRpY29sfQoKJSBRdW90YXRpb25zCiUgImRhbmlzaCIgb3IgImJyaXRpc2giClx1
c2VwYWNrYWdlW2RhbmlzaD1ndWlsbGVtZXRzXXtjc3F1b3Rlc30gICAgCSUgdHdvIHN0eWxlczog
InF1b3RlcyIgb3IgPj5ndWlsbGVtZXRzPDwKJVxNYWtlQXV0b1F1b3Rle8K7fXvCq30gICAgICAg
ICAgICAgICAgICAgICAgIAklIGRlY29tbWVudCBmb3IgZWFzeSBtYWNybwolXE1ha2VBdXRvUXVv
dGUqe+KAun174oC5fSAgICAgICAgICAgICAgICAgICAgICAJJSBkZWNvbW1lbnQgZm9yIGV2ZW4g
ZWFzaWVyIG1hY3JvcwoKJSBMaWtlIGEgcGFyYWdyYXBoLCBidXQgYWRkcyBhbHNvIGEgbGluZWJy
ZWFrIGFmdGVyLiAoQWxzbyBpcyBub3QgcmVjb3JkZWQgb24gbGFiZWxsaW5nKQpcbmV3Y29tbWFu
ZHtcbGJwYXJhZ3JhcGh9WzFde1x2c3BhY2V7MC4zZW19IFxub2luZGVudCBcdGV4dGJmeyMxfVxc
IFxub2luZGVudH0KCiUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlCiUgICAgICAgICAg
ICAgTWF0aCAgICAgICAgICAgICAlCiUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlCiVc
bmV3Y29tbWFuZHtcaG1tYXh9ezB9CQkJCQkJCQklIG1pbmltaXplcyB0aGUgYW1vdW50IG9mIGJv
bGQgZmFtaWxpZXMKJVxuZXdjb21tYW5ke1xibW1heH17MX0JCQkJCQkJCSUgdGhpcyBhbGxvd3Mg
Zm9yIG1vcmUgbWF0aCBmYW1pbGllcwoKJSB2YXJpb3VzIGJhc2ljIHN0dWZmClx1c2VwYWNrYWdl
e2JtLCBtYXRodG9vbHMsIGFtc21hdGh9CgolIFZhcmlvdXMgc3ltYm9sIHBhY2thZ2VzClx1c2Vw
YWNrYWdle2Ftc3N5bWJ9CiVcdXNlcGFja2FnZVt1dG9waWFde21hdGhkZXNpZ259CQkJCQklIGZ1
bGwgb3ZlcndyaXRlIG9mIHRoZSBmb250IHN5c3RlbQpcdXNlcGFja2FnZXtzdG1hcnlyZH0JCQkJ
CQkJCSUgZXZlbiBtb3JlIHN5bWJvbHMKCiVcbGV0XG1hdGhjYWxcdW5kZWZpbmVkCQkJCQkJCQkl
IExldCdzIHJlZGVmaW5lIHRoZSBtYXRoY2FsIGFscGhhYmV0CiVcRGVjbGFyZU1hdGhBbHBoYWJl
dHtcbWF0aGNhbH17T01TfXtjbXN5fXttfXtufQoKJSBNYXRoIHNob3J0Y3V0cwpccmVuZXdjb21t
YW5ke1xkfXtcLCBcbWF0aHJte2R9fSAgICAgICAgICAgICAgICAgICAgJSBcZCA9IGRpZmZlcmVu
dGlhbCBkIHdpdGggYSBiaXQgb2Ygc3BhY2luZwpcbmV3Y29tbWFuZHtcZX17XG1hdGhybXtlfX0g
ICAgICAgICAgICAgICAgICAgICAgICAgJSBcZSA9IGV1bGVycyBudW1iZXIKXG5ld2NvbW1hbmR7
XFJ9e1xtYXRoYmJ7Un19ICAgICAgICAgICAgICAgICAgICAgICAgICUgXFIgPSBSZWFsIG51bWJl
cnMKXG5ld2NvbW1hbmR7XE59e1xtYXRoYmJ7Tn19ICAgICAgICAgICAgICAgICAgICAgICAgICUg
XE4gPSBOYXR1cmFsIG51bWJlcnMKXG5ld2NvbW1hbmR7XEN9e1xtYXRoYmJ7Q319ICAgICAgICAg
ICAgICAgICAgICAgICAgICUgXEMgPSBDb21wbGV4IG51bWJlcnMKXG5ld2NvbW1hbmR7XFF9e1xt
YXRoYmJ7UX19ICAgICAgICAgICAgICAgICAgICAgICAgICUgXFEgPSBSYXRpb25hbCBudW1iZXJz
ClxuZXdjb21tYW5ke1xGfXtcbWF0aGJie0Z9fQkJCQkJCQklIFxGCgpcbmV3Y29tbWFuZHtcYWJz
fVsxXXtcbGVmdFxsdmVydCAjMSBccmlnaHRccnZlcnR9CQklIFxhYnN7YXJnfQkJYWJzb2x1dGUv
bW9kdWxvIG9mIHZhbHVlClxuZXdjb21tYW5ke1xub3JtfVsxXXtcbGVmdFxsVmVydCAjMSBccmln
aHRcclZlcnR9CQklIFxub3Jte2FyZ30Jbm9ybSBvZiBhIHZhbHVlClxuZXdjb21tYW5ke1xjZWls
fVsxXXtcbGVmdFxsY2VpbCAjMSBccmlnaHRccmNlaWx9CQklIFxjZWlse2FyZ30JY2VpbGluZyBv
ZiBhIHZhbHVlClxuZXdjb21tYW5ke1xmbG9vcn1bMV17XGxlZnRcbGZsb29yICMxIFxyaWdodFxy
Zmxvb3J9CSUgXGZsb29ye2FyZ30JZmxvb3Igb2YgYSB2YWx1ZQoKXG5ld2NvdW50ZXJ7aX0KClxE
ZWNsYXJlRG9jdW1lbnRDb21tYW5kIFxzZXEgeyBnIGcgZyBnIH0gewkJCSUgXHNlcXt4fXtpfXtq
fXtzfQoJXHNldGNvdW50ZXJ7aX17MH0JCQkJCQkJCSUgeF9pLCB4X2krcywgLi4uIHhfagoJXElm
VmFsdWVUIHsjMn0geyBcYWRkdG9jb3VudGVye2l9eyMyfSB9CglcSWZWYWx1ZVRGIHsjMX0KCQl7
IzF9CgkJe3h9CglfeyBcYXJhYmlje2l9IH0sCglcSWZWYWx1ZVRGIHsjNH0gCgkJe1xhZGR0b2Nv
dW50ZXJ7aX17IzR9fQoJCXtcYWRkdG9jb3VudGVye2l9ezF9fQoJXElmVmFsdWVURiB7IzF9IAoJ
CXsjMX0KCQl7eH0gCglfeyBcYXJhYmlje2l9IH0sCglcZG90cwoJXElmVmFsdWVURiB7IzN9CgkJ
eyAsICMxX3sjM30gfQoJCXt9Cn0KClxEZWNsYXJlRG9jdW1lbnRDb21tYW5kIFxlcm8geyBnIGcg
fSB7CQkJCSUgXGVybyB7eCwgeX0KCVxiZWdpbnthcnJheX17Y30JCQkJCQkJCSUJeAoJCVxJZlZh
bHVlVEZ7IzF9CQkJCQkJCQklCX4KCQkJe197IzF9fQkJCQkJCQkJCSUJeQoJCQl7XHBoYW50b217
XHNpbX19CglcXAoJCVxzaW0KCVxcCgkJXElmVmFsdWVURnsjMn0KCQkJe157IzJ9fQoJCQl7XHBo
YW50b217XHNpbX19CglcZW5ke2FycmF5fQp9CgpcRGVjbGFyZURvY3VtZW50Q29tbWFuZCBcc2V0
IHsgbSBnIH17IAkJCQklIFxzZXRze1h9e0N9CgkgXGxlZnRcbGJyYWNlCQkJCQkJCQkJJSB7WCB8
IEN9CgkgCSMxIFxJZlZhbHVlVCB7IzJ9IHsgXCB8IFwgICMyIH0KCSBccmlnaHRccmJyYWNlCn0K
ClxtYWtlYXRsZXR0ZXIJCQkJCQkJCQkJJSBhZGRzIHZlcnRpY2FsIGxpbmVzIHRvIG1hdHJpY2Vz
ClxyZW5ld2NvbW1hbmQqXGVudkBtYXRyaXhbMV1bKlxjQE1heE1hdHJpeENvbHMgY117CiAgXGhz
a2lwIC1cYXJyYXljb2xzZXAKICBcbGV0XEBpZm5leHRjaGFyXG5ld0BpZm5leHRjaGFyCiAgXGFy
cmF5eyMxfX0KXG1ha2VhdG90aGVyCgolJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJQol
ICAgICAgTG9naWMgYW5kIHByb29mcyAgICAgICAgJQolJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUl
JSUlJSUlJQoKJSBQcm9vZnMKXHVzZXBhY2thZ2V7YW1zdGhtfQkJCQkJCQkJJSBUaGVvcmVtIHBh
Y2thZ2UKXHRoZW9yZW1zdHlsZXtkZWZpbml0aW9ufQkJCQkJCSUgcGxhaW4sIGRlZmluaXRpb24s
IHJlbWFyawolXHN3YXBudW1iZXJzCQkJCQkJCQkJJSBJZiB5b3Ugd2FudCB0byBoYXZlIHRoZSBu
dW1iZXIgZmlyc3QKCiUgTG9naWMgcGFja2FnZXMKXHVzZXBhY2thZ2V7bHBsZml0Y2h9CQkJCQkJ
JSBmaXRjaCBzdHlsZSBwcm9vZnMKCiVcdXNlcGFja2FnZXtsb2dpY3Byb29mfQkJCQkJJSBhbHRl
cm5hdGl2ZSBwYWNrYWdlLCByZXNlbWJsaW5nIHRoZSBkQmVyTG9nIGJvb2sKJVxzZXRsZW5ndGhc
c3VicHJvb2Zob3JpenNwYWNlezJlbX0JCQklIEluZGVudCBmb3Igc3VicHJvb2ZzLiBDaGFuZ2Vk
IGZvciBmcmVzaCB2YXJpYWJsZXMKCgoKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUK
JSAgICAgIENvbG9yIGFuZCBwcmVzZXRzICAgICAgICUKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUl
JSUlJSUlJSUKCiVcdXNlcGFja2FnZXt4Y29sb3J9CQkJCQkJCSUgYmFzaWMgeGNvbG9yIHBhY2th
Z2UKXHVzZXBhY2thZ2VbdGFibGUseGNkcmF3XXt4Y29sb3J9CQkJCSUgeGNvbG9yIHBhY2thZ2Ug
d2l0aCBzdXBwb3J0IGZvciB0YWJsZXMKXGRlZmluZWNvbG9ye2xzdENvbW1lbnR9e3JnYn17MC40
NSwwLjQ1LDAuNDV9CSUgY29kZTogY29tbWVudHMgKEdyZXkpClxkZWZpbmVjb2xvcntsc3RLZXl9
e3JnYn17MC4xMywwLjIxLDF9CQkJJSBjb2RlOiBwcmltYXJ5IGtleXdvcmRzIChCbHVlKQpcZGVm
aW5lY29sb3J7bHN0S2V5Mn17cmdifXsxLDAuNjY2NjY3LDAuMTM3MjZ9ICAlIGNvZGU6IHNlY29u
ZGFyeSBrZXl3b3JkcyAoRGF5WzldIE9yYW5nZSkKXGRlZmluZWNvbG9ye2xzdFN0cmluZ317cmdi
fXswLjEsMC42NSwwLjF9CQklIGNvZGU6IHN0cmluZ3MgKEdyZWVuKQpcZGVmaW5lY29sb3J7bHN0
QmFzZX17cmdifXswLjAsMC4wLDAuMH0JCQklIGNvZGU6IGJhc2UgKEJsYWNrKQoKCgolJSUlJSUl
JSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJQolICAgICAgICAgICAgVGlreiAgICAgICAgICAgICAg
JQolJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJQoKXHVzZXBhY2thZ2V7dGlren0JCQkJ
CQkJCSUgaW1wb3J0IGJhc2VwYWNrYWdlClx1c2V0aWt6bGlicmFyeXtjYWxjfQkJCQkJCQklIENv
b3JkaW5hdGUgY2FsY3VhdGlvbnMKXHVzZXRpa3psaWJyYXJ5e3Bvc2l0aW9uaW5nfSAgICAgICAg
ICAgICAgICAgICAgJSBSZWxhdGl2ZSBwb3NpdGlvbmluZwpcdXNldGlremxpYnJhcnl7c2hhcGVz
fSAgICAgICAgICAgICAgICAgICAgICAgICAlIERlZmluaW5nIG5vZGVzaGFwZXMgYW5kIG1vcmUg
KGlzYSBmb3IgRS9SKQoKJSBTaW1wbGUgdHJlZSBtYWNybyB3aXRoIGNvbXBhYmlsaXR5IHRvIHRp
a3oKXHVzZXBhY2thZ2V7dGlrei1xdHJlZX0JCQkJCQkJJSBpbXBvcnQgc2ltcGxlIHRyZWUgbWFj
cm8KXHVzZXRpa3psaWJyYXJ5e2Fycm93c30gICAgICAgICAgICAgICAgICAgICAgICAgJSBhcnJv
d3MgZm9yIHRyZWVzCgolIFRpa3ogc2V0dGluZ3MgZm9yIHJlZC1ibGFjayB0cmVlcwpcdGlrenNl
dHsKICB0cmVlbm9kZS8uc3R5bGUgPSB7YWxpZ249Y2VudGVyLCBpbm5lciBzZXA9MHB0LCB0ZXh0
IGNlbnRlcmVkLAogICAgZm9udD1cc2ZmYW1pbHl9LAogIGFybl9iLy5zdHlsZSA9IHt0cmVlbm9k
ZSwgY2lyY2xlLCB3aGl0ZSwgZm9udD1cc2ZmYW1pbHlcYmZzZXJpZXMsIGRyYXc9YmxhY2ssCiAg
ICBmaWxsPWJsYWNrLCB0ZXh0IHdpZHRoPTEuNWVtfSwgICAgICAgICAgICAgICUgYmxhY2sgbm9k
ZQogIGFybl9yLy5zdHlsZSA9IHt0cmVlbm9kZSwgY2lyY2xlLCB3aGl0ZSwgZm9udD1cc2ZmYW1p
bHlcYmZzZXJpZXMsIGRyYXc9cmVkLAogICAgZmlsbD1yZWQsIHRleHQgd2lkdGg9MS41ZW19LCAg
ICAgICAgICAgICAgJSByZWQgbm9kZQogIGFybl94Ly5zdHlsZSA9IHt0cmVlbm9kZSwgcmVjdGFu
Z2xlLCBkcmF3PWJsYWNrLCBmaWxsPWJsYWNrLAogICAgbWluaW11bSB3aWR0aD0wLjVlbSwgbWlu
aW11bSBoZWlnaHQ9MC41ZW19ICAlIG5pbCBub2RlCn0KCiUgVGlreiBBdXRvbW90YSBmb3IgVHVy
aW5nIE1hY2hpbmVzClx1c2V0aWt6bGlicmFyeXthdXRvbWF0YX0KCiUgVGlreiBFL1IgZGlhZ3Jh
bQpcdXNldGlremxpYnJhcnl7ZXJ9CgolIEdyYXBoaWNzIGFuZCBwbG90cwpcdXNlcGFja2FnZXtn
cmFwaGljeH0JCQkJCQkJJSBpbXBvcnQgYmFzZXBhY2thZ2UgZm9yIGdyYXBocwpcdXNlcGFja2Fn
ZXtwZ2ZwbG90c30JCQkJCQkJJSBpbXBvcnQgcGdmcGxvdHMKXHVzZXBnZnBsb3RzbGlicmFyeXtm
aWxsYmV0d2Vlbn0JCQkJJSBhZGQgZmlsbEJldHdlZW4gY29tbWFuZApccGdmcGxvdHNzZXR7Y29t
cGF0PTEuMTB9CQkJCQkJJSBjaG9vc2UgdmVyc2lvbiBvZiBwZ2ZwbG90cwoKJSBNYWNybyBmb3Ig
Y2lyY2xlIHdpdGggc3ltYm9sIGluc2lkZS4KXG5ld2NvbW1hbmQqXGNpcmNsZWRbMV17IFx0aWt6
W2Jhc2VsaW5lPShDLmJhc2UpXVxub2RlW2RyYXcsY2lyY2xlLGlubmVyIHNlcD0wLjVwdF0oQykg
eyMxfTtcIX0KCgoKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKJSAgICAgICAgICAg
IENvZGUgICAgICAgICAgICAgICUKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKXG5l
d2NvbW1hbmR7XGNvZGV9WzFde3tcc2YgIzF9fQkJCQkJJSBcY29kZXtYfSB3cml0ZXMgWCBpbiBh
IGNvZGUtYXBwcm9wcmlhdGUgZm9udAoKCgoKJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUl
JSUKJSAgICAgICAgIGxzdGxpc3RpbmcgICAgICAgICAgICUKJSUlJSUlJSUlJSUlJSUlJSUlJSUl
JSUlJSUlJSUlJSUKCiUgSW1wb3J0IGxzdGxpc3RpbmdzIC0gYmVhdXRpZnVsIHNvdXJjZWNvZGUh
Clx1c2VwYWNrYWdle2xpc3RpbmdzfQoKCiUgQ3VzdG9tIGxhbmd1YWdlIGRlZmluaXRpb25zCiUg
RGVmaW5pdGlvbiBvZiBQc2V1ZG9jb2RlClxsc3RkZWZpbmVsYW5ndWFnZXtwc2V1ZG9jb2RlfXsK
ICBrZXl3b3Jkcz1bMV17CiAgCSAgICAgYnksIGJ5LCBkb3dudG8sIGVsc2UsIGVycm9yLCBmb3Is
IGlmLCByZXBlYXQsIHJldHVybiwgdG8sIHVudGlsLCB3aGlsZSwgd2hpbGUKICAJfSwJCQkJCQkJ
CSAgICAJCSUgbGlzdCBvZiBrZXl3b3JkcywgZmlyc3QgYW5kIGxhc3QgYXJlIG5vdCB1c2VkCiAg
a2V5d29yZHM9WzJdewogICAgICAgIGFuZCwgYW5kLCBvciwgTklMLCBOSUwKICB9CiAgc2Vuc2l0
aXZlPWZhbHNlLAkJCQkJCQkJJSBrZXl3b3JkcyBhcmUgbm90IGNhc2Utc2Vuc2l0aXZlCiAgbW9y
ZWNvbW1lbnQ9W2xdey8vfSwJCQkJCQkJJSBsIGlzIGZvciBsaW5lIGNvbW1lbnQKICBtb3JlY29t
bWVudD1bc117Lyp9eyovfSwJCQkJCQklIHMgaXMgZm9yIHN0YXJ0IGFuZCBlbmQgZGVsaW1pdGVy
CiAgbW9yZXN0cmluZz1bYl0iCQkJCQkJCQklIHN0cmluZ3MgYXJlIGVuY2xvc2VkIGluIGRvdWJs
ZSBxdW90ZXMKfQoKCiUgU2V0dGluZ3MgZm9yIGxzdGxpc3RpbmdzClxsc3RzZXR7bGFuZ3VhZ2U9
cHNldWRvY29kZSwJCQkJCSUgY2hvb3NlIGxhbmd1YWdlCiAgY29sdW1ucz1mbGV4aWJsZSwJCQkJ
CQkJCSUgbGV0IHRoZSBib3ggYWxpZ24gdG8gdGhlIHdpZHRoIG9mIHRoZSBwYWdlCiAgICBsaXRl
cmF0ZT17w6Z9e3tcYWV9fTF7w7h9e3tcb319MXvDpX17e1xhYX19MQklIGFsbG93IMOmLCDDuCBh
bmQgw6UgaW4gY29kZQogICAgICAgICAgIHvDhn17e1xBRX19MXvDmH17e1xPfX0xe8OFfXt7XEFB
fX0xLAklIAkodGhpcyBjaGFuZ2Ugd2FzIHRha2VuIGZyb20gdGhlIHByZWFtYmxlIG9mIHRoZSBN
YXRGeXNUdXRvciBMYVRlWCBHdWlkZSkKICBicmVha2xpbmVzPXRydWUsCQkJCQkJCQklIGF1dG9t
YXRpY2FsbHkgYnJlYWsgbGluZXMKICBicmVha2F0d2hpdGVzcGFjZT10cnVlLAkJCQkJCSUgYXV0
b21hdGljYWxseSBicmVhayBzaG91bGQgdGhlcmUgb25seSBiZSB3aGl0ZSBzcGFjZS4KICBudW1i
ZXJzPWxlZnQsCQkJCQkJCQkJJSBudW1iZXJpbmc6IG5vbmUsIGxlZnQsIHJpZ2h0CiAgbnVtYmVy
c2VwPTVwdCwJCQkJCQkJCSUgZGlzdGFuY2UgYmV0d2VlbiBsaW5lbnVtYmVycyBhbmQgY29kZQog
IG51bWJlcnN0eWxlPVxjb2xvcntsc3RDb21tZW50fSwJCQkJJSBjaGFuZ2Ugc3R5bGUgb2YgbnVt
YmVyaW5nIC0gY3VycmVudGx5IGdyZXkuCiAgc3RlcG51bWJlcj0xLAkJCQkJCQkJCSUgc3RlcCBi
ZXR3ZWVuIHRvIGxpbmUtbnVtYmVycy4gMSA9IGVhY2ggbGluZSBpcyBudW1iZXJlZAogIHNob3dz
cGFjZXM9ZmFsc2UsCQkJCQkJCQklIHNob3cgc3BhY2VzIGV2ZXJ5d2hlcmUgLSBhZGRpbmcgcGFy
dGljdWxhciB1bmRlcnNjb3JlcwogIHNob3dzdHJpbmdzcGFjZXM9ZmFsc2UsCQkJCQkJJSB1bmRl
cmxpbmUgc3BhY2VzIHdpdGhpbiBzdHJpbmdzIG9ubHkuCiAgc2hvd3RhYnM9ZmFsc2UsCQkJCQkJ
CQklIHNob3cgdGFicyB3aXRoaW4gc3RyaW5ncyBhZGRpbmcgcGFydGljdWxhciB1bmRlcnNjb3Jl
cy4KICBlc2NhcGVpbnNpZGU9eypAfXtAKn0sICAgICAgICAgICAgICAgIAkJJSBpZiB5b3Ugd2Fu
dCB0byBhZGQgTGFUZVggd2l0aGluIHlvdXIgY29kZQogIGJhc2ljc3R5bGU9XHR0ZmFtaWx5IFxj
b2xvcntsc3RCYXNlfSwJCQklIHNldCBiYXNpYyBjb2xvcgogIGNvbW1lbnRzdHlsZT1cY29sb3J7
bHN0Q29tbWVudH0sCQkJCSUgc2V0IGNvbG9yIG9mIGNvbW1lbnRzCiAga2V5d29yZHN0eWxlPVsx
XVxjb2xvcntsc3RLZXl9LAkJCQklIHNldCBjb2xvciBvZiBwcmltYXJ5IGtleXdvcmRzCiAga2V5
d29yZHN0eWxlPVsyXVxjb2xvcntsc3RLZXkyfSwJCQkJJSBzZXQgY29sb3Igb2Ygc2Vjb25kYXJ5
IGtleXdvcmRzCiAgc3RyaW5nc3R5bGU9XGNvbG9ye2xzdFN0cmluZ30sCQkJCSUgc2V0IGNvbG9y
IG9mIHN0cmluZ3MKfQoKJSBsc3RsaXN0aW5nIC0gUHV0IGl0IGJlYXV0aWZ1bGx5IGluIHRoZSBt
aWRkbGUKXGxzdHNldHt4bGVmdG1hcmdpbj0gLjFcdGV4dHdpZHRoICwgICAgIAkJCQkJCQklIGxl
ZnRtYXJnaW4gYmVpbmcgMTAlIG9mIHRoZSBjdXJyZW50IHdpZHRoCiAgeHJpZ2h0bWFyZ2luPSAu
MVx0ZXh0d2lkdGgsICAgICAgICAgICAJCQkJCQkJJSByaWdodCBtYXJnaW4gYWxzbyAxMCUKICBm
cmFtZT1ib3R0b21saW5lICAgICAgICAgICAgICAgICAgICAgIAkJCQkJCQklIERyYXcgYSBsaW5l
IG9uIHRoZSBib3R0b20gb2YgdGhlIHN1cnJvdW5kaW5nIGJveAp9CgolIGxzdGxpc3RpbmcgaGVh
ZGVyClxEZWNsYXJlQ2FwdGlvbkZvbnR7d2hpdGV9e1xjb2xvcnt3aGl0ZX19ICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgJSBmb250c3R5bGUgb2YgY2FwdGlvbgpcRGVjbGFy
ZUNhcHRpb25Gb3JtYXR7bGlzdGluZ317XGNvbG9yYm94e2dyYXl9e1xwYXJib3h7XGxpbmV3aWR0
aH17IzEjMiMzfX19ICAgICUgY3JlYXRlIG5pY2UgZ3JleSBib3hlcyBmb3IgY2FwdGlvbnMKXGNh
cHRpb25zZXR1cFtsc3RsaXN0aW5nXXtmb3JtYXQ9bGlzdGluZyxsYWJlbGZvbnQ9d2hpdGUsdGV4
dGZvbnQ9d2hpdGV9ICAgICAgICAlIGFwcGx5IHNldHRpbmdzIHRvIGxpc3RpbmcKCgolJSUlJSUl
JSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKJSAgICAgIFRpdGxlIGFuZCBpbmZvcm1hdGlv
biAgICAgICAlCiUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJQpcc2V0dmFsdWV7
dGl0bGUgPSB9ClxzZXR2YWx1ZXtzdWJ0aXRsZSA9IH0KClxEZWNsYXJlRG9jdW1lbnRDb21tYW5k
IFxzZXR0aXRsZSB7IG0gZyB9eyAJCQkJJSBcc2V0VGl0bGV7dGl0bGV9e3N1YnRpdGxlfQoJIFxz
ZXR2YWx1ZXt0aXRsZSA9ICMxfQoJIFxJZlZhbHVlVEYgeyMyfSB7IFxzZXR2YWx1ZXtzdWJ0aXRs
ZSA9ICMyfSBcdGl0bGV7XGh1Z2UgXGdldHZhbHVle3RpdGxlfSBcXCBcbGFyZ2UgXGdldHZhbHVl
e3N1YnRpdGxlfX19CgkgCQkJCSB7IFx0aXRsZXtcaHVnZSBcZ2V0dmFsdWV7dGl0bGV9fSB9Cn0K
ClxzZXR2YWx1ZXtuYW1lID0gfQpcc2V0dmFsdWV7ZW1haWwgPSB9ClxzZXR2YWx1ZXtpZCA9IH0K
ClxEZWNsYXJlRG9jdW1lbnRDb21tYW5kIFxhZGRhdXRoIHsgbSBnIGcgfXsgCQkJJSBcYWRkQXV0
aHtuYW1lfXtlbWFpbH17aWR9CgkgXHNldHZhbHVle25hbWUgPSAjMX0KCSBcYXV0aG9yeyMxfQoJ
IFxJZlZhbHVlVCB7IzJ9IHsKCSAJXHNldHZhbHVle2VtYWlsID0gIzJ9CgkgCVxhZmZpbHtccHJv
dGVjdFxocmVme21haWx0bzojMn17IzJ9fQoJIH0KCSBcSWZWYWx1ZVQgeyMzfSB7CgkgCVxzZXR2
YWx1ZXtpZCA9ICMzfQoJIH0KfQoKXHNldHRpdGxle0tlZXAgQ2FsbSBhbmQgXHRleHRiYWNrc2xh
c2ggc2V0dGl0bGV9CgpcZGF0ZXtcdG9kYXl9Cgpcc2V0dmFsdWV7b2YgPSBvZn0KClxsaGVhZHtc
cHJvdGVjdFxocmVme1xnZXR2YWx1ZXtlbWFpbH19e1xnZXR2YWx1ZXtuYW1lfVxnZXR2YWx1ZXtp
ZH19IFxcIFxnZXR2YWx1ZXt0aXRsZX19ClxjaGVhZHt9ClxyaGVhZHtcdGhlcGFnZVwgXGdldHZh
bHVle29mfSBccGFnZXJlZntMYXN0UGFnZX0gXFwgXG5vdXBwZXJjYXNle1xsZWZ0bWFya319Cgol
XGxmb290e30KJVxjZm9vdHt9CiVccmZvb3R7fQo=
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
ZXd0aGVvcmVte2xlbW1hfXtMZW1tYX1bc2VjdGlvbl0KXG5ld3RoZW9yZW17cHJvcG9zaXRpb259
e1Byb3Bvc2l0aW9ufVtzZWN0aW9uXQpcbmV3dGhlb3JlbXtjb3JvbGxhcnl9e0Nvcm9sbGFyeX1b
c2VjdGlvbl0KXG5ld3RoZW9yZW17ZGVmaW5pdGlvbn17RGVmaW5pdGlvbn1bc2VjdGlvbl0KXG5l
d3RoZW9yZW17Y29uamVjdHVyZX17Q29uamVjdHVyZX1bc2VjdGlvbl0KXHJlbmV3Y29tbWFuZCp7
XHByb29mbmFtZX17UHJvb2Z9CgoKCiUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlCiUg
ICAgICBFeGFtcGxlIGVudmlyb25tZW50ICAgICAlCiUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUl
JSUlJSUlClxuZXd0aGVvcmVte2V4YW1wbGV9e0V4YW1wbGV9W3NlY3Rpb25d
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
pnRuaW5nfVtzZWN0aW9uXQpcbmV3dGhlb3JlbXtsZW1tYX17TGVtbWF9W3NlY3Rpb25dClxuZXd0
aGVvcmVte3Byb3Bvc2l0aW9ufXtQcm9wb3NpdGlvbn1bc2VjdGlvbl0KXG5ld3RoZW9yZW17Y29y
b2xsYXJ5fXtLb3JvbGxhcn1bc2VjdGlvbl0KXG5ld3RoZW9yZW17ZGVmaW5pdGlvbn17RGVmaW5p
dGlvbn1bc2VjdGlvbl0KXG5ld3RoZW9yZW17Y29uamVjdHVyZX17Rm9ybW9kbmluZ31bc2VjdGlv
bl0KXHJlbmV3Y29tbWFuZCp7XHByb29mbmFtZX17QmV2aXN9CgoKJSUlJSUlJSUlJSUlJSUlJSUl
JSUlJSUlJSUlJSUlJSUKJSAgICAgIEV4YW1wbGUgZW52aXJvbm1lbnQgICAgICUKJSUlJSUlJSUl
JSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUKXG5ld3RoZW9yZW17ZXhhbXBsZX17RWtzZW1wZWx9W3Nl
Y3Rpb25dCgoKCiUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlCiUgICAgICAgVGl0bGUg
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
