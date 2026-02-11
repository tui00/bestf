// BESTF (Arduino part)

#pragma once

#include "FOR_MACRO.h"
#include <Arduino.h>

#define _INTERNAL_STR_(x) #x
#define _INTERNAL_STR(x) _INTERNAL_STR_(x)
#define _INTERNAL_RUN_TEST(N, i, p, val)   \
    Serial.println("S" #val ";" __FILE__); \
    test_##val();

#define TEST(name) void test_##name()

#define ASSUME(condition)                                                                \
    do                                                                                   \
    {                                                                                    \
        if (!(condition))                                                                \
        {                                                                                \
            Serial.println("FFalse condition: " #condition ";" _INTERNAL_STR(__LINE__)); \
            return;                                                                      \
        }                                                                                \
    } while (0)
#define END()                                        \
    do                                               \
    {                                                \
        Serial.println("T" _INTERNAL_STR(__LINE__)); \
    } while (0)
#define ABORT()                                            \
    do                                                     \
    {                                                      \
        Serial.println("FAbort;" _INTERNAL_STR(__LINE__)); \
        return;                                            \
    } while (0)

#define PRINT(...) Serial.println("D" __VA_ARGS__, ";" _INTERNAL_STR(__LINE__))

#define START void _internal_start(void)
#define NO_START \
    START {}
#define STOP void _internal_stop(void)
#define NO_STOP \
    STOP {}
#define NO_OTHERS NO_START NO_STOP

#define TESTS_LIST(...)                                                  \
    void setup(void)                                                     \
    {                                                                    \
        Serial.begin(115200);                                              \
        while (!Serial)                                                  \
            ;                                                            \
        Serial.println("\e[1;36m"                                        \
                                                                         \
                       "+-------------------------------------------+\n" \
                       "| BESTF: Best Framework for Arduino testing |\n" \
                       "+-------------------------------------------+\n" \
                                                                         \
                       "\e[0m");                                         \
        Serial.println("B");                                             \
        _internal_start();                                               \
        FOR_MACRO(_INTERNAL_RUN_TEST, 0, __VA_ARGS__)                    \
        _internal_stop();                                                \
        Serial.println("E");                                             \
    }                                                                    \
    void loop() {}
