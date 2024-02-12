set(COMPONENT_SRCS
   cmd_system.c
   cmd_wifi.c
   config.c
   console_example_main.c
   memfault_platform_device_info.c
)

FILE(GLOB_RECURSE app_sources ${CMAKE_SOURCE_DIR}/src/*.*)
set(MEMFAULT_FIRMWARE_SDK memfault/memfault-firmware-sdk)

set(COMPONENT_REQUIRES esp_https_ota app_update)

register_component()
