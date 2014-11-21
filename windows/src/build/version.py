
import os
import sys
import subprocess
import datetime

def main(version, outfile_h, outfile_wxi, designation):
    officialbuild = False
    nightlybuild = False
    devbuild = False
    desc = ''
    
    if 'JOEWIN_OFFICIAL' in os.environ:
    	officialbuild = True
    elif 'JOEWIN_NIGHTLY' in os.environ:
    	nightlybuild = True
    else:
    	devbuild = True
    
    vparts = version.split('.')
    while len(vparts) < 4:
        vparts.append('0')
    
    #svnrev = getsvnrev()
    svnrev = '999' # TODO: What to do for Mercurial?
    if svnrev:
    	svnrevstr = "svn rev %s, " % svnrev
    else:
    	svnrevstr = ""
    	svnrev = ''
    
    if officialbuild:
        if vparts[-1] == '0': vparts[-1] = getdatebld()
        buildname = designation
        if buildname == '':
            buildname = 'Final'
        desc = version + ' ' + buildname
        shortdesc = desc
    elif nightlybuild:
        if vparts[-1] == '0': vparts[-1] = cleansvnrev(svnrev)
        desc = version + ' Nightly build (%s%s)' % (svnrevstr, datetime.datetime.now().strftime('%d %b %Y'))
        shortdesc = version + '-nightly-%s' % svnrev
    else:
        if vparts[-1] == '0': vparts[-1] = cleansvnrev(svnrev)
        desc = version + ' Developer build (%s%s)' % (svnrevstr, datetime.datetime.now().strftime('%d %b %Y'))
        shortdesc = version + '-dev-%s' % svnrev
    
    year = datetime.datetime.now().year
    
    writefile(outfile_h, """
#ifndef __JWVERSION_H__
#define __JWVERSION_H__

#define JW_VERSION_MAJ """ + vparts[0] + """
#define JW_VERSION_MIN """ + vparts[1] + """
#define JW_VERSION_REV """ + vparts[2] + """
#define JW_VERSION_BLD """ + vparts[3] + """

#define JW_VERSION_STR """ + "\"" + '.'.join(vparts) + """\"
#define JW_VERSION_DESC """ + "\"" + desc + """\"
#define JW_COPYRIGHT \"""" + ("Copyright \\xa9 2010-%d John J. Jordan, and others (see About...)" % (year)) + """\"

#define JW_SHORTVERSION \"""" + version + """\"

#define JW_VERSION_BANNER \"""" + ("** Joe's Own Editor for Windows v%s ** Copyright \xc2\xa9 %d **" % (shortdesc, year)) + """\"

#endif // __JWVERSION_H__
""")
    
    writefile(outfile_wxi, """<?xml version="1.0" encoding="utf-8"?>
<Include>
  <?define JoeWinVersion = \"""" + '.'.join(vparts) + """\" ?>
  <?define JoeWinDescVersion = \"""" + shortdesc + """\" ?>
</Include>
""")
    
    return True

def writefile(fname, content):
    if os.path.exists(fname):
        inf = open(fname, 'r')
        txt = inf.read()
        inf.close()
        if txt == content:
            return
    
    outf = open(fname, 'w')
    outf.write(content)
    outf.close()

def getsvnrev():
    dir = os.path.dirname(sys.argv[0])
    if dir: os.chdir(dir)
    os.chdir("..\..")
    try:
        proc = subprocess.Popen(['svnversion', '-nc'], stdout=subprocess.PIPE)
    except:
        if 'JOEWIN_SVNREV' in os.environ:
            return os.environ['JOEWIN_SVNREV'].strip()
        return None

    output, errput = proc.communicate()
    proc.wait()
    
    revs = output.strip()
    if ':' in revs:
        revs = revs.split(':')[-1]
    
    return revs.strip()

def cleansvnrev(svnrev):
    if svnrev is None: return '0'
    return svnrev.strip('MPS')

def getdatebld():
    now = datetime.datetime.now()
    
    yearpart = (now.year % 10) // 2
    monthpart = now.month
    if now.year % 2 == 1:
    	monthpart += 12
    
    return str((yearpart * 10000) + (monthpart * 100) + now.day)

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("Syntax: %s (version) (version.h) (version.wxi) (designation)" % sys.argv[0])
    else:
        sys.exit(0 if main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]) else 1)