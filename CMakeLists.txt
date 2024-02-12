cmake_minimum_required(VERSION 3.16.0)
include($ENV{IDF_PATH}/tools/cmake/project.cmake)
project(platformio-esp32-esp-idf)

# platformio puts src files under ./src/, and esp-idf component
# registration uses directory naming; typically an esp-idf src folder
# is named 'main', so we need to change from the default to 'src'
set(MEMFAULT_PLATFORM_PORT_COMPONENTS src)

set(MEMFAULT_FIRMWARE_SDK src/third-party/memfault-firmware-sdk)
include(${MEMFAULT_FIRMWARE_SDK}/ports/esp_idf/memfault.cmake)

add_custom_command(TARGET ${CMAKE_PROJECT_NAME}.elf
  POST_BUILD
  COMMAND
  python ${MEMFAULT_FIRMWARE_SDK}/scripts/fw_build_id.py ${CMAKE_PROJECT_NAME}.elf)