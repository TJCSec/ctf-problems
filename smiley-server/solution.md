# Smiley Server Writeup
## Finding the exploit

The hint says to look for bad practice. Looking through the code, there are
several things that shouldn't be done. For example, there are missing
break statements in the worker
[switch](https://github.com/TJCSec/ctf-problems/blob/master/smiley-server/src/worker.c#L118).
That particular bad practice was actually a mistake, but it wouldn't have mattered anyway:
the credential code was read in from `access.txt`, which implies that the only user to be
able to always have access was user 0. You can assume that the problem was not designed
for you to guess randomly at user passwords, so that vantage point is not available. The
next instance is the usage of `sprintf` instead of `snprintf`. Unluckily, in the only
place that `sprintf`
[appears](https://github.com/TJCSec/ctf-problems/blob/master/smiley-server/src/worker.c#L100),
it cannot possibly overflow the buffer.

There might be other bad things that I have missed, but all those would also be red herrings.
The intended bad practice was the usage of struct packing directly from memory. This is
something that cannot be controlled because the compiler will automatically add extra padding
in between struct fields. For this problem, this effect was forced, but it could happen 
accidentally other times, which was the primary purpose of the problem.

We can find out if this actually is a vulnerability by opening gdb. We need to find places
where the struct fields are accessed. By looking at the struct definition, we can find out that
the only vulnerable field might be the `credentials` field. All the rest of them only need to
be aligned to 4 byte boundaries because the files are compiled for x86. 
In adminserver, `credentials` is accessed right at the top of `run()`.

    0x08048e01 <+20>:   fldz
    0x08048e03 <+22>:   fstpl   -0x118(%ebp)
    ...
    0x08048e13 <+38>:   lea     -0x11c(%ebp),%eax

This shows us that the struct is 4 bytes after the start of the struct. The lea instruction
is loading the query struct to `readQuery` and the fstpl instruction is storing `0.0` as the
initial value for the `credentials` field.

Finding the worker fields is a little bit more difficult. We can find the credential offset
at the beginning of the `checkCredentials` function. 

    0x08048929 <+3>:  mov   0x8(%ebp),%eax
    0x0804892c <+6>:  fldl  0x8(%eax)

This loads argument 1, the address of the query, into `eax`. Then it floads the float at
`argument 1 + 8`, which means that credentials is 8 bytes after the beginning of the struct.

That is the vulnerability! In the `worker` binary, the `credentials` field is 4 bytes later than
in the `adminserver` binary.

## Using the exploit

We can draw a map of the struct being dumped from the server into the worker. Each row below
is 4 bytes long

    ADMINSERVER                 WORKER
    -----------                 ------
    access                      access
    credentials low             PADDING
    credentials high            credentials low
    userid                      credentials high
    buf                         userid
    ...                         buf
                                ...

Thus, whatever is in the userid field gets written directly into high word of credentials. 
This problem is not noticeable because userid is initially -1, which means that credentials
will be automatically NAN and not return true for any comparison. However, we can set credentials
to something extremely high, because we have access to the floating point exponent, and that 
gives us the necessary credentials to run the restricted commands.

Once you get access, you can try to run commands, but stdout is not visible to the user. This is
a side effect of having the worker process popened. One thing we can try to do is to `read` the
flag, but I disabled that functionality. One solution is to open a port on your local server
and then connect to that port with netcat. However, the easier way is to just

    exec cat flag* 1>&2

Where we are catting the flag and piping stdout to stderr. Alternatively, we could copy the 
flag over to tmp with another name and just read it from there.

## Full Exploit

    >> login 0x7fefffff blah
    >> exec cat flag* 1>&2

