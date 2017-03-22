About
=====

This appendix is an introduction to the Command Line. I am working through
it as a refresher to make sure there are no gaps in my knowledge.

Command Notes
-------------
pwd         print working directory
hostname    my computer's network name
mkdir       make directory
cd          change directory
ls          list directory
rmdir       remove directory
pushd       push directory
popd        pop directory
cp          copy a file or directory
mv          move a file or directory
less        page through a file
cat         print the whole file
xargs       execute arguments
find        find files
grep        find things inside files
man         read a manual page
apropos     find what man page is appropriate
env         look at your environment
echo        print some arguments
export      export/set an environment variable
exit        exit the shell
sudo        ** DANGER ** become super user root, aka. Run the command with superuser permission
rm          removes a file, -f for forcibly, -r for recursively, -i for information
chmod       changes the file mode bits (aka. the file permission)
chown       changes the owner of the file
xargs       breaks a long list of arguments into smaller portion.
                Useful when piping the results of one command into another
                eg. > find /path -type f -print | xargs rm