# platformio puts src files under ./src/, and esp-idf component
# registration uses directory naming; typically an esp-idf src folder
# is named 'main', so we need to change from the default to 'src'
set(MEMFAULT_PLATFORM_PORT_COMPONENTS src)

set(MEMFAULT_FIRMWARE_SDK components/memfault-firmware-sdk)
include(${MEMFAULT_FIRMWARE_SDK}/ports/esp_idf/memfault.cmake)

cmake_minimum_required(VERSION 3.16.0)
include($ENV{IDF_PATH}/tools/cmake/project.cmake)
project(platformio-esp32-esp-idf)
