# PCL

aka: Pete's Configuration Language


PCL takes inspiriation from a few other config langs but does it in a way that is actually nice to write. It takes some notes from JSON, YAML, env, and others.

I wanted to create a config format that was typed and didnt need extra characters like quotes and crap.

## Types
PCL uses a few basic types:
* `str` -> string
* `num` -> number (float or int)
* `bool` -> boolean (true/false, yes/no, 1/0)
* `list` -> unordered list
* `dict` -> a set of key:value pairs
* `none` -> don't try and cast type, leave it as-is; useful for things like hex values and whatever

## Syntax

The baisc format of an entry is `<keyname> <type> = <value>`.

Some basic rules:
* Keys cannot have spaces in them
* Keys must have a type; if you want to ignore typing use the `none` type
* Lists and Dicts can be nested

A basic config file might look something like this:

```
foo str = my value
bar num = 145.2
ok bool = true
my_stuff list = [
    hello
    69
]
dude dict = {
    where str = is my car
}
```

