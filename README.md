# rattish-language
simple and easy language used for input macros creation and payloads writing

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


***

### BASIC ASSUMPTIONS OF LANGUAGE

- every line contains one command with one argument.
- commands are single ASCII characters in the range from 0x21 to 0x2F or from 0x3A to 0x40 or from 0x5B to 0x5F or from 0x7B to 0x7E, that starts line.
- argument for every command starts after first char and ends before EOL.
- additional character with code 0x23 is reserved for commentary.

***

### COMMANDS LIST
- [commentary](./command-list/0x23.md) [ `#` ]
###### BASIC
- [print output](./command-list/0x3c.md) [ `<` ]
- [read input](./command-list/0x3e.md) [ `>` ]
- [wait time pause](./command-list/0x2e.md) [ `.` ]
- [press key(s)](./command-list/0x5f.md) [ `_` ]
- [release key(s)](./command-list/0x5e.md) [ `^` ]
###### VARIABLES
- [point context on variable](./command-list/0x24.md) [ `$` ]
- [set context variable](./command-list/0x3d.md) [ `=` ]
- [add to context variable](./command-list/0x2b.md) [ `+` ]
- [sub from context variable](./command-list/0x2d.md) [ `-` ]
- [add to context variable](./command-list/0x2b.md) [ `+` ]
- [sub from context variable](./command-list/0x2d.md) [ `-` ]
- [copy value from context variable to variable](./command-list/0x7d.md) [ `}` ]
- [copy value from variable to context variable](./command-list/0x7b.md) [ `{` ]
###### LOGICS
- [set 1 to context variable if context variable is greater than variable, else 0](./command-list/0x5c.md) [ `\` ]
- [set 1 to context variable if context variable is lesser than variable, else 0](./command-list/0x2f.md) [ `/` ]
- [set 1 to context variable if context variable is equal to variable, else 0](./command-list/0x7c.md) [ `|` ]
- [set 1 to context variable if context variable or variable is not 0, else 0](./command-list/0x3b.md) [ `;` ]
- [set 1 to context variable if context variable and variable is not 0, else 0](./command-list/0x26.md) [ `&` ]
- [if context variable is 0 set 1, else 0](./command-list/0x7e.md) [ `~` ]
###### PROCEDURES
- [begin procedure declaration](./command-list/0x5b.md) [ `[` ]
- [end procedure declaration](./command-list/0x5d.md) [ `]` ]
- [call procedure](./command-list/0x25.md) [ `%` ]
- [begin condition block of code, based on if context variable is 1](./command-list/0x3f.md) [ `?` ]
- [end conditional block](./command-list/0x21.md) [ `!` ]
###### MECHANICS
- [import code from file](./command-list/0x40.md) [ `@` ]
- [setup enviroment and global switches](./command-list/0x22.md) [ `"` ]
- [debug echo](./command-list/0x27.md) [ `'` ]
