.. _about:


**OPBOT** is a solid, non hackable, back after reboot, intended to be
programmable in a static, only code, no popen, no imports and no reading
modules from a directory bot, it's  source is :ref:`here <source>`.

**OPBOT** is programmable, to program opbot you have to have the code
available as employing your own code requires that you install your own bot as
the system bot. This is to not have a directory to read modules from to add
commands to the bot but include the own programmed modules directly into the
python code, so only trusted code (your own written code) is included and
runnable. Reading random code from a directory is what gets avoided.

**OPBOT** stores it's data on disk where objects are time versioned and the
last version saved on disk is served to the user layer. Files are JSON dumps
that are read-only so thus should provide (disk) persistence more chance.
Paths carry the type in the path name what makes reconstruction from filename
easier then reading type from the object.

**only include your own written code should be the path to "secure".**
