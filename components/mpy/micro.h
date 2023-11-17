#ifndef _MICRO_H_
#define _MICRO_H_

#include <string.h>
#include <esp_err.h>


#include "py/stackctrl.h"
#include "py/nlr.h"
#include "py/compile.h"
#include "py/runtime.h"
#include "py/persistentcode.h"
#include "py/repl.h"
#include "py/gc.h"
#include "py/mphal.h"
#include "shared/readline/readline.h"
#include "shared/runtime/pyexec.h"
#include "uart.h"
#include "usb.h"
#include "usb_serial_jtag.h"
#include "modmachine.h"
#include "modnetwork.h"
#include "mpthreadport.h"

#ifdef __cplusplus
extern "C"
{
#endif

void register_micropython_repl();
void unregister_micropython_repl();

esp_err_t _register_micropython();
void _unregister_micropython();

void mp_embed_exec_str(const char *src);

#ifdef __cplusplus
}
#endif

#endif