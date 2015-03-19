# Joe's Own Editor

[Editing Tasks](https://sourceforge.net/p/joe-editor/mercurial/ci/default/tree/docs/tasks.md) 

[Release Notes](https://sourceforge.net/p/joe-editor/mercurial/ci/default/tree/NEWS.md)

[List of Commands](https://sourceforge.net/p/joe-editor/mercurial/ci/default/tree/docs/list.md)

[List of Options](https://sourceforge.net/p/joe-editor/mercurial/ci/default/tree/docs/options.md)

[Hacking](https://sourceforge.net/p/joe-editor/mercurial/ci/default/tree/docs/hacking.md)

[Man page](https://sourceforge.net/p/joe-editor/mercurial/ci/default/tree/docs/man.md)

[Project page](http://www.sourceforge.net/projects/joe-editor)

[Download source](http://prdownloads.sourceforge.net/joe-editor/joe-3.7.tar.gz?download)

[History](https://sourceforge.net/p/joe-editor/mercurial/ci/default/tree/docs/history.md)

<p></p>

<p>JOE is a full featured terminal-based screen editor which is distributed
under the GNU General Public License (GPL).  JOE has been around since 1988
and comes standard with many Linux distributions.</p>

<p>JOE is being maintained by its original author Joseph Allen, plus all of
the people who send bug reports, feature suggestions and patches to the
project web site.  JOE is hosted by SourceForge.net and its source code is
controlled under CVS.  Over the last few years there has been about one
major new release a year, usually in the April-May timeframe.</p>

<p>JOE is a blending of MicroPro's venerable microcomputer word processor
WordStar and Richard Stallman's famous LISP based text editor GNU-EMACS (but
it does not use code from either program): most of the basic editing keys
are the same as in WordStar as is the overall feel of the editor.  JOE also
has some of the key bindings and many of the powerful features of EMACS.</p>

<p>JOE is written in C and its only dependency is libc.  This makes JOE very
easy to build (just "configure" and "make install"), making it feasible to
include on small systems and recovery disks.  The compiled binary is about
300K in x86.  Note that JOE can use either the termcap or terminfo terminal
capabilities databases (or a built-in termcap entry for ANSI terminals).  The
choice is controlled by a "configure" option.  If terminfo is used, a
library is required to access the database (on some systems this library is
ncurses, but JOE does not use curses to control the terminal- it has its own
code for this).</p>

<p>Much of the look and feel of JOE is determined by its simple
configuration file "joerc".  Several variants of the editor are installed by
default in addition to "joe": "jmacs" (emulate GNU-EMACS), "jstar" emulate
WordStar, "jpico" emulate the Pine mailer editor PICO and "rjoe"- a
restricted version of JOE which allows the used to only edit the file given
on the command line.  JOE is linked to several names.  The name which is
used to invoke the editor with "rc" tacked on the end gives the name of
configuration file to use.  It is thus easy for you to make your own variant
if you want.  Also you can customize the editor by copying the system
"joerc" file to your home directory.</p>

<p>Here is a basic screen shot of JOE running in a Cygwin console:</p>
<img src="capture.gif" alt="screen capture">

<p>Here is a screen shot showing several windows- the first has some example
double-wide characters, the second is the same buffer as the first, but in
hex-dump view mode, the third is a shell window and the fourth shows a
selected rectangular block of numbers and their sum:</p>

<img src="https://sourceforge.net/p/joe-editor/mercurial/ci/default/tree/htdocs/elaborate.gif" alt="elaborate screen capture">

<p>JOE has the following features:</p>

<ul>

<li>Multi-file search and replace- file list is either given on command line
or by a UNIX command (grep/find) run from within JOE.</li>

<li>Mouse support, including wheel (works best when using xterm).  The mouse
can resize windows, scroll windows, select and paste text, and select menu
entries.</li>

<li>Context display on status line: allows you to see name of function
cursor is in.</li>

<li>UTF-8 support, optional auto-detect of UTF-8 files.</li>

<li>Syntax highlighting for more than 40 languages.</li>

<li>Hexadecimal edit mode.  Use JOE as a disk editor: joe -overwrite -hex
/dev/hda1,0,512 (edit first sector of /dev/hda1).</li>

<li>Non-destructive editing of binary files even when handling MS-DOS or
UNIX line endings.</li>

<li>Swap file allows editing files larger than memory.</li>

<li>Context sensitive on-line help.</li>

<li>Bash-like TAB completion and history for all prompts, or jump into the
completion menu and use it to traverse the file system.</li>

<li>Complete word in edit buffer by hitting ESC Enter�(uses other words in
buffer for dictionary).</li>

<li>EMACS-compatible file locks and file modification checking.</li>

<li>Shell windows.</li>

<li>Multiple-windows onto same or different files.</li>

<li>Compile and step through errors or Grep and step through finds.</li>

<li>Goto matching character delimiter \( \[ \{ \< which skips comments and
quoted matter.</li>

<li>Goto matching word delimiter, including XML tags and C preprocessor
directives.</li>

<li>Ctrl-arrow key block selection.</li>

<li>Search and replace system, including regular expression and optional
incremental search.  Regular expression key for matching balanced C
expressions.</li>

<li>Tags file search (tab completion at tags search prompt uses tags file as
database).</li>

<li>Spell check commands which invoke aspell or ispell.  Language for aspell
can be passed through editor.</li>

<li>Paragraph format which preserves news/mail quoting indentation
characters.</li>

<li>Unlimited Undo and Redo.</li>

<li>Yank buffer allows stepping through and insertion of previously deleted
text.</li>

<li>State file restores history buffers, yank buffer and last file cursor
positions.</li>

<li>Cursor position history allows you to step through previously visited areas
of a file.</li>

<li>Multiple interactive keyboard macros.  Macros can be assigned to key
sequences in joerc file.</li>

<li>Block move/copy/delete/filter.</li>

<li>Rectangle (columnar) block mode- search and replace can be narrowed to
the rectangular block.  Rectangular blocks can be filtered through UNIX
commands.</li>

<li>Overtype/Insert modes.</li>

<li>Indent/Unindent (shift block left or right).</li>

<li>Auto-indent mode.</li>

<li>Picture mode for ASCII graphics.</li>

<li>Line number mode displays line number of each line.</li>

<li>Powerful scientific calculator with block statistics functions
(sum/standard-deviation/count highlighted block of numbers).</li>

<li>Termcap/Terminfo support allows JOE to use any terminal or terminal
emulator.</li>

<li>Can accept data from a pipe, for example: ls \| joe</li>
</ul>
