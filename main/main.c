#include "micro.h"

void app_main()
{
    _register_micropython();
    const char * test1 = "while True:\n    print('hello')\n\n";
    mp_embed_exec_str(test1);
    _unregister_micropython()

}