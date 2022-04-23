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

### COMMANDS NAMESPACES
- [__BASIC__](#basic-namespace) - _since v0.2_
  - input, output, events, breakers and pauses
- [__VARIABLES__](#variables-namespace) - _since v0.7_
  - basic variable operations
- [__LOGICS__](#logics-namespace) - _since v0.8_
  - logic operations
- [__PROCEDURES__](#procedures-namespace) - _since v0.9_
  - procedures and conditional execution
- [__MECHANICS__](#mechanics-namespace) - _since v0.4_
  - enviroment behavior

---

### BASIC ASSUMPTIONS OF LANGUAGE

- every line contains one command with one argument.

- commands are single ASCII characters in the range from 0x21 to 0x2F or from 0x3A to 0x40 or from 0x5B to 0x5F or from 0x7B to 0x7E, that starts line.

- argument for every command starts after first char and ends before EOL.

- if line starts with other char, like for example space, letter or cipher it is commentary.

---

### ALL COMMANDS LIST

###### BASIC namespace
- [print static output / print output from variable](./command-list/0x3c.md) [ `<` ]
- [read input to file / to variable](./command-list/0x3e.md) [ `>` ]
- [wait time pause in miliseconds / seconds / minutes / hours](./command-list/0x2e.md) [ `"` ]
- [press key(s)](./command-list/0x5f.md) [ `_` ]
- [release key(s)](./command-list/0x5e.md) [ `^` ]

###### VARIABLES namespace
- [point context on variable](./command-list/0x24.md) [ `$` ]
- [set context variable](./command-list/0x3d.md) [ `=` ]
- [add to context variable / string append](./command-list/0x2b.md) [ `+` ]
- [sub from context variable / find and remove](./command-list/0x2d.md) [ `-` ]
- [multiply context variable / get char at](./command-list/0x2a.md) [ `*` ]
- [divide context variable / insert at](./command-list/0x3a.md) [ `:` ]
- [modulo of context variable / string length](./command-list/0x40.md) [ `%` ]
- [copy value from context variable to variable](./command-list/0x7d.md) [ `}` ]
- [copy value from variable to context variable](./command-list/0x7b.md) [ `{` ]

###### LOGICS namespace
- [set 1 to context variable if context variable is greater than variable, else 0](./command-list/0x5c.md) [ `\` ]
- [set 1 to context variable if context variable is lesser than variable, else 0](./command-list/0x2f.md) [ `/` ]
- [set 1 to context variable if context variable is equal to variable, else 0](./command-list/0x7c.md) [ `|` ]
- [set 1 to context variable if context variable is not 0 or variable is not 0, else 0](./command-list/0x3b.md) [ `;` ]
- [set 1 to context variable if context variable is not 0 and variable is not 0, else 0](./command-list/0x26.md) [ `&` ]
- [if context variable is 0 set 1, else 0](./command-list/0x7e.md) [ `~` ]

###### PROCEDURES namespace
- [import code from file](./command-list/0x40.md) [ `@` ]
- [label for code jumping](./) [ `.` ]
- [conditional jumper, based on if context variable is not 0 jump](./command-list/0x3f.md) [ `?` ]
- [unconditional jumper, if label not exists stops current iteration](./command-list/0x21.md) [ `!` ]

###### SYSTEM namespace
- [setup enviroment and global switches / point-of-view changing](./command-list/0x23.md) [ `#` ]

---
#### commands unused in v1.0
###### FREE namespace
- [_in future plans as procedure declaration_]() [ `[` ]
- [_in future plans as procedure declaration_]() [ `]` ]
- [_for special personalization implementations_](./command-list/0x27.md) [ `'` ]
- [_in future plans as data sets declaration_](./command-list/0x5b.md) [ `(` ]
- [_in future plans as data sets declaration_](./command-list/0x5d.md) [ `)` ]
- [_for special personalization implementations_](./command-list/0x27.md) [ `,` ]

---

### INTERPRETERS

- __HID-RAT-KEY__: badUSB HID keyboard interpreter with Rattish Scripting implementation (https://github.com/Sarverott/hid-rat-key)
- __RATATUILE__: multipurpose stand-alone engine for Windows and Linux (https://github.com/Sarverott/hid-rat-key)
- __CYBERMOUSE__: JS online emulator (_early stage project_)

---

### PROJECTS

- The Rattish Project (https://rattish.github.io/)
- Tiny Furry On Bottom Of Sewer - Game for begginers to learn how to script in it (_early stage project_)


---

### LICENSE

Published on terms of [MIT License](./LICENSE) by Sett Sarverott
