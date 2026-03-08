

namespace Rats{
    typedef struct { char index[4] = "\0" } nicktag;
    typedef struct{
        nicktag name;
        char data[256] = "\0";
        memstore* next=NULL;
    } memstore;
    typedef void (*instruction) (memstore* MEM_PTR);//COMMAND CONTAINER STRUCTURE
    struct commandScope{
        int id = 0;
        nicktag modeName;
        instruction dictionary[256];
    }
    // struct scriptreader{
    //     char read*;
    //     int line=0;
    // }
    class engine(){ // 
        nicktag modinglist[32];
        commandScope MODE*;
        nicktag context_ptr;
        memstore MEM_PTR* = NULL;
        memstore MEMORY* = new memstore;
        commandScope operationLibs[32];
        void executeCode(char scriptreader*){
            bool is_instruction=true;
            char current_order=0;
            int line=0;
            while(scriptreader!=NULL&&scriptreader!='\0'){
                if(*scriptreader=="\n"){
                    line+=1;
                    is_instruction=true;
                    scriptreader++;
                    continue;
                }
                if(is_instruction){
                    is_instruction=!is_instruction;
                    current_order=(*scriptreader);
                    scriptreader++;
                }else{
                    this->MEMORY->data[0]='\0'
                    char i = 0;
                    while(i>255 && scriptreader!='\n'){
                        this->MEMORY->data[i] = scriptreader;
                        i++;
                        scriptreader++;
                    }
                    this->MEMORY->data[i] = '\0';
                }
                *(this->MODE)->dictionary[current_order](this->MEMORY, this->context_ptr);
            }
        }
    }
    //ALL COMMAND CONTAINER,
}

