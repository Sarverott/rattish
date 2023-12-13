# Rattish language manuals
simple and easy language used for input macros creation and payloads writing.

```                                                                               

                                              %, .,,&       &#@
        █▀█ ▄▀█ ▀█▀ ▀█▀ █ █▀ █░█               %,,,,,*&   ((##/
        █▀▄ █▀█ ░█░ ░█░ █ ▄█ █▀█               ,,,,,**&/#((#(#/%%
       ~ small, simple and fast ~               &%%(*&&&(-X-(((((&&(&/#&&# .*
                                             &#%%%%%%%%%%%&##&%((#(#((#((#&,,,,
                                           %%%%%%%%%%((%%&##(((#(/#(#(#@#%&&&
                                     &&%%%%%%%%%%%%%%((((%%##&(#&%%&/&#%&&#*
        &&&,,.&&@                   &#%%%%%%#(((((##%%&#%%%((%#%&    *
                (,,&                &#%%%%%(((((###(##&#%%&&
                 &* ,.            &#%%%((((((((((((#%&&&
                 &*,,@           &%%%%#(((((((%####&(###&
                 #*(,           .%%%%%%#%((((%*****@****,
               &**,&            %%%%%%%%%#(#&/*******&**&
             &***,%           &%%%%%%&%%%#(#&/******,&**,%,&%
          .#***#&           &%&#%%%%%%&%(%%#&**,,,&,,&/&&******,,,#
        &** **&            /%%%%%%%%%%%%%&&&&&&&(**,,,&*&      &*(,&
      &** #*&             &%%%%%%%%%%%%%%%//****//&**,,/*&    &(&&&&
    *** **&               &%%%%%%%%%%#(##&******,*(&*,%***&    .&*/
   @*# *(/               &%(#%%%%%%%%%#(((&&*************,,
   &****&               #(%%%%%%%%%%%%%%#((&************,,&
  %(***&               %%%%%%%%%%%%%%%%%##(#%********,*,,*&          EVERY RAT
   &(*##&             &%%%%%%%%%%%%%%%%%(((#**********,**&           EVEN WITHOUT
   *&(((**&&        &%%%%%%%%%%%%%%#%%%%#((&***********#&            EVER LEAVING
     &&(((((#((((((%&##%%%%%%%%%%%%%%%%%#((&*********/&              STORM SEWERS
        ,&&&#/((((/%&%#%%%%%%%%%%%%%%%%##(##///////%&*,,,,&@,/&&&    DREAMS ABOUT
           ,,,,,,,,,,,,,,,,,&&%#%%%%%%%&(&//#&&#,,,,,,,,,,,          SKY AND CLOUDS
                         ,,,,,,,,,,,,,,,&%(**,,,#&&                  AT LEAST ONCE
                                            ,,&(,,,&,&,@
                                                 ,, ,

```

---

### IDEA OF PROJECT
Project is created for macro codes in standard office software, microcontroller-based project's payloads and standalone scripting. First idea was based on small and fast program for Seeeduino Xiao with microsd to sd card adapter directly attached to SPI pins. After proof-of-work construction and programming was finished successfully, many new ideas appears.

---

### BASIC ASSUMPTIONS


- every line contains one command with one argument.
- commands are single ASCII characters in the range from 0x21 to 0x2F or from 0x3A to 0x40 or from 0x5B to 0x5F or from 0x7B to 0x7E, that starts line.
- argument for every command starts after first char and ends before EOL.
- if line starts with other char, like for example space, letter or cipher it is commentary.

---

### COMMANDS

###### BASIC namespace
> input, output, events, breakers and pauses

- [wait time pause in miliseconds / seconds / minutes / hours](./command-list/0x22.md) [` " `]
- [print static output / print output from variable](./command-list/0x3c.md) [` < `]
- [read input to file / to variable](./command-list/0x3e.md) [` > `]
- [release key(s)](./command-list/0x5e.md) [` ^ `]
- [press key(s)](./command-list/0x5f.md) [` _ `]

###### VARIABLES namespace
> basic variable operations

- [point context on variable](./command-list/0x24.md) [` $ `]
- [modulo of context variable / string length](./command-list/0x25.md) [` % `]
- [multiply context variable / get char at](./command-list/0x2a.md) [` * `]
- [add to context variable / string append](./command-list/0x2b.md) [` + `]
- [sub from context variable / find and remove](./command-list/0x2d.md) [` - `]
- [divide context variable / insert at](./command-list/0x3a.md) [` : `]
- [set context variable](./command-list/0x3d.md) [` = `]
- [move variable context to left](./command-list/0x5b.md) [` [ `]
- [move variable context to right](./command-list/0x5d.md) [` ] `]
- [copy value from variable to context variable](./command-list/0x7b.md) [` { `]
- [copy value from context variable to variable](./command-list/0x7d.md) [` } `]

###### LOGICS namespace
> logic operations

- [set 1 to context variable if context variable is not 0 and variable is not 0, else 0](./command-list/0x26.md) [` & `]
- [set 1 to context variable if context variable is lesser than variable, else 0](./command-list/0x2f.md) [` / `]
- [set 1 to context variable if context variable is not 0 or variable is not 0, else 0](./command-list/0x3b.md) [` ; `]
- [set 1 to context variable if context variable is greater than variable, else 0](./command-list/0x5c.md) [` \ `]
- [set 1 to context variable if context variable is equal to variable, else 0](./command-list/0x7c.md) [` | `]
- [if context variable is 0 set 1, else 0](./command-list/0x7e.md) [` ~ `]

###### PROCEDURES namespace
> procedures and conditional execution

- [unconditional jumper, if label not exists stops current iteration](./command-list/0x21.md) [` ! `]
- [label for code jumping](./command-list/0x2e.md) [` . `]
- [conditional jumper, based on if context variable is not 0 jump](./command-list/0x3f.md) [` ? `]

###### MECHANICS namespace
> enviroment behavior and system operators

- [setup enviroment and global switches / point-of-view changing](./command-list/0x23.md) [` # `]
- [import code from file](./command-list/0x40.md) [` @ `]



---

### INTERPRETERS

<<<INTERPRETERSLIST>>>

---

### PROJECTS

<<<PROJECTSCONNECTED>>>

---

### LICENSE

Published on terms of [GPL-3.0](./LICENSE) by Sett Sarverott
