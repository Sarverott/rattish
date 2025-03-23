# Rattish language manuals
simple and easy language used for input macros creation and payloads writing.

```ascii-text-art 
BEGIN ascii-text-art                                                                               

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
END ascii-text-art 
```

---

### IDEA OF PROJECT, MAIN TARGET AND POSSIBILITIES

Project is created for macro codes in standard office software, microcontroller-based project's payloads and standalone scripting. First idea was based on small and fast program for Seeeduino Xiao with microsd to sd card adapter directly attached to SPI pins. After proof-of-work construction and programming was finished successfully, many new ideas appears.

---

### BASIC ASSUMPTIONS


 - every line contains one command char with one string argument. for example in `<input` that `<` is command and `input` is argument of this command
 - commands are single ASCII characters in the range from 0x21 to 0x2F or from 0x3A to 0x40 or from 0x5B to 0x5F or from 0x7B to 0x7E, that starts line.
 - argument for every command starts after first char and ends before EOL.
 - if line starts with other char, like for example space, letter or cipher it is commentary.

---

### COMMANDS

##### BASIC namespace
> input, output, events, breakers and pauses

- [wait time pause in miliseconds / seconds / minutes / hours](./command-list/0x22.md) [` " `]
- [print static output / print output from variable](./command-list/0x3c.md) [` < `]
- [read input to file / to variable](./command-list/0x3e.md) [` > `]
- [release key(s)](./command-list/0x5e.md) [` ^ `]
- [press key(s)](./command-list/0x5f.md) [` _ `]

##### VARIABLES namespace
> basic variable operations

- [point context on variable](./command-list/0x24.md) [` $ `]
- [modulo of context variable / string length](./command-list/0x25.md) [` % `]
- [multiply context variable / get char at](./command-list/0x2a.md) [` * `]
- [add to context variable / string append](./command-list/0x2b.md) [` + `]
- [sub from context variable / find and remove](./command-list/0x2d.md) [` - `]
- [divide context variable / insert at](./command-list/0x3a.md) [` : `]
- [set context variable](./command-list/0x3d.md) [` = `]
- [move variable context pointer to left](./command-list/0x5b.md) [` [ `]
- [move variable context pointer to right](./command-list/0x5d.md) [` ] `]
- [copy value from variable to context variable](./command-list/0x7b.md) [` { `]
- [copy value from context variable to variable](./command-list/0x7d.md) [` } `]

##### LOGICS namespace
> logic operations

- [set 1 to context variable if context variable is not 0 and variable is not 0, else 0](./command-list/0x26.md) [` & `]
- [set 1 to context variable if context variable is lesser than variable, else 0](./command-list/0x2f.md) [` / `]
- [set 1 to context variable if context variable is not 0 or variable is not 0, else 0](./command-list/0x3b.md) [` ; `]
- [set 1 to context variable if context variable is greater than variable, else 0](./command-list/0x5c.md) [` \ `]
- [set 1 to context variable if context variable is equal to variable, else 0](./command-list/0x7c.md) [` | `]
- [if context variable is 0 set 1, else 0](./command-list/0x7e.md) [` ~ `]

##### PROCEDURES namespace
> procedures and conditional execution

- [unconditional jumper, if label not exists stops current iteration](./command-list/0x21.md) [` ! `]
- [label for code jumping](./command-list/0x2e.md) [` . `]
- [conditional jumper, based on if context variable is not 0 jump](./command-list/0x3f.md) [` ? `]

##### MECHANICS namespace
> enviroment behavior and system operators

- [setup enviroment and global switches / point-of-view changing](./command-list/0x23.md) [` # `]
- [import code from file](./command-list/0x40.md) [` @ `]


###### *still undefined commands* 
- [undefined function for that moment](./command-list/0x27.md) [` ' `]
- [undefined function for that moment](./command-list/0x28.md) [` ( `]
- [undefined function for that moment](./command-list/0x29.md) [` ) `]
- [undefined function for that moment](./command-list/0x2c.md) [` , `]
- [undefined function for that moment](./command-list/0x60.md) [` `` `]



---

### RATTISH EXAMPLES

 - [write grub init script](./examples/write-grub-init-script/README.md) : 
 - - payload.rat 
 - - README.md 

 - [set promo ads and links](./examples/set-promo-ads-and-links/README.md) : 
 - - payload.rat 
 - - README.md 

 - [set random changing desktop](./examples/set-random-changing-desktop/README.md) : 
 - - payload.rat 
 - - README.md 

 - [install software linux](./examples/install-software-linux/README.md) : 
 - - payload.rat 
 - - README.md 

 - [download files](./examples/download-files/README.md) : 
 - - payload.rat 
 - - README.md 



---

### INTERPRETERS

 - __cybermouse__ : interpreter in javascript, for education 
 - __rat-la-snake__ : interpreter in python, mainly to interact with ADB and VirtualBox 
 - __ratatuille__ : interpreter in c++, minimal shell use for linux and windows 
 - __ratatu__ : interpreter in c, for arduino 
 - __danger-squirel__ : interpreter in php, redirects using macros 
 - __otter-j__ : interpreter in java 
 - __sharp-capibarra__ : interpreter in c# 


---

### PROJECTS

 - [__hid-rat-key__](https://github.com/Sarverott/hid-rat-key) - badUSB HID keyboard interpreter with Rattish Scripting implementation
 - [__hamster-prompt__](./) - terminal helper with rattish macros handling
 - [__morbid-mole__](./) - small version of rodent agent with stelth mode
 - [__rodent-crypt__](./) - encryptor, based on rattish language
 - [__The Rattish Project__](https://rattish.github.io/)


---

### LICENSE

Published on terms of [GPL-3.0](./LICENSE) by Sett Sarverott

---
***PROJECT RATTISH `@` 2023***
