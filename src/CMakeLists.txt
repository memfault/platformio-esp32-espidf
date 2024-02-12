# This file was automatically generated for projects
# without default 'CMakeLists.txt' file.

FILE(GLOB_RECURSE app_sources ${CMAKE_SOURCE_DIR}/src/*.*)
set(MEMFAULT_FIRMWARE_SDK third-party/memfault-firmware-sdk)

idf_component_register(
    SRCS
    main.c
    # memfault_platform_port.c

    INCLUDE_DIRS
    .
    ${MEMFAULT_FIRMWARE_SDK}/ports/include

		# if in the future MEMFAULT_ESP_HTTP_CLIENT_ENABLE=1, add the below component
    REQUIRES
    esp_https_ota
)