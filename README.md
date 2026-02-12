# BESTF: Best Framework for Arduino Testing

BESTF is a lightweight framework for testing code on the Arduino platform. It allows you to structure test scenarios and get detailed execution results.

The FOR_MACRO file.The h is taken from Alex Gyver

### About the name of BESTF

BESTF stands for *Best Framework* — "the best framework". Another reason for the name is the key commands used in the work: **B**, **E**, **S**, **T**, **F**. They are at the heart of the framework's reporting mechanism.

## Installation

To install the framework:

1. Copy all the project files to the 'test` folder.
2. In the `platformio.ini` file, add the following parameters:
* `test_speed = 9600`
* `test_framework = custom`

There is a simple option:

1. Run the file `install.py ` from any directory

Recommended option:

1. Go to the root of the project
2. Run `git clone http://tui00/bestf.git `
3. Run `./bestf/install.py `
4. Follow the on-screen instructions

## Description of macros

## Group 1: Test lifecycle management

These macros define the structure of test execution — they determine what is executed before and after their launch.:

* **`START`** — defines the block of code that will be executed before all tests.
* **`NO_START`** — cancels the execution of the preliminary code block before the tests.
* **`STOP`** — defines the block of code that will be executed after all tests.
* **`NO_STOP`** — cancels the execution of the final block of code after the tests.
* **`NO_OTHERS'** — simultaneously cancels the preliminary and final code blocks (equivalent to `NO_START NO_STOP').

## Group 2: Working with tests and debugging

Macros for creating tests, checking conditions, and outputting debugging information:

* **`TEST(name)`** — creates a new test with the specified name.
* **`ASSUME(condition)`** — checks the condition: if it is not fulfilled, the test is considered failed.
* **`END()`** — marks the successful completion of the test.
* **`ABORT()`** — forcibly aborts the test.
* **`PRINT(...)`** — outputs a debugging message indicating the line number.
* **`TESTS_LIST(...)`** — lists the tests that need to be run (separated by commas).

---

## Usage examples

### Example 1: with `NO_OTHERS`

```c
#include "bestf.h"

NO_OTHERS

TEST(simple_check) {
    ASSUME(1 + 1 == 2);
    PRINT("Simple math passed");
    END();
}

TESTS_LIST(simple_check)
```

### Example 2: with `NO_START`

```c
#include "bestf.h"

NO_START

STOP {
    PRINT("All tests completed, cleaning up...");
}

TEST(positive_test) {
    ASSUME(true);
    END();
}

TEST(negative_test) {
    ABORT(); // The test will be aborted
    END(); // This line will not execute
}

TESTS_LIST(positive_test, negative_test)
```

### Example 3: without abbreviations

```c
#include "bestf.h"

START {
    PRINT("Initializing test environment...");
}

STOP {
    PRINT("Shutting down test environment.");
}

TEST(division_check) {
    int a = 10, b = 2;
    ASSUME(a / b == 5);
    PRINT("Division test passed");
    END();
}

TEST(string_check) {
    const char* str = "hello";
    ASSUME(str[0] == 'h');
    END();
}

TESTS_LIST(division_check, string_check)
```