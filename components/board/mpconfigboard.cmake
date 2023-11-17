unset(IDF_TARGET)
set(IDF_TARGET esp32s3)

set(SDKCONFIG_DEFAULTS
    components/board/sdkconfig.base
    components/board/sdkconfig.240mhz
    components/board/sdkconfig.board
)

set(MICROPY_FROZEN_MANIFEST ${MICROPY_BOARD_DIR}/manifest.py)