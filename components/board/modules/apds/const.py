# APDS9960 i2c address
APDS9960_I2C_ADDR = 0x39

# APDS9960 gesture parameters
APDS9960_GESTURE_THRESHOLD_OUT = 10
APDS9960_GESTURE_SENSITIVITY_1 = 50
APDS9960_GESTURE_SENSITIVITY_2 = 20

# APDS9960 device IDs
APDS9960_DEV_ID = [0xab, 0x9c, 0xa8, -0x55]

# APDS9960 times
APDS9960_TIME_FIFO_PAUSE = 0.03

# APDS9960 register addresses
APDS9960_REG_ENABLE = 0x80
APDS9960_REG_ATIME = 0x81
APDS9960_REG_WTIME = 0x83
APDS9960_REG_AILTL = 0x84
APDS9960_REG_AILTH = 0x85
APDS9960_REG_AIHTL = 0x86
APDS9960_REG_AIHTH = 0x87
APDS9960_REG_PILT = 0x89
APDS9960_REG_PIHT = 0x8b
APDS9960_REG_PERS = 0x8c
APDS9960_REG_CONFIG1 = 0x8d
APDS9960_REG_PPULSE = 0x8e
APDS9960_REG_CONTROL = 0x8f
APDS9960_REG_CONFIG2 = 0x90
APDS9960_REG_ID = 0x92
APDS9960_REG_STATUS = 0x93
APDS9960_REG_CDATAL = 0x94
APDS9960_REG_CDATAH = 0x95
APDS9960_REG_RDATAL = 0x96
APDS9960_REG_RDATAH = 0x97
APDS9960_REG_GDATAL = 0x98
APDS9960_REG_GDATAH = 0x99
APDS9960_REG_BDATAL = 0x9a
APDS9960_REG_BDATAH = 0x9b
APDS9960_REG_PDATA = 0x9c
APDS9960_REG_POFFSET_UR = 0x9d
APDS9960_REG_POFFSET_DL = 0x9e
APDS9960_REG_CONFIG3 = 0x9f
APDS9960_REG_GPENTH = 0xa0
APDS9960_REG_GEXTH = 0xa1
APDS9960_REG_GCONF1 = 0xa2
APDS9960_REG_GCONF2 = 0xa3
APDS9960_REG_GOFFSET_U = 0xa4
APDS9960_REG_GOFFSET_D = 0xa5
APDS9960_REG_GOFFSET_L = 0xa7
APDS9960_REG_GOFFSET_R = 0xa9
APDS9960_REG_GPULSE = 0xa6
APDS9960_REG_GCONF3 = 0xaA
APDS9960_REG_GCONF4 = 0xaB
APDS9960_REG_GFLVL = 0xae
APDS9960_REG_GSTATUS = 0xaf
APDS9960_REG_IFORCE = 0xe4
APDS9960_REG_PICLEAR = 0xe5
APDS9960_REG_CICLEAR = 0xe6
APDS9960_REG_AICLEAR = 0xe7
APDS9960_REG_GFIFO_U = 0xfc
APDS9960_REG_GFIFO_D = 0xfd
APDS9960_REG_GFIFO_L = 0xfe
APDS9960_REG_GFIFO_R = 0xff

# APDS9960 bit fields
APDS9960_BIT_PON = 0b00000001
APDS9960_BIT_AEN = 0b00000010
APDS9960_BIT_PEN = 0b00000100
APDS9960_BIT_WEN = 0b00001000
APSD9960_BIT_AIEN =0b00010000
APDS9960_BIT_PIEN = 0b00100000
APDS9960_BIT_GEN = 0b01000000
APDS9960_BIT_GVALID = 0b00000001
APDS9960_BIT_AVALID = 0b00000001
APDS9960_BIT_PVALID = 0b00000010
APDS9960_BIT_GINT = 0b00000100
APDS9960_BIT_AINT = 0b00010000
APDS9960_BIT_PINT = 0b00100000
APDS9960_BIT_PGSAT = 0b01000000
APDS9960_BIT_CPSAT = 0b10000000

# APDS9960 modes
APDS9960_MODE_POWER = 0
APDS9960_MODE_AMBIENT_LIGHT = 1
APDS9960_MODE_PROXIMITY = 2
APDS9960_MODE_WAIT = 3
APDS9960_MODE_AMBIENT_LIGHT_INT = 4
APDS9960_MODE_PROXIMITY_INT = 5
APDS9960_MODE_GESTURE = 6
APDS9960_MODE_ALL = 7

# LED Drive values
APDS9960_LED_DRIVE_100MA = 0
APDS9960_LED_DRIVE_50MA = 1
APDS9960_LED_DRIVE_25MA = 2
APDS9960_LED_DRIVE_12_5MA = 3

# Proximity Gain (PGAIN) values
APDS9960_PGAIN_1X = 0
APDS9960_PGAIN_2X = 1
APDS9960_PGAIN_4X = 2
APDS9960_PGAIN_8X = 3

# ALS Gain (AGAIN) values
APDS9960_AGAIN_1X = 0
APDS9960_AGAIN_4X = 1
APDS9960_AGAIN_16X = 2
APDS9960_AGAIN_64X = 3

# Gesture Gain (GGAIN) values
APDS9960_GGAIN_1X = 0
APDS9960_GGAIN_2X = 1
APDS9960_GGAIN_4X = 2
APDS9960_GGAIN_8X = 3

# LED Boost values
APDS9960_LED_BOOST_100 = 0
APDS9960_LED_BOOST_150 = 1
APDS9960_LED_BOOST_200 = 2
APDS9960_LED_BOOST_300 = 3    

# Gesture wait time values
APDS9960_GWTIME_0MS = 0
APDS9960_GWTIME_2_8MS = 1
APDS9960_GWTIME_5_6MS = 2
APDS9960_GWTIME_8_4MS = 3
APDS9960_GWTIME_14_0MS = 4
APDS9960_GWTIME_22_4MS = 5
APDS9960_GWTIME_30_8MS = 6
APDS9960_GWTIME_39_2MS = 7

# Default values
APDS9960_DEFAULT_ATIME = 219                            # 103ms
APDS9960_DEFAULT_WTIME = 246                            # 27ms
APDS9960_DEFAULT_PROX_PPULSE = 0x87                     # 16us, 8 pulses
APDS9960_DEFAULT_GESTURE_PPULSE = 0x89                  # 16us, 10 pulses
APDS9960_DEFAULT_POFFSET_UR = 0                         # 0 offset
APDS9960_DEFAULT_POFFSET_DL = 0                         # 0 offset
APDS9960_DEFAULT_CONFIG1 = 0x60                         # No 12x wait (WTIME) factor
APDS9960_DEFAULT_LDRIVE = APDS9960_LED_DRIVE_100MA
APDS9960_DEFAULT_PGAIN = APDS9960_PGAIN_4X
APDS9960_DEFAULT_AGAIN = APDS9960_AGAIN_4X
APDS9960_DEFAULT_PILT = 0                               # Low proximity threshold
APDS9960_DEFAULT_PIHT = 50                              # High proximity threshold
APDS9960_DEFAULT_AILT = 0xffff                          # Force interrupt for calibration
APDS9960_DEFAULT_AIHT = 0
APDS9960_DEFAULT_PERS = 0x11                            # 2 consecutive prox or ALS for int.
APDS9960_DEFAULT_CONFIG2 = 0x01                         # No saturation interrupts or LED boost  
APDS9960_DEFAULT_CONFIG3 = 0                            # Enable all photodiodes, no SAI
APDS9960_DEFAULT_GPENTH = 40                            # Threshold for entering gesture mode
APDS9960_DEFAULT_GEXTH = 30                             # Threshold for exiting gesture mode    
APDS9960_DEFAULT_GCONF1 = 0x40                          # 4 gesture events for int., 1 for exit
APDS9960_DEFAULT_GGAIN = APDS9960_GGAIN_4X
APDS9960_DEFAULT_GLDRIVE = APDS9960_LED_DRIVE_100MA
APDS9960_DEFAULT_GWTIME = APDS9960_GWTIME_2_8MS
APDS9960_DEFAULT_GOFFSET = 0                            # No offset scaling for gesture mode
APDS9960_DEFAULT_GPULSE = 0xc9                          # 32us, 10 pulses
APDS9960_DEFAULT_GCONF3 = 0                             # All photodiodes active during gesture
APDS9960_DEFAULT_GIEN = 0                               # Disable gesture interrupts

# gesture directions
APDS9960_DIR_NONE = 0
APDS9960_DIR_LEFT = 1
APDS9960_DIR_RIGHT = 2
APDS9960_DIR_UP = 3
APDS9960_DIR_DOWN = 4
APDS9960_DIR_NEAR = 5
APDS9960_DIR_FAR = 6
APDS9960_DIR_ALL = 7

# state definitions
APDS9960_STATE_NA = 0
APDS9960_STATE_NEAR = 1
APDS9960_STATE_FAR = 2
APDS9960_STATE_ALL = 3