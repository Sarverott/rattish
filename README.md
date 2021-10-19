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

## BASIC ASSUMPTIONS OF LANGUAGE

- every line contains one command with one argument.
- commands are single ASCII characters in the range from 0x21 to 0x2F, that starts line.
- argument for every command starts after first char and ends before EOL.
- additional character with code 0x40 is dedicated for commentary.

***

## SYNTAX

### command 0x21 ( ` ! ` )
>*used since v1.0*
>
> write argument string as keyboard.
> example of writing "krupnioki,zymloki,beboki" on keyboard:
```
!krupnioki,zymloki,beboki
```

### command 0x22 ( ` " ` )
  > *used since v1.0*
  > 
  > wait argumented amount of milliseconds, expressed as integer.
  > example of waiting 1 second:
  ```
  "1000
  ```

### command 0x23 ( ` # ` )
  > *used since v1.0*
  > 
  > include macro file, described in full name, acceptable relative path defining or lack of path (default base location).
  > example of implementing content of file named "**winkey-r-cmdexe.rat**" as part of this payload in place of declaration:
  ```
  #winkey-r-cmdexe.rat
  ```

### ~~command 0x24~~ ( ` $ ` )
  > *CURRENTLY NOT USED*
  - planned current variable pointing eg. $THAT - now every var operation we do with var THAT

### ~~command 0x25~~ ( ` % ` )
  > *CURRENTLY NOT USED*
  
### ~~command 0x26~~ ( ` & ` )
  > *CURRENTLY NOT USED*

### ~~command 0x27~~ ( ` ' ` )
  > *CURRENTLY NOT USED*

### ~~command 0x28~~ ( ` ( ` )
  > *CURRENTLY NOT USED*

### ~~command 0x29~~ ( ` ) ` )
  > *CURRENTLY NOT USED*

### ~~command 0x2A~~ ( ` * ` )
  > *CURRENTLY NOT USED*

### ~~command 0x2B~~ ( ` + ` )
  > *CURRENTLY NOT USED*

### command 0x2C ( ` , ` )
  > *used since v1.0*
  >
  > orders to release pressed keys.
  > if you're not sure that all keys are released, simply write:
  ```
  ,
  ```

### ~~command 0x2D~~ ( ` - ` )
  > *CURRENTLY NOT USED*

### command 0x2E ( ` . ` )
  > *used since v1.0*
  >
  > orders to press key on keyboard with given code.
  > example of pressing combination ctrl+alt+del and release after 0.2 second:
  ```
   .16
   .17
   .46
   "200
   ,
  ```

### ~~command 0x2F~~ ( ` / ` )
  > *CURRENTLY NOT USED*

### commentary 0x40 ( ` @ ` )
  > *used since v1.0*
  >
  > example of commentary:
  ```
  @ this will be ignored by program
  ```
