/*
 * This file is part of the MicroPython project, http://micropython.org/
 *
 * The MIT License (MIT)
 *
 * Copyright (c) 2017 Nick Moore
 * Copyright (c) 2021 Jonathan Hogg
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

#include "py/mphal.h"
#include "adc.h"
#include "esp_adc/adc_oneshot.h"
#include "esp_adc/adc_cali.h"
#include "esp_adc/adc_cali_scheme.h"

#define DEFAULT_VREF 1100


static adc_oneshot_unit_handle_t adc1_handle = NULL;
static adc_oneshot_unit_init_cfg_t adc1_init_config;

static adc_oneshot_unit_handle_t adc2_handle = NULL;
static adc_oneshot_unit_init_cfg_t adc2_init_config;

static adc_oneshot_chan_cfg_t adc_oneshot_config;


static void start_adc_oneshot_mode()
{
    adc1_init_config.unit_id = ADC_UNIT_1;
    adc2_init_config.unit_id = ADC_UNIT_2;
    adc2_init_config.ulp_mode = ADC_ULP_MODE_DISABLE;
    adc_oneshot_config.bitwidth = ADC_BITWIDTH_DEFAULT;
    adc_oneshot_config.atten = ADC_ATTEN_DB_11;
    if (adc1_handle == NULL)
    {
        ESP_ERROR_CHECK(adc_oneshot_new_unit(&adc1_init_config, &adc1_handle));
    }
    if (adc2_handle == NULL)
    {

        ESP_ERROR_CHECK(adc_oneshot_new_unit(&adc2_init_config, &adc2_handle));
    }
    
}

static void stop_adc_oneshot_mode()
{
    if (adc1_handle)
    {
        adc_oneshot_del_unit(adc1_handle);
        adc1_handle = NULL;
    }
    if (adc2_handle)
    {
        adc_oneshot_del_unit(adc2_handle);
        adc2_handle = NULL;
    }
}


static esp_err_t adc1_oneshot_config(adc_channel_t channel)
{
    return adc_oneshot_config_channel(adc1_handle, channel, &adc_oneshot_config);
}

static esp_err_t adc2_oneshot_config(adc_channel_t channel)
{
    return adc_oneshot_config_channel(adc2_handle, channel, &adc_oneshot_config);
}

static esp_err_t adc1_oneshot_read(adc_channel_t channel, int *val)
{
    return adc_oneshot_read(adc1_handle, channel, val);
}

static esp_err_t adc2_oneshot_read(adc_channel_t channel, int *val)
{
    return adc_oneshot_read(adc2_handle, channel, val);
}

void madcblock_bits_helper(machine_adc_block_obj_t *self, mp_int_t bits) {
    switch (bits) {
        #if CONFIG_IDF_TARGET_ESP32
        case 9:
            adc_oneshot_config.bitwidth = ADC_BITWIDTH_9;
            break;
        case 10:
            adc_oneshot_config.bitwidth = ADC_BITWIDTH_10;
            break;
        case 11:
            adc_oneshot_config.bitwidth = ADC_BITWIDTH_11;
            break;
        #endif
        #if CONFIG_IDF_TARGET_ESP32 || CONFIG_IDF_TARGET_ESP32C3 || CONFIG_IDF_TARGET_ESP32S3
        case 12:
            adc_oneshot_config.bitwidth = ADC_BITWIDTH_12;
            break;
        #endif
        #if CONFIG_IDF_TARGET_ESP32S2
        case 13:
            adc_oneshot_config.bitwidth = ADC_WIDTH_BIT_13;
            break;
        #endif
        default:
            mp_raise_ValueError(MP_ERROR_TEXT("invalid bits"));
    }
    self->bits = bits;

    // if (self->unit_id == ADC_UNIT_1) {
    //     adc1_config_width(self->width);
    // }
    // for (adc_atten_t atten = ADC_ATTEN_DB_0; atten < ADC_ATTEN_MAX; atten++) {
    //     if (self->characteristics[atten] != NULL) {
    //         esp_adc_cal_characterize(self->unit_id, atten, self->width, DEFAULT_VREF, self->characteristics[atten]);
    //     }
    // }
}

mp_int_t madcblock_read_helper(machine_adc_block_obj_t *self, adc_channel_t channel_id) {
    int raw;
    if (self->unit_id == ADC_UNIT_1) {
        // raw = adc1_get_raw(channel_id);
        if(!adc1_handle)
        {
            start_adc_oneshot_mode();
        }
        adc1_oneshot_config(channel_id);
        check_esp_err(adc1_oneshot_read(channel_id,&raw));
    } else {
        if(!adc2_handle)
        {
            start_adc_oneshot_mode();
        }
        // check_esp_err(adc2_get_raw(channel_id, self->width, &raw));
        adc2_oneshot_config(channel_id);
        check_esp_err(adc2_oneshot_read(channel_id,&raw));
    }
    return raw;
}

mp_int_t madcblock_read_uv_helper(machine_adc_block_obj_t *self, adc_channel_t channel_id, adc_atten_t atten) {
    mp_int_t raw = madcblock_read_helper(self, channel_id);
    // esp_adc_cal_characteristics_t *adc_chars = self->characteristics[atten];
    // if (adc_chars == NULL) {
    //     adc_chars = malloc(sizeof(esp_adc_cal_characteristics_t));
    //     esp_adc_cal_characterize(self->unit_id, atten, self->width, DEFAULT_VREF, adc_chars);
    //     self->characteristics[atten] = adc_chars;
    // }
    // mp_int_t uv = esp_adc_cal_raw_to_voltage(raw, adc_chars) * 1000;
    
    return raw;
}
