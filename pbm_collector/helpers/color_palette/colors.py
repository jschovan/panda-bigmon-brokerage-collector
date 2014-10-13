import re
from datetime import datetime
# PIL ... Python Image Library
from PIL import Image

lower_limit_Npixels_with_color=500
WHITE=(255,255,255)

CLOUDS=[ "CERN", "CA", "DE", "ES", "FR", "IT", "ND", "NL", "TW", "UK", "US" ]

images=[ 'cloud_%s.png' % x for x in CLOUDS ]

OUTPUT_HTML='color_test_draft.html'
OUTPUT_PY='color_test_draft.py'


fo=open(OUTPUT_HTML, 'w')
fop=open(OUTPUT_PY, 'a')

fo.write("""<html>
<head></head>
<body>
<table width=100\%>

""")

fop.write("### appended on %s\n" % datetime.utcnow() )


for cloud in CLOUDS:
    f='cloud_%s.png' % cloud
    fo.write("""<tr><td>%s</td>""" % cloud )
    
    # open image
    im = Image.open(f)
    # get color palette
    colors=im.getcolors(im.size[0]*im.size[1])
    # restrict only to frequently used colors
    reduced_colors=[x for x in colors if x[0]>lower_limit_Npixels_with_color   and   x[1]!= WHITE ]
    rcolors=list(set([x[1] for x in reduced_colors]))
    print f, u'#colors:', len( im.getcolors(im.size[0]*im.size[1]) ), len(reduced_colors)
    print f, reduced_colors, rcolors
    # convert integers 0..255 to hex to get color codes
    rcolors_hex=[ '%0.2X%0.2X%0.2X' % ( x[0], x[1], x[2] ) for x in rcolors ]
    rcolors_hex.sort()
    print f, rcolors_hex
    for cl in rcolors_hex:
        fo.write("<td style=\"background-color:#%s\">%s</td>" % (cl, cl) )
    fo.write("</tr>\n")
    fop.write("%s=%s\n" % (cloud, rcolors_hex) )

fo.write("""

</table>
</body>
</html>
""")

fop.write("\n\n\n")

fo.close()
fop.close()


